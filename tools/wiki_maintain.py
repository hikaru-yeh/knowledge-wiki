from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from urllib.parse import unquote, urlsplit


WIKI_DIR_DEFAULT = "wiki-pages"
RAW_DIR_DEFAULT = "raw"
TASKS_DIR_DEFAULT = "tasks"
HANDOFF_PATH = "current-handoff.md"
BLOCKED_PATH = "blocked-content-gaps.md"
MAINTENANCE_REPORTS_DIR = "maintenance-reports"
MAIN_STATUSES = {"wiki", "reference", "stub"}
PROJECT_MANAGEMENT_STATUSES = {"active", "legacy"}
PROJECT_MANAGEMENT_CATEGORY = "專案管理"
STUB_INDEX_MARKER = "（📌 stub）"
RAW_PATH_RE = re.compile(r"raw[\\/]")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

PLACEHOLDER_MARKERS = {
    "（📌 待消化）",
    "(📌 待消化)",
    "📌 待消化",
    "TODO",
    "TBD",
}

# (canonical_repo_rel, stale_repo_rel): stale file must not coexist with canonical.
# All paths are relative to repo root and use forward slashes.
CANONICAL_GUARD_PAIRS: tuple[tuple[str, str], ...] = (
    ("wiki-pages/log.md",                       "wiki-pages/日誌.md"),
    ("wiki-pages/index/AI 工具-索引.md",        "wiki-pages/index/AI 工具索引.md"),
    ("wiki-pages/index/工具軟體-索引.md",       "wiki-pages/index/工具軟體索引.md"),
    ("wiki-pages/index/LingOrm-索引.md",        "wiki-pages/鄺玲玲-索引.md"),
    ("wiki-pages/動漫/神聖無碼帝國萬歲！.md",   "wiki-pages/生活雜記/神聖無碼帝國萬歲！-2.md"),
)


@dataclass(frozen=True)
class PageRecord:
    path: Path
    rel_path: str
    wiki_rel_path: str
    stem: str
    category: str
    frontmatter: dict[str, str]
    body: str
    status: str
    url: str
    title: str


@dataclass(frozen=True)
class RawRecord:
    path: Path
    rel_path: str
    frontmatter: dict[str, str]
    body: str
    url: str
    title: str


@dataclass(frozen=True)
class BlockedRecord:
    path: str
    title: str
    category: str
    reason: str
    source_url: str
    raw_match: str
    next_action: str
    policy_bucket: str


@dataclass(frozen=True)
class StatusIssue:
    path: str
    title: str
    category: str
    status: str
    reason: str


@dataclass(frozen=True)
class StatusAudit:
    total_pages: int
    content_pages: int
    excluded_readmes: list[str]
    main_counts: dict[str, int]
    project_management_counts: dict[str, int]
    missing: list[StatusIssue]
    unknown: list[StatusIssue]
    misplaced_project_management: list[StatusIssue]
    author_issues: list[FrontmatterIssue]


@dataclass(frozen=True)
class IndexIssue:
    code: str
    path: str
    line: int
    target: str
    detail: str


@dataclass(frozen=True)
class IndexLint:
    scanned_pages: int
    issues: list[IndexIssue]


@dataclass(frozen=True)
class ReviewFinding:
    source: str
    text: str
    bucket: str


REVIEW_RECONCILE_BUCKETS = [
    "cleanup-caused",
    "known deferred",
    "pre-existing",
    "environmental",
    "dismissed",
]

REVIEW_RECONCILE_KEYWORDS = {
    "dismissed": [
        "false positive",
        "expected",
        "intentional",
        "by design",
        "no action",
        "dismissed",
    ],
    "known deferred": [
        "deferred",
        "todo",
        "future",
        "out of scope",
        "not in this round",
        "v2 later",
        "pending",
    ],
    "environmental": [
        "environment",
        "sandbox",
        "permission",
        "network",
        "filesystem",
        "path unavailable",
        "missing dependency",
        "pycache",
        "generated cache",
    ],
    "cleanup-caused": [
        "cleanup",
        "this batch",
        "regression",
        "introduced by",
        "after cleanup",
        "moved",
        "renamed",
        "deleted",
        "stale index from cleanup",
    ],
    "pre-existing": [
        "existing",
        "pre-existing",
        "legacy",
        "already present",
    ],
}


def normalize_rel_path(path: Path, root: Path) -> str:
    try:
        rel = path.resolve().relative_to(root.resolve())
    except ValueError:
        rel = path
    return rel.as_posix()


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    text = text.lstrip("﻿")  # strip UTF-8 BOM (U+FEFF) added by some Windows editors
    if not text.startswith("---"):
        return {}, text

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        return {}, text

    metadata: dict[str, str] = {}
    for line in lines[1:end_index]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    body = "\n".join(lines[end_index + 1 :]).lstrip("\n")
    return metadata, body


def normalize_url(value: str) -> str:
    text = str(value or "").strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
        text = text[1:-1].strip()
    if text in {"", "[]", "[ ]"}:
        return ""
    if text.startswith("[") and text.endswith("]"):
        text = text[1:-1].strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
        text = text[1:-1].strip()
    return text.rstrip("/")


def normalize_status(value: str) -> str:
    text = str(value or "").strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
        text = text[1:-1].strip()
    return text


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def load_wiki_pages(root: Path, wiki_dir: Path) -> list[PageRecord]:
    base = root / wiki_dir
    if not base.exists():
        return []

    records: list[PageRecord] = []
    for path in sorted(base.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(base).parts):
            continue
        text = read_text(path)
        frontmatter, body = parse_frontmatter(text)
        wiki_rel_path = path.relative_to(base).as_posix()
        category = wiki_rel_path.split("/", 1)[0] if "/" in wiki_rel_path else ""
        title = frontmatter.get("title") or path.stem
        url = normalize_url(frontmatter.get("網址") or frontmatter.get("url") or "")
        records.append(
            PageRecord(
                path=path,
                rel_path=normalize_rel_path(path, root),
                wiki_rel_path=wiki_rel_path,
                stem=path.stem,
                category=category,
                frontmatter=frontmatter,
                body=body,
                status=frontmatter.get("status", "").strip(),
                url=url,
                title=title,
            )
        )
    return records


def load_raw_records(root: Path, raw_dir: Path) -> list[RawRecord]:
    base = root / raw_dir
    if not base.exists():
        return []

    records: list[RawRecord] = []
    for path in sorted(base.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(base).parts):
            continue
        text = read_text(path)
        frontmatter, body = parse_frontmatter(text)
        url = normalize_url(frontmatter.get("url") or frontmatter.get("網址") or "")
        records.append(
            RawRecord(
                path=path,
                rel_path=normalize_rel_path(path, root),
                frontmatter=frontmatter,
                body=body,
                url=url,
                title=frontmatter.get("title") or path.stem,
            )
        )
    return records


def has_meaningful_body(body: str) -> bool:
    meaningful: list[str] = []
    in_frontmatter = False
    for raw_line in body.replace("\r\n", "\n").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line == "---":
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter:
            continue
        if line in PLACEHOLDER_MARKERS:
            continue
        if line.startswith("#"):
            continue
        if line.startswith("- [") and "](" in line:
            continue
        if line.startswith(("- [[", "* [[", "[[")):
            continue
        if line.startswith(("http://", "https://")):
            continue
        if line in {"[]", "[ ]"}:
            continue
        meaningful.append(line)
    return sum(len(line) for line in meaningful) >= 80 or len(meaningful) >= 3


def is_stub_like(page: PageRecord) -> bool:
    body = page.body
    return page.status == "stub" or "📌 待消化" in body


def build_raw_indexes(raw_records: list[RawRecord]) -> tuple[dict[str, list[RawRecord]], dict[str, list[RawRecord]]]:
    by_url: dict[str, list[RawRecord]] = {}
    by_stem: dict[str, list[RawRecord]] = {}
    for record in raw_records:
        if record.url:
            by_url.setdefault(record.url, []).append(record)
        by_stem.setdefault(record.path.stem, []).append(record)
    return by_url, by_stem


def find_raw_matches(
    page: PageRecord,
    raw_by_url: dict[str, list[RawRecord]],
    raw_by_stem: dict[str, list[RawRecord]],
) -> list[RawRecord]:
    matches: list[RawRecord] = []
    if page.url:
        matches.extend(raw_by_url.get(page.url, []))
    if not matches:
        matches.extend(raw_by_stem.get(page.stem, []))
    return matches


def collect_blocked_records(root: Path, wiki_dir: Path, raw_dir: Path) -> list[BlockedRecord]:
    pages = load_wiki_pages(root, wiki_dir)
    raw_records = load_raw_records(root, raw_dir)
    raw_by_url, raw_by_stem = build_raw_indexes(raw_records)

    blocked: list[BlockedRecord] = []
    for page in pages:
        if page.category == "index" or not is_stub_like(page):
            continue
        if has_meaningful_body(page.body):
            continue

        raw_matches = find_raw_matches(page, raw_by_url, raw_by_stem)
        raw_with_body = [record for record in raw_matches if has_meaningful_body(record.body)]
        if raw_with_body:
            continue

        if not raw_matches:
            reason = "missing-raw-source"
            raw_match = ""
            next_action = "Find source material manually or leave as blocked bookmark."
        else:
            reason = "empty-wiki-and-raw"
            raw_match = ", ".join(record.rel_path for record in raw_matches[:5])
            next_action = "Recover source content manually before promote; do not auto-promote."

        policy_bucket = "excluded-lingorm" if page.category == "LingOrm" else "blocked-nonlingorm"

        blocked.append(
            BlockedRecord(
                path=page.rel_path,
                title=page.title,
                category=page.category or "(root)",
                reason=reason,
                source_url=page.url,
                raw_match=raw_match,
                next_action=next_action,
                policy_bucket=policy_bucket,
            )
        )

    return blocked


def is_readme_page(page: PageRecord) -> bool:
    return page.path.name.lower() == "readme.md"


def is_project_management_page(page: PageRecord) -> bool:
    return page.category == PROJECT_MANAGEMENT_CATEGORY


def collect_status_audit(root: Path, wiki_dir: Path) -> StatusAudit:
    pages = load_wiki_pages(root, wiki_dir)
    excluded_readmes: list[str] = []
    main_counts = {status: 0 for status in sorted(MAIN_STATUSES)}
    project_management_counts = {status: 0 for status in sorted(PROJECT_MANAGEMENT_STATUSES)}
    missing: list[StatusIssue] = []
    unknown: list[StatusIssue] = []
    misplaced_project_management: list[StatusIssue] = []

    for page in pages:
        if is_readme_page(page):
            excluded_readmes.append(page.rel_path)
            continue

        status = normalize_status(page.status)
        issue = StatusIssue(
            path=page.rel_path,
            title=page.title,
            category=page.category or "(root)",
            status=status,
            reason="",
        )
        if not status:
            missing.append(
                StatusIssue(
                    path=issue.path,
                    title=issue.title,
                    category=issue.category,
                    status="",
                    reason="missing-status",
                )
            )
            continue
        if status in MAIN_STATUSES:
            main_counts[status] += 1
            continue
        if status in PROJECT_MANAGEMENT_STATUSES:
            if is_project_management_page(page):
                project_management_counts[status] += 1
            else:
                misplaced_project_management.append(
                    StatusIssue(
                        path=issue.path,
                        title=issue.title,
                        category=issue.category,
                        status=status,
                        reason="project-management-status-outside-project-management",
                    )
                )
            continue
        unknown.append(
            StatusIssue(
                path=issue.path,
                title=issue.title,
                category=issue.category,
                status=status,
                reason="unknown-status",
            )
        )

    author_issues = collect_frontmatter_issues(pages)

    return StatusAudit(
        total_pages=len(pages),
        content_pages=len(pages) - len(excluded_readmes),
        excluded_readmes=excluded_readmes,
        main_counts=main_counts,
        project_management_counts=project_management_counts,
        missing=missing,
        unknown=unknown,
        misplaced_project_management=misplaced_project_management,
        author_issues=author_issues,
    )


def is_index_page(page: PageRecord) -> bool:
    if getattr(page, "is_index", False):
        return True
    return page.category == "index" or page.wiki_rel_path.startswith("index/")


def wikilink_target(value: str) -> str:
    target = value.split("|", 1)[0].split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target.strip()


def is_bare_wikilink_target(target: str) -> bool:
    return bool(target) and "/" not in target and "\\" not in target


def iter_markdown_link_destinations(line: str):
    index = 0
    while index < len(line):
        open_label = line.find("[", index)
        if open_label == -1:
            return
        if open_label > 0 and line[open_label - 1] == "!":
            index = open_label + 1
            continue
        close_label = line.find("]", open_label + 1)
        if close_label == -1 or close_label + 1 >= len(line) or line[close_label + 1] != "(":
            index = open_label + 1
            continue

        destination_start = close_label + 2
        if destination_start < len(line) and line[destination_start] == "<":
            destination_end = line.find(">", destination_start + 1)
            if destination_end == -1:
                index = destination_start
                continue
            close_paren = destination_end + 1
            while close_paren < len(line) and line[close_paren].isspace():
                close_paren += 1
            if close_paren < len(line) and line[close_paren] == ")":
                yield line[destination_start : destination_end + 1]
                index = close_paren + 1
            else:
                index = destination_end + 1
            continue

        cursor = destination_start
        depth = 0
        while cursor < len(line):
            char = line[cursor]
            if char == "\\":
                cursor += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    yield line[destination_start:cursor]
                    index = cursor + 1
                    break
                depth -= 1
            cursor += 1
        else:
            return


def markdown_link_target(value: str) -> str:
    text = value.strip()
    if text.startswith("<") and ">" in text:
        text = text[1 : text.index(">")]
    else:
        text = text.split(None, 1)[0] if text else ""
    return text.strip()


def is_ignored_markdown_target(target: str) -> bool:
    if not target or target.startswith("#"):
        return True
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith("//"):
        return True
    if target.startswith(("/", "\\")):
        return True
    return Path(target).is_absolute()


def resolve_markdown_target(base_dir: Path, target: str, wiki_base: Path) -> Path | None:
    parsed = urlsplit(target)
    target_path = unquote(parsed.path)
    if not target_path:
        return base_dir

    resolved = (base_dir / target_path).resolve()
    wiki_root = wiki_base.resolve()
    try:
        resolved.relative_to(wiki_root)
    except ValueError:
        return None

    if resolved.exists():
        return resolved
    if not resolved.suffix:
        markdown_resolved = resolved.with_suffix(".md")
        try:
            markdown_resolved.relative_to(wiki_root)
        except ValueError:
            return None
        if markdown_resolved.exists():
            return markdown_resolved
    return None


def resolve_wikilink_pages(
    target: str,
    pages_by_stem: dict[str, list[PageRecord]],
    pages_by_wiki_target: dict[str, PageRecord],
) -> list[PageRecord]:
    if is_bare_wikilink_target(target):
        return pages_by_stem.get(target, [])

    normalized = target.replace("\\", "/").strip("/")
    if normalized.endswith(".md"):
        normalized = normalized[:-3]
    page = pages_by_wiki_target.get(normalized)
    return [page] if page is not None else []


def issue_counts(issues: list[IndexIssue]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for issue in issues:
        counts[issue.code] = counts.get(issue.code, 0) + 1
    return counts


def review_reconcile_counts(findings: list[ReviewFinding]) -> dict[str, int]:
    counts = {bucket: 0 for bucket in REVIEW_RECONCILE_BUCKETS}
    for finding in findings:
        counts[finding.bucket] += 1
    return counts


def markdown_heading_text(line: str) -> tuple[int, str] | None:
    match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line.strip())
    if not match:
        return None
    return len(match.group(1)), match.group(2).strip()


def markdown_list_item_text(line: str) -> str | None:
    match = re.match(r"^\s*(?:[-*+]|\d+[.)])\s+(.+)$", line)
    if not match:
        return None
    text = match.group(1).strip()
    if re.match(r"^\[[ xX]\]\s+", text):
        text = text[3:].strip()
    return text


def is_review_reconcile_section_heading(text: str) -> bool:
    normalized = text.strip().lower().rstrip(":")
    return normalized in {
        "summary",
        "overview",
        "findings",
        "issues",
        "recommendations",
        "validation",
        "next steps",
    }


def parse_review_findings(markdown: str) -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    current_index: int | None = None
    in_fence = False

    for line_number, raw_line in enumerate(markdown.replace("\r\n", "\n").splitlines(), start=1):
        stripped = raw_line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            current_index = None
            continue
        if in_fence:
            continue
        if not stripped:
            current_index = None
            continue

        item_text = markdown_list_item_text(raw_line)
        if item_text is not None:
            findings.append((f"line {line_number}", item_text))
            current_index = len(findings) - 1
            continue

        heading = markdown_heading_text(raw_line)
        if heading is not None:
            level, text = heading
            current_index = None
            if level > 1 and not is_review_reconcile_section_heading(text):
                findings.append((f"line {line_number}", text))
            continue

        if current_index is not None and raw_line[:1].isspace():
            source, text = findings[current_index]
            findings[current_index] = (source, f"{text} {stripped}")

    return findings


def classify_review_finding(text: str) -> str:
    lowered = text.lower()
    for bucket in ["dismissed", "known deferred", "environmental", "pre-existing", "cleanup-caused"]:
        if any(keyword in lowered for keyword in REVIEW_RECONCILE_KEYWORDS[bucket]):
            return bucket
    return "pre-existing"


def collect_review_reconcile(input_path: Path) -> list[ReviewFinding]:
    text = read_text(input_path)
    findings = []
    for source, finding_text in parse_review_findings(text):
        findings.append(
            ReviewFinding(
                source=source,
                text=finding_text,
                bucket=classify_review_finding(finding_text),
            )
        )
    return findings


def collect_index_lint(root: Path, wiki_dir: Path, raw_dir: Path) -> IndexLint:
    pages = load_wiki_pages(root, wiki_dir)
    raw_records = load_raw_records(root, raw_dir)
    wiki_base = (root / wiki_dir).resolve()
    wiki_stems = {page.stem for page in pages}
    raw_stems = {record.path.stem for record in raw_records}
    pages_by_stem: dict[str, list[PageRecord]] = {}
    pages_by_path = {page.path.resolve(): page for page in pages}
    pages_by_wiki_target: dict[str, PageRecord] = {}
    for page in pages:
        pages_by_stem.setdefault(page.stem, []).append(page)
        pages_by_wiki_target[page.wiki_rel_path] = page
        if page.wiki_rel_path.endswith(".md"):
            pages_by_wiki_target[page.wiki_rel_path[:-3]] = page

    index_pages = [page for page in pages if is_index_page(page)]
    issues: list[IndexIssue] = []
    for page in index_pages:
        for line_number, line in enumerate(page.body.splitlines(), start=1):
            if RAW_PATH_RE.search(line):
                issues.append(
                    IndexIssue(
                        code="literal-raw-link",
                        path=page.rel_path,
                        line=line_number,
                        target="raw/",
                        detail=line.strip(),
                    )
                )

            line_targets: list[PageRecord] = []
            for match in WIKILINK_RE.finditer(line):
                target = wikilink_target(match.group(1))
                if not target:
                    continue
                if is_bare_wikilink_target(target) and target in wiki_stems and target in raw_stems:
                    issues.append(
                        IndexIssue(
                            code="ambiguous-bare-link",
                            path=page.rel_path,
                            line=line_number,
                            target=target,
                            detail="bare wikilink target exists in both wiki-pages/ and raw/",
                        )
                    )
                linked_pages = resolve_wikilink_pages(target, pages_by_stem, pages_by_wiki_target)
                if linked_pages:
                    line_targets.extend(linked_pages)
                else:
                    issues.append(
                        IndexIssue(
                            code="missing-target",
                            path=page.rel_path,
                            line=line_number,
                            target=target,
                            detail="wikilink target is missing",
                        )
                    )

            for destination in iter_markdown_link_destinations(line):
                target = markdown_link_target(destination)
                if is_ignored_markdown_target(target):
                    continue
                resolved = resolve_markdown_target(page.path.parent, target, wiki_base)
                if resolved is None:
                    issues.append(
                        IndexIssue(
                            code="missing-target",
                            path=page.rel_path,
                            line=line_number,
                            target=target,
                            detail="markdown relative link target is missing or outside wiki directory",
                        )
                    )
                    continue

                linked_page = pages_by_path.get(resolved)
                if linked_page is not None:
                    line_targets.append(linked_page)

            has_marker = STUB_INDEX_MARKER in line
            for linked_page in line_targets:
                linked_is_stub = normalize_status(linked_page.status) == "stub"
                if linked_is_stub and not has_marker:
                    issues.append(
                        IndexIssue(
                            code="stub-marker-mismatch",
                            path=page.rel_path,
                            line=line_number,
                            target=linked_page.rel_path,
                            detail="stub page is missing index row marker",
                        )
                    )
                elif has_marker and not linked_is_stub:
                    issues.append(
                        IndexIssue(
                            code="stub-marker-mismatch",
                            path=page.rel_path,
                            line=line_number,
                            target=linked_page.rel_path,
                            detail="non-stub page has index row marker",
                        )
                    )

    return IndexLint(scanned_pages=len(index_pages), issues=issues)


def git_status(root: Path) -> list[str]:
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError:
        return ["git status unavailable"]
    if result.returncode != 0:
        return ["git status unavailable"]
    return [line.rstrip() for line in result.stdout.splitlines() if line.strip()]


def status_path(status_line: str) -> str:
    return status_line[3:].strip().strip('"').replace("\\", "/")


def render_status_lines(lines: list[str], limit: int = 80) -> list[str]:
    if not lines:
        return ["- None detected by `git status --short`."]
    rendered = [f"- `{line}`" for line in lines[:limit]]
    if len(lines) > limit:
        rendered.append(f"- ... {len(lines) - limit} more omitted from this handoff snapshot.")
    return rendered


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, text: str) -> None:
    ensure_parent(path)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def resolve_root_relative_dir(root: Path, value: str, arg_name: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        raise ValueError(f"{arg_name} must be root-relative, not absolute: {value}")
    if ".." in path.parts:
        raise ValueError(f"{arg_name} must not contain '..': {value}")

    resolved_root = root.resolve()
    resolved_path = (resolved_root / path).resolve()
    try:
        resolved_path.relative_to(resolved_root)
    except ValueError as error:
        raise ValueError(f"{arg_name} must stay under repository root: {value}") from error
    return resolved_path


def resolve_tasks_dir(root: Path, value: str) -> Path:
    path = Path(value)
    if not path.parts or path.parts[0] != TASKS_DIR_DEFAULT:
        raise ValueError(f"--tasks-dir must point under `{TASKS_DIR_DEFAULT}/`: {value}")
    return resolve_root_relative_dir(root, value, "--tasks-dir")


def _scan_maintenance_reports(tasks_dir: Path, tasks_dir_rel: str) -> list[tuple[str, str]]:
    """Return list of (rel_path, label) for the most recent report of each type found.

    tasks_dir is the resolved absolute Path; tasks_dir_rel is the root-relative posix string
    used to build human-readable paths in the output.
    """
    report_dir = tasks_dir / MAINTENANCE_REPORTS_DIR
    if not report_dir.exists():
        return []

    REPORT_TYPE_LABELS = {
        "ingest-candidates": "latest coverage report",
        "duplicates": "latest duplicates report",
        "status-audit": "latest status audit",
        "index-lint": "latest index lint report",
        "review-reconcile": "latest review reconcile report",
    }

    latest_by_type: dict[str, Path] = {}
    for path in sorted(report_dir.glob("*.md"), reverse=True):
        for prefix in REPORT_TYPE_LABELS:
            candidate_suffix = path.name[len(prefix) + 1:]  # strip "prefix-"
            if path.name.startswith(prefix + "-") and candidate_suffix[:1].isdigit():
                if prefix not in latest_by_type:
                    latest_by_type[prefix] = path
                break

    tasks_rel = tasks_dir_rel.rstrip("/")
    result = []
    for prefix in REPORT_TYPE_LABELS:
        if prefix in latest_by_type:
            path = latest_by_type[prefix]
            rel = f"{tasks_rel}/{MAINTENANCE_REPORTS_DIR}/{path.name}"
            result.append((rel, REPORT_TYPE_LABELS[prefix]))

    blocked_path = tasks_dir / BLOCKED_PATH
    if blocked_path.exists():
        result.append((f"{tasks_rel}/{BLOCKED_PATH}", "blocked pages"))

    return result


def render_handoff(task: str, next_step: str, root: Path, tasks_dir: Path) -> str:
    now = datetime.now().replace(microsecond=0).isoformat()
    status_lines = git_status(root)
    batch_paths = {
        "tools/wiki_maintain.py",
        f"{tasks_dir.as_posix()}/{HANDOFF_PATH}",
        f"{tasks_dir.as_posix()}/{BLOCKED_PATH}",
    }
    dirty_raw = [line for line in status_lines if status_path(line).startswith("raw/")]
    dirty_other = [
        line
        for line in status_lines
        if not status_path(line).startswith("raw/") and status_path(line) not in batch_paths
    ]

    tasks_dir_rel = tasks_dir.as_posix()
    resolved_tasks_dir = (root / tasks_dir).resolve() if not tasks_dir.is_absolute() else tasks_dir.resolve()
    available_reports = _scan_maintenance_reports(resolved_tasks_dir, tasks_dir_rel)

    lines = [
        "# Current Handoff",
        "",
        f"- Generated: {now}",
        f"- Task: {task}",
        f"- Next: {next_step}",
        "",
        "## Current State Summary",
        "",
        "Wiki maintenance v2 report-only tooling is active. Available subcommands:",
        "- `coverage` — compare raw URL vs wiki URL, output ingest candidates",
        "- `duplicates` — find duplicate wiki page URLs, suggest canonical",
        "- `blocked-report` — list pages that cannot be auto-promoted",
        "- `handoff` — this file",
        "- `index-lint` — lint index page links and stub markers",
        "- `status-audit` — audit frontmatter status",
        "- `review-reconcile` — classify review findings",
        "",
        "To start next session: read this file, then run `python tools/wiki_maintain.py blocked-report` and `python tools/wiki_maintain.py coverage --report` to get current state.",
        "",
        "## Available Reports",
        "",
    ]
    if available_reports:
        for rel, label in available_reports:
            lines.append(f"- `{rel}` ({label})")
    else:
        lines.append("No report files found yet in `tasks/maintenance-reports/`.")

    lines.extend(
        [
            "",
            "## Files Touched In This Batch",
            "",
        ]
    )
    lines.extend(f"- `{path}`" for path in sorted(batch_paths))

    lines.extend(
        [
            "",
            "## Validations Passed",
            "",
            "- `python tools/wiki_maintain.py --help` — parser loads without error",
            "- `python tools/wiki_maintain.py handoff --task \"demo\" --next \"demo-next\"` — handoff file written",
            "- `python tools/wiki_maintain.py blocked-report` — blocked pages scanned and categorized by policy_bucket",
            "- `python tools/wiki_maintain.py coverage --report` — ingest candidates report written",
            "- `python tools/wiki_maintain.py duplicates --report` — duplicates report written",
            "",
            "## Explicit Next Step",
            "",
            f"{next_step}",
            "",
            "## Do Not Touch",
            "",
            "- `raw/`",
            "- `wiki-pages/` apply-style writes",
            "- `README.md`",
            "- delegate integration",
            "- index-lint upgrade",
            "",
            "## Dirty But Out Of Scope",
            "",
        ]
    )
    lines.extend(render_status_lines(dirty_other))

    lines.extend(
        [
            "",
            "## Dirty Raw Paths Out Of Scope",
            "",
        ]
    )
    lines.extend(render_status_lines(dirty_raw))

    lines.extend(
        [
            "",
            "## Report Files",
            "",
            f"- `{(tasks_dir / HANDOFF_PATH).as_posix()}`",
            f"- `{(tasks_dir / BLOCKED_PATH).as_posix()}`",
        ]
    )
    return "\n".join(lines)


def render_blocked_report(records: list[BlockedRecord]) -> str:
    today = date.today().isoformat()
    lines = [
        f"# Blocked Content Gaps - {today}",
        "",
        "These pages are report-only inventory items. Do not promote or delete them until source content is recovered or manually reviewed.",
        "",
        "## Summary",
        "",
        f"- Blocked pages: {len(records)}",
        "",
    ]
    if not records:
        lines.extend(["## LingOrm Excluded (excluded-lingorm)", "", "No blocked pages detected."])
        return "\n".join(lines)

    by_reason: dict[str, int] = {}
    for record in records:
        by_reason[record.reason] = by_reason.get(record.reason, 0) + 1
    lines.append("| Reason | Count |")
    lines.append("|---|---:|")
    for reason, count in sorted(by_reason.items()):
        lines.append(f"| {reason} | {count} |")

    lingorm_records = [r for r in records if r.policy_bucket == "excluded-lingorm"]
    nonlingorm_records = [r for r in records if r.policy_bucket == "blocked-nonlingorm"]

    lines.extend(
        [
            "",
            "| Policy Bucket | Count |",
            "|---|---:|",
            f"| excluded-lingorm | {len(lingorm_records)} |",
            f"| blocked-nonlingorm | {len(nonlingorm_records)} |",
        ]
    )

    TABLE_HEADER = [
        "| Category | Page | Reason | Source URL | Raw Match | Next Action |",
        "|---|---|---|---|---|---|",
    ]

    def _render_section_rows(section_records: list[BlockedRecord]) -> list[str]:
        rows = []
        for record in section_records:
            source_url = record.source_url or ""
            raw_match = record.raw_match or ""
            rows.append(
                f"| {record.category} | `{record.path}` | {record.reason} | {source_url} | {raw_match} | {record.next_action} |"
            )
        return rows

    lines.extend(["", "## LingOrm Excluded (excluded-lingorm)", ""])
    if lingorm_records:
        lines.extend(TABLE_HEADER)
        lines.extend(_render_section_rows(lingorm_records))
    else:
        lines.append("No excluded-lingorm pages detected.")

    lines.extend(["", "## Non-LingOrm Blocked (blocked-nonlingorm)", ""])
    if nonlingorm_records:
        lines.extend(TABLE_HEADER)
        lines.extend(_render_section_rows(nonlingorm_records))
    else:
        lines.append("No blocked-nonlingorm pages detected.")

    return "\n".join(lines)


def markdown_cell(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_status_issue_table(records: list[StatusIssue]) -> list[str]:
    if not records:
        return ["None detected."]

    lines = ["| Category | Page | Status | Reason |", "|---|---|---|---|"]
    for record in records:
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_cell(record.category),
                    f"`{markdown_cell(record.path)}`",
                    markdown_cell(record.status),
                    markdown_cell(record.reason),
                ]
            )
            + " |"
        )
    return lines


def render_status_audit_report(audit: StatusAudit, report_date: str, wiki_dir: Path) -> str:
    wiki_glob = f"{wiki_dir.as_posix().rstrip('/')}/**/*.md"
    project_management_dir = (wiki_dir / PROJECT_MANAGEMENT_CATEGORY).as_posix()
    lines = [
        f"# Status Audit - {report_date}",
        "",
        f"This is a report-only audit of `{wiki_glob}`. It excludes `README.md` files and does not modify wiki content.",
        "",
        "## Summary",
        "",
        f"- Scanned markdown pages: {audit.total_pages}",
        f"- Content pages audited: {audit.content_pages}",
        f"- Excluded README files: {len(audit.excluded_readmes)}",
        f"- Missing status pages: {len(audit.missing)}",
        f"- Unknown status pages: {len(audit.unknown)}",
        f"- Misplaced project-management statuses: {len(audit.misplaced_project_management)}",
        f"- Frontmatter author issues: {len(audit.author_issues)}",
        "",
        "## Main Statuses",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for status, count in sorted(audit.main_counts.items()):
        lines.append(f"| {status} | {count} |")

    lines.extend(
        [
            "",
            "## Project-Management Statuses",
            "",
            f"`active` and `legacy` are legal only under `{project_management_dir}/`.",
            "",
            "| Status | Count |",
            "|---|---:|",
        ]
    )
    for status, count in sorted(audit.project_management_counts.items()):
        lines.append(f"| {status} | {count} |")

    lines.extend(["", "## Missing Status", ""])
    lines.extend(render_status_issue_table(audit.missing))

    lines.extend(["", "## Unknown Status", ""])
    lines.extend(render_status_issue_table(audit.unknown))

    lines.extend(["", "## Misplaced Project-Management Statuses", ""])
    lines.extend(render_status_issue_table(audit.misplaced_project_management))

    lines.extend(["", "## Excluded README Files", ""])
    if audit.excluded_readmes:
        lines.extend(f"- `{path}`" for path in audit.excluded_readmes)
    else:
        lines.append("None detected.")

    lines.extend(["", "## Frontmatter Author Issues", ""])
    lines.append("Validates `作者` field. Valid: `[]`, `[\"@handle\"]`, `[\"@a\", \"@b\"]`. Invalid: `[@handle]` (unquoted).")
    lines.append("")
    if audit.author_issues:
        lines.extend(["| Path | Rule | Severity | Actual Value |", "|---|---|---|---|"])
        for issue in audit.author_issues:
            lines.append(
                "| "
                + " | ".join([
                    f"`{markdown_cell(issue.path)}`",
                    markdown_cell(issue.rule),
                    markdown_cell(issue.severity),
                    f"`{markdown_cell(issue.actual_value)}`",
                ])
                + " |"
            )
    else:
        lines.append("No frontmatter author issues detected.")

    return "\n".join(lines)


def render_index_issue_table(issues: list[IndexIssue]) -> list[str]:
    if not issues:
        return ["None detected."]

    lines = ["| Code | Page | Line | Target | Detail |", "|---|---|---:|---|---|"]
    for issue in issues:
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_cell(issue.code),
                    f"`{markdown_cell(issue.path)}`",
                    str(issue.line),
                    f"`{markdown_cell(issue.target)}`",
                    markdown_cell(issue.detail),
                ]
            )
            + " |"
        )
    return lines


def render_index_lint_report(lint: IndexLint, report_date: str, wiki_dir: Path) -> str:
    counts = issue_counts(lint.issues)
    lines = [
        f"# Index Lint - {report_date}",
        "",
        f"This is a report-only lint of index pages under `{wiki_dir.as_posix().rstrip('/')}/index/`. It does not modify wiki content.",
        "",
        "## Summary",
        "",
        f"- Index pages scanned: {lint.scanned_pages}",
        f"- Total issues: {len(lint.issues)}",
        "",
        "| Code | Count |",
        "|---|---:|",
    ]
    for code in ["literal-raw-link", "ambiguous-bare-link", "missing-target", "stub-marker-mismatch"]:
        lines.append(f"| {code} | {counts.get(code, 0)} |")

    lines.extend(["", "## Issues", ""])
    lines.extend(render_index_issue_table(lint.issues))
    return "\n".join(lines)


def render_review_reconcile_report(
    findings: list[ReviewFinding],
    report_date: str,
    input_path: Path,
    root: Path,
) -> str:
    counts = review_reconcile_counts(findings)
    lines = [
        f"# Review Reconcile - {report_date}",
        "",
        f"Input: `{normalize_rel_path(input_path, root)}`",
        "",
        "This is a rule-based classification report. It does not modify wiki content.",
        "",
        "## Summary",
        "",
        f"- Findings classified: {len(findings)}",
        "",
        "| Bucket | Count |",
        "|---|---:|",
    ]
    for bucket in REVIEW_RECONCILE_BUCKETS:
        lines.append(f"| {bucket} | {counts[bucket]} |")

    for bucket in REVIEW_RECONCILE_BUCKETS:
        lines.extend(["", f"## {bucket}", ""])
        bucket_findings = [finding for finding in findings if finding.bucket == bucket]
        if not bucket_findings:
            lines.append("None detected.")
            continue
        for finding in bucket_findings:
            lines.append(f"- {finding.source}: {markdown_cell(finding.text)}")

    return "\n".join(lines)


THREADS_RAW_SUBDIRS = ["threads", "threads-saved", "threads-iphone"]

# Non-content files that live inside raw/threads* but are not thread posts.
# Matched case-insensitively against the file stem (filename without .md).
RAW_EXCLUDED_STEMS: set[str] = {
    "handoff",
    "memory",
    "readme",
    "_template",
    "_index",
    "_project_template",
}

CATEGORY_HINTS: list[tuple[list[str], str]] = [
    (["Claude", "Codex", "Agent", "AI", "LLM", "MCP", "NotebookLM", "Gemini", "OpenAI", "GPT", "Copilot"], "AI 工具"),
    (["履歷", "面試", "求職", "LinkedIn", "HR", "職涯"], "求職履歷"),
    (["泰國", "台北", "美食", "旅遊", "奶茶", "地圖", "食記", "餐廳", "漢堡", "海外"], "旅遊美食"),
    (["運動", "睡眠", "皮質醇", "ADHD", "健康", "健身", "肌肉", "體重", "迷走神經", "腸道"], "健康生活"),
    (["Ling", "Orm", "鄺玲玲", "泰百", "Heart Talk", "LingOrm", "林"], "LingOrm"),
]
DEFAULT_CATEGORY = "生活雜記"


@dataclass(frozen=True)
class CoverageEntry:
    raw_record: RawRecord
    suggested_category: str


@dataclass(frozen=True)
class CoverageResult:
    total_raw: int
    raw_with_url: int
    raw_only: list[CoverageEntry]
    raw_missing_url: list[RawRecord]
    wiki_coverage: int


def categorize_raw_record(record: RawRecord) -> str:
    search_text = record.title + " " + record.path.stem
    for keywords, category in CATEGORY_HINTS:
        for keyword in keywords:
            if keyword.isascii():
                if keyword.lower() in search_text.lower():
                    return category
            else:
                if keyword in search_text:
                    return category
    return DEFAULT_CATEGORY


def load_threads_raw_records(root: Path, raw_dir: Path) -> list[RawRecord]:
    """Load raw records only from the threads subdirectories."""
    base = root / raw_dir
    if not base.exists():
        return []

    records: list[RawRecord] = []
    for subdir_name in THREADS_RAW_SUBDIRS:
        subdir = base / subdir_name
        if not subdir.exists():
            continue
        for path in sorted(subdir.rglob("*.md")):
            if any(part.startswith(".") for part in path.relative_to(subdir).parts):
                continue
            if path.stem.lower() in RAW_EXCLUDED_STEMS:
                continue
            text = read_text(path)
            frontmatter, body = parse_frontmatter(text)
            url = normalize_url(frontmatter.get("url") or frontmatter.get("網址") or "")
            records.append(
                RawRecord(
                    path=path,
                    rel_path=normalize_rel_path(path, root),
                    frontmatter=frontmatter,
                    body=body,
                    url=url,
                    title=frontmatter.get("title") or path.stem,
                )
            )
    return records


def collect_coverage(root: Path, wiki_dir: Path, raw_dir: Path) -> CoverageResult:
    raw_records = load_threads_raw_records(root, raw_dir)
    wiki_pages = load_wiki_pages(root, wiki_dir)

    wiki_urls: set[str] = {page.url for page in wiki_pages if page.url}

    raw_only: list[CoverageEntry] = []
    raw_missing_url: list[RawRecord] = []

    # Load optional exclusion list (repo-relative forward-slash paths)
    exclusion_file = root / "tasks" / "coverage-excluded-raw.txt"
    excluded_raw: set[str] = set()
    if exclusion_file.exists():
        for line in read_text(exclusion_file).splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                excluded_raw.add(line)

    for record in raw_records:
        if record.rel_path in excluded_raw:
            continue
        if not record.url:
            raw_missing_url.append(record)
        elif record.url not in wiki_urls:
            raw_only.append(CoverageEntry(
                raw_record=record,
                suggested_category=categorize_raw_record(record),
            ))

    wiki_coverage = sum(
        1 for record in raw_records
        if record.url and record.url in wiki_urls
    )

    return CoverageResult(
        total_raw=len(raw_records),
        raw_with_url=sum(1 for r in raw_records if r.url),
        raw_only=raw_only,
        raw_missing_url=raw_missing_url,
        wiki_coverage=wiki_coverage,
    )


def render_coverage_report(result: CoverageResult, report_date: str) -> str:
    lines = [
        f"# Ingest Candidates - {report_date}",
        "",
        "> Heuristic category suggestions are rule-based only. Verify before ingesting.",
        "",
        "## Summary",
        "",
        f"- Raw files scanned: {result.total_raw}",
        f"- Raw files with URL: {result.raw_with_url}",
        f"- Raw files missing URL: {len(result.raw_missing_url)}",
        f"- Raw-only URLs (not yet in wiki): {len(result.raw_only)}",
        f"- Wiki coverage: {result.wiki_coverage} already in wiki",
        "",
        "## Raw-Only Candidates",
        "",
    ]

    if result.raw_only:
        lines.extend([
            "| Raw File | URL | Suggested Category |",
            "|---|---|---|",
        ])
        for entry in result.raw_only:
            rel = markdown_cell(entry.raw_record.rel_path)
            url = markdown_cell(entry.raw_record.url)
            cat = markdown_cell(entry.suggested_category)
            lines.append(f"| `{rel}` | {url} | {cat} |")
    else:
        lines.append("No raw-only candidates detected.")

    lines.extend([
        "",
        "## Raw Files Missing URL",
        "",
    ])

    if result.raw_missing_url:
        lines.extend([
            "| Raw File | Title |",
            "|---|---|",
        ])
        for record in result.raw_missing_url:
            rel = markdown_cell(record.rel_path)
            title = markdown_cell(record.title)
            lines.append(f"| `{rel}` | {title} |")
    else:
        lines.append("No raw files missing URL detected.")

    return "\n".join(lines)


def unique_ingest_candidates_report_path(report_dir: Path, report_date: str) -> Path:
    first_path = report_dir / f"ingest-candidates-{report_date}.md"
    if not first_path.exists():
        return first_path

    for index in range(2, 1000):
        path = report_dir / f"ingest-candidates-{report_date}-{index}.md"
        if not path.exists():
            return path

    raise RuntimeError(f"too many ingest candidates reports already exist for {report_date}")


def parse_report_date(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as error:
        raise argparse.ArgumentTypeError("--date must use YYYY-MM-DD format") from error


def unique_status_report_path(report_dir: Path, report_date: str) -> Path:
    first_path = report_dir / f"status-audit-{report_date}.md"
    if not first_path.exists():
        return first_path

    for index in range(2, 1000):
        path = report_dir / f"status-audit-{report_date}-{index}.md"
        if not path.exists():
            return path

    raise RuntimeError(f"too many status audit reports already exist for {report_date}")


def unique_index_lint_report_path(report_dir: Path, report_date: str) -> Path:
    first_path = report_dir / f"index-lint-{report_date}.md"
    if not first_path.exists():
        return first_path

    for index in range(2, 1000):
        path = report_dir / f"index-lint-{report_date}-{index}.md"
        if not path.exists():
            return path

    raise RuntimeError(f"too many index lint reports already exist for {report_date}")


def unique_review_reconcile_report_path(report_dir: Path, report_date: str) -> Path:
    first_path = report_dir / f"review-reconcile-{report_date}.md"
    if not first_path.exists():
        return first_path

    for index in range(2, 1000):
        path = report_dir / f"review-reconcile-{report_date}-{index}.md"
        if not path.exists():
            return path

    raise RuntimeError(f"too many review reconcile reports already exist for {report_date}")


def command_handoff(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    try:
        tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    output_path = tasks_dir / HANDOFF_PATH
    content = render_handoff(args.task, args.next, root, Path(args.tasks_dir))
    write_text(output_path, content)
    print(f"wrote {normalize_rel_path(output_path, root)}")
    return 0


def command_blocked_report(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    records = collect_blocked_records(root, Path(args.wiki_dir), Path(args.raw_dir))
    try:
        tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    output_path = tasks_dir / BLOCKED_PATH
    write_text(output_path, render_blocked_report(records))
    print(f"wrote {normalize_rel_path(output_path, root)}")
    lingorm_count = sum(1 for r in records if r.policy_bucket == "excluded-lingorm")
    nonlingorm_count = sum(1 for r in records if r.policy_bucket == "blocked-nonlingorm")
    print(f"blocked pages: {len(records)}")
    print(f"- excluded-lingorm (LingOrm policy): {lingorm_count}")
    print(f"- blocked-nonlingorm (need manual recovery): {nonlingorm_count}")
    for record in records[:20]:
        print(f"  {record.policy_bucket} | {record.path} [{record.reason}]")
    if len(records) > 20:
        print(f"... and {len(records) - 20} more")
    return 0


def print_status_issue_sample(label: str, records: list[StatusIssue], limit: int = 20) -> None:
    print(f"{label}: {len(records)}")
    for record in records[:limit]:
        status = f" status={record.status}" if record.status else ""
        print(f"- {record.path}{status} [{record.reason}]")
    if len(records) > limit:
        print(f"... and {len(records) - limit} more")


def print_index_issue_sample(issues: list[IndexIssue], limit: int = 20) -> None:
    for issue in issues[:limit]:
        print(f"- {issue.path}:{issue.line} [{issue.code}] {issue.target} - {issue.detail}")
    if len(issues) > limit:
        print(f"... and {len(issues) - limit} more")


def command_status_audit(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    audit = collect_status_audit(root, Path(args.wiki_dir))

    print("status audit")
    print(f"scanned markdown pages: {audit.total_pages}")
    print(f"content pages audited: {audit.content_pages}")
    print(f"excluded README files: {len(audit.excluded_readmes)}")
    for status, count in sorted(audit.main_counts.items()):
        print(f"{status}: {count}")
    for status, count in sorted(audit.project_management_counts.items()):
        print(f"{status} under {PROJECT_MANAGEMENT_CATEGORY}: {count}")
    print_status_issue_sample("missing status pages", audit.missing)
    print_status_issue_sample("unknown status pages", audit.unknown)
    print_status_issue_sample("misplaced project-management statuses", audit.misplaced_project_management)
    print(f"frontmatter author issues: {len(audit.author_issues)}")
    for issue in audit.author_issues[:20]:
        print(f"- {issue.path} [{issue.rule}] ({issue.severity}): {issue.message[:80]}")
    if len(audit.author_issues) > 20:
        print(f"... and {len(audit.author_issues) - 20} more")

    if args.report:
        report_date = args.date or date.today().isoformat()
        try:
            tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
            report_path = unique_status_report_path(tasks_dir / MAINTENANCE_REPORTS_DIR, report_date)
        except (RuntimeError, ValueError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        write_text(report_path, render_status_audit_report(audit, report_date, Path(args.wiki_dir)))
        print(f"wrote {normalize_rel_path(report_path, root)}")

    return 0


def command_index_lint(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    lint = collect_index_lint(root, Path(args.wiki_dir), Path(args.raw_dir))
    counts = issue_counts(lint.issues)

    print("index lint")
    print(f"index pages scanned: {lint.scanned_pages}")
    print(f"total issues: {len(lint.issues)}")
    for code in ["literal-raw-link", "ambiguous-bare-link", "missing-target", "stub-marker-mismatch"]:
        print(f"{code}: {counts.get(code, 0)}")
    print_index_issue_sample(lint.issues)

    if args.report:
        report_date = args.date or date.today().isoformat()
        try:
            tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
            report_path = unique_index_lint_report_path(tasks_dir / MAINTENANCE_REPORTS_DIR, report_date)
        except (RuntimeError, ValueError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        write_text(report_path, render_index_lint_report(lint, report_date, Path(args.wiki_dir)))
        print(f"wrote {normalize_rel_path(report_path, root)}")

    return 0


def command_review_reconcile(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = root / input_path
    input_path = input_path.resolve()
    if not input_path.exists() or not input_path.is_file():
        print(f"error: input file does not exist: {args.input}", file=sys.stderr)
        return 2

    findings = collect_review_reconcile(input_path)
    counts = review_reconcile_counts(findings)

    print("review reconcile")
    print(f"findings classified: {len(findings)}")
    for bucket in REVIEW_RECONCILE_BUCKETS:
        print(f"{bucket}: {counts[bucket]}")

    report_date = args.date or date.today().isoformat()
    try:
        tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
        report_path = unique_review_reconcile_report_path(tasks_dir / MAINTENANCE_REPORTS_DIR, report_date)
    except (RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    write_text(report_path, render_review_reconcile_report(findings, report_date, input_path, root))
    print(f"wrote {normalize_rel_path(report_path, root)}")
    return 0


def command_coverage(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    result = collect_coverage(root, Path(args.wiki_dir), Path(args.raw_dir))

    print("coverage")
    print(f"raw files scanned: {result.total_raw}")
    print(f"raw files with URL: {result.raw_with_url}")
    print(f"raw files missing URL: {len(result.raw_missing_url)}")
    print(f"raw-only (not yet in wiki): {len(result.raw_only)}")
    print(f"wiki coverage: {result.wiki_coverage} already in wiki")

    if args.report:
        report_date = args.date or date.today().isoformat()
        try:
            tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
            report_path = unique_ingest_candidates_report_path(tasks_dir / MAINTENANCE_REPORTS_DIR, report_date)
        except (RuntimeError, ValueError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        write_text(report_path, render_coverage_report(result, report_date))
        print(f"wrote {normalize_rel_path(report_path, root)}")

    return 0


STATUS_RANK = {"reference": 0, "wiki": 1, "stub": 2}


@dataclass(frozen=True)
class DuplicatePageEntry:
    page: PageRecord
    is_hub: bool
    index_refs: int


@dataclass(frozen=True)
class DuplicateGroup:
    url: str
    pages: list[DuplicatePageEntry]
    suggested_canonical: str


@dataclass(frozen=True)
class DuplicatesResult:
    total_pages: int
    pages_with_url: int
    pages_without_url: int
    groups: list[DuplicateGroup]


def is_hub_page(page: PageRecord) -> bool:
    body = page.body
    has_sources = "## Sources" in body or "## 來源" in body
    wikilink_count = len(WIKILINK_RE.findall(body))
    return has_sources and wikilink_count >= 2


def _status_rank(status: str) -> int:
    return STATUS_RANK.get(normalize_status(status), 3)


def _canonical_sort_key(entry: DuplicatePageEntry) -> tuple:
    page = entry.page
    return (
        _status_rank(page.status),
        1 if is_index_page(page) else 0,
        -len(page.body),
        len(page.rel_path),
        page.rel_path,
    )


def _count_index_refs(page: PageRecord, all_pages: list[PageRecord]) -> int:
    stem = page.stem
    count = 0
    for other in all_pages:
        if other.path == page.path:
            continue
        for match in WIKILINK_RE.finditer(other.body):
            if wikilink_target(match.group(1)) == stem:
                count += 1
                break  # count this page once even if stem referenced multiple times
    return count


def collect_duplicates(root: Path, wiki_dir: Path) -> DuplicatesResult:
    pages = load_wiki_pages(root, wiki_dir)
    total_pages = len(pages)
    pages_with_url = sum(1 for p in pages if p.url)
    pages_without_url = total_pages - pages_with_url

    by_url: dict[str, list[PageRecord]] = {}
    for page in pages:
        if page.url:
            by_url.setdefault(page.url, []).append(page)

    groups: list[DuplicateGroup] = []
    for url, url_pages in sorted(by_url.items()):
        if len(url_pages) < 2:
            continue
        entries: list[DuplicatePageEntry] = []
        for page in url_pages:
            hub = is_hub_page(page)
            refs = _count_index_refs(page, pages)
            entries.append(DuplicatePageEntry(page=page, is_hub=hub, index_refs=refs))

        sorted_entries = sorted(entries, key=_canonical_sort_key)
        suggested_canonical = sorted_entries[0].page.rel_path
        groups.append(DuplicateGroup(url=url, pages=sorted_entries, suggested_canonical=suggested_canonical))

    return DuplicatesResult(
        total_pages=total_pages,
        pages_with_url=pages_with_url,
        pages_without_url=pages_without_url,
        groups=groups,
    )


def render_duplicates_report(result: DuplicatesResult, report_date: str) -> str:
    total_in_groups = sum(len(g.pages) for g in result.groups)
    lines = [
        f"# Duplicate URL Report - {report_date}",
        "",
        "This is a report-only scan. No files were modified.",
        "",
        "> Note: Hub pages (pages with `## Sources` and multiple wikilinks) are annotated",
        "> but still listed. Manual review is required before merging or deleting.",
        "",
        "## Summary",
        "",
        f"- Wiki pages scanned: {result.total_pages}",
        f"- Pages with URL: {result.pages_with_url}",
        f"- Pages without URL: {result.pages_without_url}",
        f"- Duplicate URL groups: {len(result.groups)}",
        f"- Total pages in duplicate groups: {total_in_groups}",
    ]

    if not result.groups:
        lines.extend(["", "## Duplicate URL Groups", "", "No duplicate URLs detected."])
        return "\n".join(lines)

    lines.extend(["", "## Duplicate URL Groups", ""])
    for group_index, group in enumerate(result.groups, start=1):
        lines.extend([
            f"### Group {group_index} — {group.url}",
            "",
            f"Suggested canonical: `{group.suggested_canonical}`",
            "",
            "| Status | Is Hub | Path | Body chars | Index refs |",
            "|---|---|---|---:|---:|",
        ])
        for entry in group.pages:
            status = markdown_cell(entry.page.status or "(none)")
            is_hub = "yes" if entry.is_hub else "no"
            path = markdown_cell(entry.page.rel_path)
            body_chars = len(entry.page.body)
            refs = entry.index_refs
            lines.append(f"| {status} | {is_hub} | `{path}` | {body_chars} | {refs} |")

        canonical_path = group.suggested_canonical
        lines.extend([
            "",
            "Suggested action:",
            f"- Keep `{canonical_path}` as canonical.",
            "- Merge useful content from other pages.",
            "- Replace wikilinks pointing to duplicates.",
            "- Delete duplicates after review.",
            "",
        ])

    return "\n".join(lines)


def unique_duplicates_report_path(report_dir: Path, report_date: str) -> Path:
    first_path = report_dir / f"duplicates-{report_date}.md"
    if not first_path.exists():
        return first_path

    for index in range(2, 1000):
        path = report_dir / f"duplicates-{report_date}-{index}.md"
        if not path.exists():
            return path

    raise RuntimeError(f"too many duplicates reports already exist for {report_date}")


def command_duplicates(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    result = collect_duplicates(root, Path(args.wiki_dir))
    total_in_groups = sum(len(g.pages) for g in result.groups)

    print("duplicates")
    print(f"wiki pages scanned: {result.total_pages}")
    print(f"pages with URL: {result.pages_with_url}")
    print(f"pages without URL: {result.pages_without_url}")
    print(f"duplicate URL groups: {len(result.groups)}")
    print(f"total pages in duplicate groups: {total_in_groups}")
    for group in result.groups[:20]:
        print(f"- {group.url} ({len(group.pages)} pages, canonical: {group.suggested_canonical})")
    if len(result.groups) > 20:
        print(f"... and {len(result.groups) - 20} more groups")

    if args.report:
        report_date = args.date or date.today().isoformat()
        try:
            tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
            report_path = unique_duplicates_report_path(tasks_dir / MAINTENANCE_REPORTS_DIR, report_date)
        except (RuntimeError, ValueError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        write_text(report_path, render_duplicates_report(result, report_date))
        print(f"wrote {normalize_rel_path(report_path, root)}")

    return 0


@dataclass(frozen=True)
class FrontmatterIssue:
    path: str            # repo-relative path (e.g. "wiki-pages/...")
    field: str           # field name (e.g. "作者")
    actual_value: str    # raw frontmatter value string
    rule: str            # error/warn code
    message: str         # human-readable explanation
    severity: str        # "error" or "warn"


def _parse_author_raw_value(raw_value: str) -> tuple[str, list[str]]:
    value = raw_value.strip()
    if not value or value in ("[]", "[ ]"):
        return "empty", []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return "empty", []
        elements = [e.strip() for e in inner.split(",")]
        return "list", elements
    return "non-list", [value]


def validate_author_field(path: str, raw_value: str) -> list[FrontmatterIssue]:
    """Validate the 作者 frontmatter field. Returns list of issues (empty = valid)."""
    value = raw_value.strip() if raw_value else ""
    if not value:
        return []  # missing field is OK

    value_type, elements = _parse_author_raw_value(value)

    if value_type == "non-list":
        return [FrontmatterIssue(
            path=path,
            field="作者",
            actual_value=raw_value,
            rule="invalid-author-field-type",
            message=f"作者 must be a YAML list (e.g. [\"@handle\"] or []); got: {raw_value!r}",
            severity="error",
        )]

    if value_type == "empty":
        return []

    # value_type == "list"
    issues: list[FrontmatterIssue] = []
    for element in elements:
        is_double_quoted = len(element) >= 2 and element[0] == '"' and element[-1] == '"'
        is_single_quoted = len(element) >= 2 and element[0] == "'" and element[-1] == "'"

        if not (is_double_quoted or is_single_quoted):
            issues.append(FrontmatterIssue(
                path=path,
                field="作者",
                actual_value=raw_value,
                rule="invalid-author-bracket-format",
                message=f"作者 array element must be quoted (e.g. \"@handle\"); got unquoted: {element!r}",
                severity="error",
            ))
        elif is_single_quoted:
            issues.append(FrontmatterIssue(
                path=path,
                field="作者",
                actual_value=raw_value,
                rule="noncanonical-author-quote-style",
                message=f"作者 array element uses single quotes; prefer double quotes: {element!r}",
                severity="warn",
            ))

    return issues


def collect_frontmatter_issues(pages: list[PageRecord]) -> list[FrontmatterIssue]:
    """Collect all frontmatter constraint violations across wiki pages."""
    issues: list[FrontmatterIssue] = []
    for page in pages:
        raw_author = page.frontmatter.get("作者", "")
        issues.extend(validate_author_field(page.rel_path, raw_author))
    return issues


def normalize_author_in_file(path: Path, dry_run: bool = True) -> tuple[bool, str, str]:
    """Fix 作者 field in a single wiki page file.

    Returns (changed, old_value, new_value).
    Only touches the 作者: line in frontmatter block. Leaves everything else intact.
    """
    text = read_text(path)
    lines = text.splitlines(keepends=True)

    if not lines or lines[0].rstrip("\r\n") != "---":
        return False, "", ""

    end_index = None
    for i, line in enumerate(lines[1:], start=1):
        if line.rstrip("\r\n") == "---":
            end_index = i
            break
    if end_index is None:
        return False, "", ""

    for i in range(1, end_index):
        if ":" not in lines[i]:
            continue
        key, value = lines[i].split(":", 1)
        if key.strip() != "作者":
            continue

        raw = value.strip()
        if not raw or raw.startswith("["):
            return False, raw, raw

        handle = raw.lstrip("@")
        canonical = f'["@{handle}"]'

        if not dry_run:
            ending = ""
            if lines[i].endswith("\r\n"):
                ending = "\r\n"
            elif lines[i].endswith("\n"):
                ending = "\n"
            lines[i] = f"作者: {canonical}{ending}"
            path.write_text("".join(lines), encoding="utf-8")

        return True, raw, canonical

    return False, "", ""


def command_author_fix(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    wiki_dir = Path(args.wiki_dir)
    pages = load_wiki_pages(root, wiki_dir)
    issues = collect_frontmatter_issues(pages)

    fixable = [i for i in issues if i.rule == "invalid-author-field-type"]

    if not fixable:
        print("No author issues to fix.")
        return 0

    dry_run = not args.apply
    mode = "DRY RUN" if dry_run else "APPLYING"
    print(f"[{mode}] Found {len(fixable)} author issues\n")

    fixed = 0
    errors: list[tuple[str, str]] = []
    for issue in fixable:
        page_path = root / issue.path
        try:
            changed, old, new = normalize_author_in_file(page_path, dry_run=dry_run)
            if changed:
                fixed += 1
                print(f"  {'WOULD FIX' if dry_run else 'FIXED'}: {issue.path}")
                print(f"    {old!r} → {new!r}")
        except Exception as exc:
            errors.append((issue.path, str(exc)))
            print(f"  ERROR: {issue.path}: {exc}")

    print(f"\n{'Would fix' if dry_run else 'Fixed'}: {fixed}/{len(fixable)}")
    if errors:
        print(f"Errors: {len(errors)}")
    if dry_run and fixed:
        print("\nRe-run with --apply to write changes.")
    return 0


# ---------------------------------------------------------------------------
# bare-link-fix: rewrite ambiguous [[wikilinks]] to explicit relative links
# ---------------------------------------------------------------------------


def collect_ambiguous_bare_links(
    root: Path, wiki_dir: Path, raw_dir: Path
) -> tuple[list[IndexIssue], dict[str, list[PageRecord]]]:
    """Return ambiguous-bare-link issues and a stem->pages lookup."""
    lint = collect_index_lint(root, wiki_dir, raw_dir)
    issues = [i for i in lint.issues if i.code == "ambiguous-bare-link"]
    pages = load_wiki_pages(root, wiki_dir)
    by_stem: dict[str, list[PageRecord]] = {}
    for page in pages:
        by_stem.setdefault(page.stem, []).append(page)
    return issues, by_stem


def resolve_bare_link_replacement(
    index_file: Path, target_stem: str, pages_by_stem: dict[str, list[PageRecord]]
) -> str | None:
    """Build the explicit Markdown link text for a bare wikilink target.

    Returns e.g. ``[title](<../AI 工具/page.md>)`` or *None* if the target
    cannot be resolved to a single wiki page.
    """
    candidates = pages_by_stem.get(target_stem, [])
    # Filter out index pages – the link should point to a content page.
    non_index = [p for p in candidates if not is_index_page(p)]
    if len(non_index) == 1:
        target_page = non_index[0]
    elif len(candidates) == 1:
        target_page = candidates[0]
    else:
        return None  # ambiguous or missing

    # Compute a relative path from the index file's directory to the target.
    try:
        rel = Path(target_page.path.resolve()).relative_to(
            index_file.parent.resolve()
        )
    except ValueError:
        # Fallback: use os-level relpath
        import os

        rel = Path(os.path.relpath(target_page.path.resolve(), index_file.parent.resolve()))

    rel_posix = rel.as_posix()
    return f"[{target_stem}](<{rel_posix}>)"


def fix_bare_links_in_file(
    file_path: Path,
    targets: set[str],
    pages_by_stem: dict[str, list[PageRecord]],
    dry_run: bool = True,
) -> list[tuple[str, str, str]]:
    """Rewrite ambiguous bare wikilinks in *file_path*.

    Returns a list of (target, old_fragment, new_fragment) for each replacement.
    """
    text = read_text(file_path)
    replacements: list[tuple[str, str, str]] = []

    def _replace(match: re.Match[str]) -> str:
        inner = match.group(1)
        target = wikilink_target(inner)
        if target not in targets:
            return match.group(0)
        new_link = resolve_bare_link_replacement(file_path, target, pages_by_stem)
        if new_link is None:
            return match.group(0)
        replacements.append((target, match.group(0), new_link))
        return new_link

    new_text = WIKILINK_RE.sub(_replace, text)

    if not dry_run and replacements:
        file_path.write_text(new_text, encoding="utf-8")

    return replacements


def command_bare_link_fix(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    wiki_dir = Path(args.wiki_dir)
    raw_dir = Path(args.raw_dir)

    issues, pages_by_stem = collect_ambiguous_bare_links(root, wiki_dir, raw_dir)

    if not issues:
        print("No ambiguous bare links to fix.")
        return 0

    # Group issues by file so we process each file once.
    from collections import defaultdict

    by_file: dict[str, set[str]] = defaultdict(set)
    for issue in issues:
        by_file[issue.path].add(issue.target)

    dry_run = not args.apply
    mode = "DRY RUN" if dry_run else "APPLYING"
    print(f"[{mode}] Found {len(issues)} ambiguous bare links across {len(by_file)} files\n")

    total_fixed = 0
    all_results: list[tuple[str, str, str, str]] = []  # (file, target, old, new)
    errors: list[tuple[str, str]] = []

    for rel_path, targets in sorted(by_file.items()):
        file_path = root / rel_path
        try:
            replacements = fix_bare_links_in_file(
                file_path, targets, pages_by_stem, dry_run=dry_run
            )
            for target, old, new in replacements:
                total_fixed += 1
                all_results.append((rel_path, target, old, new))
        except Exception as exc:
            errors.append((rel_path, str(exc)))
            print(f"  ERROR: {rel_path}: {exc}")

    # Print results
    for rel_path, target, old, new in all_results:
        verb = "WOULD FIX" if dry_run else "FIXED"
        print(f"  [{verb}] {rel_path}")
        print(f"    {old} -> {new}")

    # Verify that resolved paths point to real files
    unresolved = len(issues) - total_fixed
    print(f"\n{'Would fix' if dry_run else 'Fixed'}: {total_fixed}/{len(issues)}")
    if unresolved:
        print(f"Unresolved (ambiguous or missing): {unresolved}")
    if errors:
        print(f"Errors: {len(errors)}")
    if dry_run and total_fixed:
        print("\nRe-run with --apply to write changes.")
    return 0


@dataclass(frozen=True)
class CanonicalGuardIssue:
    canonical: str  # repo-relative canonical path (forward slashes)
    stale: str      # repo-relative stale path (forward slashes)


@dataclass(frozen=True)
class CanonicalGuardResult:
    stale_conflicts: list[CanonicalGuardIssue]
    author_issues: list[FrontmatterIssue]
    total_pages: int


def collect_canonical_guard(root: Path, wiki_dir: Path) -> CanonicalGuardResult:
    """Detect stale file conflicts (canonical vs restored-stale) and author frontmatter violations."""
    pages = load_wiki_pages(root, wiki_dir)

    stale_conflicts: list[CanonicalGuardIssue] = []
    for canonical_rel, stale_rel in CANONICAL_GUARD_PAIRS:
        stale_path = root / Path(stale_rel)
        if stale_path.exists():
            stale_conflicts.append(CanonicalGuardIssue(
                canonical=canonical_rel,
                stale=stale_rel,
            ))

    author_issues = collect_frontmatter_issues(pages)

    return CanonicalGuardResult(
        stale_conflicts=stale_conflicts,
        author_issues=author_issues,
        total_pages=len(pages),
    )


def unique_canonical_guard_report_path(report_dir: Path, report_date: str) -> Path:
    first_path = report_dir / f"canonical-guard-{report_date}.md"
    if not first_path.exists():
        return first_path

    for index in range(2, 1000):
        path = report_dir / f"canonical-guard-{report_date}-{index}.md"
        if not path.exists():
            return path

    raise RuntimeError(f"too many canonical-guard reports already exist for {report_date}")


def render_canonical_guard_report(result: CanonicalGuardResult, report_date: str) -> str:
    lines = [
        f"# Canonical Guard - {report_date}",
        "",
        "This is a report-only guard. No files were modified.",
        "",
        "## Summary",
        "",
        f"- Scanned wiki pages: {result.total_pages}",
        f"- Stale file conflicts: {len(result.stale_conflicts)}",
        f"- Frontmatter author issues: {len(result.author_issues)}",
        "",
        "## Stale File Conflicts",
        "",
        "Stale files are old or renamed copies that must not coexist with their canonical counterpart.",
        "",
    ]
    if result.stale_conflicts:
        lines.extend(["| Canonical | Stale | Action |", "|---|---|---|"])
        for issue in result.stale_conflicts:
            lines.append(f"| `{markdown_cell(issue.canonical)}` | `{markdown_cell(issue.stale)}` | merge-then-delete |")
    else:
        lines.append("No stale file conflicts detected.")

    lines.extend([
        "",
        "## Frontmatter Author Issues",
        "",
        "Validates `作者` field. Valid: `[]`, `[\"@handle\"]`, `[\"@a\", \"@b\"]`. Invalid: `[@handle]` (unquoted).",
        "",
    ])
    if result.author_issues:
        lines.extend(["| Path | Rule | Severity | Actual Value |", "|---|---|---|---|"])
        for issue in result.author_issues:
            lines.append(
                "| "
                + " | ".join([
                    f"`{markdown_cell(issue.path)}`",
                    markdown_cell(issue.rule),
                    markdown_cell(issue.severity),
                    f"`{markdown_cell(issue.actual_value)}`",
                ])
                + " |"
            )
    else:
        lines.append("No frontmatter author issues detected.")

    return "\n".join(lines)


def command_canonical_guard(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    result = collect_canonical_guard(root, Path(args.wiki_dir))

    print("canonical-guard")
    print(f"stale file conflicts: {len(result.stale_conflicts)}")
    for issue in result.stale_conflicts:
        print("ERROR canonical-stale-file")
        print(f"  canonical: {issue.canonical}")
        print(f"  stale: {issue.stale}")
        print("  action: merge-then-delete")
    print(f"frontmatter author issues: {len(result.author_issues)}")
    for issue in result.author_issues[:20]:
        print(f"- {issue.path} [{issue.rule}] ({issue.severity}): {issue.message[:80]}")
    if len(result.author_issues) > 20:
        print(f"... and {len(result.author_issues) - 20} more")

    if args.report:
        report_date = args.date or date.today().isoformat()
        try:
            tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
            report_path = unique_canonical_guard_report_path(tasks_dir / MAINTENANCE_REPORTS_DIR, report_date)
        except (RuntimeError, ValueError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        write_text(report_path, render_canonical_guard_report(result, report_date))
        print(f"wrote {normalize_rel_path(report_path, root)}")

    return 0


# ---------------------------------------------------------------------------
# scan aggregator
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ScanSectionSummary:
    name: str
    errors: int
    warnings: int
    info: int


@dataclass(frozen=True)
class ScanResult:
    status_audit: StatusAudit
    canonical_guard: CanonicalGuardResult
    index_lint: IndexLint
    coverage: CoverageResult
    duplicates: DuplicatesResult
    blocked: list[BlockedRecord]
    inject_pending: InjectPendingResult | None = None


def _section_summary(name: str, errors: int = 0, warnings: int = 0, info: int = 0) -> ScanSectionSummary:
    return ScanSectionSummary(name=name, errors=errors, warnings=warnings, info=info)


def collect_scan(
    root: Path,
    wiki_dir: Path,
    raw_dir: Path,
    pending_dir: Path | None = None,
) -> ScanResult:
    ip = (
        collect_inject_pending(pending_dir, root, wiki_dir)
        if pending_dir is not None
        else None
    )
    return ScanResult(
        status_audit=collect_status_audit(root, wiki_dir),
        canonical_guard=collect_canonical_guard(root, wiki_dir),
        index_lint=collect_index_lint(root, wiki_dir, raw_dir),
        coverage=collect_coverage(root, wiki_dir, raw_dir),
        duplicates=collect_duplicates(root, wiki_dir),
        blocked=collect_blocked_records(root, wiki_dir, raw_dir),
        inject_pending=ip,
    )


def _scan_section_summaries(result: ScanResult) -> list[ScanSectionSummary]:
    sa = result.status_audit
    cg = result.canonical_guard
    il = result.index_lint
    cv = result.coverage
    dp = result.duplicates
    bl = result.blocked

    status_errors = len(sa.missing) + len(sa.unknown) + len(sa.misplaced_project_management)
    author_errors = len(sa.author_issues)

    lint_errors = sum(1 for i in il.issues if i.code in ("literal-raw-link", "missing-target"))
    lint_warnings = sum(1 for i in il.issues if i.code in ("ambiguous-bare-link", "stub-marker-mismatch"))

    blocked_nonlingorm = sum(1 for b in bl if b.policy_bucket == "blocked-nonlingorm")
    blocked_lingorm = sum(1 for b in bl if b.policy_bucket == "excluded-lingorm")

    summaries = [
        _section_summary("status-audit", errors=status_errors),
        _section_summary("author-validation", errors=author_errors),
        _section_summary("canonical-guard", errors=len(cg.stale_conflicts)),
        _section_summary("index-lint", errors=lint_errors, warnings=lint_warnings),
        _section_summary("coverage", info=len(cv.raw_only), warnings=len(cv.raw_missing_url)),
        _section_summary("duplicates", errors=sum(len(g.pages) for g in dp.groups)),
        _section_summary("blocked-nonlingorm", warnings=blocked_nonlingorm),
        _section_summary("blocked-lingorm", info=blocked_lingorm),
    ]
    if result.inject_pending is not None:
        ip = result.inject_pending
        summaries.append(_section_summary(
            "inject-pending",
            info=len(ip.eligible),
            warnings=len(ip.duplicate_match),
        ))
    return summaries


def render_scan_report(result: ScanResult, report_date: str) -> str:
    sections = _scan_section_summaries(result)
    total_e = sum(s.errors for s in sections)
    total_w = sum(s.warnings for s in sections)
    total_i = sum(s.info for s in sections)

    lines = [
        f"# Wiki Maintenance Report - {report_date}",
        "",
        "## Summary",
        "",
        "| Check | Errors | Warnings | Info |",
        "|---|---:|---:|---:|",
    ]
    for s in sections:
        lines.append(f"| {s.name} | {s.errors} | {s.warnings} | {s.info} |")
    lines.append(f"| **Total** | **{total_e}** | **{total_w}** | **{total_i}** |")
    lines.append("")

    sa = result.status_audit
    lines.extend([
        "## Status Audit",
        "",
        f"- Content pages: {sa.content_pages}",
        f"- wiki: {sa.main_counts.get('wiki', 0)}, reference: {sa.main_counts.get('reference', 0)}, stub: {sa.main_counts.get('stub', 0)}",
        "",
    ])
    if sa.missing:
        lines.append("### Missing Status")
        lines.append("")
        for issue in sa.missing:
            lines.append(f"- `{issue.path}`")
        lines.append("")
    if sa.author_issues:
        lines.append(f"### Author Validation Issues ({len(sa.author_issues)})")
        lines.append("")
        for issue in sa.author_issues[:20]:
            lines.append(f"- `{issue.path}` [{issue.rule}]: {issue.message}")
        if len(sa.author_issues) > 20:
            lines.append(f"- ... and {len(sa.author_issues) - 20} more")
        lines.append("")

    cg = result.canonical_guard
    if cg.stale_conflicts:
        lines.extend(["## Canonical Guard", ""])
        for conflict in cg.stale_conflicts:
            lines.append(f"- ERROR stale: `{conflict.stale}` (canonical: `{conflict.canonical}`)")
        lines.append("")

    il = result.index_lint
    if il.issues:
        lines.extend(["## Index Lint", ""])
        by_code: dict[str, list[IndexIssue]] = {}
        for issue in il.issues:
            by_code.setdefault(issue.code, []).append(issue)
        for code, issues in sorted(by_code.items()):
            lines.append(f"### {code} ({len(issues)})")
            lines.append("")
            for issue in issues[:15]:
                lines.append(f"- `{issue.path}`:{issue.line} → {issue.target}: {issue.detail}")
            if len(issues) > 15:
                lines.append(f"- ... and {len(issues) - 15} more")
            lines.append("")

    cv = result.coverage
    lines.extend([
        "## Coverage",
        "",
        f"- Raw scanned: {cv.total_raw}, with URL: {cv.raw_with_url}",
        f"- Raw-only (not in wiki): {len(cv.raw_only)}",
        f"- Missing URL: {len(cv.raw_missing_url)}",
        f"- Wiki coverage: {cv.wiki_coverage}",
        "",
    ])
    if cv.raw_only:
        lines.extend(["| Raw File | Suggested Category |", "|---|---|"])
        for entry in cv.raw_only:
            lines.append(f"| `{entry.raw_record.rel_path}` | {entry.suggested_category} |")
        lines.append("")
    if cv.raw_missing_url:
        lines.extend(["### Missing URL", ""])
        for record in cv.raw_missing_url:
            lines.append(f"- `{record.rel_path}`")
        lines.append("")

    dp = result.duplicates
    if dp.groups:
        lines.extend(["## Duplicates", ""])
        for group in dp.groups:
            lines.append(f"### {group.url}")
            lines.append(f"Suggested canonical: `{group.suggested_canonical}`")
            lines.append("")
            for entry in group.pages:
                hub = " (hub)" if entry.is_hub else ""
                lines.append(f"- `{entry.page.rel_path}` [status: {entry.page.status}]{hub}")
            lines.append("")

    bl = result.blocked
    nonlingorm = [b for b in bl if b.policy_bucket == "blocked-nonlingorm"]
    lingorm = [b for b in bl if b.policy_bucket == "excluded-lingorm"]
    if nonlingorm:
        lines.extend([f"## Blocked Non-LingOrm ({len(nonlingorm)})", ""])
        for b in nonlingorm:
            lines.append(f"- `{b.path}` [{b.reason}]")
        lines.append("")
    if lingorm:
        lines.extend([f"## Blocked LingOrm Excluded ({len(lingorm)})", ""])
        lines.append(f"{len(lingorm)} LingOrm stubs excluded by policy.")
        lines.append("")

    if result.inject_pending is not None:
        ip = result.inject_pending
        lines += [
            "## Inject Pending",
            "",
            f"- Eligible for injection: {len(ip.eligible)}",
            f"- Already filled: {len(ip.already_filled)}",
            f"- LingOrm skipped: {len(ip.lingorm_skipped)}",
            f"- No wiki match: {len(ip.no_match)}",
            f"- Duplicate match: {len(ip.duplicate_match)}",
            f"- Missing URL: {len(ip.pending_missing_url)}",
            "",
        ]
        if ip.eligible:
            lines += ["### Eligible", ""]
            for entry in ip.eligible:
                lines.append(
                    f"- `{entry.pending.rel_path}` → `{entry.wiki_page.rel_path}` [{entry.new_status}]"
                )
            lines.append("")

    lines.extend([
        "## Suggested Next Agent Prompt",
        "",
        "```text",
        f"請依照 tasks/maintenance-reports/maintenance-report-{report_date}.md，只處理 Errors。",
        "LingOrm stub 保留。",
        "先提出修復計畫，不要直接大批刪檔。",
        "```",
    ])

    return "\n".join(lines)


def unique_scan_report_path(report_dir: Path, report_date: str) -> Path:
    first_path = report_dir / f"maintenance-report-{report_date}.md"
    if not first_path.exists():
        return first_path
    for index in range(2, 1000):
        path = report_dir / f"maintenance-report-{report_date}-{index}.md"
        if not path.exists():
            return path
    raise RuntimeError(f"too many scan reports already exist for {report_date}")


def command_scan(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    wiki_dir = Path(args.wiki_dir)
    raw_dir = Path(args.raw_dir)
    pending_dir = Path(args.pending_dir).resolve() if args.pending_dir else None

    print("scan: running all report-only checks...")
    result = collect_scan(root, wiki_dir, raw_dir, pending_dir=pending_dir)
    sections = _scan_section_summaries(result)

    total_e = sum(s.errors for s in sections)
    total_w = sum(s.warnings for s in sections)
    total_i = sum(s.info for s in sections)

    for s in sections:
        if s.errors or s.warnings or s.info:
            print(f"  {s.name}: errors={s.errors} warnings={s.warnings} info={s.info}")

    print(f"totals: errors={total_e} warnings={total_w} info={total_i}")

    if args.report:
        report_date = args.date or date.today().isoformat()
        try:
            tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
            report_path = unique_scan_report_path(tasks_dir / MAINTENANCE_REPORTS_DIR, report_date)
        except (RuntimeError, ValueError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        write_text(report_path, render_scan_report(result, report_date))
        print(f"wrote {normalize_rel_path(report_path, root)}")

    return 0


# ---------------------------------------------------------------------------
# pending-match: compare external pending digest URLs against wiki URLs
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PendingRecord:
    path: Path
    rel_path: str          # relative to pending_dir
    url: str
    title: str


def load_pending_records(pending_dir: Path) -> list[PendingRecord]:
    """Load all .md files from an external pending digest directory."""
    records: list[PendingRecord] = []
    if not pending_dir.exists():
        return records
    for path in sorted(pending_dir.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(pending_dir).parts):
            continue
        text = read_text(path)
        frontmatter, _body = parse_frontmatter(text)
        url = normalize_url(frontmatter.get("url") or frontmatter.get("網址") or "")
        title = frontmatter.get("title") or path.stem
        try:
            rel = path.relative_to(pending_dir).as_posix()
        except ValueError:
            rel = path.name
        records.append(PendingRecord(path=path, rel_path=rel, url=url, title=title))
    return records


@dataclass(frozen=True)
class PendingMatchResult:
    matched_one: list[tuple[PendingRecord, PageRecord]]       # exactly 1 wiki match
    no_match: list[PendingRecord]                             # 0 wiki matches
    duplicate_match: list[tuple[PendingRecord, list[PageRecord]]]  # >1 wiki matches
    pending_missing_url: list[PendingRecord]                  # pending has no url


def collect_pending_match(pending_dir: Path, root: Path, wiki_dir: Path) -> PendingMatchResult:
    pending_records = load_pending_records(pending_dir)
    wiki_pages = load_wiki_pages(root, wiki_dir)

    wiki_by_url: dict[str, list[PageRecord]] = {}
    for page in wiki_pages:
        if page.url:
            wiki_by_url.setdefault(page.url, []).append(page)

    matched_one: list[tuple[PendingRecord, PageRecord]] = []
    no_match: list[PendingRecord] = []
    duplicate_match: list[tuple[PendingRecord, list[PageRecord]]] = []
    pending_missing_url: list[PendingRecord] = []

    for record in pending_records:
        if not record.url:
            pending_missing_url.append(record)
            continue
        wiki_hits = wiki_by_url.get(record.url, [])
        if len(wiki_hits) == 0:
            no_match.append(record)
        elif len(wiki_hits) == 1:
            matched_one.append((record, wiki_hits[0]))
        else:
            duplicate_match.append((record, wiki_hits))

    return PendingMatchResult(
        matched_one=matched_one,
        no_match=no_match,
        duplicate_match=duplicate_match,
        pending_missing_url=pending_missing_url,
    )


def render_pending_match_report(result: PendingMatchResult, report_date: str, pending_dir: Path) -> str:
    total = (
        len(result.matched_one)
        + len(result.no_match)
        + len(result.duplicate_match)
        + len(result.pending_missing_url)
    )
    lines = [
        f"# Pending Digest Match Report - {report_date}",
        "",
        f"Pending directory: `{pending_dir.as_posix()}`",
        "",
        "This is a report-only scan. No wiki files were modified.",
        "",
        "## Summary",
        "",
        f"- Total pending files: {total}",
        f"- Matched one wiki page: {len(result.matched_one)}",
        f"- No wiki match: {len(result.no_match)}",
        f"- Duplicate wiki match: {len(result.duplicate_match)}",
        f"- Pending missing URL: {len(result.pending_missing_url)}",
        "",
        "## Matched One Wiki Page",
        "",
    ]
    if result.matched_one:
        lines.extend(["| Pending File | Wiki Page |", "|---|---|"])
        for pending, page in result.matched_one:
            lines.append(
                f"| `{markdown_cell(pending.rel_path)}` | `{markdown_cell(page.rel_path)}` |"
            )
    else:
        lines.append("None.")

    lines.extend(["", "## No Wiki Match", ""])
    if result.no_match:
        lines.extend(["| Pending File | URL |", "|---|---|"])
        for pending in result.no_match:
            lines.append(
                f"| `{markdown_cell(pending.rel_path)}` | {markdown_cell(pending.url)} |"
            )
    else:
        lines.append("None.")

    lines.extend(["", "## Duplicate Wiki Match", ""])
    if result.duplicate_match:
        lines.extend(["| Pending File | URL | Wiki Pages |", "|---|---|---|"])
        for pending, pages in result.duplicate_match:
            wiki_list = ", ".join(f"`{markdown_cell(p.rel_path)}`" for p in pages)
            lines.append(
                f"| `{markdown_cell(pending.rel_path)}` | {markdown_cell(pending.url)} | {wiki_list} |"
            )
    else:
        lines.append("None.")

    lines.extend(["", "## Pending Missing URL", ""])
    if result.pending_missing_url:
        lines.extend(["| Pending File |", "|---|"])
        for pending in result.pending_missing_url:
            lines.append(f"| `{markdown_cell(pending.rel_path)}` |")
    else:
        lines.append("None.")

    return "\n".join(lines)


def unique_pending_match_report_path(report_dir: Path, report_date: str) -> Path:
    first_path = report_dir / f"pending-match-{report_date}.md"
    if not first_path.exists():
        return first_path
    for index in range(2, 1000):
        path = report_dir / f"pending-match-{report_date}-{index}.md"
        if not path.exists():
            return path
    raise RuntimeError(f"too many pending-match reports already exist for {report_date}")


def command_pending_match(args: argparse.Namespace) -> int:
    if not args.pending_dir:
        print("error: --pending-dir is required", file=sys.stderr)
        print("usage: pending-match --pending-dir PATH [--report]", file=sys.stderr)
        return 2

    root = args.root.resolve()
    pending_dir = Path(args.pending_dir).resolve()

    if not pending_dir.exists():
        print(f"error: pending directory does not exist: {args.pending_dir}", file=sys.stderr)
        return 2
    if not pending_dir.is_dir():
        print(f"error: pending-dir is not a directory: {args.pending_dir}", file=sys.stderr)
        return 2

    result = collect_pending_match(pending_dir, root, Path(args.wiki_dir))
    total = (
        len(result.matched_one)
        + len(result.no_match)
        + len(result.duplicate_match)
        + len(result.pending_missing_url)
    )

    print("pending-match")
    print(f"pending directory: {pending_dir.as_posix()}")
    print(f"total pending files: {total}")
    print(f"matched one wiki page: {len(result.matched_one)}")
    for pending, page in result.matched_one[:20]:
        print(f"  {pending.rel_path} -> {page.rel_path}")
    if len(result.matched_one) > 20:
        print(f"  ... and {len(result.matched_one) - 20} more")
    print(f"no wiki match: {len(result.no_match)}")
    for pending in result.no_match[:10]:
        print(f"  {pending.rel_path} | {pending.url}")
    if len(result.no_match) > 10:
        print(f"  ... and {len(result.no_match) - 10} more")
    print(f"duplicate wiki match: {len(result.duplicate_match)}")
    for pending, pages in result.duplicate_match[:10]:
        wiki_paths = ", ".join(p.rel_path for p in pages)
        print(f"  {pending.rel_path} | {pending.url} | [{wiki_paths}]")
    if len(result.duplicate_match) > 10:
        print(f"  ... and {len(result.duplicate_match) - 10} more")
    print(f"pending missing url: {len(result.pending_missing_url)}")
    for pending in result.pending_missing_url[:10]:
        print(f"  {pending.rel_path}")
    if len(result.pending_missing_url) > 10:
        print(f"  ... and {len(result.pending_missing_url) - 10} more")

    if args.report:
        report_date = args.date or date.today().isoformat()
        try:
            tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
            report_path = unique_pending_match_report_path(tasks_dir / MAINTENANCE_REPORTS_DIR, report_date)
        except (RuntimeError, ValueError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        write_text(report_path, render_pending_match_report(result, report_date, pending_dir))
        print(f"wrote {normalize_rel_path(report_path, root)}")

    return 0


# ---------------------------------------------------------------------------
# inject-pending: inject content from pending digest files into stub wiki pages
# ---------------------------------------------------------------------------

_INJECT_STUB_MARKERS = [
    "## Main Content\n\n（📌 待消化）",
    "## Main Content\n（📌 待消化）",
]

_INJECT_LEVEL2_RE = re.compile(
    r"```|❶|❷|❸|❹|❺|步驟\s*[：:]|Step\s+\d|第[一二三四五六七八九十]+步"
    r"|^\d+\.\s|^[•▪▸]\s.*(?:指令|設定|安裝|執行)|如何[^嗎]|怎麼做"
    r"|(?:N|[0-9]+)\s*個(?:方法|技巧|步驟|招|指令)",
    re.MULTILINE,
)


def _determine_inject_status(body: str) -> str:
    """Return 'wiki' if body is Level 2 (has code/steps/commands), else 'stub'."""
    if _INJECT_LEVEL2_RE.search(body):
        return "wiki"
    if body.count("\n---\n") >= 2 and len(body) > 300:
        return "wiki"
    return "stub"


@dataclass(frozen=True)
class InjectPendingEntry:
    pending: PendingRecord
    wiki_page: PageRecord
    pending_body: str       # body extracted from pending file (after frontmatter)
    new_status: str         # "wiki" or "stub"


@dataclass(frozen=True)
class InjectPendingResult:
    eligible: list[InjectPendingEntry]                              # stub marker found, ready to inject
    already_filled: list[tuple[PendingRecord, PageRecord]]          # matched but no stub marker
    lingorm_skipped: list[tuple[PendingRecord, PageRecord]]         # LingOrm pages always skipped
    no_match: list[PendingRecord]                                   # pending url not in wiki
    duplicate_match: list[tuple[PendingRecord, list[PageRecord]]]   # ambiguous
    pending_missing_url: list[PendingRecord]                        # pending has no url


def collect_inject_pending(pending_dir: Path, root: Path, wiki_dir: Path) -> InjectPendingResult:
    """Build a report of which pending files would be injected into wiki stubs."""
    pending_records = load_pending_records(pending_dir)
    wiki_pages = load_wiki_pages(root, wiki_dir)

    wiki_by_url: dict[str, list[PageRecord]] = {}
    for page in wiki_pages:
        if page.url:
            wiki_by_url.setdefault(page.url, []).append(page)

    eligible: list[InjectPendingEntry] = []
    already_filled: list[tuple[PendingRecord, PageRecord]] = []
    lingorm_skipped: list[tuple[PendingRecord, PageRecord]] = []
    no_match: list[PendingRecord] = []
    duplicate_match: list[tuple[PendingRecord, list[PageRecord]]] = []
    pending_missing_url: list[PendingRecord] = []

    for record in pending_records:
        if not record.url:
            pending_missing_url.append(record)
            continue
        wiki_hits = wiki_by_url.get(record.url, [])
        if len(wiki_hits) == 0:
            no_match.append(record)
        elif len(wiki_hits) > 1:
            duplicate_match.append((record, wiki_hits))
        else:
            wiki_page = wiki_hits[0]
            # Skip LingOrm
            if "LingOrm" in wiki_page.category or "LingOrm" in wiki_page.wiki_rel_path:
                lingorm_skipped.append((record, wiki_page))
                continue
            # Read wiki file to check for stub marker
            wiki_abs_path = root / wiki_page.rel_path
            try:
                wiki_text = read_text(wiki_abs_path)
            except Exception:
                no_match.append(record)
                continue
            has_stub = any(marker in wiki_text for marker in _INJECT_STUB_MARKERS)
            if not has_stub:
                already_filled.append((record, wiki_page))
                continue
            # Read pending body
            pending_text = read_text(record.path)
            _fm, pending_body = parse_frontmatter(pending_text)
            new_status = _determine_inject_status(pending_body)
            eligible.append(InjectPendingEntry(
                pending=record,
                wiki_page=wiki_page,
                pending_body=pending_body,
                new_status=new_status,
            ))

    return InjectPendingResult(
        eligible=eligible,
        already_filled=already_filled,
        lingorm_skipped=lingorm_skipped,
        no_match=no_match,
        duplicate_match=duplicate_match,
        pending_missing_url=pending_missing_url,
    )


def render_inject_pending_report(result: InjectPendingResult, report_date: str, pending_dir: Path) -> str:
    lines = [
        f"# Inject Pending Report - {report_date}",
        "",
        f"Pending directory: `{pending_dir.as_posix()}`",
        "",
        "## Summary",
        "",
        f"- Eligible for injection: {len(result.eligible)}",
        f"- Already filled (no stub marker): {len(result.already_filled)}",
        f"- LingOrm skipped: {len(result.lingorm_skipped)}",
        f"- No wiki match: {len(result.no_match)}",
        f"- Duplicate wiki match: {len(result.duplicate_match)}",
        f"- Pending missing URL: {len(result.pending_missing_url)}",
        "",
        "## Eligible for Injection",
        "",
    ]
    if result.eligible:
        lines.extend(["| Pending File | Wiki Page | New Status |", "|---|---|---|"])
        for entry in result.eligible:
            lines.append(
                f"| `{markdown_cell(entry.pending.rel_path)}` "
                f"| `{markdown_cell(entry.wiki_page.rel_path)}` "
                f"| {entry.new_status} |"
            )
    else:
        lines.append("None.")

    lines.extend(["", "## Already Filled", ""])
    if result.already_filled:
        lines.extend(["| Pending File | Wiki Page |", "|---|---|"])
        for pending, page in result.already_filled:
            lines.append(
                f"| `{markdown_cell(pending.rel_path)}` | `{markdown_cell(page.rel_path)}` |"
            )
    else:
        lines.append("None.")

    lines.extend(["", "## LingOrm Skipped", ""])
    if result.lingorm_skipped:
        lines.extend(["| Pending File | Wiki Page |", "|---|---|"])
        for pending, page in result.lingorm_skipped:
            lines.append(
                f"| `{markdown_cell(pending.rel_path)}` | `{markdown_cell(page.rel_path)}` |"
            )
    else:
        lines.append("None.")

    lines.extend(["", "## No Wiki Match", ""])
    if result.no_match:
        lines.extend(["| Pending File | URL |", "|---|---|"])
        for pending in result.no_match:
            lines.append(
                f"| `{markdown_cell(pending.rel_path)}` | {markdown_cell(pending.url)} |"
            )
    else:
        lines.append("None.")

    lines.extend(["", "## Duplicate Wiki Match", ""])
    if result.duplicate_match:
        lines.extend(["| Pending File | URL | Wiki Pages |", "|---|---|---|"])
        for pending, pages in result.duplicate_match:
            wiki_list = ", ".join(f"`{markdown_cell(p.rel_path)}`" for p in pages)
            lines.append(
                f"| `{markdown_cell(pending.rel_path)}` | {markdown_cell(pending.url)} | {wiki_list} |"
            )
    else:
        lines.append("None.")

    lines.extend(["", "## Pending Missing URL", ""])
    if result.pending_missing_url:
        lines.extend(["| Pending File |", "|---|"])
        for pending in result.pending_missing_url:
            lines.append(f"| `{markdown_cell(pending.rel_path)}` |")
    else:
        lines.append("None.")

    return "\n".join(lines)


def unique_inject_pending_report_path(report_dir: Path, report_date: str) -> Path:
    first_path = report_dir / f"inject-pending-{report_date}.md"
    if not first_path.exists():
        return first_path
    for index in range(2, 1000):
        path = report_dir / f"inject-pending-{report_date}-{index}.md"
        if not path.exists():
            return path
    raise RuntimeError(f"too many inject-pending reports already exist for {report_date}")


def apply_inject_pending(
    entries: list[InjectPendingEntry],
    root: Path,
    limit: int | None = None,
    dry_run: bool = False,
) -> tuple[list[str], list[tuple[str, str]]]:
    """Inject content from pending files into matching wiki stubs.

    Returns (injected_paths, errors) where injected_paths are repo-relative
    paths (forward-slash) and errors are (path, message) pairs.
    """
    to_inject = entries[:limit] if limit is not None else entries
    injected: list[str] = []
    errors: list[tuple[str, str]] = []

    for entry in to_inject:
        wiki_path = root / entry.wiki_page.rel_path
        # Safety: skip LingOrm
        if "LingOrm" in entry.wiki_page.category or "LingOrm" in entry.wiki_page.wiki_rel_path:
            errors.append((entry.wiki_page.rel_path, "LingOrm page — always skipped"))
            continue
        try:
            wiki_text = read_text(wiki_path)
        except Exception as exc:
            errors.append((entry.wiki_page.rel_path, f"read error: {exc}"))
            continue

        # Replace stub marker
        new_text = wiki_text
        replaced = False
        for marker in _INJECT_STUB_MARKERS:
            if marker in new_text:
                new_text = new_text.replace(marker, f"## Main Content\n\n{entry.pending_body}", 1)
                replaced = True
                break
        if not replaced:
            errors.append((entry.wiki_page.rel_path, "stub marker no longer present — already filled?"))
            continue

        # Update status field in frontmatter
        new_text = re.sub(r"(status:\s*)stub", rf"\g<1>{entry.new_status}", new_text, count=1)

        if not dry_run:
            write_text(wiki_path, new_text)

        injected.append(normalize_rel_path(wiki_path, root))

    return injected, errors


def command_inject_pending(args: argparse.Namespace) -> int:
    if not args.pending_dir:
        print("error: --pending-dir is required for inject-pending", file=sys.stderr)
        return 1
    pending_dir = Path(args.pending_dir).resolve()
    if not pending_dir.exists():
        print(f"error: pending directory does not exist: {args.pending_dir}", file=sys.stderr)
        return 1
    if not pending_dir.is_dir():
        print(f"error: pending-dir is not a directory: {args.pending_dir}", file=sys.stderr)
        return 1

    root = args.root.resolve()
    wiki_dir = Path(args.wiki_dir)
    result = collect_inject_pending(pending_dir, root, wiki_dir)

    apply_mode: bool = getattr(args, "apply", False)
    limit: int | None = getattr(args, "limit", None)

    print("inject-pending")
    print(f"pending directory: {pending_dir.as_posix()}")
    print(f"eligible for injection: {len(result.eligible)}")
    for i, entry in enumerate(result.eligible[:30]):
        print(f"  {entry.pending.rel_path} → {entry.wiki_page.rel_path} [{entry.new_status}]")
    if len(result.eligible) > 30:
        print(f"  ... and {len(result.eligible) - 30} more")
    print(f"already filled: {len(result.already_filled)}")
    print(f"LingOrm skipped: {len(result.lingorm_skipped)}")
    print(f"no wiki match: {len(result.no_match)}")
    print(f"duplicate match: {len(result.duplicate_match)}")
    print(f"pending missing url: {len(result.pending_missing_url)}")

    if apply_mode:
        injected, errors = apply_inject_pending(
            result.eligible, root, limit=limit, dry_run=False
        )
        print(f"\nInjected {len(injected)} pages.")
        for path in injected:
            print(f"  {path}")
        if errors:
            print(f"\nSkipped/errors ({len(errors)}):")
            for path, msg in errors:
                print(f"  {path}: {msg}")

        if injected:
            log_path = root / wiki_dir / "log.md"
            today = date.today().isoformat()
            log_entry = (
                f"\n## [{today}] inject-pending | {len(injected)} pages injected by inject-pending --apply\n"
            )
            existing = read_text(log_path) if log_path.exists() else ""
            write_text(log_path, existing.rstrip() + log_entry)
            print(f"\nAppended log entry to {normalize_rel_path(log_path, root)}")
            print(
                f"\nReminder: Dashboard in 總索引.md needs manual update "
                f"for any pages promoted to wiki."
            )
    else:
        if result.eligible:
            print("\nUse --apply to inject content into these stubs.")
            print("Use --apply --limit N to cap batch size.")

    if args.report:
        report_date = args.date or date.today().isoformat()
        try:
            tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
            report_path = unique_inject_pending_report_path(tasks_dir / MAINTENANCE_REPORTS_DIR, report_date)
            report_path.parent.mkdir(parents=True, exist_ok=True)
            write_text(report_path, render_inject_pending_report(result, report_date, pending_dir))
            print(f"\nReport written: {normalize_rel_path(report_path, root)}")
        except RuntimeError as exc:
            print(f"warning: {exc}", file=sys.stderr)

    return 0


# ---------------------------------------------------------------------------
# promote-ready: find non-LingOrm stubs with substantial content
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PromoteReadyEntry:
    page: PageRecord
    body_length: int
    heading_count: int
    reason: str


@dataclass(frozen=True)
class PromoteReadyResult:
    ready: list[PromoteReadyEntry]
    blocked: list[PageRecord]   # empty body or URL-only — go to blocked, not ready


PROMOTE_HEADING_RE = re.compile(r"^#{1,6}\s+\S", re.MULTILINE)
PROMOTE_PLACEHOLDER_RE = re.compile(r"（📌\s*待消化）|\(📌\s*待消化\)|📌\s*待消化")


def _count_body_headings(body: str) -> int:
    return len(PROMOTE_HEADING_RE.findall(body))


def _body_has_substantial_content(body: str) -> bool:
    """Return True if body has real content (not just frontmatter lines or URLs)."""
    meaningful: list[str] = []
    for raw_line in body.replace("\r\n", "\n").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        if line.startswith(("http://", "https://")):
            continue
        if line in {"[]", "[ ]", "---"}:
            continue
        if line in PLACEHOLDER_MARKERS:
            continue
        if line.startswith(("- [[", "* [[", "[[")):
            continue
        if line.startswith("- [") and "](" in line:
            continue
        meaningful.append(line)
    total_chars = sum(len(line) for line in meaningful)
    return total_chars >= 80 or len(meaningful) >= 3


def collect_promote_ready(root: Path, wiki_dir: Path) -> PromoteReadyResult:
    """Identify non-LingOrm stub pages ready for promotion."""
    pages = load_wiki_pages(root, wiki_dir)
    ready: list[PromoteReadyEntry] = []
    blocked: list[PageRecord] = []

    for page in pages:
        # Only look at stub pages
        if normalize_status(page.status) != "stub":
            continue
        # Skip index pages
        if page.category == "index" or page.wiki_rel_path.startswith("index/"):
            continue
        # Skip LingOrm — per project rules they can stay stub forever
        if "LingOrm" in page.category or "LingOrm" in page.wiki_rel_path:
            continue

        body = page.body
        body_length = len(body)
        heading_count = _count_body_headings(body)

        # Pages with empty body or only URL go to blocked
        if not body.strip() or (body_length < 30 and ("http://" in body or "https://" in body)):
            blocked.append(page)
            continue

        # Pages with 待消化 marker are not ready
        if PROMOTE_PLACEHOLDER_RE.search(body):
            continue

        # Readiness criteria (any one sufficient):
        reasons: list[str] = []
        if body_length > 300:
            reasons.append(f"body>{300}chars")
        if heading_count >= 2:
            reasons.append(f"{heading_count}headings")
        if _body_has_substantial_content(body) and body_length > 150:
            reasons.append("substantial-content")

        if reasons:
            ready.append(PromoteReadyEntry(
                page=page,
                body_length=body_length,
                heading_count=heading_count,
                reason=", ".join(reasons),
            ))

    return PromoteReadyResult(ready=ready, blocked=blocked)


def render_promote_ready_report(result: PromoteReadyResult, report_date: str) -> str:
    lines = [
        f"# Promote-Ready Stubs - {report_date}",
        "",
        "This is a report-only scan. No wiki files were modified.",
        "LingOrm pages are excluded per project rules.",
        "",
        "## Summary",
        "",
        f"- Ready to promote: {len(result.ready)}",
        f"- Blocked (empty/URL-only body): {len(result.blocked)}",
        "",
        "## Ready to Promote",
        "",
    ]
    if result.ready:
        lines.extend(["| Page | Body chars | Headings | Reason |", "|---|---:|---:|---|"])
        for entry in result.ready:
            path = markdown_cell(entry.page.rel_path)
            lines.append(
                f"| `{path}` | {entry.body_length} | {entry.heading_count} | {markdown_cell(entry.reason)} |"
            )
    else:
        lines.append("No stub pages ready for promotion detected.")

    lines.extend(["", "## Blocked (empty or URL-only body)", ""])
    if result.blocked:
        lines.extend(["| Page | Category |", "|---|---|"])
        for page in result.blocked:
            lines.append(
                f"| `{markdown_cell(page.rel_path)}` | {markdown_cell(page.category or '(root)')} |"
            )
    else:
        lines.append("None.")

    if result.ready:
        lines.extend([
            "",
            "> Use `--apply` to promote these pages (changes `status: stub` → `status: wiki` and removes stub markers from index files).",
            "> Use `--apply --limit N` to cap the number of pages promoted.",
        ])

    return "\n".join(lines)


# Regex: matches [[stem]] or [[stem|alias]] followed by the stub marker.
# Also matches [stem](<../path>) style relative links.
_STUB_MARKER_WIKILINK_RE_TEMPLATE = r'(\[\[{stem}[^\]]*\]\])\s*（📌 stub）'
_STUB_MARKER_RELLINK_RE_TEMPLATE = r'(\[{stem}\]\(<[^>]*>\))\s*（📌 stub）'


def _build_stub_marker_patterns(stem: str) -> list[re.Pattern[str]]:
    escaped = re.escape(stem)
    return [
        re.compile(_STUB_MARKER_WIKILINK_RE_TEMPLATE.format(stem=escaped)),
        re.compile(_STUB_MARKER_RELLINK_RE_TEMPLATE.format(stem=escaped)),
    ]


def _remove_stub_marker_from_index_files(
    wiki_dir: Path, stem: str, dry_run: bool = False
) -> list[Path]:
    """Strip （📌 stub） from all index files that reference *stem*.

    Returns list of index files modified (or that would be modified in dry-run).
    """
    index_dir = wiki_dir / "index"
    if not index_dir.is_dir():
        return []

    patterns = _build_stub_marker_patterns(stem)
    modified: list[Path] = []

    for index_path in sorted(index_dir.glob("*.md")):
        text = read_text(index_path)
        new_text = text
        for pattern in patterns:
            new_text = pattern.sub(r'\1', new_text)
        if new_text != text:
            if not dry_run:
                write_text(index_path, new_text)
            modified.append(index_path)

    return modified


def _promote_stub_to_wiki(page_path: Path, dry_run: bool = False) -> bool:
    """Change `status: stub` → `status: wiki` in *page_path* frontmatter.

    Returns True if the file was (or would be) changed.
    Raises ValueError if the file does not have `status: stub`.
    """
    text = read_text(page_path)
    # Match status line in frontmatter — look for `status: stub` (with optional quotes)
    status_re = re.compile(
        r'^(status:\s*)([\'"]?)stub([\'"]?\s*)$',
        re.MULTILINE | re.IGNORECASE,
    )
    match = status_re.search(text)
    if not match:
        raise ValueError(f"no 'status: stub' found in frontmatter of {page_path}")

    new_text = status_re.sub(r'\1\2wiki\3', text, count=1)
    if new_text == text:
        return False
    if not dry_run:
        write_text(page_path, new_text)
    return True


def apply_promote_ready(
    entries: list[PromoteReadyEntry],
    root: Path,
    wiki_dir: Path,
    limit: int | None,
    dry_run: bool = False,
) -> tuple[list[str], list[tuple[str, str]]]:
    """Promote up to *limit* stub pages to wiki status.

    *wiki_dir* may be relative (to *root*) or absolute.
    Returns (promoted_paths, errors) where promoted_paths are repo-relative
    paths (forward-slash) and errors are (path, message) pairs.
    """
    to_promote = entries[:limit] if limit is not None else list(entries)
    promoted: list[str] = []
    errors: list[tuple[str, str]] = []

    # Accept either relative or absolute wiki_dir.
    wiki_abs = wiki_dir if wiki_dir.is_absolute() else (root / wiki_dir).resolve()

    for entry in to_promote:
        page = entry.page
        # Safety: skip if not actually stub (race or stale data)
        if normalize_status(page.status) != "stub":
            errors.append((page.rel_path, "status is not stub — skipped"))
            continue
        # Safety: skip LingOrm
        if "LingOrm" in page.wiki_rel_path or "LingOrm" in page.category:
            errors.append((page.rel_path, "LingOrm page — always skipped"))
            continue

        page_path = root / page.rel_path
        try:
            changed = _promote_stub_to_wiki(page_path, dry_run=dry_run)
        except Exception as exc:
            errors.append((page.rel_path, str(exc)))
            continue

        if changed:
            _remove_stub_marker_from_index_files(wiki_abs, page.stem, dry_run=dry_run)
            promoted.append(page.rel_path)

    return promoted, errors


def unique_promote_ready_report_path(report_dir: Path, report_date: str) -> Path:
    first_path = report_dir / f"promote-ready-{report_date}.md"
    if not first_path.exists():
        return first_path
    for index in range(2, 1000):
        path = report_dir / f"promote-ready-{report_date}-{index}.md"
        if not path.exists():
            return path
    raise RuntimeError(f"too many promote-ready reports already exist for {report_date}")


def command_promote_ready(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    wiki_dir = Path(args.wiki_dir)
    result = collect_promote_ready(root, wiki_dir)

    apply_mode: bool = getattr(args, "apply", False)
    limit: int | None = getattr(args, "limit", None)

    print("promote-ready")
    print(f"ready to promote: {len(result.ready)}")
    for entry in result.ready[:30]:
        print(f"  {entry.page.rel_path} [body={entry.body_length} headings={entry.heading_count}] {entry.reason}")
    if len(result.ready) > 30:
        print(f"  ... and {len(result.ready) - 30} more")
    print(f"blocked (empty/url-only): {len(result.blocked)}")

    if apply_mode:
        promoted, errors = apply_promote_ready(
            result.ready, root, wiki_dir, limit=limit, dry_run=False
        )
        print(f"\nPromoted {len(promoted)} pages.")
        for path in promoted:
            print(f"  {path}")
        if errors:
            print(f"\nSkipped/errors ({len(errors)}):")
            for path, msg in errors:
                print(f"  {path}: {msg}")

        if promoted:
            # Append to log
            log_path = root / wiki_dir / "log.md"
            today = date.today().isoformat()
            log_entry = (
                f"\n## [{today}] promote | {len(promoted)} pages promoted by promote-ready --apply\n"
            )
            existing = read_text(log_path) if log_path.exists() else ""
            write_text(log_path, existing.rstrip() + log_entry)
            print(f"\nAppended log entry to {normalize_rel_path(log_path, root)}")

            print(
                f"\nReminder: Dashboard in 總索引.md needs manual update "
                f"(+{len(promoted)} wiki, -{len(promoted)} stub for affected category)."
            )

    if args.report:
        report_date = args.date or date.today().isoformat()
        try:
            tasks_dir = resolve_tasks_dir(root, args.tasks_dir)
            report_path = unique_promote_ready_report_path(tasks_dir / MAINTENANCE_REPORTS_DIR, report_date)
        except (RuntimeError, ValueError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        write_text(report_path, render_promote_ready_report(result, report_date))
        print(f"wrote {normalize_rel_path(report_path, root)}")

    return 0


# ---------------------------------------------------------------------------
# audit-list: list open items from audit/*.md
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AuditItem:
    filename: str
    severity: str
    target: str
    comment_first_line: str


def load_audit_items(audit_dir: Path) -> list[AuditItem]:
    """Parse audit/*.md files for severity, target, and first comment line."""
    items: list[AuditItem] = []
    for path in sorted(audit_dir.glob("*.md")):
        text = read_text(path)
        frontmatter, body = parse_frontmatter(text)
        severity = frontmatter.get("severity", "").strip()
        target = frontmatter.get("target", "").strip()
        # First non-empty body line as comment preview
        comment_first_line = ""
        for raw_line in body.replace("\r\n", "\n").splitlines():
            stripped = raw_line.strip()
            if stripped and not stripped.startswith("#"):
                comment_first_line = stripped[:120]
                break
        items.append(AuditItem(
            filename=path.name,
            severity=severity,
            target=target,
            comment_first_line=comment_first_line,
        ))
    return items


def command_audit_list(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    audit_dir = root / "audit"

    if not audit_dir.exists() or not audit_dir.is_dir():
        print("no audit directory")
        return 0

    items = load_audit_items(audit_dir)
    if not items:
        print("audit directory exists but contains no .md files")
        return 0

    print(f"audit-list: {len(items)} item(s)")
    print("")
    for item in items:
        severity_label = f"[{item.severity}] " if item.severity else ""
        target_label = f"target: {item.target} | " if item.target else ""
        comment = item.comment_first_line or "(no comment)"
        print(f"  {item.filename}")
        print(f"    {severity_label}{target_label}{comment}")

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Repo-specific report-only wiki maintenance helpers.",
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root. Defaults to current directory.")
    parser.add_argument("--wiki-dir", default=WIKI_DIR_DEFAULT, help="Wiki directory relative to root.")
    parser.add_argument("--raw-dir", default=RAW_DIR_DEFAULT, help="Raw directory relative to root.")
    parser.add_argument("--tasks-dir", default=TASKS_DIR_DEFAULT, help="Tasks/report directory relative to root.")

    subparsers = parser.add_subparsers(dest="command", required=True)

    scan = subparsers.add_parser("scan", help="Run all report-only checks and produce a combined maintenance report.")
    scan.add_argument("--report", action="store_true", help="Write a dated maintenance report Markdown file.")
    scan.add_argument("--date", type=parse_report_date, help="Report date for naming, in YYYY-MM-DD format.")
    scan.add_argument(
        "--pending-dir",
        metavar="PATH",
        default=None,
        help="Optional: directory of pending digest output .md files. If provided, includes inject-pending results.",
    )
    scan.set_defaults(func=command_scan)

    handoff = subparsers.add_parser("handoff", help="Write tasks/current-handoff.md for session recovery.")
    handoff.add_argument("--task", required=True, help="Current task or batch name.")
    handoff.add_argument("--next", required=True, help="Explicit next step for the next session.")
    handoff.set_defaults(func=command_handoff)

    blocked = subparsers.add_parser("blocked-report", help="Write tasks/blocked-content-gaps.md.")
    blocked.set_defaults(func=command_blocked_report)

    status_audit = subparsers.add_parser("status-audit", help="Audit wiki page status frontmatter.")
    status_audit.add_argument("--report", action="store_true", help="Write a dated status audit Markdown report.")
    status_audit.add_argument("--date", type=parse_report_date, help="Report date for naming, in YYYY-MM-DD format.")
    status_audit.set_defaults(func=command_status_audit)

    index_lint = subparsers.add_parser("index-lint", help="Lint index page links and stub markers.")
    index_lint.add_argument("--report", action="store_true", help="Write a dated index lint Markdown report.")
    index_lint.add_argument("--date", type=parse_report_date, help="Report date for naming, in YYYY-MM-DD format.")
    index_lint.set_defaults(func=command_index_lint)

    review_reconcile = subparsers.add_parser(
        "review-reconcile",
        help="Classify review findings into reconciliation buckets.",
    )
    review_reconcile.add_argument(
        "input",
        help="Markdown review/findings file to classify. A dated report is always written.",
    )
    review_reconcile.add_argument(
        "--report",
        action="store_true",
        help="Write a dated review reconcile Markdown report. Reports are always written when input is provided.",
    )
    review_reconcile.add_argument("--date", type=parse_report_date, help="Report date for naming, in YYYY-MM-DD format.")
    review_reconcile.set_defaults(func=command_review_reconcile)

    coverage = subparsers.add_parser(
        "coverage",
        help="Report raw threads files not yet ingested into wiki.",
    )
    coverage.add_argument("--report", action="store_true", help="Write a dated ingest-candidates Markdown report.")
    coverage.add_argument("--date", type=parse_report_date, help="Report date for naming, in YYYY-MM-DD format.")
    coverage.set_defaults(func=command_coverage)

    duplicates = subparsers.add_parser(
        "duplicates",
        help="Scan wiki pages for duplicate URLs and report suggested canonicals.",
    )
    duplicates.add_argument("--report", action="store_true", help="Write a dated duplicates Markdown report.")
    duplicates.add_argument("--date", type=parse_report_date, help="Report date for naming, in YYYY-MM-DD format.")
    duplicates.set_defaults(func=command_duplicates)

    canonical_guard = subparsers.add_parser(
        "canonical-guard",
        help="Detect stale file conflicts and author frontmatter violations.",
    )
    canonical_guard.add_argument("--report", action="store_true", help="Write a dated canonical-guard Markdown report.")
    canonical_guard.add_argument("--date", type=parse_report_date, help="Report date for naming, in YYYY-MM-DD format.")
    canonical_guard.set_defaults(func=command_canonical_guard)

    author_fix = subparsers.add_parser(
        "author-fix",
        help="Fix bare-string 作者 fields to canonical [\"@handle\"] format.",
    )
    author_fix.add_argument(
        "--apply", action="store_true",
        help="Actually write fixes (default is dry-run).",
    )
    author_fix.set_defaults(func=command_author_fix)

    bare_link_fix = subparsers.add_parser(
        "bare-link-fix",
        help="Fix ambiguous bare [[wikilinks]] to explicit relative Markdown links.",
    )
    bare_link_fix.add_argument(
        "--apply", action="store_true",
        help="Actually write fixes (default is dry-run).",
    )
    bare_link_fix.set_defaults(func=command_bare_link_fix)

    pending_match = subparsers.add_parser(
        "pending-match",
        help="Compare external pending digest URLs against wiki page URLs (report-only).",
    )
    pending_match.add_argument(
        "--pending-dir",
        required=True,
        help="Path to external pending digest directory (required, not hardcoded).",
    )
    pending_match.add_argument("--report", action="store_true", help="Write a dated pending-match Markdown report.")
    pending_match.add_argument("--date", type=parse_report_date, help="Report date for naming, in YYYY-MM-DD format.")
    pending_match.set_defaults(func=command_pending_match)

    inject_pending = subparsers.add_parser(
        "inject-pending",
        help="Inject content from pending digest files into matching wiki stubs.",
    )
    inject_pending.add_argument(
        "--pending-dir",
        metavar="PATH",
        help="Directory containing pending digest output .md files.",
    )
    inject_pending.add_argument(
        "--apply",
        action="store_true",
        help="Actually inject content (replace stub markers, update status).",
    )
    inject_pending.add_argument(
        "--limit",
        type=int,
        default=None,
        metavar="N",
        help="Cap the number of pages injected when --apply is given (default: no limit).",
    )
    inject_pending.add_argument("--report", action="store_true", help="Write a dated inject-pending Markdown report.")
    inject_pending.add_argument("--date", type=parse_report_date, help="Report date for naming, in YYYY-MM-DD format.")
    inject_pending.set_defaults(func=command_inject_pending)

    promote_ready = subparsers.add_parser(
        "promote-ready",
        help="List non-LingOrm stub pages with substantial content ready for promotion.",
    )
    promote_ready.add_argument("--report", action="store_true", help="Write a dated promote-ready Markdown report.")
    promote_ready.add_argument("--date", type=parse_report_date, help="Report date for naming, in YYYY-MM-DD format.")
    promote_ready.add_argument(
        "--apply",
        action="store_true",
        help="Actually promote pages (change status: stub → wiki, strip stub markers from indexes).",
    )
    promote_ready.add_argument(
        "--limit",
        type=int,
        default=None,
        metavar="N",
        help="Cap the number of pages promoted when --apply is given (default: no limit).",
    )
    promote_ready.set_defaults(func=command_promote_ready)

    audit_list = subparsers.add_parser(
        "audit-list",
        help="List open items from the audit/ directory.",
    )
    audit_list.set_defaults(func=command_audit_list)

    return parser


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

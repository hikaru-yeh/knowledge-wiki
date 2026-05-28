from __future__ import annotations

import argparse
import json
import logging
import math
import os
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from playwright.sync_api import Page, sync_playwright

logger = logging.getLogger(__name__)


COOKIE_SELECTORS = [
    "button:has-text('Decline optional cookies')",
    "button:has-text('Allow all cookies')",
    "button:has-text('Accept all')",
    "button:has-text('Accept')",
    "button:has-text('Allow all')",
    "button:has-text('Only allow essential cookies')",
    "button:has-text('Continue without logging in')",
    "button:has-text('Not now')",
    "[role='button']:has-text('Accept')",
]

NOISE_LINES = {
    "Log in",
    "Thread",
    "Translate",
    "Related threads",
    "Log in to see more replies.",
}


@dataclass(frozen=True)
class SocialCrawlResult:
    url: str
    root_author_username: str | None
    root_author_display_name: str | None
    root_post_text: str
    raw_data: dict[str, Any]


@dataclass(frozen=True)
class AuthorContentResult:
    url: str
    target_handle: str
    main_post: str
    author_comments: list[str]
    body_text: str


def string_or_none(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def fetch_threads_post(url: str, api_key: str) -> SocialCrawlResult:
    endpoint = f"https://www.socialcrawl.dev/v1/threads/post?{urlencode({'url': url})}"
    request = Request(endpoint, headers={"x-api-key": api_key})
    with urlopen(request, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))

    data = payload.get("data", {})
    post = data.get("post", {})
    author = post.get("author", {})
    content = post.get("content", {})

    return SocialCrawlResult(
        url=url,
        root_author_username=string_or_none(author.get("username")),
        root_author_display_name=string_or_none(author.get("display_name")),
        root_post_text=str(content.get("text", "") or "").strip(),
        raw_data=payload,
    )


def normalize_body_lines(body_text: str) -> list[str]:
    body_text = body_text.replace("\xa0", " ")
    for marker in (
        "Related threads",
        "Log in to see more replies.",
        "Allow the use of cookies from Threads by Instagram on this browser?",
        "Threads Terms",
    ):
        if marker in body_text:
            body_text = body_text.split(marker)[0]
    return [line.strip() for line in body_text.splitlines() if line.strip()]


def looks_like_timestamp(line: str) -> bool:
    lowered = line.strip().lower()
    return bool(
        re.fullmatch(r"\d{2}/\d{2}/\d{2}", line.strip())
        or re.fullmatch(r"\d+[smhdwy](?:\s+edited)?", lowered)
    )


def looks_like_metric(line: str) -> bool:
    return bool(re.fullmatch(r"[0-9.]+[kKmM]?", line.strip()))


def looks_like_handle(line: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9._]{2,32}", line.strip()))


def is_probable_new_author_start(lines: list[str], index: int, current_content: list[str]) -> bool:
    line = lines[index]
    if not looks_like_handle(line) or not current_content:
        return False

    lookahead = lines[index + 1 : index + 5]
    if any(looks_like_timestamp(candidate) for candidate in lookahead):
        return True

    if lookahead and all(looks_like_metric(candidate) or looks_like_handle(candidate) for candidate in lookahead[:3]):
        return True

    return False


def clean_author_blocks(body_text: str, target_handle: str) -> list[str]:
    lines = normalize_body_lines(body_text)
    blocks: list[str] = []
    i = 0

    while i < len(lines):
        if lines[i] != target_handle:
            i += 1
            continue

        j = i + 1
        if j < len(lines) and looks_like_timestamp(lines[j]):
            j += 1

        content_lines: list[str] = []
        while j < len(lines):
            line = lines[j]

            if line in NOISE_LINES:
                if line == "Related threads":
                    break
                j += 1
                continue

            if looks_like_metric(line):
                j += 1
                continue

            if is_probable_new_author_start(lines, j, content_lines):
                break

            content_lines.append(line)
            j += 1

        text = "\n".join(content_lines).strip()
        if text:
            blocks.append(text)
        i = j

    return blocks


def dedupe_comments(comments: list[str]) -> list[str]:
    seen: set[str] = set()
    deduped: list[str] = []
    for comment in comments:
        normalized = comment.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(normalized)
    return deduped


def is_noise_comment_line(line: str) -> bool:
    stripped = line.strip()
    lowered = stripped.lower()
    return (
        not stripped
        or stripped in {"·", "Author"}
        or lowered.startswith("x.com/")
        or lowered.startswith("http://")
        or lowered.startswith("https://")
    )


def clean_main_post_text(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) >= 2 and looks_like_handle(lines[0]) and looks_like_timestamp(lines[1]):
        lines = lines[2:]

    cleaned: list[str] = []
    for line in lines:
        if line in {"Author"} or looks_like_timestamp(line):
            continue
        if line.lower().startswith(("x.com/", "http://", "https://", "cr.:", "cr:")):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()


def clean_author_comments(comments: list[str]) -> list[str]:
    cleaned_comments: list[str] = []
    for comment in comments:
        lines = [line.strip() for line in comment.splitlines()]
        kept = [line for line in lines if not is_noise_comment_line(line)]
        cleaned = "\n".join(line for line in kept if line).strip()
        if cleaned:
            cleaned_comments.append(cleaned)
    return dedupe_comments(cleaned_comments)


def dismiss_overlays(page: Page) -> None:
    for selector in COOKIE_SELECTORS:
        try:
            locator = page.locator(selector).first
            if locator.count() > 0 and locator.is_visible(timeout=1000):
                locator.click(timeout=1500)
                return
        except Exception:
            continue


def fetch_author_content(url: str, target_handle: str) -> AuthorContentResult:
    normalized_handle = extract_handle(target_handle)
    if not normalized_handle:
        raise RuntimeError("缺少作者 handle，無法從頁面抽取作者主文與留言")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        )
        page.goto(url, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(5000)
        dismiss_overlays(page)
        page.wait_for_timeout(1000)
        body_text = page.inner_text("body")
        browser.close()

    author_blocks = clean_author_blocks(body_text, normalized_handle)
    if not author_blocks:
        raise RuntimeError(f"找不到作者 {normalized_handle} 在頁面中的主文內容")

    return AuthorContentResult(
        url=url,
        target_handle=normalized_handle,
        main_post=author_blocks[0],
        author_comments=dedupe_comments(author_blocks[1:]),
        body_text=body_text,
    )


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        raise RuntimeError("頁面缺少 frontmatter")

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise RuntimeError("frontmatter 格式不完整")

    body = parts[2].lstrip("\r\n")
    metadata: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata, body


def normalize_author_field(raw: str) -> str:
    """Any author format → canonical YAML list: [] or ["@handle"]."""
    v = raw.strip()
    if not v or v in ("[]", "[ ]"):
        return "[]"
    if v.startswith("[") and v.endswith("]"):
        return v
    handle = v.lstrip("@")
    return f'["@{handle}"]'


def extract_handle(author_field: str) -> str:
    """Any author format → bare handle string (no @, no brackets)."""
    v = author_field.strip()
    if v.startswith("[") and v.endswith("]"):
        v = v[1:-1].strip().strip('"').strip("'")
    return v.lstrip("@")


def render_frontmatter(metadata: dict[str, str]) -> list[str]:
    lines = ["---"]
    for key, value in metadata.items():
        lines.append(f"{key}: {value}")
    lines.append("---")
    return lines


def infer_cross_references(path: Path) -> list[str]:
    normalized_parts = [part.lower() for part in path.parts]
    if "lingorm" in normalized_parts:
        return ["- [[LingOrm-索引]]：LingOrm 分類總覽"]
    if "ai 工具" in normalized_parts:
        return ["- [[AI 工具-索引]]：AI 工具分類總覽"]
    if "工具軟體" in normalized_parts:
        return ["- [[工具軟體-索引]]：工具軟體分類總覽"]
    if "求職履歷" in normalized_parts:
        return ["- [[求職履歷-索引]]：求職履歷分類總覽"]
    if "旅遊美食" in normalized_parts:
        return ["- [[旅遊美食-索引]]：旅遊美食分類總覽"]
    if "健康生活" in normalized_parts:
        return ["- [[健康生活-索引]]：健康生活分類總覽"]
    return []


# ---------------------------------------------------------------------------
# OCR output sanity checks
# ---------------------------------------------------------------------------

# Thresholds (configurable)
MAX_CONSECUTIVE_REPEATS = 5      # same line repeated > N times consecutively
MAX_SECTION_LINES = 500          # single section exceeding this is suspicious
LENGTH_RATIO_LIMIT = 10.0        # OCR text > N× main post length
MIN_CHAR_ENTROPY = 2.0           # Shannon entropy below this = degenerate

OCR_TRUNCATION_MARKER = "<!-- OCR output truncated: degenerate repetition detected -->"


def _char_entropy(text: str) -> float:
    """Shannon entropy (bits) of the character distribution in *text*."""
    if not text:
        return 0.0
    freq = Counter(text)
    total = len(text)
    return -sum(
        (count / total) * math.log2(count / total) for count in freq.values()
    )


def _max_consecutive_repeats(lines: list[str]) -> tuple[int, str]:
    """Return (count, repeated_line) for the longest consecutive run."""
    max_count = 0
    max_line = ""
    current_count = 1
    prev = None
    for line in lines:
        stripped = line.strip()
        if stripped and stripped == prev:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                max_line = stripped
        else:
            current_count = 1
        prev = stripped
    return max_count, max_line


@dataclass(frozen=True)
class OCRSanityResult:
    """Outcome of an OCR sanity check."""
    is_clean: bool
    reason: str          # empty when clean
    cleaned_text: str    # original text if clean, truncated otherwise


def check_ocr_sanity(
    ocr_text: str,
    main_post_text: str = "",
    *,
    source_label: str = "OCR",
) -> OCRSanityResult:
    """Validate *ocr_text* for degenerate OCR output.

    Returns an ``OCRSanityResult`` whose ``cleaned_text`` is either the
    original text (when clean) or a truncated version ending with a comment
    marker.

    Checks performed (in order):
    1. Consecutive-line repetition  (> MAX_CONSECUTIVE_REPEATS)
    2. Total line count             (> MAX_SECTION_LINES)
    3. Length ratio vs main post    (> LENGTH_RATIO_LIMIT)
    4. Character entropy            (< MIN_CHAR_ENTROPY)
    """
    if not ocr_text or not ocr_text.strip():
        return OCRSanityResult(is_clean=True, reason="", cleaned_text=ocr_text)

    lines = ocr_text.splitlines()

    # --- 1. Consecutive repetition ----------------------------------------
    consec_count, consec_line = _max_consecutive_repeats(lines)
    if consec_count > MAX_CONSECUTIVE_REPEATS:
        reason = (
            f"{source_label}: consecutive repetition detected — "
            f"'{consec_line}' repeated {consec_count}× consecutively"
        )
        logger.warning(reason)
        # Keep lines up to the first run of the repeated line
        kept: list[str] = []
        run = 0
        for line in lines:
            if line.strip() == consec_line:
                run += 1
                if run > MAX_CONSECUTIVE_REPEATS:
                    continue
            else:
                run = 0
            kept.append(line)
        cleaned = "\n".join(kept).rstrip() + "\n" + OCR_TRUNCATION_MARKER + "\n"
        return OCRSanityResult(is_clean=False, reason=reason, cleaned_text=cleaned)

    # --- 2. Section line count --------------------------------------------
    if len(lines) > MAX_SECTION_LINES:
        reason = (
            f"{source_label}: section has {len(lines)} lines "
            f"(limit {MAX_SECTION_LINES})"
        )
        logger.warning(reason)
        cleaned = "\n".join(lines[:MAX_SECTION_LINES]).rstrip() + "\n" + OCR_TRUNCATION_MARKER + "\n"
        return OCRSanityResult(is_clean=False, reason=reason, cleaned_text=cleaned)

    # --- 3. Length ratio --------------------------------------------------
    if main_post_text.strip():
        ratio = len(ocr_text) / max(len(main_post_text), 1)
        if ratio > LENGTH_RATIO_LIMIT:
            reason = (
                f"{source_label}: text is {ratio:.1f}× the main post length "
                f"(limit {LENGTH_RATIO_LIMIT}×)"
            )
            logger.warning(reason)
            # Don't truncate for length ratio alone — just warn.
            # The content might be legitimately long (e.g. AWS cheat sheet).
            # Only flag, don't modify.
            return OCRSanityResult(is_clean=False, reason=reason, cleaned_text=ocr_text)

    # --- 4. Character entropy ---------------------------------------------
    entropy = _char_entropy(ocr_text.strip())
    if entropy < MIN_CHAR_ENTROPY:
        reason = (
            f"{source_label}: character entropy {entropy:.2f} bits "
            f"(minimum {MIN_CHAR_ENTROPY})"
        )
        logger.warning(reason)
        cleaned = ocr_text.rstrip() + "\n" + OCR_TRUNCATION_MARKER + "\n"
        return OCRSanityResult(is_clean=False, reason=reason, cleaned_text=cleaned)

    return OCRSanityResult(is_clean=True, reason="", cleaned_text=ocr_text)


def sanitize_page_text(page_text: str) -> tuple[str, list[str]]:
    """Scan a full page for ``## 圖片文字`` sections and validate each one.

    Returns ``(cleaned_page_text, list_of_warnings)``.
    This can be used as a standalone post-processing step on any wiki page.
    """
    warnings: list[str] = []

    # Extract main post text for ratio comparison
    main_post_match = re.search(
        r"^## (?:主文|Main Content)\s*\n(.*?)(?=^## |\Z)",
        page_text,
        re.MULTILINE | re.DOTALL,
    )
    main_post_text = main_post_match.group(1).strip() if main_post_match else ""

    # Find all 圖片文字 sections
    pattern = re.compile(
        r"(^## 圖片文字\s*\n)(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )

    def _replace_section(match: re.Match) -> str:
        header = match.group(1)
        body = match.group(2)
        result = check_ocr_sanity(body, main_post_text, source_label="圖片文字")
        if not result.is_clean:
            warnings.append(result.reason)
            return header + result.cleaned_text
        return match.group(0)

    cleaned = pattern.sub(_replace_section, page_text)
    return cleaned, warnings


def build_page_content(
    title: str,
    path: Path,
    metadata: dict[str, str],
    main_post: str,
    author_comments: list[str],
) -> str:
    url = metadata["網址"]
    author = extract_handle(metadata["作者"])
    lines: list[str] = [
        *render_frontmatter(metadata),
        "",
        "## 主文",
        "",
        main_post.strip(),
        "",
    ]

    if author_comments:
        lines.extend(["## 作者留言", ""])
        for index, comment in enumerate(author_comments, start=1):
            lines.append(f"{index}. {comment.strip()}")
            lines.append("")

    cross_references = infer_cross_references(path)
    lines.extend(
        [
            "## Sources",
            "",
            f"- [{title}]({url}) | 作者: {author}",
            "",
            "## Cross References",
            "",
        ]
    )
    lines.extend(cross_references)
    if cross_references:
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def update_page(path: Path, api_key: str) -> dict[str, Any]:
    original_text = path.read_text(encoding="utf-8")
    metadata, _body = parse_frontmatter(original_text)
    url = metadata.get("網址", "").strip()
    author = metadata.get("作者", "").strip()
    metadata["作者"] = normalize_author_field(author)
    author_handle = extract_handle(author)
    if not url:
        raise RuntimeError(f"{path} 缺少網址")
    if not author_handle:
        raise RuntimeError(f"{path} 缺少作者")

    social: SocialCrawlResult | None = None
    try:
        social = fetch_threads_post(url, api_key)
    except HTTPError:
        social = None

    extraction_mode = "playwright_only"
    extracted: AuthorContentResult | None = None
    try:
        extracted = fetch_author_content(url, author_handle)
        extraction_mode = "playwright+socialcrawl" if social else "playwright_only"
    except Exception:
        extracted = None
        extraction_mode = "socialcrawl_only" if social else "unavailable"

    playwright_main = clean_main_post_text(extracted.main_post) if extracted else ""
    social_main = clean_main_post_text(social.root_post_text) if social else ""
    main_post = playwright_main or social_main
    if not main_post:
        raise RuntimeError(f"{path} 無法抽取主文")

    author_comments = clean_author_comments(extracted.author_comments) if extracted else []

    new_text = build_page_content(
        title=path.stem,
        path=path,
        metadata=metadata,
        main_post=main_post,
        author_comments=author_comments,
    )

    # --- Sanity-check the final page text before writing -------------------
    sanitized_text, ocr_warnings = sanitize_page_text(new_text)
    if ocr_warnings:
        for warning in ocr_warnings:
            logger.warning("OCR sanity check (%s): %s", path, warning)
        new_text = sanitized_text

    path.write_text(new_text, encoding="utf-8")

    return {
        "path": str(path),
        "main_post": main_post,
        "comment_count": len(author_comments),
        "socialcrawl_root_author": social.root_author_username if social else None,
        "extraction_mode": extraction_mode,
        "ocr_warnings": ocr_warnings,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="Markdown page paths to fill")
    args = parser.parse_args()

    api_key = os.getenv("SOCIALCRAWL_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("缺少必要環境變數：SOCIALCRAWL_API_KEY")

    failures: list[dict[str, str]] = []
    for raw_path in args.paths:
        try:
            result = update_page(Path(raw_path), api_key)
            print(json.dumps(result, ensure_ascii=True))
        except Exception as exc:
            failure = {"path": raw_path, "error": str(exc)}
            failures.append(failure)
            print(json.dumps(failure, ensure_ascii=True))

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

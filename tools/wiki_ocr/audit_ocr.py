from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _image_ocr import (
    _OCR_SECTION_RE,
    DEFAULT_MODEL,
    apply_ocr_section,
    build_ocr_image,
    load_dotenv,
    ocr_post_images,
)

OBSIDIAN_URI_RE = re.compile(r"obsidian://open\?vault=knowledge-wiki&file=([^)]+)")
URL_RE = re.compile(r"^網址:\s*(.+)$", re.MULTILINE)
_REPO_ROOT = Path(__file__).resolve().parents[2]


def parse_audit_report(path: Path) -> tuple[str, list[dict]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    fmt: str | None = None
    all_rows: list[dict] = []
    headers: list[str] = []
    in_table = False

    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            in_table = False
            continue

        cells = [c.strip() for c in stripped.strip("|").split("|")]

        if not in_table:
            headers = cells
            # Only detect format from data tables (those with 頁面 column)
            if "頁面" in cells:
                detected = "B" if "signals" in cells else "A"
                # Once we see Format B, never downgrade to A
                if fmt is None or detected == "B":
                    fmt = detected
            in_table = True
            continue

        if all(set(c) <= {"-", ":", " "} for c in cells):
            continue

        # Only collect rows from data tables (those with 頁面 in headers)
        if "頁面" in headers:
            row = dict(zip(headers, cells))
            all_rows.append(row)

    return fmt or "A", all_rows


def filter_ocr_targets(fmt: str, rows: list[dict]) -> list[dict]:
    targets: list[dict] = []
    for row in rows:
        action = row.get("處置", "").strip()
        if not action:
            continue

        if fmt == "A":
            if re.match(r"路線.+#\d+", action):
                continue
            if "ocr" not in action.lower():
                continue
        else:
            dup = row.get("dup", "").strip()
            if dup:
                continue
            tokens = [t.strip() for t in action.split(",")]
            if "ocr-images" not in tokens:
                continue

        targets.append(row)
    return targets


def extract_wiki_path(page_cell: str) -> Path | None:
    m = OBSIDIAN_URI_RE.search(page_cell)
    if not m:
        return None
    decoded = unquote(m.group(1))
    return _REPO_ROOT / "wiki-pages" / (decoded + ".md")


def extract_threads_url(wiki_path: Path) -> str | None:
    try:
        text = wiki_path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = URL_RE.search(text)
    if not m:
        return None
    url = m.group(1).strip().strip("[]\"'")
    return url if url else None


def has_ocr_section(wiki_path: Path) -> bool:
    try:
        text = wiki_path.read_text(encoding="utf-8")
    except OSError:
        return False
    return "## 圖片文字" in text


def build_work_items(targets: list[dict]) -> list[dict]:
    items: list[dict] = []
    for row in targets:
        wiki_path = extract_wiki_path(row.get("頁面", ""))
        if wiki_path is None:
            print(f"  WARN: cannot extract path from: {row.get('頁面', '')}", file=sys.stderr)
            continue
        items.append({"row": row, "wiki_path": wiki_path})
    return items


def dry_run(audit_path: Path, fmt: str, work_items: list[dict]) -> int:
    print("== DRY RUN ==")
    print(f"audit format: {'B (new)' if fmt == 'B' else 'A (legacy)'}")
    print(f"audit file: {audit_path}")
    print(f"targets found: {len(work_items)}")
    print()

    existing_count = 0
    for i, item in enumerate(work_items, 1):
        wp = item["wiki_path"]
        url = extract_threads_url(wp)
        has_existing = has_ocr_section(wp)
        if has_existing:
            existing_count += 1

        print(f"[{i}] {wp}")
        print(f"    threads URL: {url or '(none)'}")
        print(f"    status: would fetch images + OCR + apply ## 圖片文字")
        print(f"    has existing ## 圖片文字: {'Yes' if has_existing else 'No'}")
        print()

    print(f"summary: {len(work_items)} targets | {existing_count} with existing OCR | run with --apply to execute")
    return 0


def apply_mode(work_items: list[dict], *, api_key: str, model: str,
               headless: bool, skip_existing: bool) -> int:
    print("== APPLY ==")
    ocr_image = build_ocr_image(api_key=api_key, model=model)
    total = len(work_items)
    ocrd = 0
    skipped = 0
    errors = 0

    for i, item in enumerate(work_items, 1):
        wp = item["wiki_path"]
        print(f"[{i}/{total}] processing {wp}")

        if not wp.exists():
            print(f"      SKIP: file not found")
            skipped += 1
            continue

        if skip_existing and has_ocr_section(wp):
            print(f"      SKIP: already has ## 圖片文字")
            skipped += 1
            continue

        url = extract_threads_url(wp)
        if not url:
            print(f"      SKIP: no 網址 in frontmatter", file=sys.stderr)
            skipped += 1
            continue
        print(f"      threads URL: {url}")

        try:
            ocr_texts = ocr_post_images(post_url=url, ocr_image=ocr_image, headless=headless)
        except Exception as exc:
            print(f"      ERROR: {exc}", file=sys.stderr)
            errors += 1
            continue

        if not ocr_texts:
            print(f"      SKIP: no images found (may be text-only — flag for review)")
            skipped += 1
            continue

        print(f"      fetched + OCR'd {len(ocr_texts)} images")

        try:
            apply_ocr_section(wp, ocr_texts)
            total_chars = sum(len(t) for t in ocr_texts)
            print(f"      wrote ## 圖片文字 section ({total_chars} chars)")
            ocrd += 1
        except Exception as exc:
            print(f"      ERROR writing: {exc}", file=sys.stderr)
            errors += 1

    print()
    print(f"summary: targets={total} | ocr'd={ocrd} | skipped={skipped} | errors={errors}")
    return 1 if errors else 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read audit reports, OCR Threads images, write ## 圖片文字 to wiki pages."
    )
    parser.add_argument("audit_report", help="path to audit report (Format A or B)")
    parser.add_argument("--apply", action="store_true", help="execute OCR (default: dry-run)")
    parser.add_argument("--limit", type=int, default=0, help="process at most N pages")
    parser.add_argument("--env-file", default=".env", help="dotenv location")
    parser.add_argument("--headed", action="store_true", help="run Playwright with visible browser")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Gemini model name")
    parser.add_argument("--skip-existing", action="store_true", help="skip pages with existing ## 圖片文字")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    load_dotenv(Path(args.env_file))

    audit_path = Path(args.audit_report)
    if not audit_path.exists():
        print(f"ERROR: audit report not found: {audit_path}", file=sys.stderr)
        return 1

    fmt, all_rows = parse_audit_report(audit_path)
    targets = filter_ocr_targets(fmt, all_rows)
    work_items = build_work_items(targets)

    if args.limit > 0:
        work_items = work_items[: args.limit]

    if not args.apply:
        return dry_run(audit_path, fmt, work_items)

    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found. Set in .env or environment.", file=sys.stderr)
        return 1

    return apply_mode(
        work_items,
        api_key=api_key,
        model=args.model,
        headless=not args.headed,
        skip_existing=args.skip_existing,
    )


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from playwright.sync_api import Page, sync_playwright


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
    normalized_handle = target_handle.strip().lstrip("@")
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


def build_page_content(
    title: str,
    path: Path,
    metadata: dict[str, str],
    main_post: str,
    author_comments: list[str],
) -> str:
    url = metadata["網址"]
    author = metadata["作者"]
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
    if not url:
        raise RuntimeError(f"{path} 缺少網址")
    if not author or author == "[]":
        raise RuntimeError(f"{path} 缺少作者")

    social: SocialCrawlResult | None = None
    try:
        social = fetch_threads_post(url, api_key)
    except HTTPError:
        social = None

    extraction_mode = "playwright_only"
    extracted: AuthorContentResult | None = None
    try:
        extracted = fetch_author_content(url, author)
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
    path.write_text(new_text, encoding="utf-8")

    return {
        "path": str(path),
        "main_post": main_post,
        "comment_count": len(author_comments),
        "socialcrawl_root_author": social.root_author_username if social else None,
        "extraction_mode": extraction_mode,
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

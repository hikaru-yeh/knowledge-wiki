from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Callable
from urllib import request

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _gemini_client import GeminiClient


DEFAULT_OCR_BACKEND = "gemini"
DEFAULT_MODEL = "gemini-3.1-flash"
OCR_PROMPT = (
    "分析這張圖片的內容，以結構化 Markdown 格式輸出。規則：\n"
    "1. 程式碼截圖 → 用 fenced code block（附語言標籤），保留縮排\n"
    "2. 終端機/命令列輸出 → 用 ```text 或 ```bash code block\n"
    "3. 對話截圖（聊天、推文、留言串）→ 用引言格式（> ），標明發言者\n"
    "4. 圖表/流程圖 → 先用一句話描述，再列出關鍵節點或數據\n"
    "5. 一般文字 → 用適當的標題、列表、段落組織\n"
    "6. 混合內容 → 依各區塊類型分別處理\n"
    "直接輸出 Markdown，不要加前言或解釋。"
)
_OCR_SECTION_RE = re.compile(r"\n*## 圖片文字\n\n.*?(?=\n## |\Z)", re.DOTALL)


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export "):].strip()
        key, raw_value = line.split("=", 1)
        key = key.strip()
        if not key or key in os.environ:
            continue
        value = raw_value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        os.environ[key] = value


def apply_ocr_section(markdown_path: Path, ocr_texts: list[str]) -> None:
    if not ocr_texts:
        return
    text = markdown_path.read_text(encoding="utf-8")
    text = _OCR_SECTION_RE.sub("", text).rstrip()
    section = "## 圖片文字\n\n" + "\n\n---\n\n".join(t.strip() for t in ocr_texts if t.strip()) + "\n\n"
    sources_index = text.find("## Sources")
    if sources_index == -1:
        updated = text + "\n\n" + section
    else:
        updated = text[:sources_index].rstrip() + "\n\n" + section + text[sources_index:]
    if not updated.endswith("\n"):
        updated += "\n"
    markdown_path.write_text(updated, encoding="utf-8")


def extract_post_image_urls_from_dom_records(records: list[dict]) -> list[str]:
    urls: list[str] = []
    seen: set[str] = set()
    for record in records:
        src = str(record.get("src") or "")
        width = int(record.get("w") or 0)
        height = int(record.get("h") or 0)
        if "/v/t51.82787-15/" not in src:
            continue
        if width < 200 or height < 250:
            continue
        if src in seen:
            continue
        seen.add(src)
        urls.append(src)
    return urls


def fetch_image_urls_with_playwright(post_url: str, *, headless: bool = True) -> list[str]:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        try:
            page = browser.new_page(
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                )
            )
            page.goto(post_url, wait_until="domcontentloaded", timeout=30000)
            page.wait_for_timeout(5000)
            records = page.evaluate(
                """() => Array.from(document.images).map((img) => ({
                    src: img.currentSrc || img.src,
                    w: img.naturalWidth,
                    h: img.naturalHeight,
                    alt: img.alt || "",
                }))"""
            )
            return extract_post_image_urls_from_dom_records(records)
        finally:
            browser.close()


def download_image(url: str) -> bytes:
    with request.urlopen(url, timeout=20) as response:
        return response.read()


def build_gemini_ocr_image(*, api_key: str, model: str = DEFAULT_MODEL) -> Callable[[str], str]:
    if not api_key.strip():
        raise RuntimeError("GEMINI_API_KEY missing. Set in .env or pass --api-key.")
    client = GeminiClient(api_key=api_key)

    def ocr_image(image_url: str) -> str:
        return client.generate_text_from_image(download_image(image_url), OCR_PROMPT, model=model)

    return ocr_image


def build_ocr_image(*, api_key: str, model: str = DEFAULT_MODEL) -> Callable[[str], str]:
    return build_gemini_ocr_image(api_key=api_key, model=model)


def ocr_post_images(*, post_url: str, ocr_image: Callable[[str], str], headless: bool = True) -> list[str]:
    texts: list[str] = []
    for image_url in fetch_image_urls_with_playwright(post_url, headless=headless):
        try:
            text = ocr_image(image_url)
        except Exception:
            continue
        if text.strip():
            texts.append(text.strip())
    return texts

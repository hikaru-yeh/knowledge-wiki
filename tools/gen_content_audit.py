#!/usr/bin/env python3
"""Generate content quality audit report with auto-filled signals."""
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote

sys.stdout.reconfigure(encoding="utf-8")

wiki_dir = Path("wiki-pages")
raw_dir = Path("raw")
vault_name = "knowledge-wiki"

promo_patterns = [
    r"儲存\s*💾", r"追蹤\s*@", r"獲取更多", r"分享給.*朋友",
    r"按讚.*收藏", r"#\w+\s+#\w+", r"👇.*留言", r"tag.*朋友",
]
promo_re = "|".join(promo_patterns)

video_re = re.compile(
    r"instagram\.com/reel|youtube\.com|youtu\.be|tiktok\.com|x\.com/.*?/status/.*?/video",
    re.IGNORECASE,
)
url_extract_re = re.compile(r"https?://[^\s)>\]]+")


def collect_raw_urls(raw_dir):
    urls = set()
    if not raw_dir.exists():
        return urls
    for raw in raw_dir.rglob("*.md"):
        try:
            text = raw.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if not m:
            continue
        for key in ("網址", "url"):
            url_match = re.search(rf"^{key}:\s*(.+)$", m.group(1), re.MULTILINE)
            if url_match:
                u = url_match.group(1).strip().strip("[]\"'")
                if u:
                    urls.add(u)
                break
    return urls


def detect_signals(body, cat, fm_url, raw_urls):
    sigs = []
    if cat == "LingOrm":
        sigs.append("lingorm")
    if video_re.search(body):
        sigs.append("video")
    ext_urls = url_extract_re.findall(body)
    non_threads = [u for u in ext_urls if "threads.com" not in u]
    bare_urls = [m.group(0) for m in bare_url_re.finditer(body) if "threads.com" not in m.group(0).lower()]
    if non_threads or bare_urls:
        sigs.append("ext_url")
    combined = " ".join(non_threads + bare_urls).lower()
    if "github.com" in combined:
        sigs.append("github")
    body_strip = re.sub(r"\s+", "", body)
    if body_strip.startswith(("[https://www.threads.com", "[http://www.threads.com")) and len(body_strip) < 250:
        sigs.append("tw_url_only")
    if fm_url:
        fm_url_clean = fm_url.strip("[]\"'")
        if fm_url_clean and fm_url_clean not in raw_urls:
            sigs.append("raw_gone")
    if re.search(promo_re, body, re.IGNORECASE):
        sigs.append("cta")
    return ",".join(sigs)


bare_url_re = re.compile(
    r"(?:https?://)?(?:www\.)?"
    r"(github\.com|youtube\.com|youtu\.be|x\.com|twitter\.com|medium\.com|instagram\.com|"
    r"claude\.com|anthropic\.com|notion\.so|reddit\.com|substack\.com|dev\.to)"
    r"/[^\s)>\]\"']+",
    re.IGNORECASE,
)


def suggest_url(body, signals_list, fm_url):
    if "tw_url_only" in signals_list and fm_url:
        return fm_url.strip("[]\"'")[:80]
    bare = bare_url_re.findall(body)
    full_urls = bare_url_re.finditer(body)
    candidates = []
    for m in full_urls:
        u = m.group(0).rstrip(".,;)…")
        if "threads.com" in u.lower():
            continue
        if not u.lower().startswith("http"):
            u = "https://" + u
        candidates.append(u)
    if not candidates:
        ext_urls = url_extract_re.findall(body)
        non_threads = [u.rstrip(".,;)") for u in ext_urls if "threads.com" not in u]
        candidates = non_threads
    if not candidates:
        return ""
    github = [u for u in candidates if "github.com" in u.lower()]
    return (github[0] if github else candidates[0])[:80]


raw_urls = collect_raw_urls(raw_dir)

route1 = []
route2 = []
route3_a = []
route3_b = []

for md in sorted(wiki_dir.rglob("*.md")):
    rel_str = str(md.relative_to(wiki_dir))
    if "index" in rel_str or "專案管理" in rel_str or rel_str == "log.md":
        continue
    text = md.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        continue
    fm = m.group(1)
    if "status: wiki" not in fm and "status: reference" not in fm:
        continue

    status_match = re.search(r"status:\s*(\S+)", fm)
    status = status_match.group(1) if status_match else "?"

    url_match = re.search(r"網址:\s*(.+)", fm)
    fm_url = url_match.group(1).strip() if url_match else ""

    body = text[m.end():].strip()
    body_clean = re.sub(r"^##\s*Main Content\s*\n*", "", body).strip()
    blen = len(body_clean)

    note_rel = "wiki-pages/" + rel_str.replace("\\", "/").replace(".md", "")
    obs_uri = f"obsidian://open?vault={vault_name}&file={quote(note_rel, safe='/')}"

    parts = rel_str.replace("\\", "/").split("/")
    cat = parts[0] if len(parts) > 1 else "root"

    preview = body_clean[:120].replace("|", "\\|").replace("\n", " ")

    signals = detect_signals(body_clean, cat, fm_url, raw_urls)
    suggested = suggest_url(body_clean, signals.split(","), fm_url)

    entry = {
        "name": md.stem,
        "cat": cat,
        "status": status,
        "blen": blen,
        "fm_url": fm_url,
        "obs_uri": obs_uri,
        "preview": preview,
        "signals": signals,
        "suggested": suggested,
    }

    if blen < 500 and re.search(promo_re, body_clean, re.IGNORECASE) and fm_url:
        route1.append(entry)
    if blen < 300 and re.search(r"https?://|github\.com", body_clean):
        route2.append(entry)
    if blen < 200:
        route3_a.append(entry)
    if 200 <= blen < 300:
        route3_b.append(entry)


sorted_routes = {
    "1": [dict(e) for e in sorted(route1, key=lambda x: x["blen"])],
    "2": [dict(e) for e in sorted(route2, key=lambda x: x["blen"])],
    "3a": [dict(e) for e in sorted(route3_a, key=lambda x: x["blen"])],
    "3b": [dict(e) for e in sorted(route3_b, key=lambda x: x["blen"])],
}

seen = {}
for label in ["1", "2", "3a", "3b"]:
    for i, e in enumerate(sorted_routes[label], 1):
        if e["name"] not in seen:
            seen[e["name"]] = (label, i)

for label in ["1", "2", "3a", "3b"]:
    for i, e in enumerate(sorted_routes[label], 1):
        primary = seen[e["name"]]
        e["dup"] = "" if primary == (label, i) else f"→ 路線{primary[0]} #{primary[1]}"


def suggest_action(e):
    if e["dup"]:
        return ""
    sigs = set(e["signals"].split(",")) if e["signals"] else set()
    if "raw_gone" in sigs:
        return "delete"
    if "lingorm" in sigs:
        return "demote"
    if "video" in sigs:
        return "demote"
    if "github" in sigs and e["suggested"]:
        return "fetch-url"
    if "ext_url" in sigs and e["suggested"] and "threads.com" not in e["suggested"]:
        return "fetch-url"
    if "tw_url_only" in sigs:
        return "demote"
    if "cta" in sigs:
        return "ocr-images"
    return "demote"


for label in ["1", "2", "3a", "3b"]:
    for e in sorted_routes[label]:
        e["action"] = suggest_action(e)


def table(entries):
    lines = []
    lines.append("| # | 分類 | signals | dup | suggested_url | 處置 | 頁面 | status | 字元 | body 預覽 |")
    lines.append("|---|------|---------|-----|---------------|------|------|--------|------|-----------|")
    for i, e in enumerate(entries, 1):
        p = e["preview"][:60]
        sug = e["suggested"][:60]
        lines.append(
            f'| {i} | {e["cat"]} | {e["signals"]} | {e["dup"]} | {sug} | {e["action"]} | '
            f'[{e["name"]}]({e["obs_uri"]}) | {e["status"]} | {e["blen"]} | {p} |'
        )
    return "\n".join(lines)


today = date.today().isoformat()

report = f"""# 內容品質審查報告

> Generated: {today}
> Total wiki/reference: 392 | Route 1: {len(route1)} | Route 2: {len(route2)} | Route 3a (<200): {len(route3_a)} | Route 3b (200-300): {len(route3_b)}

## Signals 說明

| signal | 觸發條件 | 隱含建議 |
|--------|---------|---------|
| `lingorm` | 分類為 LingOrm | 依 CLAUDE.md 規則降級 stub |
| `video` | body 含 instagram reel / youtube / tiktok 連結 | 無法純文字補完，降級 stub |
| `raw_gone` | wiki 的 `網址` 不在 raw/ URL 集合中 | raw 被刪除，建議 delete |
| `ext_url` | body 含非 threads.com 外部 URL | 可 fetch 該 URL 補完 |
| `github` | body 含 github.com URL | fetch GitHub repo 內容 |
| `tw_url_only` | body 主要內容只是 threads URL 嵌入 | 內容空，視情況降級或 ocr 補完 |
| `cta` | body 含推廣文案（追蹤/儲存/分享） | 實質內容可能在附圖 |

## 處置動詞建議

| 動詞 | 說明 |
|------|------|
| `demote` | 降級 stub |
| `delete` | 刪除頁面（通常配合 raw_gone） |
| `fetch-url` | fetch suggested_url 內容覆寫 |
| `ocr-images` | OCR 原 threads 附圖補入 |
| `embed-images` | 把圖片本身嵌入頁面（不只 OCR） |
| `noop` | 內容雖短但 acceptable |
| `rewrite` | 內容夠但需重寫整理 |
| `fix-url` / `fix-title` / `fix-category` / `add-xref` | 微修補 |

## 處置欄自動填規則

工具會根據 signals 自動填入建議動作，使用者可覆寫。優先序：

1. 有 `dup` marker → 空（看 primary）
2. `raw_gone` → `delete`
3. `lingorm` → `demote`
4. `video` → `demote`
5. `github` + 有 suggested_url → `fetch-url`
6. `ext_url` + 有 suggested_url（非 threads）→ `fetch-url`
7. `tw_url_only` → `demote`（保守；若內容有價值改 `ocr-images`）
8. `cta` 單獨 → `ocr-images`（假設有附圖）
9. 其他 → `demote`

工具無法判斷 `embed-images`（圖片本身有視覺價值）vs `ocr-images`，預設 `ocr-images`。也無法判斷 `fix-url` / `fix-title` / `noop`，需要人工覆寫。

---

## 路線一：可能含未 OCR 附圖（< 500 字元 + 推廣文案 + 有網址）

共 {len(route1)} 頁。

{table(sorted_routes["1"])}

---

## 路線二：含外部連結但未消化（< 300 字元 + 外部 URL）

共 {len(route2)} 頁。

{table(sorted_routes["2"])}

---

## 路線三 A：body < 200 字元的 wiki/reference 頁面

共 {len(route3_a)} 頁。

{table(sorted_routes["3a"])}

---

## 路線三 B：body 200-300 字元的 wiki/reference 頁面

共 {len(route3_b)} 頁。

{table(sorted_routes["3b"])}
"""

audit_dir = Path("audit")
audit_dir.mkdir(exist_ok=True)
out = audit_dir / f"content-audit-{today}.md"
out.write_text(report, encoding="utf-8")
print(f"wrote {out}")
print(f"raw URLs indexed: {len(raw_urls)}")
print(f"Route 1: {len(route1)}, Route 2: {len(route2)}, Route 3a: {len(route3_a)}, Route 3b: {len(route3_b)}")

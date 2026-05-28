"""
inject_pending_digest.py

Matches pending-digest-app-output files to wiki-pages by URL,
then replaces "## Main Content（📌 待消化）" stubs with actual content.
Updates status: stub → wiki (Level 2) or keeps stub (Level 1).
"""

import os
import re

PENDING_DIR = r"D:\shane_yeh\Documents\_Claude_Code\crawl-the-threads\data\pending-digest-app-output"
WIKI_DIR = r"D:\shane_yeh\Documents\_Claude_Code\knowledge-wiki\wiki-pages"

STUB_PATTERNS = [
    "## Main Content\n\n（📌 待消化）",
    "## Main Content\n（📌 待消化）",
]

LEVEL2_RE = re.compile(
    r"```|❶|❷|❸|❹|❺|步驟\s*[：:]|Step\s+\d|第[一二三四五六七八九十]+步"
    r"|^\d+\.\s|^[•▪▸]\s.*(?:指令|設定|安裝|執行)|如何[^嗎]|怎麼做"
    r"|(?:N|[0-9]+)\s*個(?:方法|技巧|步驟|招|指令)",
    re.MULTILINE,
)


def parse_frontmatter(text):
    """Return (frontmatter_str, body_str). frontmatter_str excludes --- delimiters."""
    text = text.lstrip("﻿")  # strip UTF-8 BOM (U+FEFF) added by some Windows editors
    if not text.startswith("---"):
        return "", text
    end = text.find("---", 3)
    if end == -1:
        return "", text
    return text[3:end].strip(), text[end + 3:].strip()


def get_field(fm_str, key):
    for line in fm_str.splitlines():
        if line.strip().startswith(key + ":"):
            val = line.split(":", 1)[1].strip().strip('"').strip("'")
            val = val.lstrip("[").rstrip("]").strip()
            return val
    return ""


def determine_status(body):
    if LEVEL2_RE.search(body):
        return "wiki"
    # Also promote if body has numbered image-text sections (多個 ---分隔)
    if body.count("\n---\n") >= 2 and len(body) > 300:
        return "wiki"
    return "stub"


# ── Build URL index from wiki-pages ──────────────────────────────────────────
wiki_url_index = {}  # normalised_url → file_path

for root, _, files in os.walk(WIKI_DIR):
    for fname in files:
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(root, fname)
        try:
            with open(fpath, encoding="utf-8") as f:
                raw = f.read()
            fm, _ = parse_frontmatter(raw)
            url = get_field(fm, "網址").rstrip("/")
            if url.startswith("http"):
                if url in wiki_url_index:
                    print(f"[WARN] duplicate URL {url}\n  old={wiki_url_index[url]}\n  new={fpath}")
                else:
                    wiki_url_index[url] = fpath
        except Exception as e:
            print(f"[ERR] reading {fpath}: {e}")

print(f"Wiki URL index: {len(wiki_url_index)} entries\n")

# ── Process pending files ─────────────────────────────────────────────────────
updated, skipped = [], []

for fname in sorted(os.listdir(PENDING_DIR)):
    if not fname.endswith(".md"):
        continue

    pending_path = os.path.join(PENDING_DIR, fname)
    try:
        with open(pending_path, encoding="utf-8") as f:
            pending_raw = f.read()

        fm, body = parse_frontmatter(pending_raw)
        url = get_field(fm, "url").rstrip("/")
        if not url.startswith("http"):
            skipped.append((fname, "no URL in frontmatter"))
            continue

        wiki_path = wiki_url_index.get(url)
        if not wiki_path:
            skipped.append((fname, f"no wiki match — {url}"))
            continue

        with open(wiki_path, encoding="utf-8") as f:
            wiki_raw = f.read()

        # Check this is still a stub
        has_stub = any(p in wiki_raw for p in STUB_PATTERNS)
        if not has_stub:
            skipped.append((fname, f"already has content — {os.path.basename(wiki_path)}"))
            continue

        new_status = determine_status(body)

        # Replace stub block
        new_wiki = wiki_raw
        for p in STUB_PATTERNS:
            if p in new_wiki:
                new_wiki = new_wiki.replace(p, f"## Main Content\n\n{body}", 1)
                break

        # Update status field
        new_wiki = re.sub(r"(status:\s*)stub", rf"\g<1>{new_status}", new_wiki, count=1)

        with open(wiki_path, "w", encoding="utf-8") as f:
            f.write(new_wiki)

        updated.append((fname, wiki_path, new_status))
        print(f"[OK] {fname}\n     → {os.path.relpath(wiki_path, WIKI_DIR)}  [{new_status}]")

    except Exception as e:
        skipped.append((fname, f"error: {e}"))

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"Updated : {len(updated)}")
print(f"Skipped : {len(skipped)}")
if skipped:
    print("\nSkipped details:")
    for f, r in skipped:
        print(f"  {f}: {r}")

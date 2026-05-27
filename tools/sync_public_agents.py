"""Generate the public AGENTS.md from the private CLAUDE.md rules.

This helper is intentionally conservative: it reads a CLAUDE.md source from a
git ref (default: ``master``), removes private category/project-only rules, and
writes a public-safe AGENTS.md skeleton that preserves the general wiki
maintenance workflow.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


PRIVATE_TOKENS = (
    "LingOrm",
    "專案管理",
    "専案管理",
    "PROJECTS.md",
    "_Claude_Code",
    "privacy_sanitize_rules.md",
    ".gbrain-source",
    "gbrain",
    "Heart Talk",
    "台北 FM",
    "Lint 例外",
)

PRIVATE_HEADING_TOKENS = (
    "LingOrm",
    "專案管理",
    "専案管理",
)


PUBLIC_HEADER = """# AGENTS.md

This file is generated from the private `CLAUDE.md` workflow rules and then
sanitized for the public showcase branch. Private category exceptions, local
absolute paths, editor state, and project-only rules are intentionally omitted.

"""


PUBLIC_STRUCTURE = """## Repository Structure

```text
knowledge-wiki/
├── AGENTS.md
├── README.md
├── raw/
│   ├── README.md
│   └── examples/
├── tasks/
│   └── maintenance-reports/
├── tools/
│   ├── wiki_maintain.py
│   └── sync_public_agents.py
└── wiki-pages/
    ├── README.md
    ├── index/
    │   └── example-index.md
    ├── example-topic/
    │   └── example-wiki-page.md
    └── log.example.md
```

Private working vaults may contain many more category folders and operational
task files. Those are intentionally ignored in the public showcase branch.

"""


PUBLIC_QUERY = """### Query

當使用者詢問既有 wiki 知識時，使用 query 模式。

必要流程：

1. 優先搜尋 `wiki-pages/` 內的 curated pages。若私有工作環境有語意搜尋工具，可先用語意搜尋，再用文字搜尋補查。
2. 根據 wiki 內容回答。
3. 在回答中引用相關頁面名稱。
4. 知識缺口回報：query 結束時，若發現以下狀況必須回報給使用者：
   - **檢索失敗**：相關主題在 wiki 中明明有來源，但因為被過度精簡而答不出來
     → 提示：「這個問題在 [[X]] 應該有答案但細節已被精簡，建議 re-ingest」
   - **stub 阻塞**：相關主題的頁面多為 stub 狀態，無法整合回答
     → 提示：「以下 stub 頁面與本問題相關，建議 promote：[[A]] [[B]] [[C]]」
   - **散落問題**：相關資訊分散在 3 個以上頁面，沒有索引整合
     → 提示：「建議建立能力索引：能力-XXX.md」
   - **過期問題**：找到的頁面引用了舊版工具/API
     → 提示：「[[Y]] 內容可能已過期，最後更新於 YYYY-MM-DD」
5. 如果本次查詢產生了可長期保存的新洞察，將其整理成新的 wiki 頁面。
6. 如果 query 發現既有內容錯誤，應切換到 correction 模式，而不是直接靜默修改。
7. 在 `wiki-pages/log.md` 追加一筆 log：
   - `## [YYYY-MM-DD] query | <question summary>`

"""


PUBLIC_SUBCATEGORY_NAMING = """## 子分類命名規範

當一個分類包含本質不同的內容類型時，索引 H2 應明確標示內容格式或性質。

### 區分維度：格式/媒介

同一主題下有不同媒介的內容時，H2 用媒介前綴區分：

- `影片素材-XXX`：影片片段、直播剪輯、教學錄影
- `文字創作-XXX`：文章、故事、散文、長文整理
- `訪談素材-XXX`：採訪、對談、問答整理
- `圖文素材-XXX`：圖片集、攝影集、視覺素材

規則：

- 若分類內只有一種格式，不需要加前綴，直接用內容語意命名。
- 同一 H2 內不可混合不同媒介格式。

"""


def read_git_blob(source_ref: str, source_path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{source_ref}:{source_path}"],
        check=True,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
    )
    return result.stdout


def heading_level(line: str) -> int | None:
    stripped = line.lstrip()
    if not stripped.startswith("#"):
        return None
    hashes = len(stripped) - len(stripped.lstrip("#"))
    if hashes and stripped[hashes : hashes + 1] == " ":
        return hashes
    return None


def sanitize_claude(source: str) -> str:
    lines = source.splitlines()
    output: list[str] = [PUBLIC_HEADER.rstrip(), "", PUBLIC_STRUCTURE.rstrip(), ""]

    skip_until_level: int | None = None
    in_repo_structure = False

    for line in lines:
        level = heading_level(line)

        if line.strip() == "# CLAUDE.md":
            continue

        if level is not None:
            if skip_until_level is not None and level <= skip_until_level:
                skip_until_level = None

            if line.strip() == "## Repository 結構":
                in_repo_structure = True
                continue

            if line.strip() == "### Query":
                output.append(PUBLIC_QUERY.rstrip())
                output.append("")
                skip_until_level = level
                continue

            if line.strip() == "## 子分類命名規範":
                output.append(PUBLIC_SUBCATEGORY_NAMING.rstrip())
                output.append("")
                skip_until_level = level
                continue

            if in_repo_structure and level <= 2:
                in_repo_structure = False

            if any(token in line for token in PRIVATE_HEADING_TOKENS):
                skip_until_level = level
                continue

        if skip_until_level is not None or in_repo_structure:
            continue

        if any(token in line for token in PRIVATE_TOKENS):
            continue

        cleaned = line.replace("CLAUDE.md", "AGENTS.md")
        output.append(cleaned)

    text = "\n".join(output).strip() + "\n"
    text = text.replace("`作者: gracetzeng`", '`作者: ["@gracetzeng"]`')
    text = text.replace("則自動以 `<account>` 作為 `作者`", '則自動以 `["@<account>"]` 作為 `作者`')
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    return text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate public AGENTS.md from a private CLAUDE.md source."
    )
    parser.add_argument("--source-ref", default="master", help="Git ref containing CLAUDE.md.")
    parser.add_argument("--source-path", default="CLAUDE.md", help="Source path in the git ref.")
    parser.add_argument("--output", default="AGENTS.md", help="Output AGENTS.md path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if output differs, without writing.",
    )
    args = parser.parse_args()

    source = read_git_blob(args.source_ref, args.source_path)
    rendered = sanitize_claude(source)
    output_path = Path(args.output)

    if args.check:
        existing = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
        if existing != rendered:
            print(f"{output_path} is out of sync with {args.source_ref}:{args.source_path}")
            return 1
        print(f"{output_path} is in sync")
        return 0

    output_path.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {output_path} from {args.source_ref}:{args.source_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

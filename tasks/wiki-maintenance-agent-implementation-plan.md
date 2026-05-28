# Agent Implementation Plan: knowledge-wiki 維護自動化工具

> 這份文件是給 Claude Code / Codex agent 實作的，不是給 Shane 手動照做的。  
> Shane 不需要會 Python。Agent 必須依本文件建立腳本、驗證、報告格式與使用文件。

## 0.1 執行進度更新（2026-05-28）

本節記錄本 session 中 Claude Code / worker 已回報完成的任務，避免下一個 session 只看到原始規格而誤以為尚未開始。

### 已完成

- CLI skeleton 與共用 options 已建立於 `tools/wiki_maintain.py`。
- 基礎 loader / frontmatter parser / URL normalize / wiki/raw 掃描能力已可支撐目前 subcommands。
- `handoff` 已可寫入 `tasks/current-handoff.md`。
- `blocked-report` 已可寫入 `tasks/blocked-content-gaps.md`，並區分 blocked 類型。
- `status-audit` 已完成，包含 status 掃描、missing/unknown status、excluded README 與 frontmatter author issue。
- `index-lint` 已完成第一版，能偵測 ambiguous bare links、missing target、literal raw link、stub marker mismatch。
- `review-reconcile` 已完成第一版，可將 review findings 分到固定 buckets。
- `coverage` 已完成，能輸出 raw-only ingest candidates、missing-url 與 heuristic category。
- `duplicates` 已完成，能掃 duplicate URL groups；目前 repo 已清到 0 duplicate groups。
- `canonical-guard` 已完成，包含 stale canonical conflict 與 author frontmatter canonical rule。
- shared frontmatter author validator 已完成，canonical rule 為 `作者: ["@handle"]` 或 `作者: []`。
- `author-fix` subcommand 已完成並執行 `--apply`：83 個 bare-string `作者` 已全部修正為 canonical `["@handle"]` 格式，驗證 0 remaining（commit `822fd3f`）。
- Generator hardening 已完成：`fill_threads_stub_pages.py` 新增 `normalize_author_field()` + `extract_handle()` 雙函數，防止未來再產生 bare-string author。後續工具不可再產生 `作者: [@handle]` / `作者: [handle]`。
- Author frontmatter canonical rule 已同步到 runtime agent docs：`master` 的 `CLAUDE.md` 以及 `codex/public-showcase` 的 `AGENTS.md` / `AGENTS_en.md` 都已明確要求 `作者: ["@handle"]` 或 `作者: []`，並禁止 bare string / unquoted bracket 形式。
- `scan` aggregator 已完成，會彙整已實作的 report-only checks 並輸出 `maintenance-report-YYYY-MM-DD*.md`。
- `coverage` exclusion polish 已完成。
- public showcase branch 已補：
  - sanitized public `AGENTS.md`
  - English companion `AGENTS_en.md`
  - `tools/sync_public_agents.py`
  - README / README.zh-TW 維護工具說明、架構狀態、靈感來源與 WIP 進度
- `bare-link-fix` subcommand 已完成並執行 `--apply`：353/355 ambiguous bare `[[wikilinks]]` 已轉為 explicit relative links（7 個 index files），2 個 genuinely ambiguous（LingOrm 同 stem 多目錄）保留。功能：reuses `collect_index_lint()` detection, `resolve_bare_link_replacement()` 計算 relative path, `fix_bare_links_in_file()` single-pass regex replacement。Commit `bf2efa9`。
- OCR sanity check 已加入 `fill_threads_stub_pages.py`：`check_ocr_sanity()` 4-check（consecutive repetition >5, line count >500, length ratio >10x, Shannon entropy <2.0）+ `sanitize_page_text()` 包裝。Module constants: `MAX_CONSECUTIVE_REPEATS=5`, `MAX_SECTION_LINES=500`, `LENGTH_RATIO_LIMIT=10`, `MIN_CHAR_ENTROPY=2.0`。
- 33 stub-marker-mismatches 修正於 LingOrm-索引.md。
- 2 broken wikilinks 修正於 專案管理-索引.md。
- 曼谷茶冰淇淋.md OCR garble 修正（16,471→20 lines）。
- 擲杯技巧.md promoted stub→wiki。
- 3 empty pages deleted（147個AI員工, 壺鈴運動, 練肩）。
- 工程師最常用的 12 個 Claude Code 指令.md 建立（merged 2 raw files, status: wiki）。
- 總索引 dashboard 更新：Wiki 359, Reference 28, Stub 95。

目前 `tools/wiki_maintain.py --help` 顯示的 subcommands：

```text
scan
handoff
blocked-report
status-audit
index-lint
review-reconcile
coverage
duplicates
canonical-guard
author-fix
bare-link-fix
pending-match
promote-ready
audit-list
```

### 尚未完成

- `inject-pending --apply`（subcommand 存在但僅 report-only）
- canonical cleanup automation
- delegate integration
- CI/report cleanliness gates
- 完整 README/tool docs for future apply commands

### 下一步建議

建議順序：

1. ~~`author-fix --apply`~~ ✅ 已完成（2026-05-27，commit `822fd3f`）
2. ~~OCR garble prevention~~ ✅ 已完成（2026-05-28，commit `bf2efa9`）
3. ~~Ambiguous bare link bulk fix~~ ✅ 已完成（2026-05-28，commit `bf2efa9`，353/355 fixed）
4. ~~`pending-match`~~ ✅ 已完成（2026-05-28，commit `650e21c`，report-only，tested with 0 pending files）
5. ~~`promote-ready` dry-run/report-only~~ ✅ 已完成（2026-05-28，commit `650e21c`，9 stubs ready）
6. ~~`audit-list`~~ ✅ 已完成（2026-05-28，commit `650e21c`）
7. ~~Claude Code maintenance hook~~ ✅ 已完成（handoff / implementation-plan reminder）
8. 再評估 `inject-pending --dry-run`
9. ~~LingOrm content dedup~~ ✅ 已完成（2026-05-28，commit `650e21c`，deleted LingOrm 系列 duplicate，kept 鄺玲玲系列）
10. ~~BOM frontmatter fix~~ ✅ 已完成（2026-05-28，commit `650e21c`，3 parsers patched + file BOM stripped）
11. ~~`promote-ready --apply`~~ ✅ 已完成（2026-05-28，commit `6ef6b64`，7 stubs promoted，dashboard updated）
12. ~~Playwright auth cookie injection~~ ✅ N/A（2 求職履歷 stubs 來源帖文已刪除，頁面已刪除，commit `82cee22`）

`inject-pending --apply` 應等 inject-pending report-only 層穩定且被人工 review 後再做。

## 0. 任務目標

在 `D:\shane_yeh\Documents\_Claude_Code\knowledge-wiki` 內建立一套 repo-specific wiki 維護工具，讓下列反覆工作可以自動掃描、產報告，並在安全模式下分批修復：

- `wiki-pages/index` 索引混亂、重複索引、舊索引回魂。
- `wiki-pages/AI 工具/其他 AI 工具` 裡與 agent harness / Claude Code / Codex 相關頁面需要搬到更合適的 `AI Agent` 類別。
- `pending-digest-app-output` 依 URL 注入 wiki-pages，且不改 wiki 檔名。
- raw 有 URL 但 wiki-pages 沒有，需列出 ingest candidates。
- 非 LingOrm `status: stub` 且已有完整內文者可直接 promote。
- LingOrm stub 依專案規則保留，不視為錯誤。
- `frontmatter` 的 `網址` 重複時，一組 URL 只能保留一個 canonical page。
- `log.md`、`AI 工具-索引.md`、`LingOrm-索引.md` 等 canonical 檔案不可被舊檔回魂取代。
- bare wikilink 若同名檔同時存在於 `raw/` 與 `wiki-pages/`，必須被視為高風險 ambiguous link。
- 多來源 hub 頁可合法保留，但不一定應保留單一 `網址` frontmatter。
- 空白 stub 或 raw/wiki 皆無正文的頁面，需進入 blocked content gap，而不是被誤 promote 或誤刪。
- 長任務需要可恢復的 handoff 與 batch checkpoint，不依賴 Shane 手動重述上下文。
- 若使用本機 Claude Code CLI 委派執行，Codex/Codex-like supervisor 應保留規劃、驗收與 review。

本階段優先實作「掃描與報告」；只有明確 safe subcommand 才能寫入檔案，且所有寫入命令必須支援 `--dry-run`。

## 1. 必讀規則

Agent 開始實作前必須讀：

- `AGENTS.md`
- `CLAUDE.md`
- `tasks/wiki-maintenance-framework-plan.html`
- 本文件

若本輪要導入委派執行流程，額外讀：

- `D:\shane_yeh\Documents\_Claude_Code\claude-code-delegate\skills\claude-code-delegate\SKILL.md`
- `D:\shane_yeh\Documents\_Claude_Code\claude-code-delegate\README_zh-TW.md`

必須遵守：

- 不修改 `raw/`。
- 不硬編碼絕對路徑。外部 pending digest 路徑必須由 CLI 參數或環境變數提供。
- 不引入非必要第三方套件。第一版只用 Python 標準函式庫。
- 所有 destructive write 都必須有 `--dry-run`，預設 dry-run 或 report-only。
- LingOrm stub 不 promote、不列為錯誤。
- Windows 路徑要用 `pathlib.Path` 處理。
- 若產生 `.toml`，Windows path 要用單引號；本計畫不需要產生 TOML。
- 不執行 `gbrain`，也不要在工具或 skill 流程中加入 `gbrain sync`。
- 若使用 `claude-code-delegate`，Claude 是 executor，不是第二 supervisor；不得把架構、產品、風險判斷丟給 delegate。

## 2. 檔案與目錄

### 2.1 新增

```text
tools/wiki_maintain.py
tasks/wiki-maintenance-agent-implementation-plan.md
tasks/maintenance-reports/.gitkeep
tasks/current-handoff.md
tasks/blocked-content-gaps.md
.ai/.gitkeep
```

### 2.2 可選新增

若 agent 判斷單檔太大，可建立 package，但第一版建議單檔完成：

```text
tools/wiki_maintenance/
├── __init__.py
├── frontmatter.py
├── scanner.py
├── reports.py
└── cli.py
```

若採 package，`tools/wiki_maintain.py` 只做 CLI entrypoint。

### 2.3 不要修改

- 不修改 `raw/`
- 不修改 README
- 第一版不要改 `.obsidian/`
- 第一版不要建立 Obsidian plugin

## 3. CLI 總設計

建立：

```powershell
python tools/wiki_maintain.py <subcommand> [options]
```

共用 options：

```text
--root PATH          repo root，預設 current working directory
--wiki-dir PATH      預設 wiki-pages
--raw-dir PATH       預設 raw
--tasks-dir PATH     預設 tasks
--json               同時輸出 JSON 到 stdout
--report             寫入 markdown report
--date YYYY-MM-DD    報告日期，預設今天
--dry-run            不寫入 wiki，只顯示會做什麼
--verbose            顯示更多資訊
```

第一版 subcommands：

```text
scan
index-lint
duplicates
coverage
pending-match
inject-pending
promote-ready
canonical-guard
audit-list
handoff
blocked-report
review-reconcile
status-audit
```

第一版只要求 `scan`、`index-lint`、`duplicates`、`coverage`、`pending-match`、`promote-ready`、`canonical-guard`、`handoff`、`blocked-report` 完成。  
`inject-pending` 可先做 dry-run + 明確 TODO，除非時間足夠再實作寫入。

## 4. 核心資料模型

在 `tools/wiki_maintain.py` 中使用 `dataclasses`。

### 4.1 PageRecord

```python
@dataclass
class PageRecord:
    path: Path              # absolute path
    rel_path: str           # repo-relative with /
    wiki_rel_path: str      # wiki-pages-relative with /
    stem: str               # filename without .md
    category: str           # first folder under wiki-pages, or "" for root
    is_index: bool
    frontmatter: dict[str, str]
    body: str
    status: str
    url: str
    title: str
```

`url` 解析規則：

- 優先 frontmatter `網址`
- 其次 `url`
- 去除外層引號
- 去除 `[]`
- 去除尾端 `/`
- 空值回傳 `""`

### 4.2 RawRecord

```python
@dataclass
class RawRecord:
    path: Path
    rel_path: str
    frontmatter: dict[str, str]
    body: str
    url: str
    title: str
```

raw URL 解析規則：

- 優先 `url`
- 其次 `網址`
- 同樣 normalize

### 4.3 IndexLink

```python
@dataclass
class IndexLink:
    index_path: Path
    index_rel_path: str
    target: str
    line_no: int
    line_text: str
    has_stub_marker: bool
    is_raw_like: bool
    resolved_paths: list[str]
```

wikilink regex 第一版：

```python
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
```

### 4.4 Issue

```python
@dataclass
class Issue:
    severity: str           # error | warn | info
    code: str               # duplicate-url, raw-index-link, ...
    message: str
    path: str = ""
    line: int | None = None
    details: dict[str, Any] = field(default_factory=dict)
```

### 4.5 BlockedRecord

```python
@dataclass
class BlockedRecord:
    path: str
    title: str
    category: str
    reason: str           # empty-wiki-and-raw | missing-source-body | manual-review
    source_url: str
    raw_match: str
    next_action: str
```

## 5. 基礎函式設計

Agent 必須先實作這些小函式，再做 subcommands。

### 5.1 `normalize_rel_path(path: Path, root: Path) -> str`

回傳 repo-relative path，使用 `/`，即使在 Windows 也不要輸出 `\`。

驗收：

- `wiki-pages\index\總索引.md` 變成 `wiki-pages/index/總索引.md`

### 5.2 `parse_frontmatter(text: str) -> tuple[dict[str, str], str]`

要求：

- 若文字不是 `---` 開頭，回傳 `({}, text)`
- 找第二個 `---`
- 支援簡單 `key: value`
- 不需要完整 YAML parser
- 保留值為字串

驗收範例：

```markdown
---
網址: https://example.com/
作者: [@abc]
tags: []
status: stub
---

## Main Content
```

應解析：

```python
{"網址": "https://example.com/", "作者": "[@abc]", "tags": "[]", "status": "stub"}
```

### 5.3 `normalize_url(value: str) -> str`

要求：

- trim 空白
- 去掉外層 `'` 或 `"`
- `[]`、`[ ]`、空字串回傳 `""`
- 去掉尾端 `/`
- 不改 query string

### 5.4 `load_wiki_pages(root, wiki_dir) -> list[PageRecord]`

要求：

- 掃描 `wiki-pages/**/*.md`
- 排除 `.obsidian`、`tasks`、`raw`
- index 判定：path 中包含 `/index/` 或 `wiki_rel_path` 以 `index/` 開頭
- category：`wiki_rel_path` 第一段；index 檔 category 可為 `index`

### 5.5 `load_raw_records(root, raw_dir) -> list[RawRecord]`

要求：

- 掃描 `raw/**/*.md`
- 只讀，不寫
- 只收有 URL 的 raw record

### 5.6 `extract_index_links(page_records) -> list[IndexLink]`

要求：

- 只掃 index pages
- 解析每個 wikilink
- 跳過 `總索引` 自己與返回導覽時仍可保留，不要當錯誤
- `is_raw_like` 判斷：
  - target 以 `raw/` 或 `raw\` 開頭
  - line_text 含 `raw/` 或 `raw\`
  - markdown link URL 含 raw path
- resolved_paths：
  - 以 stem 對應 wiki page
  - 若多個同 stem，列全部
  - 若同 stem 同時命中 `raw/` 與 `wiki-pages/`，必須能在上層檢查中列為 ambiguous bare wikilink risk

## 6. Subcommand 詳細規格

## 6.1 `scan`

### 功能

一次執行所有檢查，產出人與 agent 都可讀的 markdown report。

### CLI

```powershell
python tools/wiki_maintain.py scan --report
```

### 內部執行

依序呼叫：

1. `check_canonical_guard`
2. `check_duplicate_urls`
3. `check_index_links`
4. `check_status_index_mismatch`
5. `check_non_lingorm_stub_candidates`
6. `check_raw_coverage`
7. `check_pending_digest` only if `--pending-dir` 有提供
8. `check_blocked_content_gaps`
9. `check_hub_pages_without_primary_url`

### Report 路徑

```text
tasks/maintenance-reports/maintenance-report-YYYY-MM-DD.md
```

若資料夾不存在，建立 `tasks/maintenance-reports/`。

### Report 格式

```markdown
# Wiki Maintenance Report - YYYY-MM-DD

## Summary

| Check | Errors | Warnings | Info |
|---|---:|---:|---:|

## Errors

### duplicate-url
- ...

## Warnings

### non-lingorm-stub-ready
- ...

## Info

## Suggested Next Agent Prompt

```text
請依照 tasks/maintenance-reports/maintenance-report-YYYY-MM-DD.md，只處理 Errors。
LingOrm stub 保留。
先提出修復計畫，不要直接大批刪檔。
```
```

### 驗收

```powershell
python tools/wiki_maintain.py scan --report
Test-Path tasks\maintenance-reports
Get-ChildItem tasks\maintenance-reports
```

## 6.2 `canonical-guard`

### 功能

偵測已知 canonical 衝突與舊檔回魂。

### 規則

| canonical | forbidden/restored stale |
|---|---|
| `wiki-pages/log.md` | `wiki-pages/日誌.md` |
| `wiki-pages/index/AI 工具-索引.md` | `wiki-pages/index/AI 工具索引.md` |
| `wiki-pages/index/工具軟體-索引.md` | `wiki-pages/index/工具軟體索引.md` |
| `wiki-pages/index/LingOrm-索引.md` | `wiki-pages/鄺玲玲-索引.md` |
| `wiki-pages/動漫/神聖無碼帝國萬歲！.md` | `wiki-pages/生活雜記/神聖無碼帝國萬歲！-2.md` |

### CLI

```powershell
python tools/wiki_maintain.py canonical-guard
```

### 輸出

若 stale exists：

```text
ERROR canonical-stale-file
canonical: wiki-pages/log.md
stale: wiki-pages/日誌.md
action: merge-then-delete
```

### 驗收

- 目前 repo 若有這些檔案，必須被列出。
- 不可自動刪除。

## 6.3 `duplicates`

### 功能

列出 `wiki-pages/**/*.md` frontmatter `網址/url` 重複的 groups。

### CLI

```powershell
python tools/wiki_maintain.py duplicates --report
```

### canonical 建議排序

Agent 實作 deterministic ranking：

1. `status: reference`
2. `status: wiki`
3. `status: stub`
4. 非 index 優先於 index
5. body 長度較長者
6. path 較短者

注意：這只是建議，report 要寫「suggested canonical」，不可自動刪。

### Report 格式

```markdown
## Duplicate URL Groups

### https://...

Suggested canonical: `wiki-pages/...`

| Status | Path | Body chars | Index refs |
|---|---|---:|---:|

Suggested action:
- Merge useful content into canonical.
- Replace wikilinks to duplicates.
- Delete duplicates after review.
```

### 驗收

目前 repo 的重複 URL 應列出類似：

- `臺北市漢堡.md` / `台北漢堡排名.md` / `台灣美食.md`
- `每天10-20分鐘把核心練起來.md` / `核心運動.md` / `健身動作.md`
- 其他重複 URL groups

## 6.4 `index-lint`

### 功能

檢查 `wiki-pages/index/*.md`：

- raw links
- broken wikilinks
- ambiguous wikilinks
- stub marker 與 page status 不一致
- URL-only 重點欄
- 重點欄長度違規，LingOrm 除外
- page exists but not listed in any category index

### CLI

```powershell
python tools/wiki_maintain.py index-lint --report
```

### LingOrm 例外

- `wiki-pages/index/LingOrm-索引.md` 不檢查重點欄。
- LingOrm stub marker 合法。

### 重點欄檢查

只檢查雙欄表格行：

```markdown
| [[Page]] | summary |
```

違規：

- summary 含 `http://` 或 `https://`
- summary 去除空白後少於 15 字
- summary 超過 50 字

先以 warning 呈現，不要自動改。

### 驗收

```powershell
python tools/wiki_maintain.py index-lint --report
rg -n "raw[\\/]" wiki-pages\index
```

若 `rg` 有 raw links，report 必須列出。

## 6.5 `coverage`

### 功能

比對：

1. `raw/threads` 與 `raw/threads-saved` frontmatter 的 `url`
2. `wiki-pages` frontmatter 的 `網址`

列出 raw 有但 wiki 沒有的 URL。

### CLI

```powershell
python tools/wiki_maintain.py coverage --report
```

### 輸出檔

```text
tasks/maintenance-reports/ingest-candidates-YYYY-MM-DD.md
```

### 分類建議

第一版不用做 LLM 分類，只用 rule-based hints：

| raw path/title contains | suggested category |
|---|---|
| `Claude`, `Codex`, `Agent`, `AI`, `LLM`, `MCP`, `NotebookLM`, `Gemini` | `AI 工具` |
| `履歷`, `面試`, `求職`, `LinkedIn`, `HR` | `求職履歷` |
| `泰國`, `台北`, `美食`, `旅遊`, `奶茶`, `地圖` | `旅遊美食` |
| `運動`, `睡眠`, `皮質醇`, `ADHD`, `健康` | `健康生活` |
| `Ling`, `Orm`, `鄺玲玲`, `泰百` | `LingOrm` |
| otherwise | `生活雜記` |

Report 要清楚標示這只是 heuristic。

### 驗收

- raw-only URLs 被列出。
- wiki 已存在的 URL 不列出。
- raw 無 URL 的檔案列入 skipped。

## 6.5a `status-audit`

### 功能

檢查所有 `wiki-pages/**/*.md` 是否有缺失、未知或專案特殊 `status`。

### 規則

- `wiki` / `reference` / `stub` 為主體系
- `active` / `legacy` 在 `專案管理/` 合法，但不得混入一般 dashboard
- `README.md` 可列入 excluded，不視為內容頁
- 缺 status 的內容頁列為 warning 或 error，供補正

### 驗收

- 能列出 missing status 內容頁
- 能區分 `專案管理` 的 `active/legacy`

## 6.6 `pending-match`

### 功能

比對外部 pending digest markdown 的 frontmatter `url` 與 wiki-pages frontmatter `網址`。

### CLI

```powershell
python tools/wiki_maintain.py pending-match --pending-dir "D:\path\to\pending-digest-app-output" --report
```

注意：

- 不可 hardcode 此路徑。
- 若未提供 `--pending-dir`，顯示錯誤與用法。

### 輸出分類

```markdown
## Pending Digest Match Report

### Matched one wiki page
- pending file -> wiki page

### No wiki match
- pending file | url

### Duplicate wiki match
- pending file | url | wiki pages

### Pending missing url
- pending file
```

### 驗收

用真實 pending dir 跑時，應能匹配如：

```text
1992屬猴2026開運翻身術.md -> wiki-pages/生活雜記/屬猴2026開運儀式.md
```

不可寫入 wiki。

## 6.7 `inject-pending`

### 功能

在 pending-match 成功且只有唯一 wiki match 時，把 pending body 注入 wiki page。

### CLI

```powershell
python tools/wiki_maintain.py inject-pending --pending-dir "D:\path\to\pending" --dry-run
python tools/wiki_maintain.py inject-pending --pending-dir "D:\path\to\pending" --apply
```

### 安全規則

- 預設 dry-run。
- 必須明確 `--apply` 才寫入。
- 不改 wiki 檔名。
- 不修改 raw。
- duplicate wiki match 一律 skip。
- no wiki match 一律 skip。

### 替換規則

若 wiki body 含以下任一 stub block，替換成 pending body：

```text
## Main Content（📌 待消化）
## Main Content

（📌 待消化）
## Main Content
（📌 待消化）
```

若沒有 stub block：

- 若 `--force` 未提供，skip 並報告 `already-has-content`
- 若 `--force` 提供，仍不覆蓋，第一版不要實作 force overwrite

### status 推定

使用既有 `tools/inject_pending_digest.py` 的概念：

若 body 含以下任一特徵，改 `status: wiki`：

- code block ``` 
- 明確步驟：`1. `、`第一步`、`Step 1`
- CLI 指令、設定、API 參數
- `如何`、`怎麼做`、`N 個技巧`
- body 長度 > 300 且包含多段結構

否則保留 `stub`。

LingOrm：

- 即使注入內容，是否 promote 仍依 `CLAUDE.md` 例外。第一版可保留原 status，或在 report 標示「LingOrm skipped status promotion」。

### 驗收

- dry-run 顯示將更新哪些檔案與 status。
- apply 後檔名不變。
- apply 後 `wiki-pages/log.md` 追加一筆簡短 log。

## 6.8 `promote-ready`

### 功能

找出非 LingOrm `status: stub` 但已經有完整內容的頁面，產出可 promote 清單；可選擇 apply。

### CLI

```powershell
python tools/wiki_maintain.py promote-ready --report
python tools/wiki_maintain.py promote-ready --apply --limit 20
```

### ready 判斷

非 LingOrm 頁面符合以下條件之一：

- body 不只 frontmatter，且 body 長度 > 300
- body 不含 `（📌 待消化）`
- body 有 `## 主文`、`## Main Content`、`## Sources`、`## Cross References`
- body 有多段 heading

不 ready：

- body 空
- 只有 URL
- 含待消化 marker
- wiki 與 raw 都無正文時，列入 blocked content gap，不列入 ready

### apply 行為

若 `--apply`：

1. 將 page frontmatter `status: stub` 改為 `status: wiki`
2. 移除所有 index 中該頁的 `（📌 stub）`
3. 不重寫正文
4. 更新 report
5. 追加 `wiki-pages/log.md`
6. 若有 blocked 頁，更新 `tasks/blocked-content-gaps.md`

第一版可以不自動更新 `總索引.md` dashboard，但必須在 report 中列出「dashboard needs update」。若時間足夠，實作 dashboard recompute。

### 驗收

```powershell
python tools/wiki_maintain.py promote-ready --report
python tools/wiki_maintain.py promote-ready --apply --limit 3
rg -n "（📌 stub）" wiki-pages\index | rg -v "LingOrm-索引"
```

## 6.9 `audit-list`

### 功能

列出 `audit/*.md` open items。第一版只需讀取，不需處理。

### CLI

```powershell
python tools/wiki_maintain.py audit-list
```

### 規則

- 若沒有 `audit/`，輸出「no audit directory」
- 若有，列出 severity、target、comment first line

## 6.10 `handoff`

### 功能

把當前維護 session 的可恢復狀態寫成固定 handoff 檔，供下一個 Claude Code / Codex session 直接接手。

### CLI

```powershell
python tools/wiki_maintain.py handoff --task "Task 12 Batch B-2a" --next "Task 12 Batch B-2b"
```

### 輸出檔

```text
tasks/current-handoff.md
```

### 必含欄位

- current state summary
- files touched in this batch
- validations passed
- explicit next step
- explicit do-not-touch list
- dirty-but-out-of-scope paths such as `raw/...`

### 驗收

- 下一個 session 只讀 `tasks/current-handoff.md` 就能知道下一步做什麼

## 6.11 `blocked-report`

### 功能

掃描並更新無法 promote、無法安全刪除、需人工回補內容的 blocked pages。

### 規則

- raw 和 wiki 都空的頁面列入 blocked
- Facebook share 類、短影片類但無正文者可列入 blocked
- blocked 頁面不得混入 promote-ready

### 輸出檔

```text
tasks/blocked-content-gaps.md
```

## 6.12 `review-reconcile`

### 功能

將 review agent / review council findings 分類成：

- cleanup-caused
- known deferred
- pre-existing
- environmental
- dismissed

### 目的

避免 review findings 被直接當成下一批執行清單，造成任務混線。

## 7. Report 渲染函式

實作：

```python
def write_markdown_report(path: Path, title: str, sections: list[ReportSection]) -> None:
    ...
```

可簡化為直接 list of strings，但必須確保：

- UTF-8
- newline `\n`
- 建立 parent dir
- report 內所有 path 使用 `/`

## 8. JSON 輸出

若 `--json`，stdout 輸出：

```json
{
  "ok": false,
  "issue_count": 12,
  "issues": [
    {
      "severity": "error",
      "code": "duplicate-url",
      "message": "...",
      "path": "...",
      "line": null,
      "details": {}
    }
  ],
  "reports": ["tasks/maintenance-reports/...md"]
}
```

不要把 markdown report 混進 JSON stdout。

## 9. 測試與驗證

第一版不要求完整 pytest，但 agent 至少要建立可手動驗證的 sanity commands。

### 必跑命令

```powershell
python tools/wiki_maintain.py --help
python tools/wiki_maintain.py scan --report
python tools/wiki_maintain.py canonical-guard
python tools/wiki_maintain.py duplicates --report
python tools/wiki_maintain.py index-lint --report
python tools/wiki_maintain.py coverage --report
python tools/wiki_maintain.py handoff --task "sanity" --next "none"
python tools/wiki_maintain.py blocked-report
```

### 若有 pending dir

```powershell
python tools/wiki_maintain.py pending-match --pending-dir "D:\shane_yeh\Documents\_Claude_Code\crawl-the-threads\data\pending-digest-app-output" --report
```

### 不應發生

- 不應修改 `raw/`
- 不應在 report-only command 修改 `wiki-pages/`
- 不應要求 Shane 手動寫 Python

驗證：

```powershell
git status --short
```

確認只有預期新增/修改：

- `tools/wiki_maintain.py`
- `tasks/maintenance-reports/*.md`
- 可能的 `tasks/wiki-maintenance-agent-implementation-plan.md`

## 10. 實作任務順序

## Task 1: 建立 CLI skeleton ✅

**Description:** 建立 `tools/wiki_maintain.py`，支援 argparse、共用 options、subcommands stub。

**Acceptance criteria:**
- [x] `python tools/wiki_maintain.py --help` 顯示所有 subcommands
- [x] 每個 subcommand 至少可執行並顯示 not implemented 或空 report
- [x] 無第三方 dependency

**Files touched:**
- `tools/wiki_maintain.py`

**Verification:**

```powershell
python tools/wiki_maintain.py --help
python tools/wiki_maintain.py scan --help
```

## Task 2: 實作 frontmatter 與 page/raw loader ✅

**Description:** 實作 `parse_frontmatter`、`normalize_url`、`load_wiki_pages`、`load_raw_records`。

**Acceptance criteria:**
- [x] 可讀取所有 wiki markdown，不因無 frontmatter crash
- [x] 可讀取 raw markdown，不寫入 raw
- [x] URL normalize 正確

**Verification:**

```powershell
python tools/wiki_maintain.py scan --json
```

## Task 3: 實作 canonical-guard ✅

**Description:** 偵測 stale/canonical conflict。

**Acceptance criteria:**
- [x] 能列出 `日誌.md`、`AI 工具索引.md`、`鄺玲玲-索引.md` 等存在的 stale files
- [x] 不自動刪除

**Verification:**

```powershell
python tools/wiki_maintain.py canonical-guard
```

## Task 4: 實作 duplicate URL scanner ✅

**Description:** 找出 wiki-pages 中 frontmatter `網址/url` 重複 groups。

**Acceptance criteria:**
- [x] report 列出每組 URL、全部頁面、建議 canonical
- [x] path 使用 `/`
- [x] 不修改檔案

**Verification:**

```powershell
python tools/wiki_maintain.py duplicates --report
```

## Task 5: 實作 index-lint ✅

**Description:** 檢查 index raw links、broken links、ambiguous links、stub/status mismatch、重點欄違規。

**Acceptance criteria:**
- [x] LingOrm 例外生效
- [x] broken links 能列 path + line
- [x] stub mismatch 能列 index row 與 page status
- [x] URL-only summary 能列 warning

**Verification:**

```powershell
python tools/wiki_maintain.py index-lint --report
```

## Task 6: 實作 coverage ✅

**Description:** 比對 raw URL 與 wiki URL，列 raw-only ingest candidates。

**Acceptance criteria:**
- [x] raw-only URL list 正確
- [x] skipped no-url raw list 正確
- [x] 有 heuristic category

**Verification:**

```powershell
python tools/wiki_maintain.py coverage --report
```

## Task 7: 實作 pending-match ✅

**Description:** 比對 pending digest URL 與 wiki URL。

**Acceptance criteria:**
- [x] matched one / no match / duplicate match / missing url 分組
- [x] 不寫入 wiki
- [x] pending dir 必須由 CLI 傳入

**Verification:**

```powershell
python tools/wiki_maintain.py pending-match --pending-dir "D:\shane_yeh\Documents\_Claude_Code\crawl-the-threads\data\pending-digest-app-output" --report
```

## Task 8: 實作 promote-ready dry-run ✅

**Description:** 找出已補完整內容、可 promote 的非 LingOrm stubs。

**Acceptance criteria:**
- [x] LingOrm 排除
- [x] ready/not-ready 有理由
- [x] 不寫入

**Verification:**

```powershell
python tools/wiki_maintain.py promote-ready --report
```

## Task 9: 實作 handoff + blocked-report ✅

**Description:** 補上長任務接力能力與 blocked content gap 清單。

**Acceptance criteria:**
- [x] `tasks/current-handoff.md` 可生成
- [x] `tasks/blocked-content-gaps.md` 可列出空白 stub / raw 缺正文頁
- [x] blocked 頁不會被 promote-ready 列為 ready

**Verification:**

```powershell
python tools/wiki_maintain.py handoff --task "demo" --next "demo-next"
python tools/wiki_maintain.py blocked-report
```

## Task 10: 實作 scan aggregator ✅

**Description:** `scan` 一次跑所有 report-only checks。

**Acceptance criteria:**
- [x] 產生總 report
- [x] summary table 有 issue counts
- [x] report 末尾有 Suggested Next Agent Prompt

**Verification:**

```powershell
python tools/wiki_maintain.py scan --report
```

## Task 11: 實作可選寫入命令 ✅ 部分完成（promote-ready --apply 已實作）

**Description:** 若前面都穩定，再實作 `inject-pending --apply` 與 `promote-ready --apply`。

> **已完成的 apply 命令**：`author-fix --apply`（commit `822fd3f`）、`bare-link-fix --apply`（commit `bf2efa9`）、`promote-ready --apply`（commit `6ef6b64`）皆符合以下所有 criteria。
> **尚未實作**：`inject-pending --apply`。

**Acceptance criteria:**
- [x] 預設 dry-run（author-fix、bare-link-fix 已實作）
- [x] 必須明確 `--apply`（同上）
- [x] 寫入前列出檔案（同上）
- [x] 寫入後更新 `wiki-pages/log.md`（promote-ready --apply 已實作）
- [x] 不碰 raw

**Verification:**

```powershell
python tools/wiki_maintain.py promote-ready --apply --limit 1
git diff -- wiki-pages tasks tools
```

## 11. 建議 commit/交付內容

第一個 agent session 建議只做到 Task 1-10，不做 Task 11 寫入命令。

交付時回報：

- 新增/修改檔案
- 已支援的 subcommands
- 每個驗證命令結果
- 最新 report 路徑
- 目前工具偵測到的 top issues
- 哪些功能仍是 dry-run/report-only
- `tasks/current-handoff.md` 路徑
- `tasks/blocked-content-gaps.md` 路徑

## 12. 給 Claude Code 的實作 prompt

```text
你現在在 D:\shane_yeh\Documents\_Claude_Code\knowledge-wiki。

請閱讀：
1. AGENTS.md
2. CLAUDE.md
3. tasks/wiki-maintenance-agent-implementation-plan.md

請依照 implementation plan 實作第一階段 wiki 維護工具。

本輪只做 Task 1-10：
- 建立 tools/wiki_maintain.py
- 支援 scan、canonical-guard、duplicates、index-lint、coverage、pending-match、promote-ready dry-run、handoff、blocked-report
- 產生 tasks/maintenance-reports/*.md
- 不實作任何會修改 wiki-pages 的 apply 寫入，除非只是建立 report
- 不修改 raw/
- LingOrm stub 保留，不列為錯誤
- 不 hardcode pending digest 絕對路徑，必須由 --pending-dir 傳入
- 不執行 gbrain
- 若需要委派執行，可參考 D:\shane_yeh\Documents\_Claude_Code\claude-code-delegate，但 supervisor 仍需自行驗收

完成後請執行：
python tools/wiki_maintain.py --help
python tools/wiki_maintain.py scan --report
python tools/wiki_maintain.py canonical-guard
python tools/wiki_maintain.py duplicates --report
python tools/wiki_maintain.py index-lint --report
python tools/wiki_maintain.py coverage --report
python tools/wiki_maintain.py blocked-report
python tools/wiki_maintain.py handoff --task "phase-1" --next "review report"

若 pending digest 路徑存在，再執行：
python tools/wiki_maintain.py pending-match --pending-dir "D:\shane_yeh\Documents\_Claude_Code\crawl-the-threads\data\pending-digest-app-output" --report

最後回報：
- 改了哪些檔案
- 驗證命令結果
- report 路徑
- 工具掃出的 top issues
- 尚未實作的寫入功能
```

<!-- hook-test -->

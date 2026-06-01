# Knowledge Wiki

Languages: [English](README.md) | [繁體中文](README.zh-TW.md)

一個由 LLM 維護的知識 wiki 腳手架。

這個專案把原始保存資料整理成耐用、可交叉連結的 wiki 頁面。原始 vault 作為私人的第二大腦使用，內容包含筆記、參考資料、專案記憶、AI 工具研究、求職資料、健康筆記、旅遊與美食筆記，以及粉絲向／媒體筆記。這個適合公開展示的版本保留架構與工作流程，但移除私人筆記內容。

## 這個專案展示什麼

- 一套實用的 AI 輔助個人知識庫資訊架構。
- 原始來源資料與整理後 wiki 頁面的清楚分離。
- 將雜亂保存的貼文、參考資料、專案筆記與匯入文件轉成結構化 Markdown 知識的工作流程。
- 索引維護規則、頁面狀態慣例，以及工作流程知識模式。
- 可重複用於 Obsidian、Claude Code、Codex 或其他 LLM 輔助寫作流程的 repository 結構。
- 包含 20 個子命令的維護工具層，可回報 wiki 健康狀態、檢查交叉參照、稽核內容可讀性、執行安全的批次修復。

## Repository 結構

```text
knowledge-wiki/
├── AGENTS.md
├── AGENTS_en.md
├── audit/
│   └── example-reports/             # 每個工具的清理後範例輸出
├── raw/                             # 使用者管理的來源資料，視為唯讀
│   ├── README.md
│   └── examples/                    # 合成的可公開來源範例
├── tasks/
│   └── maintenance-reports/         # 產生本地報告的佔位資料夾
├── tools/                           # Repository 專用維護腳本
│   ├── wiki_maintain.py             # 主 CLI：20 個子命令，掃描／檢查／修復
│   ├── validate-wiki.ps1            # CI gate：解析 scan 輸出，有 error 就失敗
│   ├── gen_content_audit.py         # 一次性內容品質分流工具
│   ├── fill_threads_stub_pages.py   # 從 raw/threads 批次建立 stub 頁面
│   ├── sync_public_agents.py        # 從私人 CLAUDE.md 重新產生公開版 AGENTS.md
│   └── wiki_ocr/                    # 獨立的稽核驅動 OCR 擷取工具
│       ├── _gemini_client.py        # Gemini API 包裝器
│       ├── _image_ocr.py            # 圖片 OCR 管線（僅 Gemini）
│       └── audit_ocr.py             # CLI：讀取稽核報告 → 擷取圖片 → OCR → 套用
└── wiki-pages/                      # 由 LLM 維護的結構化知識頁面
    ├── README.md
    ├── index/                       # 範例索引結構
    ├── example-topic/               # 合成的整理後頁面範例
    └── log.example.md
```

## 核心工作流程

這個 wiki 使用雙層模型：

1. `raw/` 是來源收件匣。這裡的檔案由使用者管理，並視為不可變更的證據。
2. `wiki-pages/` 是整理後的知識層。LLM agent 讀取選定的原始資料，決定保存等級，撰寫結構化頁面，並更新索引。

常見操作：

- **Ingest**：將原始來源轉成 wiki 頁面。
- **Promote**：把輕量書籤或 stub 擴充成完整的 wiki／reference 頁面。
- **Re-ingest**：當原始擷取遺失太多細節時，重新建立頁面。
- **Reorganize**：在保留內部連結的前提下，移動、重新命名、合併或拆分頁面。
- **Query**：根據整理後的 wiki 回答問題，並回報知識缺口。
- **Lint**：檢查壞掉的連結、過期參考、重複 URL、受阻頁面、薄弱摘要，以及不一致的 frontmatter metadata。

---

## 維護工具

這個 repository 包含一個「先報告」維護 CLI，共 20 個子命令：

```powershell
python tools\wiki_maintain.py <subcommand> [options]
```

設計原則：

- `raw/` 是唯讀——沒有工具會寫入。
- 預設只報告。破壞性命令需要明確的 `--apply` 旗標。
- 報告驅動有邊界的清理批次——不要盲目執行 apply。
- LingOrm stub 依策略排除在 promote／error 檢查之外。

### 維護架構狀態

靈感來源：

- [`kfchou/wiki-skills`](https://github.com/kfchou/wiki-skills)
- [`lewislulu/llm-wiki-skill`](https://github.com/lewislulu/llm-wiki-skill)

**已完成（Phase 1–4）：**

- 公開／私人 agent 指令同步：`AGENTS.md` 與 `AGENTS_en.md`
- session handoff 報告產生
- blocked content gap 報告
- status / frontmatter 稽核與作者欄位修復（`author-fix --apply`）
- 索引 lint 與 bare-link 自動修正（`bare-link-fix --apply`）
- 交叉參照 lint：斷鏈 wikilinks、孤兒頁、斷鏈 xref 區塊（`xref-lint`）
- 可讀性 lint：偵測未消化的 wiki 頁面（`readability-lint`）
- tags 稽核：缺欄位／空值、孤立 tag、頻率統計（`tags-lint`）
- review finding reconciliation
- raw-to-wiki coverage 報告
- duplicate URL 偵測
- canonical guard：偵測過期檔案與作者 frontmatter 規則違反
- 一鍵 `scan` aggregator（執行所有檢查）
- pending raw-to-wiki matching（`pending-match`）與 digest injection（`inject-pending --apply`）
- 安全的 promote 流程（`promote-ready --apply`）
- audit inbox 生命週期（`audit-list`、`audit-resolve --apply`）
- CI gate（`tools/validate-wiki.ps1`）——發布前強制 0 errors
- 內容品質分流工具（`tools/gen_content_audit.py`）
- 獨立的稽核驅動 OCR 擷取工具（`tools/wiki_ocr/`）
- `wiki-maintenance` Claude Code skill：引導式批次維護

**尚未完成：**

- canonical cleanup automation
- 多 agent 維護批次的 delegate integration（Phase 4.5）
- Obsidian/Web feedback UI（Phase 5）

---

### 快速開始

```powershell
# 完整掃描——執行所有檢查，寫入 markdown 報告
python tools\wiki_maintain.py scan --report

# CI gate——發現任何 error 時 exit 1
pwsh tools\validate-wiki.ps1

# 為下一個 agent 產生 session handoff
python tools\wiki_maintain.py handoff --task "batch-name" --next "next-step"
```

### 常用指令

```powershell
# 掃描與報告（彙整所有檢查）
python tools\wiki_maintain.py scan --report

# 個別 lint 檢查
python tools\wiki_maintain.py status-audit --report
python tools\wiki_maintain.py index-lint --report
python tools\wiki_maintain.py xref-lint --report
python tools\wiki_maintain.py readability-lint --report
python tools\wiki_maintain.py tags-lint --report
python tools\wiki_maintain.py canonical-guard --report
python tools\wiki_maintain.py coverage --report
python tools\wiki_maintain.py duplicates --report

# Apply 類型命令（需要 --apply 旗標）
python tools\wiki_maintain.py promote-ready --apply --limit 10
python tools\wiki_maintain.py author-fix --apply
python tools\wiki_maintain.py bare-link-fix --apply
python tools\wiki_maintain.py audit-resolve content-audit-2026-05-29.md --apply --summary "Done"

# 營運類
python tools\wiki_maintain.py blocked-report
python tools\wiki_maintain.py audit-list --include-resolved
python tools\wiki_maintain.py handoff --task "batch-name" --next "next-step"
```

---

### 子命令參考

| 子命令 | 類型 | 嚴重度 | 用途 | 輸出 |
|---|---|---|---|---|
| `scan` | report | — | 彙整所有報告型檢查為一份報告 | `audit/maintenance-reports/maintenance-report-YYYY-MM-DD*.md` |
| `status-audit` | report | error | 偵測缺漏／未知 `status`、作者格式違規 | `audit/maintenance-reports/status-audit-YYYY-MM-DD*.md` |
| `index-lint` | report | error/warn | 檢查索引連結、stub marker、摘要品質 | `audit/maintenance-reports/index-lint-YYYY-MM-DD*.md` |
| `xref-lint` | report | warn/info | 斷鏈 wikilinks、孤兒頁、斷鏈 xref 區塊、缺少 xref 區塊 | `audit/maintenance-reports/xref-lint-YYYY-MM-DD*.md` |
| `readability-lint` | report | info | 偵測未消化的 `status: wiki` 頁面（4 種信號） | `audit/maintenance-reports/readability-lint-YYYY-MM-DD*.md` |
| `tags-lint` | report | info | 稽核 `tags:` 欄位：缺漏、空值、孤立 tag；頻率統計 | `audit/maintenance-reports/tags-lint-YYYY-MM-DD*.md` |
| `canonical-guard` | report | error | 偵測過期 canonical 衝突與作者 frontmatter 違規 | `audit/maintenance-reports/canonical-guard-YYYY-MM-DD*.md` |
| `coverage` | report | info | 找出尚未匯入 wiki 的 raw source | `audit/maintenance-reports/ingest-candidates-YYYY-MM-DD*.md` |
| `duplicates` | report | error | 偵測重複的 frontmatter URL，建議 canonical | `audit/maintenance-reports/duplicates-YYYY-MM-DD*.md` |
| `review-reconcile` | report | — | 將 review 發現分類到 reconciliation 類別 | `audit/maintenance-reports/review-reconcile-YYYY-MM-DD*.md` |
| `blocked-report` | write | — | 列出無法自動 promote 的頁面 | `tasks/blocked-content-gaps.md` |
| `handoff` | write | — | 為下一個 agent／session 記錄 session 狀態 | `tasks/current-handoff.md` |
| `audit-list` | report | — | 列出 open audit items；`--include-resolved` 顯示已解決數 | stdout |
| `audit-resolve` | apply | — | 解決 audit item：移到 `audit/resolved/`、附加 resolution | `audit/resolved/*.md` |
| `author-fix` | apply | — | 修正 bare-string `作者` 為 canonical `["@handle"]` 格式 | 就地修改 wiki 檔 |
| `bare-link-fix` | apply | — | 將模糊的 bare `[[wikilinks]]` 轉為明確的 relative links | 就地修改索引檔 |
| `pending-match` | report | — | 比對外部 pending digest URL 與 wiki URL | stdout |
| `inject-pending` | apply | — | 將 pending digest 內容注入匹配的 wiki stub | 就地修改 wiki 檔 |
| `promote-ready` | apply | — | 將有足夠內容的非 LingOrm stub promote 為 `status: wiki` | 就地修改 wiki 檔 |

所有報告型子命令支援 `--report` 寫入帶日期的 markdown 檔案。所有 apply 類型子命令預設為 dry-run，需要 `--apply` 才會寫入。

---

### 工具使用方法與 agent prompt

#### `xref-lint` — 交叉參照 lint

掃描所有非索引 wiki 頁面，偵測斷鏈 `[[wikilinks]]`、孤兒頁（未被任何頁面或索引引用）、`## Cross References` 區塊內的斷鏈。

```powershell
# 主控台輸出
python tools\wiki_maintain.py xref-lint

# 寫入帶日期的報告
python tools\wiki_maintain.py xref-lint --report
# → audit/maintenance-reports/xref-lint-YYYY-MM-DD.md
```

**給 agent 的 prompt（搭配報告使用）：**

```text
請讀 audit/maintenance-reports/xref-lint-YYYY-MM-DD.md，處理所有 xref 問題。

處理方式：
- broken-xref-section：修正 Cross References 區塊的斷鏈 wikilink，改成正確的 relative link。
- broken-wikilink：log.md 歷史斷鏈移除 [[]]，shell code 改 backtick，session-筆記範例改純文字。
- orphan-page：加入適當的索引頁。
- missing-xref-section：為缺少 ## Cross References 的 wiki/reference 頁面補上區塊，至少加 2-3 個相關頁面連結。數量多可分批處理，先處理前 20 個。

修完跑 python tools/wiki_maintain.py xref-lint 和 pwsh tools/validate-wiki.ps1 驗證。
```

範例輸出：[`audit/example-reports/xref-lint-example.md`](audit/example-reports/xref-lint-example.md)

---

#### `readability-lint` — 內容可讀性檢查

偵測 `status: wiki` 頁面中未經適當結構化處理的內容。四種信號類型：

| 信號 | 意義 |
|------|------|
| `single-dump` | 0 個有意義的 heading + 無格式元素（純貼上） |
| `no-headings` | <2 個有意義的 heading + 無格式元素 |
| `social-tone` | emoji 群集或社群媒體短行風格 |
| `no-formatting` | 有 heading 但無 bullet list、code block、table 或 blockquote |

```powershell
# 主控台輸出
python tools\wiki_maintain.py readability-lint

# 寫入帶日期的報告
python tools\wiki_maintain.py readability-lint --report
# → audit/maintenance-reports/readability-lint-YYYY-MM-DD.md

# 包含在完整掃描中
python tools\wiki_maintain.py scan --report
```

**給 agent 的 prompt（搭配報告使用）：**

```text
請讀 audit/maintenance-reports/readability-lint-YYYY-MM-DD.md，對其中的頁面進行批次重整。

處理方式：
- single-dump：只有 ## Main Content 無結構 → 重新組織成至少 2-3 個有意義的 H2，加摘要段
- no-headings：有少量 heading 但不足 → 補齊段落結構
- social-tone：emoji／口語化內文 → 改寫為正式 wiki 語氣，整理成段落
- no-formatting：有標題但全是長段落 → 視內容適情況加 bullet list 或 table

每次處理前先確認：頁面 URL 對應的來源內容是否仍可取得（Threads 帖文可能已刪除）。
若來源已不可得，判斷現有內容是否足以 restructure（字數 > 300 → 可直接整理；否則降回 stub）。

數量多，先處理前 20 個 single-dump，每批完成後跑：
  python tools/wiki_maintain.py readability-lint
確認 issue count 下降後再繼續。
```

範例輸出：[`audit/example-reports/readability-lint-example.md`](audit/example-reports/readability-lint-example.md)

---

#### `tags-lint` — Tags 欄位稽核

稽核所有非索引 wiki 頁面的 `tags:` frontmatter 欄位。三種 issue 類型：

| Issue | 嚴重度 | 意義 |
|-------|--------|------|
| `missing-tags-field` | info | wiki/reference 頁面缺少 `tags:` 欄位 |
| `empty-tags` | info | wiki/reference 頁面的 `tags: []` 為空 |
| `singleton-tag` | info | tag 在整個 wiki 只出現 1 次 |

```powershell
python tools\wiki_maintain.py tags-lint
python tools\wiki_maintain.py tags-lint --report
# → audit/maintenance-reports/tags-lint-YYYY-MM-DD.md
```

**給 agent 的 prompt（搭配報告使用）：**

```text
請讀 audit/maintenance-reports/tags-lint-YYYY-MM-DD.md。

Phase A（低成本）：為 wiki/reference 頁面補上缺少的 tags: 欄位並填入 tags。
- 根據頁面分類 + 標題 + 內容建議 2-4 個相關 tag。
- 優先使用報告中頻率表裡的高頻 tag。
- 格式：tags: [tag1, tag2, tag3]

先處理前 20 個 missing-tags-field issue，每批完成後跑：
  python tools/wiki_maintain.py tags-lint
```

範例輸出：[`audit/example-reports/tags-lint-example.md`](audit/example-reports/tags-lint-example.md)

---

#### `scan` — 完整維護掃描

一次執行所有報告型檢查，產出合併報告。

```powershell
python tools\wiki_maintain.py scan --report
# → audit/maintenance-reports/maintenance-report-YYYY-MM-DD.md

# 搭配外部 pending digest 目錄
python tools\wiki_maintain.py scan --report --pending-dir "D:\path\to\pending-digest"
```

報告包含摘要表、每項檢查詳情，以及建議的下一步 agent prompt。CI gate（`validate-wiki.ps1`）解析 scan 輸出的 `totals:` 行。

範例輸出：[`audit/example-reports/scan-report-example.md`](audit/example-reports/scan-report-example.md)

---

#### `audit-resolve` — Audit inbox 生命週期

解決 open audit items：移到 `audit/resolved/`、改寫 frontmatter、附加 `# Resolution` 區塊。

```powershell
# Dry-run（預設）
python tools\wiki_maintain.py audit-resolve content-audit-2026-05-29.md --summary "Batches 1-7 complete"

# 套用
python tools\wiki_maintain.py audit-resolve content-audit-2026-05-29.md --summary "Batches 1-7 complete" --apply

# 列出（含已解決數）
python tools\wiki_maintain.py audit-list
python tools\wiki_maintain.py audit-list --include-resolved
```

---

### CI gate：`validate-wiki.ps1`

PowerShell 包裝器，執行 `scan` 並在發現任何 error 時 exit non-zero。

```powershell
pwsh tools\validate-wiki.ps1

# 搭配 pending 目錄
pwsh tools\validate-wiki.ps1 -PendingDir "D:\path\to\pending-digest"
```

解析 `totals: errors=N warnings=M info=P` 行。Exit 0 = PASS（無 error），exit 1 = FAIL。

---

### 內容品質分流：`gen_content_audit.py`

一次性工具，掃描 `wiki-pages/` 中 body < 500 字元的 `status: wiki` 或 `reference` 頁面，偵測內容信號（video、GitHub、CTA、外部 URL），並建議分流動作。

```powershell
python tools\gen_content_audit.py
# → audit/content-audit-YYYY-MM-DD.md
```

**信號類型**：`video`、`github`、`cta`、`ext_url`、`tw_url_only`、`raw_gone`、`lingorm`

**建議動作**：`re-ingest`、`ocr-images`、`demote-stub`、`manual-review`

範例輸出：[`audit/example-reports/content-audit-example.md`](audit/example-reports/content-audit-example.md)

---

### Stub 頁面產生器：`fill_threads_stub_pages.py`

從 `raw/threads-saved/` 來源檔案批次建立 stub 頁面。包含從 Threads URL 擷取作者與 OCR sanity check。

```powershell
# Dry-run
python tools\fill_threads_stub_pages.py

# 套用
python tools\fill_threads_stub_pages.py --apply --limit 10
```

---

### OCR 擷取工具：`wiki_ocr/`

讀取內容稽核報告，找出標記需要 OCR 的 wiki 頁面，透過 Playwright 擷取原始 Threads 貼文圖片，再經由 Gemini 進行 OCR，最後附加 `## 圖片文字` 區塊。

```powershell
# Dry-run
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md

# 套用（含限制）
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md --apply --limit 3

# 寫入報告
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md --report
```

需要 `.env` 中的 `GEMINI_API_KEY` 與 Playwright。

---

### 公開版 agent 指令同步

```powershell
# 從私人 CLAUDE.md 重新產生 AGENTS.md + AGENTS_en.md
python tools\sync_public_agents.py --source-ref master

# 檢查同步狀態而不寫入
python tools\sync_public_agents.py --source-ref master --check
```

---

### `wiki-maintenance` skill（Claude Code）

Claude Code 專案 skill（`.claude/commands/wiki-maintenance.md`），自動化完整維護工作流程。

**呼叫方式：**

```text
/wiki-maintenance
```

**運作流程：**

1. 執行 `scan --report`，讀取最新報告。
2. 呈現 P0–P3 triage 表格，詢問要處理哪個優先級。
3. 批次修復：P0 全修 / P1 ≤20 / P2 ≤15 每批。
4. 每批結束後跑 `pwsh tools/validate-wiki.ps1`（CI gate）。
5. 完成後更新 `tasks/current-handoff.md`。

**Triage 優先級：**

| 優先級 | Issue 類型 | 行動 |
|--------|-----------|------|
| **P0** | `status-audit` errors、`canonical-guard` conflicts、`duplicates` errors | 立即全修 |
| **P1** | `index-lint` warnings、`xref-lint` broken links | 本次 session 修復，≤20/批 |
| **P2** | `readability-lint`、`tags-lint`、`xref-lint` orphans/missing-xref | 有時間再批次修，≤15/批 |
| **P3** | `coverage` ingest candidates、`blocked` records | 僅回報，不自動修 |

**給 agent 的 prompt：**

```text
/wiki-maintenance
```

在 triage 後指定優先級：

```text
處理 P0 和 P1。
```

指定特定 issue type：

```text
/wiki-maintenance

triage 後只修 P2 readability-lint single-dump issue，前 15 個，修完跑 validate-wiki.ps1 再停。
```

---

### 目前 frontmatter 限制

`作者` 欄位視為 YAML list 欄位：

```yaml
作者: ["@handle"]
作者: []
```

以下格式無效，未來工具不應重新引入：

```yaml
作者: [@handle]
作者: [handle]
```

透過 `status-audit` 與 `canonical-guard` 顯示。

---

## 範例報告

`audit/example-reports/` 目錄包含每個工具的清理後範例輸出，展示報告格式而不暴露私人 wiki 內容：

| 報告 | 工具 | 展示內容 |
|------|------|----------|
| [`scan-report-example.md`](audit/example-reports/scan-report-example.md) | `scan --report` | 完整彙整維護報告 |
| [`xref-lint-example.md`](audit/example-reports/xref-lint-example.md) | `xref-lint --report` | 斷鏈 wikilinks、孤兒頁、xref 區塊問題 |
| [`readability-lint-example.md`](audit/example-reports/readability-lint-example.md) | `readability-lint --report` | 未消化的 wiki 頁面與信號分類 |
| [`tags-lint-example.md`](audit/example-reports/tags-lint-example.md) | `tags-lint --report` | 缺漏／空值 tags、孤立 tag、頻率統計 |
| [`content-audit-example.md`](audit/example-reports/content-audit-example.md) | `gen_content_audit.py` | 內容品質分流（含信號與動作） |
| [`status-audit-example.md`](audit/example-reports/status-audit-example.md) | `status-audit --report` | 各分類的 frontmatter status 欄位稽核 |
| [`index-lint-example.md`](audit/example-reports/index-lint-example.md) | `index-lint --report` | 索引連結驗證、stub 標記檢查 |
| [`canonical-guard-example.md`](audit/example-reports/canonical-guard-example.md) | `canonical-guard --report` | 過時的 canonical 衝突與解決建議 |
| [`coverage-example.md`](audit/example-reports/coverage-example.md) | `coverage --report` | Raw 與 wiki URL 比對、待 ingest 候選 |
| [`duplicates-example.md`](audit/example-reports/duplicates-example.md) | `duplicates --report` | 重複 wiki 頁面 URL 與 canonical 建議 |
| [`review-reconcile-example.md`](audit/example-reports/review-reconcile-example.md) | `review-reconcile` | 審查發現的規則分類 |
| [`blocked-report-example.md`](audit/example-reports/blocked-report-example.md) | `blocked-report --report` | 無法自動 promote 的頁面及原因 |
| [`handoff-example.md`](audit/example-reports/handoff-example.md) | `handoff` | Agent 接續用的 session 交接狀態 |

## 包含的維護輸出

在私人工作 vault 中，`tasks/` 與 `audit/` 是交接、報告與 audit 生命週期的操作層。公開腳手架只保留佔位目錄；產生的報告會刻意被忽略，避免私人維護狀態外洩到 showcase commit。

## 頁面狀態

每個 wiki 頁面都可以用 frontmatter status 標記：

```yaml
status: stub | wiki | reference
```

- `stub`：尚未完整消化的輕量書籤或佔位頁。
- `wiki`：經過綜合整理的結構化知識頁。
- `reference`：用於技術文件、GitHub repository、API 或詳細 how-to 材料的高保存度頁面。

私人工作 vault 可能會定義分類專用例外或額外狀態。這些私人例外會刻意從公開腳手架中省略。

## 保存等級

匯入工作流程會決定要保留多少來源細節：

- **Level 1：意見或短篇筆記**：摘要並濃縮。
- **Level 2：教學與 how-to 材料**：保留指令、步驟、範例與設定細節。
- **Level 3：工具文件與 GitHub 參考**：幾乎完整保留技術細節，主要重組結構，而不是壓縮內容。

## 索引規則

索引位於 `wiki-pages/index/` 底下，用於導覽、dashboard 與能力地圖。

常見索引類型：

- 整個 wiki 的全域索引。
- 主要知識領域的分類索引。
- 用於跨主題問題的能力索引，例如「哪些工具可以幫我降低 token 使用量？」
- 追蹤有多少頁面屬於 `stub`、`wiki` 或 `reference` 的狀態 dashboard。

索引項目應包含有意義的摘要，而不只是 URL。好的摘要會包含具體方法、工具清單、數字或結論。

當索引項目可能與 `raw/` 底下同名檔案衝突時，較安全的格式是 Markdown 相對連結，而不是 bare wikilink。例如：

```markdown
[Page Title](<../分類/Page Title.md>)
```

## 與 Personal Wiki 的關係

這個 repository 有意與 [`hikaru-yeh/personal-wiki`](https://github.com/hikaru-yeh/personal-wiki) 分開。兩者都是由 LLM 維護的 wiki 系統，但它們保護的知識類型不同，所以需要不同規則。

| 領域 | 這個 Repository：`knowledge-wiki` | Personal Wiki：[`hikaru-yeh/personal-wiki`](https://github.com/hikaru-yeh/personal-wiki) |
|---|---|---|
| 內容類型 | 外部知識集合：保存貼文、工具筆記、AI 工作流程、教學與可重用方法 | 個人事實與歷史：身份、關係、職涯紀錄、面試、課程與生活事件 |
| 敏感度 | 較低；多為公開或可分享來源 | 較高；可能包含 PII、關係、職涯脈絡、薪資筆記與私人紀錄 |
| 維護節奏 | 每當有實用外部資料出現時持續匯入 | 圍繞面試、工作、課程、里程碑與個人變化進行事件驅動更新 |
| 隱私規則 | 輕量；重點是讓公開腳手架不含私人來源資料 | 明確的個人事實與紀錄隱私、清理規則 |
| 主要讀者 | 擁有者，以及可能公開分享的讀者 | 私人版本中只有擁有者 |
| Agent 規則複雜度 | 中等；針對匯入、索引、查詢與維護報告最佳化 | 較高；包含隱私、生命週期 metadata、修正流程與人物／實體消歧 |

合併兩者會造成錯誤的安全取捨。把 personal-wiki 的隱私規則套到這裡，會讓一般知識匯入過度沉重；把這個 repository 較輕量的規則套到 personal wiki，則不夠安全。

比較好的模式是單向橋接：personal wiki 可以引用這個 knowledge wiki 的方法論頁面，但每個 vault 都保留自己的規則、所有權與隱私模型。例如，私人面試準備頁面可以引用 `[[knowledge-wiki::Resume Optimization]]`，而不需要把該方法論頁面複製進 personal vault。

## 為什麼存在

這個 repository 不是一般筆記 dump。它示範如何把 LLM 當作知識維護者：原始材料保持不動，整理後的頁面變得可查詢、可重用，而 wiki 會逐漸把零散個人輸入轉成有組織的工作記憶。

私人版本包含實際筆記。這個公開展示用腳手架的目的，是展示系統設計、資料夾分類法、維護工具與 skill 輔助工作流程，同時不暴露個人資料。

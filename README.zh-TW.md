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
- 輕量的維護工具層。它可在任何 apply 工作流程執行前，回報 wiki 健康狀態、受阻頁面、重複 URL 與匯入覆蓋率。

## Repository 結構

```text
knowledge-wiki/
├── AGENTS.md
├── AGENTS_en.md
├── raw/                             # 使用者管理的來源資料，視為唯讀
│   ├── README.md
│   └── examples/                    # 合成的可公開來源範例
├── tasks/
│   └── maintenance-reports/         # 產生本地報告的佔位資料夾
├── tools/                           # Repository 專用維護腳本
│   ├── sync_public_agents.py        # 從私人 CLAUDE.md 重新產生公開版 AGENTS.md
│   ├── wiki_maintain.py
│   └── wiki_ocr/                    # 獨立的稽核驅動 OCR 擷取工具
│       ├── _gemini_client.py        # Gemini API 包裝器（從 crawl-the-threads 克隆）
│       ├── _image_ocr.py            # 圖片 OCR 管線（僅 Gemini，精簡克隆）
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

## 維護工具

這個 repository 包含一個專用的「先報告」維護 CLI：

```powershell
python tools\wiki_maintain.py <subcommand> [options]
```

目前的經驗規則：

- `raw/` 是唯讀。
- 目前工具主要只用於報告。
- 用報告來決定下一批有邊界的清理工作。
- 不要盲目從工具執行 apply 類型的維護操作。

### 維護架構狀態

這套維護架構的靈感來源包含：

- [`kfchou/wiki-skills`](https://github.com/kfchou/wiki-skills)
- [`lewislulu/llm-wiki-skill`](https://github.com/lewislulu/llm-wiki-skill)

目前實作仍在進行中。這個公開腳手架展示的是 **report-first 維護層**，不是完整自動化的 wiki 改寫器。

已完成：

- 公開／私人 agent 指令同步：`AGENTS.md` 與 `AGENTS_en.md`
- session handoff 報告產生
- blocked content gap 報告
- status / frontmatter 稽核
- index lint
- review finding reconciliation
- raw-to-wiki coverage 報告
- duplicate URL 偵測
- canonical guard：偵測過期檔案與作者 frontmatter 規則違反
- 一鍵 `scan` aggregator
- pending raw-to-wiki matching（`pending-match`）與 digest injection（`inject-pending --apply`）
- promote（`promote-ready --apply`）與作者欄位修復（`author-fix`）的安全 apply 流程
- audit-list generation（`audit-list`）
- CI gate（`tools/validate-wiki.ps1`）：發布前強制 0 errors
- 獨立的稽核驅動 OCR 擷取工具（`tools/wiki_ocr/`）

尚未完成：

- canonical cleanup automation
- 多 agent 維護批次的 delegate integration

### 常用指令

```powershell
python tools\wiki_maintain.py status-audit --report
python tools\wiki_maintain.py canonical-guard --report
python tools\wiki_maintain.py index-lint --report
python tools\wiki_maintain.py coverage --report
python tools\wiki_maintain.py duplicates --report
python tools\wiki_maintain.py blocked-report
python tools\wiki_maintain.py handoff --task "batch-name" --next "next-step"
```

### 公開版 agent 指令同步

公開分支將 `AGENTS.md` 保留為私人工作 vault 中 `CLAUDE.md` 的清理版，並用 `AGENTS_en.md` 作為英文伴隨版本。在私人分支修改 `CLAUDE.md` 後，請從公開分支重新產生兩個公開指令檔：

```powershell
python tools\sync_public_agents.py --source-ref master
```

若只想檢查 `AGENTS.md` 或 `AGENTS_en.md` 是否不同步，而不寫入檔案：

```powershell
python tools\sync_public_agents.py --source-ref master --check
```

同步腳本會移除私人分類／專案專用規則，並保留相對路徑以方便公開展示。如果 `AGENTS.md` 有變更，`AGENTS_en.md` 必須在同一個 commit 中更新。

### Subcommand 參考

| Subcommand | 主要用途 | 是否寫入報告／檔案 | 輸出路徑 | 是否修改 `wiki-pages/` |
|---|---|---|---|---|
| `handoff` | 為下一個 agent／session 記錄目前 session 狀態 | 是 | `tasks/current-handoff.md` | 否 |
| `blocked-report` | 列出尚不應 promote 的受阻頁面 | 是 | `tasks/blocked-content-gaps.md` | 否 |
| `status-audit` | 稽核 `status` frontmatter 與 frontmatter schema 問題 | 搭配 `--report` 時可選擇寫入 | `tasks/maintenance-reports/status-audit-YYYY-MM-DD*.md` | 否 |
| `index-lint` | 檢查索引連結、模糊 bare links、缺失目標，以及 stub marker 不一致 | 搭配 `--report` 時可選擇寫入 | `tasks/maintenance-reports/index-lint-YYYY-MM-DD*.md` | 否 |
| `review-reconcile` | 將 review 發現分類為 cleanup-caused／deferred／pre-existing／environmental／dismissed | 是 | `tasks/maintenance-reports/review-reconcile-YYYY-MM-DD*.md` | 否 |
| `coverage` | 找出尚未匯入 wiki 的 raw source pages | 搭配 `--report` 時可選擇寫入 | `tasks/maintenance-reports/ingest-candidates-YYYY-MM-DD*.md` | 否 |
| `duplicates` | 偵測重複的 frontmatter URL，並建議 canonical | 搭配 `--report` 時可選擇寫入 | `tasks/maintenance-reports/duplicates-YYYY-MM-DD*.md` | 否 |
| `canonical-guard` | 偵測過期的 canonical 衝突與 frontmatter 作者規則違反 | 搭配 `--report` 時可選擇寫入 | `tasks/maintenance-reports/canonical-guard-YYYY-MM-DD*.md` | 否 |

### OCR 擷取工具

`tools/wiki_ocr/` 底下的獨立 CLI，可讀取內容稽核報告，找出標記需要 OCR 的 wiki 頁面，透過 Playwright 擷取原始 Threads 貼文圖片，再經由 Gemini 進行 OCR，最後將 `## 圖片文字` 區塊附加到 wiki 頁面。

```powershell
# 乾跑模式：列出目標，不呼叫 API 也不寫入
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md
python tools\wiki_ocr\audit_ocr.py tasks\content-quality-audit.md

# 套用模式：擷取圖片、OCR、寫入 wiki 頁面
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md --apply --limit 3

# 將輸出寫入 tasks/maintenance-reports/ocr-YYYY-MM-DD.md
python tools\wiki_ocr\audit_ocr.py audit\content-audit-2026-05-29.md --report
```

這個工具支援兩種稽核報告格式（舊版自由文字與標準化 `ocr-images` token）。需要 `.env` 中的 `GEMINI_API_KEY` 以及 Playwright 來擷取瀏覽器中的圖片。`--report` 旗標會將輸出寫入 `tasks/maintenance-reports/ocr-YYYY-MM-DD[-N].md`，採用與 `wiki_maintain.py` subcommand 相同的命名慣例。核心元件（`_gemini_client.py`、`_image_ocr.py`）是從 `crawl-the-threads` 管線精簡克隆而來，只保留 Gemini OCR 路徑。

### 目前 frontmatter 限制

維護工具將 frontmatter 規則視為硬性限制。特別是，`作者` 欄位會被視為 YAML list 欄位：

```yaml
作者: ["@handle"]
作者: []
```

以下格式無效，未來工具不應重新引入：

```yaml
作者: [@handle]
作者: [handle]
```

這條規則會透過 `status-audit` 與 `canonical-guard` 顯示。未來的 normalize／rewrite 流程應保留有效的 list 語法。

## 包含的維護輸出

在私人工作 vault 中，`tasks/` 是交接、受阻頁面報告、promote inventory 與帶日期掃描輸出的操作層。公開腳手架只保留 `tasks/maintenance-reports/.gitkeep`；產生的報告會刻意被忽略，避免私人維護狀態外洩到 showcase commit。

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

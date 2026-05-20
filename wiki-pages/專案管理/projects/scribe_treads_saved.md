---
type: project
status: active
last_updated: 2026-05-18
time: 2026-05
tech_stack:
  - JavaScript
  - Tampermonkey
  - Python
  - Gemini CLI
  - Claude CLI
  - OpenAI Responses API
  - File System Access API
depends_on: []
feeds_into:
  - scribe.json
  - scribe-ai.json
  - Threads Saved cleanup
location: "D:\\shane_yeh\\Documents\\_Claude_Code\\PROJECT_scribe_treads_saved"
---

# scribe_treads_saved

Threads `Saved posts` 匯出與清理工具鏈。核心是 Tampermonkey userscript：在 Threads 收藏頁抓取已載入貼文，輸出 `scribe.json`；再由本機 AI 分類器產生 `scribe-ai.json`，回到瀏覽器中標亮、勾選並半自動取消儲存 AI 相關貼文。

## 専案任務

Shane 在 Threads 收藏了大量貼文，需要先把收藏內容匯出成可保存的本機資料，再逐步清掉已整理或不再需要的 AI 相關收藏。手動整理會卡在三件事：Threads 收藏頁是虛擬列表、DOM 會改版與重建、取消儲存操作有誤刪風險。

因此此專案採「本機瀏覽器抓取 + 本機 AI 後處理 + 人工複核 + 半自動取消儲存」路線：不把資料送到外部爬蟲服務、不在 userscript 內直接呼叫模型，也不做全自動刪除。

## Briefing（原始需求）

最初需求是做一個可安裝到 Tampermonkey 的 userscript，在 Threads 網頁版 `Saved posts` 頁面抓取目前已載入的收藏貼文，支援截止日期、最大抓取筆數、自動捲動、去重，以及下載 `CSV` / `JSON`。

後續需求演變為 AI cleanup workflow：
- 用 userscript 產生或覆寫 `scribe.json`
- 用本機 Python 分類器把貼文判斷為 `ai` / `not_ai` / `unsure`
- 輸出 `scribe-ai.json`
- userscript 載入分類結果，在 Threads 頁面標亮 AI 貼文
- 高信心 AI 預設勾選，中低信心與 `unsure` 只標示
- 使用者人工修正選取後，再執行「取消儲存已選取」

## 成品描述

目前成品包含三層：

1. `threads-saved-export.user.js`：Tampermonkey userscript 主程式，提供浮動面板、抓取、匯出、自動存檔、AI 結果載入、標亮、選取、半自動 unsave 與 debug log。
2. `scripts/classify_ai_posts.py` + `scripts/ai_classifier_backends.py`：本機 AI 分類器，讀取 `scribe.json`，分批呼叫 `gemini-cli`、`claude-cli` 或 OpenAI Responses API，輸出 `scribe-ai.json`。
3. `scripts/watch_debug_log.py`：監看 `threads-unsave-debug.ndjson`，把最近事件組成 systematic-debugging prompt，可選擇呼叫 Codex CLI 產生除錯回覆。

目前主流程已具備實用形態，但仍處在 active debugging：多輪修正已寫入 userscript，尚未完成最新版在 Threads `Saved posts` 頁面的實機 smoke test。

## 技術與架構

使用技術：JavaScript userscript、Tampermonkey、Browser DOM API、File System Access API、IndexedDB file handles、Python、Gemini CLI、Claude CLI、OpenAI Responses API、unittest、Codex CLI

```text
Threads Saved posts page
    ↓ Tampermonkey userscript
scribe.json
    ↓ Python classifier
scribe-ai.json
    ↓ userscript loads AI result
Threads page highlights + selected keys
    ↓ human review
semi-automated unsave
    ↓ debug events
threads-unsave-debug.ndjson
    ↓ watch_debug_log.py
systematic-debugging prompt / Codex response
```

userscript 內部主要模組：
- `DateUtils`：截止日期、貼文時間解析與 old-only 停止條件
- `Parser`：從 Threads DOM 解析 `postId`、URL、作者、正文與時間
- `Scroller`：自動捲動、pending load、bottom nudge 與可見貼文簽名
- `ExportUtils` / `AutoSaveUtils`：CSV / JSON 匯出與 File System Access API 自動覆寫
- `AiReviewUtils`：AI 結果索引、confidence tier、標亮、選取、suppressed keys、unsave 狀態與指定貼文診斷
- `DebugLogUtils`：寫入 `threads-unsave-debug.ndjson`
- `UI`：浮動控制面板與操作入口

## 可複用的元件

- `threads-saved-export.user.js` / `Parser`：面向不穩定社群網站 DOM 的保守解析器，可複用於 Threads 類頁面抓取。
- `threads-saved-export.user.js` / `Scroller`：虛擬列表自動捲動策略，包含 scroll container 重解析、post-scroll progress 判斷、bottom nudge、可見簽名診斷。
- `threads-saved-export.user.js` / `AiReviewUtils`：AI 分類結果回灌瀏覽器 DOM、confidence tier 標亮、人工複核後再執行批次操作的模式。
- `scripts/ai_classifier_backends.py`：本機 LLM backend adapter，處理 Gemini CLI / Claude CLI / OpenAI Responses API 的命令解析、JSON 抽取與輸出正規化。
- `scripts/classify_ai_posts.py`：批次分類 orchestration，支援 retry、partial failure fallback、summary 與衍生 JSON 輸出。
- `scripts/watch_debug_log.py`：NDJSON debug log → systematic-debugging prompt 的 watcher，可複用於其他 browser automation 除錯。

## 學到什麼 / 踩過的坑

- Threads `Saved posts` 是虛擬列表，scroll metrics 短暫不變不等於到底；抓取 loop 必須在實際捲動後再判斷 progress，並重新解析 scroll container。
- Threads DOM 會重建與位移；unsave 每處理一篇前要用 key 重新 resolve 當前 visible DOM，不能沿用上一輪 article reference。
- More button 不一定在 `<article>` 內，可能在 parent / sibling scope；需要 parent scope fallback，甚至用 spatial fallback 依文章 rect 匹配全頁可見按鈕。
- `scribe-ai.json` 與實際收藏頁會漂移；本輪沒看見的 selected key 不能永久寫入 `suppressedAiKeys`，否則會污染後續高亮與全選狀態。
- `ai_order_exhausted` 不能當停止條件，因為 AI 清單順序與 Threads 虛擬列表順序不保證單調；只能作為診斷訊號。
- Windows CLI integration 容易踩 command parsing：`shlex.split()` 要用 Windows 模式保留 `C:\...`，Gemini `.cmd` 需用 `shutil.which()` resolve，Codex CLI 不應直接執行 WindowsApps 版本。
- Gemini / Claude / OpenAI 回傳不一定是乾淨裸 JSON；分類器要支援 code fence、包裝 JSON 與缺漏 item 的保守 fallback。
- 取消儲存是破壞性操作，專案刻意保留人工複核與高信心預選，而不是讓模型直接決定刪除。

## 遺留問題 / 未完成

- 最新版 `threads-saved-export.user.js` 尚未在 Threads `Saved posts` 頁面完成實機 smoke test。
- 原始抓取新 loop 尚未驗證是否完全解掉「中途停住，需要手動再按開始」。
- `unsave_menu_still_open` 根因尚未完全確認：3000ms timeout 是否足夠，以及 `triggerElementClick(unsaveItem)` 是否穩定觸發 Threads React handler。
- `outcome: verified` 可能受 DOM recycling 影響，仍需重整後確認貼文是否真的消失。
- `全選全部標亮`、`診斷指定貼文`、spatial more fallback、`ai_order_boundary_no_selected` 都需要實機驗證。
- 工作樹目前仍有未 commit 變更，包含 userscript、README、Python classifier 與測試檔。

## Cross References

- [[專案管理/_overview]]：跨專案總覽
- [[專案管理/projects/threads_saved_v2]]：另一條 Threads 書籤知識捕捉管線，輸出到 Notion

---
type: project
status: active
last_updated: 2026-05-13
time: 2025-02
tech_stack:
  - Python
  - Playwright
  - Notion API
  - Google Gemini
  - SocialCrawl
  - python-dotenv
depends_on: []
feeds_into:
  - Notion (知識頁面)
---

# threads_saved_v2

從 Threads 書籤清單（`threads_saved.txt`）逐筆抓取貼文內容，用 Gemini 生成中文標題與分類，寫入 Notion 頁面。

## 専案任務

Shane 在 Threads 大量收藏 AI 工具類貼文，但手動整理進 Notion 耗時且容易遺漏。需要一個自動化工具把書籤批次抓取並存成結構化知識頁面，供日後查閱。

## Briefing（原始需求）

給一份 Threads 書籤 URL 清單（`threads_saved.txt`），自動抓取每篇貼文的作者主文與留言，用 Gemini 生成中文標題與分類標籤，建立對應的 Notion 頁面，避免重複新增。

## 成品描述

Python CLI 工具（`app.py`），讀取 `threads_saved.txt` 逐行處理：
- SocialCrawl API 抓取 thread root context
- Playwright 補抓作者主文與留言（作為正文主體）
- Gemini API 生成中文標題 + 分類（rules 優先，Gemini fallback）
- Notion API 查重後建立頁面（標題、URL 嵌入卡片、主文、留言）

模組化重構完成，主流程穩定可用。

## 技術與架構

使用技術：Python、Playwright、Notion API、Google Gemini、SocialCrawl、python-dotenv

```
threads_saved.txt（書籤 URL 清單）
    ↓ app.py
    ├── SocialCrawl API → thread root context
    ├── Playwright → 作者主文 + 作者留言（正文主體）
    ├── Gemini API → 中文標題 + 分類（rules first, Gemini fallback）
    └── Notion Writer（URL 查重 → 建頁面）
```

## 可複用的元件

- `domain/author_content_extractor.py`：從 Threads 頁面文字抽出作者主文與留言，可複用於其他 Threads 相關工具
- `domain/notion_content_builder.py`：組裝 Notion page input（網址嵌入卡片、主文、留言），Notion 頁面建構邏輯可複用
- `services/category_classifier.py`：rules 優先 + Gemini fallback 的混合分類器，分類規則與 AI 補判斷的架構模式可複用
- `services/title_generator.py`：Gemini 標題生成，含單一標題限制與清洗邏輯
- `services/notion_writer.py`：Notion 寫入 + URL 查重，可複用於任何 Notion 寫入場景

## 學到什麼 / 踩過的坑

- SocialCrawl `threads/post` 抓到的是 thread root context（最高層），不一定是 URL handle 本人的貼文 → 正文以 Playwright 抽到的作者內容為準，不能完全依賴 SocialCrawl
- Gemini 有時回傳多個標題建議（即使 prompt 說「只要一個」）→ 需在 prompt 加嚴格限制 + 標題清洗邏輯（取第一個）
- 重跑整份清單沒有查重保護時會重複建立 Notion 頁面 → 必須在寫入前查重（已實作 URL 查重）
- 中文字串在 PowerShell / 內嵌 Python 環境下可能被 cp950 編碼污染

## 遺留問題 / 未完成

- Claude Code 類貼文的子分類細化（目前統一歸 `Claude Code`，不區分 skill / hook / config 等）
- 考慮將 Claude Code 貼文改寫入 Obsidian wiki 而非 Notion
- 大量清單（100+ 筆）的批次分段與可中斷恢復策略
- 清理舊版截圖產物（`screenshots/`）

## Cross References

- [[專案管理/_overview]]：跨專案總覽

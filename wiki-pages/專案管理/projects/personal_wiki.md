---
type: project
status: active
last_updated: 2026-05-13
time: 2024-11
tech_stack:
  - Claude Code
  - Gemini CLI
  - Markdown
  - Obsidian wikilinks
  - YAML frontmatter
depends_on:
  - data_preprocess
feeds_into: []
location: "D:\\_Claude_Code\\personal-wiki"
---

# personal_wiki（personal-wiki）

以 Claude Code 為維護引擎的個人知識庫。將多平台來源資料（Gmail、LINE、IG、FB、Threads、職涯文件、課程）整理成結構化 Wiki 頁面。

## 専案任務

個人資料散落在多個平台（社群、通訊、職涯、課程），沒有統一的知識存取介面。需要一個長期、可查詢的個人記憶庫，讓 AI 助手能協助存取並更新個人知識脈絡。

## Briefing（原始需求）

建立一個 LLM-driven 個人 wiki：Claude Code 負責讀取 `Raw_Sources/` 的多平台匯出資料，整理成 `Wiki_Pages/` 的結構化 wiki 頁面，支援 ingest / query / lint 三種操作模式，含隱私治理層（v2 方向）。

## 成品描述

96+ 頁 wiki，Claude Code 為維護引擎：
- `Raw_Sources/`（user 管理，唯讀）→ `Wiki_Pages/`（LLM 管理）
- 分類：career、cc_projects、courses、people、self、social
- `log.md`：append-only 操作日誌（context compaction 後的 ground truth）
- `index.md`：主索引
- 隱私治理層：`privacy_sanitize_rules.md`、`lifecycle_rules.md`（v2）

## 技術與架構

使用技術：Claude Code、Gemini CLI、Markdown、Obsidian wikilinks、YAML frontmatter

```
Raw_Sources/（唯讀，user 管理）
    ↓ ingest / query / lint
Wiki_Pages/（LLM 管理）
    ├── index.md
    ├── log.md（append-only 操作日誌）
    ├── career/
    ├── cc_projects/
    ├── courses/
    ├── people/
    ├── self/
    └── social/
```

操作模式：
- **ingest**：Raw_Sources → Wiki_Pages（需 sanitize check 與使用者核准）
- **query**：搜尋 Wiki_Pages 回答問題（private/sensitive 頁需過 privacy gate）
- **lint**：健康檢查（孤兒頁、失效連結、stale 判定、metadata 缺漏）

## 學到什麼 / 踩過的坑

- context compaction 後，`log.md` 比 transcript 更適合當作進度還原 ground truth → log 要即時寫、要具體
- 多 agent 同時執行可能遇到 API rate limit → 分批執行或加 delay
- 只改規則文件不夠，`CLAUDE.md` 與 `AGENTS.md` 需保持一致 → 改動規則時同步更新兩個檔案

## 遺留問題 / 未完成

- 部分 social brain 頁面的身份/關係描述待更新
- lifecycle metadata 標準化持續補充中
- 定期 lint pass 尚未自動化

## Cross References

- [[專案管理/projects/personal_wiki_v2]]：治理升級方向
- [[專案管理/projects/data_preprocess]]：上游資料管線
- [[專案管理/_overview]]：跨專案總覽

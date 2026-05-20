---
status: wiki
last_updated: 2026-05-18
---

# 跨專案總覽

`_Claude_Code/` 下所有專案的狀態快照。每次有專案狀態變動時更新。

## 狀態表格

| 專案 | 狀態 | 類型 | Tech Stack | 依賴 | 輸出到 | 備註 |
|------|------|------|------------|------|--------|------|
| data_pipeline | legacy | 資料管線 | Python, AnythingLLM, MarkItDown | — | AnythingLLM, Raw_Sources | 被 data_preprocess 取代主線 |
| data_preprocess | active | 資料管線 | Python, Tkinter, pytest | — | Raw_Sources (personal_wiki) | GUI-driven，約 90% 完成度 |
| threads_saved_v2 | active | 爬蟲/知識捕捉 | Python, Playwright, Notion API, Gemini | — | Notion | 模組化完成，分類細化待做 |
| scribe_treads_saved | active | Threads 收藏清理 | JavaScript, Tampermonkey, Python, Gemini CLI | — | scribe.json, scribe-ai.json | 匯出收藏、AI 標亮與半自動 unsave，待實機 smoke test |
| personal_wiki | active | 個人知識庫 | Claude Code, Gemini CLI, Markdown | data_preprocess | — | personal-wiki |
| personal_wiki_v2 | active | 知識庫治理升級 | Claude Code, YAML frontmatter | personal_wiki | — | 持續進行中的治理升級方向 |
| assignment_pipeline | active | 文件處理 | Python, Gemini CLI, Google Docs API | — | Google Docs | PDF → Gemini → Google Doc |
| knowledge_wiki | active | 知識庫 | Claude Code, Gemini CLI, Markdown | — | — | 本 wiki（D:\knowledge-wiki） |

## 專案相依圖

```
original_input/
    ↓ data_preprocess (active, 主線)
    ↓ data_pipeline (legacy, 背景服務)
Raw_Sources/ → personal_wiki (ingest)
                ↑ personal_wiki_v2（治理升級）

Threads saved list → threads_saved_v2 → Notion
Threads Saved posts → scribe_treads_saved → scribe.json / scribe-ai.json → cleanup

PDF → assignment_pipeline → Google Docs
```

## 架構決策（ADR）

| ADR | 決策摘要 |
|-----|---------|
| [[專案管理/adr/adr_crossproject_kb_location\|KB 選址]] | knowledge-wiki（無隱私閘、技術定位吻合） |
| [[專案管理/adr/adr_two_layer_architecture\|雙層架構]] | knowledge-wiki 深度 + PROJECTS.md 平面 AI context |
| [[專案管理/adr/adr_bridge_page_pattern\|橋接頁模式]] | cc_projects 縮為職涯敘事 + canonical 指標 |
| [[專案管理/adr/adr_rules_extraction\|規則抽離]] | 専案管理-rules.md 獨立，@引用 |
| [[專案管理/adr/adr_bridge_creation_via_update\|橋接頁建立]] | update 模式 + 自動讀 canonical |

## 注意事項

- `data_pipeline` 進入 legacy 模式（主資料流已由 `data_preprocess` 取代）
- `personal_wiki_v2` 不是獨立程式，是 `personal_wiki` 的治理升級方向
- `knowledge_wiki` 即本 wiki，自我記錄

## Cross References

- [[專案管理-索引]]：各專案詳細頁面

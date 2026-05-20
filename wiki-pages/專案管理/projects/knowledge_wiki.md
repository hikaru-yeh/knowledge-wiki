---
type: project
status: active
last_updated: 2026-05-13
time: 2025-04
tech_stack:
  - Claude Code
  - Gemini CLI
  - Markdown
  - Obsidian
  - YAML frontmatter
depends_on: []
feeds_into: []
location: "D:\\_Claude_Code\\knowledge-wiki"
---

# knowledge_wiki（本 wiki）

以 Claude Code 為維護引擎的技術與工具知識庫。涵蓋 AI 工具、工具軟體、求職履歷、旅遊美食、健康生活、LingOrm 等分類，以及本跨專案管理知識庫。

## 専案任務

與 personal_wiki（個人生活記憶庫）的職責分離：knowledge_wiki 存放沒有隱私顧慮的技術/工具/知識內容，可被 AI 助手自由查詢，不需過 privacy gate。同時作為跨專案管理知識庫（`專案管理/`）的容器，讓任意 `_Claude_Code/` 子專案的 AI session 都能查詢到跨專案知識。

## Briefing（原始需求）

建立技術知識庫，整合 Threads 書籤、課程筆記、AI 工具研究的知識沉澱。後續增加「專案管理」分類，存放跨專案狀態快照、ADR、patterns、踩坑記錄，並透過 `PROJECTS.md`（根目錄）讓任意子專案的 AI session 都能看到跨專案地圖。

## 成品描述

122+ 頁 wiki，Claude Code 為維護引擎：
- 集中式索引（`wiki-pages/index/`）
- `日誌.md`：操作記錄
- `PROJECTS.md`（`_Claude_Code/` 根目錄）：AI-readable 跨專案地圖（≤200 行），透過 CLAUDE.md 繼承機制讓所有子專案可見

| 分類 | 頁數 | 說明 |
|------|------|------|
| AI 工具 | 33 | Claude Code、Codex、Gemini CLI 等 |
| 工具軟體 | 8 | 各類軟體工具筆記 |
| 求職履歷 | 9 | 履歷、求職、面試 |
| 旅遊美食 | 6 | 旅遊與美食紀錄 |
| 健康生活 | 7 | 健康習慣與生活方式 |
| LingOrm | 47 | LingOrm 相關知識 |
| 專案管理 | 12+ | 跨專案知識庫（本區段） |

## 技術與架構

使用技術：Claude Code、Gemini CLI、Markdown、Obsidian、YAML frontmatter

```
raw/（唯讀，user 管理）
    ↓ ingest
wiki-pages/（LLM 管理）
    ├── 日誌.md（操作紀錄）
    ├── index/（集中式索引）
    │   ├── 總索引.md
    │   └── *-索引.md
    └── <分類>/
        └── *.md
```

與 `_Claude_Code/CLAUDE.md` 整合：根目錄 `@PROJECTS.md` 讓任意子專案的 AI session 都能看到跨專案地圖。

## 學到什麼 / 踩過的坑

- knowledge_wiki 和 personal_wiki 職責分離很重要：混合隱私與非隱私內容會讓 query 變複雜，privacy gate 也更難設計
- 集中式索引（`index/`）比分散式索引（每個分類各自維護）更容易維護全域統計
- 跨專案知識應放在無隱私閘的 wiki，不應放在 personal-wiki（有 private/sensitive 管控）

## 遺留問題 / 未完成

- 部分早期頁面未補 YAML frontmatter（lifecycle metadata 標準化待補）
- `PROJECTS.md` 需隨專案更新手動同步
- 跨 wiki（knowledge_wiki ↔ personal_wiki）的查詢路由設計尚未系統化

## Cross References

- [[總索引]]：知識庫總索引
- [[專案管理/_overview]]：跨專案總覽
- [[專案管理/projects/personal_wiki]]：姊妹個人知識庫

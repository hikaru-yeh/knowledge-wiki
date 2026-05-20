---
type: adr
status: active
last_updated: 2026-05-14
---

# ADR：橋接頁透過 update 模式建立（非 ingest）

## 背景

project-wrap skill 的輸出路徑已從 `personal-wiki/Raw_Sources/cc_projects/` 改為 `knowledge-wiki/raw/cc_projects/`。personal-wiki 的 `Raw_Sources/cc_projects/` 不再有新的來源稿。需要決定如何在 personal-wiki 建立新的橋接頁。

## 考慮過的替代方案

### ingest 模式（從 Raw_Sources）

- Pros：符合 personal-wiki 既有 ingest 流程
- Cons：Raw_Sources 已無專案來源稿（project-wrap 輸出到 knowledge-wiki）；要讓 ingest 生效需手動複製內容到 Raw_Sources
- 拒絕原因：來源已不在 Raw_Sources，走 ingest 流程不合理

### project-wrap 雙輸出

- Pros：一次產出兩個 wiki 的來源稿
- Cons：project-wrap 需要知道兩個 wiki 的存在，增加耦合；橋接頁內容（職涯敘事）與 project-wrap 收集的技術資訊性質不同
- 拒絕原因：橋接頁需要人工判斷職涯價值，自動產出品質不穩定

### update 模式（採用）

- Pros：CLAUDE.md 已定義 update 模式「來源不是 Raw_Sources 時使用」，完全吻合；agent 可自動讀 knowledge-wiki canonical 頁面
- Cons：需在 CLAUDE.md 加入觸發詞與自動讀取路徑

## 決策

橋接頁使用 personal-wiki 的 **update 模式**建立：
1. Agent 自動讀取 `knowledge-wiki/wiki-pages/專案管理/projects/<name>.md`（canonical 頁面）
2. 套用 `Wiki_Pages/cc_projects/_bridge_template.md`
3. 撰寫 `## 職涯價值` 段落
4. 更新 `project_index.md`

在 CLAUDE.md 和 AGENTS.md 的 update 模式下加入 `#### 橋接頁快捷建立` 子段落，定義觸發詞（「新增 project_X 橋接頁」「建 X 橋接頁」）和自動讀取路徑，使用者不需手動提供內容。

同步更新 `course_project_ingest_rules.md` 的 Project Ingest Rules 段落，標記舊規則停用。

## 後果

- 好：不改 project-wrap skill，不增加兩個 wiki 之間的耦合
- 好：使用者只需說「建 X 橋接頁」，agent 自動完成
- 好：update 模式語意正確——橋接頁來源確實不是 Raw_Sources
- 壞：橋接頁建立仍需人工觸發（但這是設計意圖——需判斷職涯價值）

## 目前狀態

active

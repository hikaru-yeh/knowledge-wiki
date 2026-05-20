---
type: adr
status: active
last_updated: 2026-05-14
---

# ADR：橋接頁模式（cc_projects 職涯敘事 + canonical 指標）

## 背景

跨專案知識庫遷入 knowledge-wiki 後，personal-wiki 的 `Wiki_Pages/cc_projects/` 原有 6 個完整專案頁面面臨定位衝突：技術內容已在 knowledge-wiki，但 cc_projects 頁面仍有職涯 portfolio 敘事價值。

## 考慮過的替代方案

### 完全遷移（刪除 cc_projects）

- Pros：乾淨，無重複
- Cons：失去職涯 portfolio 視角；career_history、skills_profile 等頁面的 wikilink 全部斷裂
- 拒絕原因：cc_projects 的職涯敘事是 personal-wiki 的核心內容之一

### 雙寫（兩邊都維護完整頁）

- Pros：兩邊都完整
- Cons：維護成本翻倍；內容不同步風險高；cc_projects 頁面仍受 privacy gate 限制
- 拒絕原因：違反 single source of truth 原則

### 橋接頁（採用）

- Pros：cc_projects 保留職涯價值，技術細節單一來源在 knowledge-wiki；wikilink 不斷裂
- Cons：查技術內容需跳轉到 knowledge-wiki

## 決策

將 `Wiki_Pages/cc_projects/` 所有頁面縮減為橋接頁：
- frontmatter 加 `type: project-bridge` 和 `canonical:` 指向 knowledge-wiki
- 正文只保留 `## 職涯價值` 段落
- 技術內容全部移除，替換為 canonical 頁面指標

建立 `_bridge_template.md` 供未來新增橋接頁使用。

## 後果

- 好：single source of truth 在 knowledge-wiki，消除重複維護
- 好：職涯 portfolio 敘事完整保留，cross references 不斷裂
- 好：cc_projects 頁面大幅精簡，privacy review 負擔降低
- 壞：需更新 `course_project_ingest_rules.md` 的 Project Ingest Rules 段落
- 壞：不是所有 knowledge-wiki 專案都需要橋接頁（需人工判斷職涯價值）

## 目前狀態

active

---
type: adr
status: active
last_updated: 2026-05-14
---

# ADR：専案管理規則抽離為獨立檔案

## 背景

knowledge-wiki 的 `CLAUDE.md` 和 `AGENTS.md` 需要加入專案管理操作規則（頁面格式、ingest 流程、索引同步等）。這些規則內容量大（模板 + 流程 + 索引規則 ≈ 160 行），直接嵌入會讓 CLAUDE.md 膨脹。

personal-wiki 已有先例：`privacy_sanitize_rules.md` 和 `lifecycle_rules.md` 都是從 `AGENTS.md` 抽離的獨立規則檔。

## 考慮過的替代方案

### 嵌入 CLAUDE.md

- Pros：一個檔案看完所有規則
- Cons：CLAUDE.md 已經很長；專案管理規則只適用於 `専案管理/` 子區段，混入主體會降低可讀性
- 拒絕原因：personal-wiki 的教訓——AGENTS.md 承載全部規則時「臃腫、脆弱」

### 放在 wiki-pages/専案管理/ 內

- Pros：靠近使用位置
- Cons：wiki-pages 是 LLM 管理的知識頁面區，規則檔不屬於知識頁面
- 拒絕原因：規則檔與知識頁面混在一起會導致 ingest/lint 邏輯混淆

## 決策

建立 `専案管理-rules.md` 放在 knowledge-wiki 根目錄，與 CLAUDE.md / AGENTS.md 同層。在 CLAUDE.md 和 AGENTS.md 中用 `@専案管理-rules.md` 引用。

內容包含：事實來源、全域忽略、頁面格式（7 段模板）、ADR/Pattern/Error 格式、操作模式、draft-first 規則、merge 規則、索引同步規則、ingest 保留度例外。

## 後果

- 好：CLAUDE.md 保持精簡，專案管理規則獨立維護
- 好：與 personal-wiki 的 `privacy_sanitize_rules.md` 模式一致
- 好：修改專案管理規則不需動 CLAUDE.md 主體
- 壞：新增一個需要記住的檔案（但 `@` 引用機制讓 agent 自動載入）

## 目前狀態

active

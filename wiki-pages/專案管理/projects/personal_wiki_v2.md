---
type: project
status: active
last_updated: 2026-05-13
time: 2025-04
tech_stack:
  - Claude Code
  - Gemini CLI
  - YAML frontmatter
  - Markdown
depends_on:
  - personal_wiki
feeds_into: []
---

# personal_wiki_v2（知識庫治理升級）

這不是獨立的程式專案，而是 `personal_wiki` 的持續治理升級方向。將 wiki 從簡單的 ingest/query/lint 系統，演進為具備隱私控制、lifecycle metadata、關係圖譜的治理型知識庫。

## 専案任務

`AGENTS.md` 承載所有 wiki 規則（臃腫、脆弱）；沒有標準化的 metadata 框架；人物識別與隱私治理未分開設計。需要將治理規則系統化，拆分成多個專用文件，各司其職，讓單一規則修改不影響整體。

## Briefing（原始需求）

將 wiki 治理升級：
- 隱私規則抽離 AGENTS.md → `privacy_sanitize_rules.md`
- lifecycle metadata 標準化（confidence、status、stale、superseded、archive）
- YAML frontmatter 規格化（sensitivity、pii_categories、review_required）
- 人物消歧流程正式化（保守策略）

## 成品描述

治理文件集合（非可執行程式）：
- `privacy_sanitize_rules.md`：隱私分級、sanitize 流程、query 隱私閘
- `lifecycle_rules.md`：confidence、decay_profile、last_confirmed、stale、superseded、archive 語意
- YAML frontmatter 標準（含 sensitivity、pii_categories、review_required）
- `people/disambiguation_queue.md`：人物消歧候選清單

v2-lite 治理層已完成。

## 技術與架構

使用技術：Claude Code、YAML frontmatter（非程式架構，為治理規則文件）

治理規則演進方向：
```
AGENTS.md（單一大檔，原始狀態）
    ↓ 拆分
privacy_sanitize_rules.md（隱私治理）
lifecycle_rules.md（頁面生命週期）
course_project_ingest_rules.md（特定 ingest 規則）
AGENTS.md（剩餘協調規則，精簡後）
```

關鍵設計決策：
- 治理規則拆成多個專用檔，不塞在 AGENTS.md
- Privacy sanitize 為一等公民行為（not optional）
- 人物消歧採保守策略：證據不足時寧可分離，不早合併
- 面試準備與一般 query 的隱私策略必須區分

## 學到什麼 / 踩過的坑

- sanitize 規則若寫太硬，會破壞知識價值（太鬆也有隱私風險）→ 需在「保護 PII」與「保留知識價值」之間平衡，不能二元化
- 人物圖譜與隱私治理不能分開設計 → `disambiguation_queue` 與 `privacy_sanitize_rules` 必須互參
- `AGENTS.md` 不應承載全部治理規則（一個檔案難以維護）→ 拆出專用規則文件，AGENTS.md 只保留協調邏輯

## 遺留問題 / 未完成

- 在 Wiki_Pages 中落實 Markdown 關係圖（Cross References 區段充實）
- 建立人物消歧正式流程（目前 queue 存在但流程半手動）
- 建立 JSONL graph / audit.jsonl
- 設計並落實自動化 hooks（lint trigger 等）
- 設計 weekly lint 排程
- 設計 crystallization（高價值 query 結果 → 結晶化知識頁）

## Cross References

- [[專案管理/projects/personal_wiki]]：基礎 wiki 專案
- [[專案管理/_overview]]：跨專案總覽

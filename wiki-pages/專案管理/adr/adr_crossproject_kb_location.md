---
type: adr
status: active
last_updated: 2026-05-14
---

# ADR：跨專案知識庫選址 knowledge-wiki

## 背景

Shane 在 `_Claude_Code/` 下有 15+ 個活躍 CC 專案，需要建立統一的跨專案知識層。候選位置兩個：`knowledge-wiki` 和 `personal-wiki`。

兩者定位不同：
- knowledge-wiki：技術/工具/AI 能力知識庫，無隱私閘
- personal-wiki：個人生活/社交/職涯敘事，有 privacy_sanitize_rules 管控

## 考慮過的替代方案

### personal-wiki

- Pros：已有 `cc_projects/` 6 頁，與職涯 portfolio 整合
- Cons：query 需過 privacy gate；`cc_projects/` 頁面標記 private/sensitive，不適合 AI 自由查詢；架構分散
- 拒絕原因：跨專案知識庫應可被 AI 助手快速查詢，不應被 private 標籤阻擋

### 獨立新 wiki

- Pros：乾淨起點
- Cons：多一個 vault 增加維護成本；knowledge-wiki 已有相關基礎設施（能力索引、集中式 index）
- 拒絕原因：不必要的複雜度

## 決策

選擇 knowledge-wiki，在 `wiki-pages/專案管理/` 建立跨專案知識庫子區段。

理由：
- 技術定位吻合
- 無隱私閘阻擋 AI 查詢
- 已有集中式 index 與 status dashboard
- `raw/cc_projects/` 原始材料已在此

## 後果

- 好：AI 助手在任何子專案 session 中都能查詢跨專案知識，無隱私閘延遲
- 好：利用 knowledge-wiki 既有索引架構，不需從零建立
- 壞：personal-wiki 的 `cc_projects/` 需改為橋接頁（見 ADR：橋接頁模式）
- 壞：兩個 wiki 之間的專案知識需手動保持一致

## 目前狀態

active

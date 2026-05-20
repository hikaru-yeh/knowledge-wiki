---
type: adr
status: active
last_updated: 2026-05-14
---

# ADR：雙層架構（深度知識庫 + 平面 AI context 層）

## 背景

跨專案知識庫選定 knowledge-wiki 後，需要決定 AI 助手如何在各子專案 session 中取得跨專案 context。knowledge-wiki 的完整頁面太深（需要逐頁查詢），但完全壓縮又會丟失細節。

## 考慮過的替代方案

### 單層深度（只有 knowledge-wiki）

- Pros：一個地方維護，內容完整
- Cons：AI 助手需要先查 knowledge-wiki index 再讀個別頁面，context 注入慢；非 knowledge-wiki session 無法自動看到跨專案資訊
- 拒絕原因：不利用 CLAUDE.md 繼承機制的話，跨專案 context 無法被動注入

### 單層平面（只有 PROJECTS.md）

- Pros：簡單，一個檔案搞定
- Cons：200 行上限放不下架構細節、踩坑、ADR；只能當目錄不能當知識庫
- 拒絕原因：缺乏深度查詢能力

## 決策

雙層架構：

1. **Layer 1 — knowledge-wiki 詳細知識庫**：`wiki-pages/專案管理/`，含 projects / adr / patterns / errors，深度查詢用
2. **Layer 2 — 根目錄 PROJECTS.md**：`_Claude_Code/PROJECTS.md`，≤200 行平面檔，透過根目錄 `CLAUDE.md` 的 `@PROJECTS.md` 自動注入所有子專案 session

利用 Claude Code 的 CLAUDE.md 繼承機制：根目錄指引自動套用到所有子專案。

## 後果

- 好：任何子專案的 AI session 自動看到跨專案地圖（被動注入，零操作）
- 好：需要深度查詢時可指向 knowledge-wiki 完整頁
- 壞：PROJECTS.md 需隨專案更新手動同步（索引同步規則已定義在 `専案管理-rules.md`）
- 壞：兩層之間可能資訊不同步

## 目前狀態

active

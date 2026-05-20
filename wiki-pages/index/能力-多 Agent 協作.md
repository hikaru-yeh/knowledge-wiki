---
status: wiki
---

# 能力-多 Agent 協作

← [[總索引]]

> 整理 Claude Code、Codex、Gemini 等多 Agent 分工、交接、審碼與自動循環相關頁面，方便依成熟度挑選協作策略。

## 推薦組合

**情境 A**：[[工作流與配置]] → [[Claude 高手用法設定即執行]] → [[AI 多模型協作審碼抓漏]]
**情境 B**：[[Claude Code 自動開發15訣]] + [[drift_ai]] + [[ralph-loop]]
**情境 C**：[[MCP 工具]] + [[kinggyusuh-gemini-search-cc]] + [[提示詞技巧]]
**情境 D**：[[obra-superpowers]] + [[agent-skills]] + [[everything-claude-code 冠軍配置]]

## 新手入門

| 頁面 | 適用場景 | 搭配建議 |
|------|----------|----------|
| [[工作流與配置]] | 先理解 Agent 權限模式、完成定義與自動化觸發 | 作為所有協作流程的底座，再接 [[Claude 高手用法設定即執行]] |
| [[Claude 高手用法設定即執行]] | 想快速掌握 Skills / Subagents / Hooks 如何分工 | 讀完可直接接 [[AI 多模型協作審碼抓漏]] 看角色分派 |
| [[AI 多模型協作審碼抓漏]] | 想了解 Claude / Codex / Gemini 的典型分工方式 | 可與 [[提示詞技巧]] 一起看共識審碼做法 |

## 進階配置

| 頁面 | 適用場景 | 搭配建議 |
|------|----------|----------|
| [[everything-claude-code 冠軍配置]] | 想參考完整多 Agent 配置包與並行分工設計 | 適合對照自己的 harness 缺哪些模組 |
| [[Claude Code 自動開發15訣]] | 想導入 `/loop`、Hooks、Git Worktrees 等並行機制 | 可延伸到 [[ralph-loop]] 的自動循環實作 |
| [[MCP 工具]] | 想補齊多 Agent 共用的文件、GitHub、瀏覽器與排程工具層 | 配 [[kinggyusuh-gemini-search-cc]] 擴充搜尋與 audit 能力 |

## 進階技巧

| 頁面 | 適用場景 | 搭配建議 |
|------|----------|----------|
| [[drift_ai]] | 常在 Claude Code、Codex、Cursor 等 agent 間切換任務 | 適合作為跨 Agent handoff 與脈絡保存層 |
| [[Claude Code 脆文實作50招]] | 想快速掃描多 Agent、工具整合與 workflow 技巧清單 | 可作為主題導航，再回跳各專頁深挖 |
| [[提示詞技巧]] | 想用多模型共識、分角色提示詞提升審碼與分析穩定度 | 與 [[AI 多模型協作審碼抓漏]] 搭配最完整 |

## 參考實作

| 頁面 | 適用場景 | 搭配建議 |
|------|----------|----------|
| [[ralph-loop]] | 想實作 Stop Hook 驅動的 while-true 自動循環 Agent | 與 [[Claude Code 自動開發15訣]] 的 loop 概念互補 |
| [[agent-skills]] | 想建立跨 IDE、跨 Agent 都能重用的能力模板 | 適合抽出與單一工具無關的角色能力 |
| [[obra-superpowers]] | 想參考成熟 Skill 框架與多階段協作方法論 | 可和 [[agent-skills]] 對照結構層次 |
| [[kinggyusuh-gemini-search-cc]] | 想把 Gemini 搜尋 / 審計能力併入 Claude Code 協作鏈 | 適合補上即時搜尋與 package audit 守門員 |

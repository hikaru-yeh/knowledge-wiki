---
status: wiki
---

# 能力-Agent 優化

← [[總索引]]

> 整理 Claude Code / Codex 的 harness、配置、工作流與多 Agent 協作頁面，方便依成熟度挑選可直接套用的做法。

## 推薦組合

**情境 A**：[[工作流與配置]] → [[CLAUDE.md 與記憶設定]] → [[MCP 工具]]
**情境 B**：[[Skill 設計]] + [[Token 優化]] + [[Claude Code 自動開發15訣]]
**情境 C**：[[planning-with-files]] + [[obra-superpowers]] + [[agent-skills]]
**情境 D**：[[drift_ai]] + [AI 多模型協作審碼抓漏](<../AI 工具/AI Agent/AI 多模型協作審碼抓漏.md>) + [[kinggyusuh-gemini-search-cc]]

## 新手入門

| 頁面 | 適用場景 | 搭配建議 |
|------|----------|----------|
| [[工作流與配置]] | 先建立 Claude Code 的權限模式、完成定義與排程觀念 | 讀完接 [[CLAUDE.md 與記憶設定]] 固化專案規則 |
| [[Claude 高手用法設定即執行]] | 想快速掌握 CLAUDE.md / Skills / Subagents / Hooks 四大槓桿 | 適合作為進入 [[Skill 設計]] 前的總覽 |
| [[CLAUDE.md 與記憶設定]] | 要避免跨專案記憶污染，建立穩定上下文與長期記憶 | 與 [[MCP 工具]] 一起看，補齊 Obsidian / RAG 流程 |
| [[MCP 工具]] | 想先把文件、瀏覽器、GitHub、排程等外部能力接進 harness | 後續接 [[kinggyusuh-gemini-search-cc]] 看進一步擴充 |

## 進階配置

| 頁面 | 適用場景 | 搭配建議 |
|------|----------|----------|
| [[Skill 設計]] | 要把重複任務封裝成可重用 Skill，並加入驗證機制 | 可和 [[obra-superpowers]]、[[agent-skills]] 對照結構 |
| [[Token 優化]] | 想壓低長任務成本，減少記憶、搜尋與工具濫用 | 配 [[CLAUDE.md 與記憶設定]] 一起調整 context 策略 |
| [[Claude Code 自動開發15訣]] | 要導入 `/loop`、Hooks、Git Worktrees、背景排程等自動化配置 | 可直接延伸到 [[ralph-loop]] 的循環執行模式 |
| [[everything-claude-code 冠軍配置]] | 想參考已驗證的完整配置包，快速對照自己缺哪些模組 | 最適合搭配 [[工作流與配置]] 做差距盤點 |

## 進階技巧

| 頁面 | 適用場景 | 搭配建議 |
|------|----------|----------|
| [[Claude Code 脆文實作50招]] | 要一次收斂 Skill、Token、工具整合與 workflow 實戰 tips | 可當總表，再回跳到各主題深挖 |
| [[Claude 蒸餾 Skill-Set 大禮包]] | 想把他人的流程、角色或專長快速蒸餾成可重用 Skill | 與 [[Skill 設計]] 搭配，補驗證與結構化 |
| [AI 多模型協作審碼抓漏](<../AI 工具/AI Agent/AI 多模型協作審碼抓漏.md>) | 想讓 Claude / Codex / Gemini 分工審碼與實作 | 可加上 [[drift_ai]] 管理 agent 間 handoff |
| [[drift_ai]] | 常在 Claude Code、Codex、Cursor 等 agent 之間切換任務 | 適合作為跨工具工作流的脈絡保存層 |

## 參考實作

| 頁面 | 適用場景 | 搭配建議 |
|------|----------|----------|
| [[planning-with-files]] | 想採用 `/plan`、`/start`、`/status` 檔案式 workflow | 適合當你自己的專案執行骨架 |
| [[obra-superpowers]] | 想直接參考成熟的 Claude Code Skill 框架與方法論 | 與 [[agent-skills]] 對照，補齊通用與專案化技能 |
| [[agent-skills]] | 想建立跨 IDE 可搬移的 agent / skill 套件 | 適合拿來抽象出與工具無關的能力層 |
| [[ralph-loop]] | 想實作 Stop Hook 驅動的無限循環 Agent | 可和 [[Claude Code 自動開發15訣]] 的 loop / hooks 觀念一起看 |
| [[kinggyusuh-gemini-search-cc]] | 想替 Claude Code 補上即時搜尋、audit guard 與 slash 指令 | 可與 [[MCP 工具]] 一起規劃外部搜尋與驗證層 |

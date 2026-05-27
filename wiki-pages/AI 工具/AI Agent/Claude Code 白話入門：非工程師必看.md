---
網址: https://www.threads.com/@denniswei1310/post/DYgDTdRmWFj
作者: ["@denniswei1310"]
tags: [Claude Code, 入門, 非工程師, 白話]
status: wiki
---

## 摘要

作者整合 120+ 篇文章、30+ 篇論文（含 Anthropic 工程師 Boris、Thariq 的社群觀點），製作了 50 張 ELI5 投影片，用「公司員工」「廚房品管員」「銀行金庫」等比喻，把 Claude Code 最佳實踐白話化給非工程師。

## 五個白話重點

### 1. CLAUDE.md = 員工手冊

就像新員工第一天要讀的工作守則，CLAUDE.md 告訴 Claude Code：這個專案的規矩、禁忌、你應該怎麼工作。

### 2. Subagents = 分工合作的員工

Claude Code 可以把任務拆給多個子 Agent 同時執行，就像一個 PM 指揮多個分工的同事，而不是一個人做所有事。

### 3. Hooks = 品管員

在你讓 Claude Code 做事的前後，自動執行檢查（例如：改完程式碼後自動跑測試，確認沒壞掉）。就像廚房的品管員在出菜前自動抽檢。

### 4. MCP = 外掛工具箱

讓 Claude Code 連接外部工具（瀏覽器 / 資料庫 / GitHub），就像給員工增加新的技能包，讓他能做更多種類的任務。

### 5. Context Window = 短期記憶

Claude Code 每次對話的「工作記憶」有限，就像銀行金庫的進出通道有大小限制，超過就要重新載入。

## 資源

- **Google 簡報（50 張）**：[Claude Code 最佳實踐 v2](https://docs.google.com/presentation/d/1mnjmwNZKsl1afDW2ia_QjWbJ9t45-FNC/edit)
- **參考 GitHub**：`github.com/zeuik…`（完整最佳實踐整理）

## Sources

- [denniswei1310 Threads](https://www.threads.com/@denniswei1310/post/DYgDTdRmWFj) | 作者: Dennis Wei

## Cross References

- [[CLAUDE.md 與記憶設定]]：CLAUDE.md 完整設定指南
- [[Token 優化]]：Context Window 管理技巧
- [[工作流與配置]]：Hooks、MCP 實作細節

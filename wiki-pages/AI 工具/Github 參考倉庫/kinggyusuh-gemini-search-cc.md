---
網址: https://github.com/KingGyuSuh/gemini-search-cc
作者: []
status: reference
---

# Gemini Search for Claude Code

**gemini-search-cc** 是一個 Claude Code Plugin，讓 Claude Code 直接使用 Gemini 的 Google Search 即時搜尋能力，彌補 Claude 的知識截止日期限制。

**7 個 Slash 指令：**

| 指令 | 用途 |
|------|------|
| `/gemini:search <query>` | 快速 Google 搜尋 + 引用來源 |
| `/gemini:research <topic>` | 深度多步驟研究，交叉參照來源 |
| `/gemini:audit <package>` | 資安 & 依賴審計（CVE、棄用、破壞性變更）|
| `/gemini:fact-check` | 事實查核 |
| `/gemini:changelog` | 查詢函式庫變更記錄 |
| `/gemini:compare` | 比較技術選項 |
| `/gemini:setup` | 設置引導 |

**Auto-audit Guard Hook：**  
自動在安裝新套件時觸發 audit 檢查。

## Cross References

- [[MCP 工具]]: MCP 工具整合
- [[指令與整合]]: Gemini 與 NotebookLM 整合


---
網址: https://www.threads.com/@0xspeter/post/DYWV0qXE-SD
作者: ["@0xspeter"]
tags: [Claude Code]
status: wiki
---

## Main Content

最近看到一個很適合 AI coding 重度使用者的開源專案：
agentmemory
它不是一般的 AI 筆記工具。
而是一套給 AI 寫程式 Agent 使用的長期記憶系統。
簡單說：
你的 coding agent 不用每次開新 session，
都重新認識你的專案、架構、偏好、bug、技術選擇。
它會記得。
這件事表面上看起來是記憶功能。
但真正重要的是：
AI 寫程式開始從「單次對話」
進入「長期協作」。

現在很多 AI coding 工具最大問題不是不夠聰明。
而是太健忘。
每次重開對話，
你都要重新解釋：
專案架構
技術棧
資料夾位置
之前修過的 bug
為什麼不用某個套件
測試怎麼跑
你的 coding style
一個人類工程師如果每天失憶，
你不會覺得他是同事。
你會覺得他是災難。

agentmemory 想解決的就是這件事。
它會在背景記錄 AI agent 做過什麼，
把 session 裡的操作、工具使用、決策、錯誤修正，壓縮成可搜尋的記憶。
下一次你再開新的任務，
AI 不用從零開始。
它可以知道：
你之前怎麼做 auth
哪個檔案放 middleware
測試在哪裡
你為什麼選 jose 而不是 jsonwebtoken
上次修過什麼坑
這才比較像真正的工程協作。

它最有意思的地方是：
記憶不是綁在單一工具裡。
agentmemory 可以透過 MCP 或 REST API，
讓不同 AI coding 工具共用同一個 memory server。
Claude Code
Cursor
Gemini CLI
Codex CLI

這類工具真正改變的，
可能不是 AI 寫程式速度變快。
而是 AI 開始有「專案脈絡」。
以前 AI 像臨時外包。
每次來都要重新交接。
有了長期記憶之後，
AI 更像一個慢慢熟悉你系統的工程夥伴。
未來 coding agent 的差距，
不只會來自模型能力。
也會來自它能不能記住你的世界。

agentmemory 值得看的地方是：
它把 AI coding 的核心問題，
從「怎麼讓模型更會寫」
推到「怎麼讓 Agent 更懂專案」。
這很重要。
因為真正能進入工作流的 AI，
不是每次都表現得很厲害。
而是它能持續累積脈絡、減少重複解釋、降低交接成本，
最後變成一個越用越懂你的系統。
AI coding 的下一步，
不是更會回答。
而是更會記得。

## Sources

- [讓 AI coding 記得你的專案](https://www.threads.com/@0xspeter/post/DYWV0qXE-SD) | 作者: 0xspeter

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

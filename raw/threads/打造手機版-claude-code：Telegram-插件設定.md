---
url: "https://www.threads.com/@jungchun_/post/DXSNGB-H79T"
author: "@jungchun_"
clip_type: "Claude Code"
---

# 把 claude code 改造成 openclaw
身為 cli-base ai tool 早期使用者（跟重度依賴者），其實之前看到龍蝦在風行沒啥感覺，覺得就是串上聊天軟體(而非terminal)，使用者友好才會這麼火爆。
直到工作需要才測試了一下，發現可以隨時在手機上密他是一個蠻特別的感覺！
走在路上、上廁所也心心念念工作(?)
雖然說 claude code official plugin 原生支持 telegram，安裝起來也很簡單
但實際跑起來其實不算開箱即用。分享一下 setup 過程

先去 BotFather 開 bot 拿 token。已經會拿 token 的可以跳過這段
在 claude session 裡：
> /telegram:configure <token>
然後 DM 你的 bot 任意訊息 → 會給你 6 碼 pairing code → 回 session 跑：
> /telegram:access pair <code>
之後把 access policy 從 pairing 改成僅限自己(allowlist)
> /telegram:access policy allowlist

關鍵在啟動 claude 要帶兩個 flag：
> claude --channels plugin:telegram@claude-plugins-official --dangerously-load-development-channels plugin:telegram@claude-plugins-official
第一個叫 plugin 進來、第二個跳過 Anthropic 的 channel allowlist（telegram plugin 還沒上 production allowlist）
進去 claude 之後 `/mcp` 看狀態, 確定 telegram server 活著
之後就能在 telegram 上跟 claude code 對話了！
之後有空再寫 `/loop`： heartbeat - 讓他自己甦醒整理 todo、檢查未完成任務

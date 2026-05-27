---
網址: https://www.threads.com/@weilingkang3/post/DYRj6-jE8iX
作者: ["@weilingkang3"]
tags: [Claude Code]
status: wiki
---

## Main Content

<康勞德日記> remoteControlAtStartup — Claude Code 桌面 app 一個低調但實用的設定。
開了之後每次新 session 啟動，桌機自動變成「可被遠端接管」的後端，CLI 或瀏覽器（claude.com/code）都能連進來。
#康勞德日記 #ClaudeCode #AIThreads #多端整合

設定方式很簡單，~/.claude/settings.json 加一行：
"remoteControlAtStartup": true
下次開新 session 就會看到 banner：「Remote control is active. Code in CLI or at claude.com/code」。
這行訊息不只是裝飾 — 它在告訴你「現在這台桌機是開放可連入的」。
claude.ai
Claude Code

我目前的用法是：在桌機開好一個跑 long-running task 的 session，比如統計 pipeline 或抓資料的 script。
人離開後，手機開瀏覽器到 claude.com/code 就能接著看進度、追問、改 prompt。
等於把 desktop app 變成一個永遠開著的後端，不用 SSH 也不用另外架伺服器。

要注意一件事：banner 不是花俏的 UI 提示。它在提醒你 session 是公開可被連入的，在共享電腦或公司網路要想清楚 trade-off。
我自己覺得目前還可以接受，所以保留 true。如果不常多端切換，預設關掉（false）也不會少什麼，要用再手動 /remote-control on 就好。

## 圖片文字

### 圖片 1

桌機當遠端後端
remoteControlAtStartup 設定

C 1. settings.json 加一行

2. 桌機 session 自動公開

3. CLI 或瀏覽器都能接管

4. 多端切換不用 SSH

康勞德日記

## Sources

- [Claude Code 桌面自動遠端接管](https://www.threads.com/@weilingkang3/post/DYRj6-jE8iX) | 作者: weilingkang3

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

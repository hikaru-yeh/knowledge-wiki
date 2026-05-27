---
網址: https://www.threads.com/@jungchun_/post/DYNKgI6n023
作者: ["@jungchun_"]
tags: []
status: wiki
---

## Main Content

教大家一個 Claude Code 效率提升大法：Hooks
如果你跟我一樣對 Slack 通知的聲音有 PTSD 的話
這招可以大幅提升工作效率：
讓 Claude Code 在工作完成、或是需要你介入時，送通知到 Slack
因為你當時可能正專注在另一個 session，也可能在專注看小廢片
及時把注意力拉回來
可以把原本需要一個下午才能做完的事，壓縮在一個小時內
做完之後就可以安心看小廢片了(?

設定方法很簡單 -- 其實還是那招, 請 Claude Code 幫你設定
原理簡單說就是：
1. 在 Slack 你的 workspace 上開一隻 bot, 拿到 bot token
2. 複製自己的 member id (可以在 Slack 上直接複製到)
剩下交給 Claude Code: 在 Notification 跟 Stop hook 觸發時跑通知腳本，用這個 bot 送 DM 給你自己
懶人包：可以直接將這個連結餵給你的 Claude Code 請他先裝好這個 skill
github.com/rjchi…
之後觸發這個 skill 就可以把 slack 通知設定好囉！

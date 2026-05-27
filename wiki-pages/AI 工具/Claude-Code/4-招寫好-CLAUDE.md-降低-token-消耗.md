---
網址: https://www.threads.com/@kanisleo328/post/DXO2PlPEoOQ
作者: ["@kanisleo328"]
tags: []
status: wiki
---

## Main Content

Opus 4.7 發佈第二天
很多人在抱怨 token 消耗變多
官方公告自己寫了
同樣 input 會吃 1.0-1.35 倍
模型那層動不了
能動的是 CLAUDE.md
每次 session 開頭就完整載入
我去看自己的：
136 行 + 6 個 .claude/rules/ 條件載入
還算精瘦
翻 Anthropic 官方 memory 文件
4 招我做了 3 招
剩一招從來沒用：
HTML 區塊註解
<!-- --> 包起來的內容
會在 inject 進 context 前被剝掉
給人看的歷史筆記 0 token
整理成一頁了
每招附 Before / After + 為什麼能省
連結放下面

leoaido.com/claud…
4 招簡表：
1. 歷史筆記包成 HTML 區塊註解
— 官方說會在 inject 進 context 前被剝掉
2. 用 .claude/rules/ + paths 讓規則條件載入
— 寫前端時後端規則不會載入
3. 每個 CLAUDE.md 控制在 200 行內
— 官方硬上限
4. @import 把長段落搬到外部檔
— 老實說不直接省 token，是結構工具
每招有可以複製的 before / after
leoaido.com
Claude Code memory 完整教學（附懶人包）：4 招寫好 CLAUDE.md 降低 token 消耗

我整理的是整體的整理方式，搭一下4.7的消息發的
不管哪個模型都適用這種整理方式

歐給

歐歐歐歐利奧

認同 他要加東西的時候我也不會那麼容易加進來

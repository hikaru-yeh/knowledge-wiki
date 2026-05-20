---
url: "https://www.threads.com/@ci.fullstack/post/DXKIDzzFFsS"
author: "@ci.fullstack"
clip_type: "Claude Code"
---

Harness Engineering
04/15/26
Harness Engineering 這個詞最近突然到處都是
我第一次看到的反應是
「等等，這不就是我去年在做的事嗎」
先講結論：
Agent = Model + Harness
Model 是 LLM 本身
Harness 是模型以外的一切
規格、測試、code review、工具串接、防護欄
大家一直在比誰用什麼模型
但老實說
模型是最容易換的部分
Harness 才是真正難的工程
我去年鐵人賽 60 篇寫的
很多後來被歸納進了這個框架
但也有我完全沒碰到的部分
下面展開講
有興趣也可以在主頁回顧一下我去年的文章

Harness Engineering 到底是什麼
Mitchell Hashimoto 今年 2 月替這個概念命了名
他的做法是：每次 agent 犯錯
就把修復方式工程化到環境裡
不是修 prompt，是改 harness
同一時間 OpenAI Codex 團隊發了一篇文章
說他們用 Codex agents 建了大約 100 萬行 code
零人工手寫
靠的不是更強的模型，是更好的 harness
4 月 Birgitta Boeckeler 在 Martin Fowler 網站上
發了一篇完整定義文章
把 harness 拆成兩類控制：
Feedforward（提前預防）
規格文件、CLAUDE.md、type system
在 AI 動手前就限制它的行為
Feedback（事後修正）
測試、linter、code review
AI 做完再檢查有沒有問題
他們還提了一個 Steering Loop
每次出問題就回去改控制機制
不是改 prompt，是改整個工程環境

跟我去年做的事有什麼關係
去年 9 月鐵人賽我寫了 60 篇
回頭看，很多東西其實就是 harness 的元件
SDD 規格驅動開發 = Feedforward control
寫 code 之前先定義規格
讓 AI 照著框架走，不要自由發揮
TDD 測試驅動 = Feedback control
先寫測試定義「什麼是對的」
AI 寫完 code 馬上跑測試驗證
Code Review = Feedback control
讓另一個 AI 角色審查產出
標記 CRITICAL / HIGH / MEDIUM
AI 團隊分工 — 我當時用 prompt 讓 AI 扮不同角色
現在 Agent Teams 原生支援了這件事
知識庫 — 跟 Karpathy 今年提的 LLM Wiki 同一個問題
他更進一步讓 AI 自己維護知識庫
但有些我沒碰到
像 observability 和 lifecycle management
不是「我早就在做一樣的事」
是「我做的一部分後來有了名字」

這對一般工程師代表什麼
工程師的角色正在轉變
從「寫 code 的人」變成「設計 harness 的人」
以前你花 80% 時間寫邏輯
現在 AI 幫你寫邏輯
你花 80% 時間在設計規格、寫測試、建防護欄
不用換工作
但工作方式會變
老實說我覺得這是好事
因為規格、測試、review 這些東西
本來就應該是工程的核心
只是以前大家趕專案都跳過了
現在 AI 逼你把這些做好
不然它跑出來的東西你根本不敢用
你目前有在 engineering your harness 嗎？
還是還在用「把需求貼給 AI 然後祈禱」模式？

同意，很多好的工程實踐本來就存在，現在有了框架把它們串起來而已

有，我去年鐵人賽實戰篇做了 4 個 side project，每個都跑完整的 AI 開發流程
接下來也會有更完整的實戰內容，可以追蹤或訂閱部落格

我自己的理解是兩個切入點不同
Context Engineering 偏向怎麼給 LLM 正確的資訊和工具
Harness Engineering 偏向模型以外的整個控制系統
兩個有重疊，這些概念都還很新，大家切的角度不太一樣

對，skills 算是 harness 的一部分
定義行為規範讓 AI 照著走
屬於 feedforward control — 動手前先限制範圍

搞過的人才知道痛XD

確實，我自己覺得 harness engineering 是一個硬實力，每個場景不太一樣，需要根據自己的 codebase 和流程去設計

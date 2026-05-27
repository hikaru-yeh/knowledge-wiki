---
網址: https://www.threads.com/@crazyaitools_/post/DXX70erknkQ
作者: ["@crazyaitools_"]
tags: []
status: wiki
---

## Main Content

我看到一個數據，AI 處理程式碼上下文的 Token 消耗，竟然可以減少 71.5 倍🤯。這數字嚇到我了，因為我最近在處理一個老專案，每次都要花半天跟 Claude Code 解釋專案架構，它還是常常誤解我的「為什麼」。

我發現一個叫 safishamsi/graphify 的 GitHub 專案，星星數有 31.4k。它做的事很單純，就是把你專案裡的程式碼、文件甚至影音資料，轉成「知識圖譜」。 → 掃描專案文件：跑 /graphify . 指令，它會自動掃描，分析你的程式碼結構。
→ 建立知識圖譜：透過 AST 解析、語音轉錄，再用 Claude 子代理來理解，幫專案建一張「地圖」。
→ 自動整合 AI 助手：你只要 graphify install，它就能把這張圖譜整合進 Claude Code 這些 AI 助手，讓 AI 在回答問題前先看地圖，不是自己盲猜。

我裝來試了一下，它在理解程式碼「為什麼」這件事上，確實幫 Claude Code 省了不少彎路。以前 AI 只知道「這是什麼程式碼」，現在它能透過這圖譜，多少摸到「當初為什麼要這樣寫」。特別是那些動輒幾十萬行的老舊專案，這種知識圖譜的價值才真正浮現。它還支援 25 種程式語言，適用範圍很廣。 小工提醒：這東西不是要取代你寫 CLAUDE.md，而是幫 AI 更有效地讀懂 CLAUDE.md 以外的「隱藏知識」。它反直覺的地方是，它用圖結構的邊緣密度來做社群聚類，不依賴傳統的 Embedding 技術，這點我覺得很酷。
code.claude.com
Claude Code overview - Claude Code Docs

專案連結：github.com/safis…
⭐ 31.4k stars
這方向對了，AI 最終還是要懂專案的底層邏輯。

@goliathplus
@goliathplus
兄台，你這句話直接點出了我當初的困惑啊！我第一次看到它說什麼『知識圖譜』、『減少 Token 消耗』，也覺得這是不是在畫大餅，畢竟讓 AI 真正『懂』程式碼，那根本是奇蹟。

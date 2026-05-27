---
網址: https://www.threads.com/@hanlinhans/post/DYN7bMVE_Ky
作者: ["@hanlinhans"]
tags: []
status: wiki
---

## Main Content

AI coding agent 不是不夠聰明，是看不到自己改動之外的世界。這個盲區現在有名字了：cross-repo context。
Cortex 2026 那份 benchmark：每個 PR 事故數 +23.5%，change failure rate +30%。三週後整個對話的語言就換了，所有人都在講同一件事。
● LLM 的 context window 是平的，但你的程式碼不是。
agent 改一個函數，可能被另外三個 repo 呼叫，下游凌晨四點告警。它不是忘了，是從來沒看過。
以前人腦在維護這張圖。但 agent 一天開三十個 PR，沒人能即時對齊。Cortex 那組難看的數據就是這麼來的。
● 過去六週有三個團隊從不同角度給了同一個診斷，最代表性的是 Neilos 的 ttal 架構 — 一個人管 15+ repo、跨五種語言、用 Telegram 協調十個 Claude Code agent。
核心設計：讀與寫徹底分開。

exploration agent 跨所有 repo 讀；worker agent 任何時刻只能寫入一個 repo，在隔離的 git worktree 裡；manager agent 持有完整跨 repo 計畫。
● 為什麼讀寫分離這麼關鍵？
讓單一 agent 同時擁有跨 repo 讀寫，是把 blast radius 打開到無限大。推理鏈出錯不是會不會，是多久一次。一旦錯了，多個 repo 同時寫入衝突修改，你連回滾單元都找不到。
讀寫分離把風險量化：讀無副作用所以可無界，寫收斂到單一 worktree，可以乾淨丟棄重做。跟資料庫分 OLTP/OLAP 是同一個工程直覺。
● 靜態 dependency graph 查詢快但維護貴，動態探索零維護但每次新路徑要重發現。未來會收斂到 hybrid — 靜態圖加速常見路徑，動態探索處理 long tail。
● 別以為這只是大團隊的問題。

任何團隊用 Claude Code、Cursor 在多個 repo 跑 agent，都會撞到同樣盲區。差別只是你的 incident 會不會進公司 retro。
agent runtime infrastructure 這層 — 介於 LLM 跟 git 之間、管 context、權限、寫入邊界 — 六到十二個月內會變成獨立產品類別。Neilos 的 ttal 是個人版，企業版的玩家應該已經在路上。
把 agent 當單 repo 工具用，是過渡期的權宜。會 scale 的團隊，會在「context 怎麼進到 agent」跟「agent 怎麼寫回程式碼」這兩件事建立明確紀律。
那組難看的數據，本質上就是還沒建立紀律的代價。
— 漢斯先生
AI #漢斯先生 #AIAgent #CrossRepoContext #AI工程

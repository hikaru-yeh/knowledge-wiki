---
url: "https://www.threads.com/@andrew54068/post/DYC_uMUj339"
author: "@andrew54068"
clip_type: "Claude Code"
---

Day 127 Cowork VS. CLI
身邊很多新手最近開始接觸 Claude，幾乎全部都是裝 Claude Desktop，不是 Claude Code（那個黑色 terminal 視窗）。
我懂，點開就用、有對話框、學習曲線低。
如果你主要用 Cowork 或 Claude Desktop，這篇是寫給你的。

Cowork 是 Claude Desktop 上最常用的 agentic 模式。
可以跨檔案、跨 app 幫你跑任務，確實方便。
Claude Desktop 和 Claude Code CLI 其實都是呼叫同一個 Claude API。
底層模型能力一樣，差的是包裝。
差距具體在哪？
以下說四件事。

【第一件：CLI skill 比 Cowork 早兩個月】
當你看到"Cowork 開始有 skill"這件事被介紹，
CLI 上的 skill 已經跑了兩個月了。
可以想像很多其他功能都是，因為定位問題甚至到現在還沒推出
【第二件：Cowork 的 skill 很難裝，而且跟 CLI 的 skill 裝在不同路徑】
CLI 裝別人的 skill 是一行指令打完。
大神寫的 skill 三秒就用上。
Cowork 自己做 skill 點一下"save skill"很直覺。
但你要去安裝別人寫的 skill，路徑藏得很深，不好找。
更重要的是：Cowork 和 Claude Code 的 skill 裝在不同路徑，不會自動共用。
CLI 裝好的 skill，Cowork 看不到；反過來也一樣。
兩邊都想用，要分別裝兩次。

【第三件：CLI 早就有 agent team，Cowork 還沒有】
CLI 上我們天天在用 subagent（Claude 派出去的分身）。
主對話派 subagent 出去做事，subagent 回報結果。
主對話的記憶不會撐爆。
再進階是 agent team（多個 AI 分身互相辯論）。
一個 AI 負責產出 code，另一個專門挑毛病。
互相對抗直到結果通過。
Cowork 目前還是"一個 agent 幫你跨 app 做事"的階段。
多個 agent 互相討論收斂的協作模式還沒有。
對 CLI 用戶來說，agent team 是家常便飯。

【第四件：CLI 有 hook，可以在特定時機自動做事】
Hook 簡單說就是：你寫一段命令，讓 Claude 在"特定時機"自動跑。
例如：
對話結束前，自動跑一遍驗證。
確認剛剛說好要做的任務真的做完了，沒有跳掉。
對話結束後，把聊出來的東西整理成小抄。
下次做類似事情時拿來複習，不用每次從零開始想。
CLI 支援一連串可以掛 hook 的時機：
送出訊息之前、Claude 用工具之前、用工具之後、整段對話結束前。
每個時機都可以掛一段你寫的事情，自動發生。
Cowork 上還沒有 hook 系統。
"對話結束自動驗證"、"自動寫小抄"這些事，Cowork 沒辦法做。
你只能每次都手動。

這不是說 Cowork 沒有用。
如果你不寫 code，只想 AI 幫你在檔案、文件、app 之間跨來跨去做點瑣事，
Cowork 設計給你的場景比 CLI 友善很多。
介面好、不用 terminal、學習成本低。
Cowork 對標的是 OpenClaw（龍蝦）。
只是沒有 OpenClaw 那麼強大。
但如果可以，我還是強烈建議克服 Terminal 的障礙。
你會看見新世界。
你現在用的是 Cowork 還是 CLI？
或是你覺得 Claude Code 出個 GUI 版本，大家反而會更有興趣？

功能上算是 cli 的閹割版
因為受眾應該是沒有工程背景的人

---
url: "https://www.threads.com/@andrew54068/post/DXMo9JMGmPH"
author: "@andrew54068"
clip_type: "Claude Code"
---

正在回覆@andrew54068
【先搞懂 subagent 到底在省什麼】
Subagent 是一個獨立的 Claude session，有自己的 context window、系統提示詞、工具權限。Claude 遇到適合的任務就把它派出去，subagent 自己做完之後，只把"結論摘要"回傳給主對話。
這個設計解決的不是成本問題——是 context 爆炸問題。
舉個例子:你叫 Claude 幫你找"這個 repo 裡所有用到某個函式的地方，哪些寫法有問題"。直接在主對話做，Claude 會 grep 一百個檔案、讀五六十個 component、把幾千行 code 灌進 context。等它要給你答案時，對話視窗已經被垃圾塞爆，後面幾輪就開始失憶、重複問你先前講過的事。
改用 Explore subagent(內建的，跑 Haiku、只讀不寫)做同一件事，主對話只會看到一段"我找到 x 個問題，分別是……"的摘要。十倍以上的 context 差距，而且會疊加累積。 2/14

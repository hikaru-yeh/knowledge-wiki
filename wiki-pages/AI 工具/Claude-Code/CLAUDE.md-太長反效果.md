---
網址: https://www.threads.com/@shareuhack/post/DX8iUMOEle5
作者: ["@shareuhack"]
tags: []
status: wiki
---

## Main Content

claude code
6d
你的 CLAUDE.md 寫了 300 行，Claude 還是不照做。
直覺反應是再加規則。但這正好是問題本身。

CLAUDE.md 不是系統指令，官方文件寫得很清楚：它是以「用戶訊息」傳進去的。Claude 會自己判斷跟當前任務相不相關，覺得不相關就跳過。
官方建議控制在 200 行以內。超過之後遵守率明顯下降，而且社群觀察到是所有規則一起變弱，不是只有新加的那條。

Claude Code 的創造者 Boris Cherny 自己的 CLAUDE.md 是「surprisingly vanilla」，基本上就兩行指向團隊共用的設定檔。
社群後來歸納出的原則也類似：與其堆 300 行常識，不如只留 Claude 從程式碼本身看不出來的 gotchas。

真正不能被忽略的規則，搬到 command hooks。
Command hooks 在 shell 層跑，不經過 LLM 判斷。commit 前自動跑 lint，不過就擋掉，沒有「Claude 覺得不相關」的問題。

大部分人花時間讓 CLAUDE.md 更長。但 200 行寫對的東西，Claude 每條都記得住。方向搞反了。

只能盡量程式檢查的全交給 hook、工作流程加上 review 機制，靠架構和流程來增加可控性

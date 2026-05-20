---
url: "https://www.threads.com/@endman100/post/DXK_D-mEzO4"
author: "@endman100"
clip_type: "AI"
---

介紹一個可以有近乎用不完 Claude Opus 的方法
順便推坑一堆在CC中用完200美額度的朋友(X
1. 下載 GitHub Copilot
2. 讓 Copilot 安裝這個 Skill → github.com/endma…
3. 完成，開始用
為什麼這樣能「用不完」？
GitHub Copilot 訂閱附帶 Claude Opus 使用額度，而且目前相對寬鬆。
Copilot 計費是用算 Request 次數的，並不在意你一次 Request 多長、用多少 Token，都只算你一次 Request。
另外如果觸發 Copilot 的選項，亦算是還在同一個 Request 中。
這個 Skill 做的事只有一件：
每次 Copilot 做完事、準備結束前，強制問你：
「接下來你想做什麼？」
然後根據當前情境，自動幫你列出 3 個下一步選項與一個輸入框。
選一個或輸入文字，直接繼續指令，維持在同一個 Request 中，直到你真正重構/Debug完。
算是個漏洞（？）
且用且珍惜吧。
github.com
GitHub - endman100/skill-always-ask-next

依舊還是能使用喔
只是現在改用 Opus 4.7+讓 requests 次數變多

你可以讓你的 Agent 按照 readme 安裝這個skill (實際上就是在你的copilot的設定中追加 always-ask-next.instructions. md檔案
多數情況都可以連續產出3個建議，除非你提到要結束或是token太多被壓縮

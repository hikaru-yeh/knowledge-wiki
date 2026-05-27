---
網址: https://www.threads.com/@andrew54068/post/DXE81eYGqG0
作者: ["@andrew54068"]
tags: []
status: wiki
---

## Main Content

[https://www.threads.com/@andrew54068/post/DXE81eYGqG0](https://www.threads.com/@andrew54068/post/DXE81eYGqG0)

## 主文

ClaudeCode
04/13/26
Day 103 讓 Claude Code 的 skill 自己進化：我做了一個從失敗中學習的工具
你的 Claude Code 是不是也有這種狀況？
有些 skill 用得很順，但有些會一直踩坑——AI 做了你不想要的事，你糾正它；或同一個工具連續失敗好幾次。
每一次你說 "不是這樣"、每一次同一個工具連續炸三四次，這些痕跡全部都留在 Claude Code 的 session 紀錄裡（~/.claude/projects/ 底下的 .jsonl 檔）。
這些 "負面訊號" 其實就是改進的線索。
昨天聊到的 Hermes 是根據對話紀錄自動判斷要不要做成 skill、或是改進現有的 skill。但如果我不用 Hermes，而是用 Claude Code 自己，是否也有機會讓 skill 進化？
Day 100 提到 "先求有再求好"。在 AI 協作的脈絡下，"求好" 這件事能不能也自動化？
於是我做了一個工具，叫 claude-evolver。

## 作者留言

ClaudeCode
04/13/26
·
Author
【Darwinian Evolver：讓 skill 像生物一樣演化】
設計靈感來自生物演化：找出不適應的個體，產生突變，讓突變體跟原本的版本比賽，贏的留下來。
整個流程是這樣：
Miner → 掃描最近的 session 紀錄，找出失敗訊號（使用者糾正、重試、砍掉重來、工具連續失敗），然後追溯是哪個 skill 或規則在當時被使用
Mutator → 把有問題的 skill 複製到沙盒裡，用 Claude 根據失敗的脈絡產生一個改良版本
Evaluator → 用同樣的情境分別跑原版和改良版，然後讓另一個 AI 當裁判打分。不是看文字改了什麼，而是看行為有沒有變好
Reporter → 產出一份 HTML 報告，左右對比兩個版本的實際輸出，讓我自己決定要不要採用
最後如果我同意，才會把改良版推上去取代原本的。所有歷史版本都用 git 追蹤，隨時可以回滾。

ClaudeCode
04/13/26
·
Author
【離峰時間自動復盤】
這套流程我設計成可以在離峰時間自動跑。我自己是排凌晨 3 點，讓它根據前一天的 session 紀錄自動判斷哪些 skill 需要優化，等我早上起來就有一份報告可以看。
好處是不會佔用白天工作的時間，也不會干擾正在進行的對話。整個過程就像夜裡的健康檢查——隔天醒來直接看結果。
當然這需要搭配一些設定檔：要掃描哪個目錄、用哪個模型當裁判、失敗訊號的門檻怎麼設、哪些 skill 不要動等等。
目前是做成 CLI 工具，自己再用一陣子、把設定跟流程磨順之後再考慮開源。有興趣的人可以先追蹤，之後會分享更多細節。

ClaudeCode
04/13/26
·
Author
【跟 Hermes 的差異】
Day 102 介紹的 Hermes Agent 走的是 "邊用邊學"——在每次互動中順便改進 skill。
我做的 claude-evolver 是 "定期體檢"——從累積的失敗中系統性地抽取改進方向，然後用對照實驗驗證。
兩種方向不衝突。Hermes 適合即時的、對話層級的學習。claude-evolver 適合跨 session 的、需要比較才能判斷的改進。
一個像是每天運動保持健康，另一個像是定期做健康檢查。
目前沒有做成全自動是因為品質把關還是得人來界定，不然很可能發生昨天還用得好好的 skill，今天卻被改壞的慘況。

ClaudeCode
04/13/26
·
Author
【背後的模式】
Day 99 提到一個觀察：大家的問題不是 AI 不夠強，而是不知道怎麼把資料接進 AI。
同樣的邏輯也適用於 AI 改進自己的工具。Claude Code 的 session 紀錄裡藏著大量可以用來改進的資訊，只是之前沒有工具把它挖出來。
我覺得這是一個值得關注的方向。不只是用 AI 做事，而是讓 AI 改進它做事的方式。先求有，再讓它自己求好。
你平常用 Claude Code 遇到最常重複踩的坑是什麼？留言聊聊，說不定那就是下一個該被 evolve 的 skill。

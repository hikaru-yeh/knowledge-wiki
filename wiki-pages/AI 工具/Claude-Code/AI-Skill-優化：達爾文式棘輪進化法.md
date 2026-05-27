---
網址: https://www.threads.com/@fu_liren.ai/post/DXMepJsE8Gg
作者: ["@fu_liren.ai"]
tags: []
status: wiki
---

## Main Content

棘輪是一種只能往一個方向轉的齒輪，倒著轉不動
進化論是棘輪。物種只能越來越適應環境，沒辦法退化回去。科學也是，一個理論被證偽了就永遠出局，人類的知識只增不減。git 歷史也是，每個 commit 都是一個存檔點，你永遠能回到某個好狀態。
而我一直在思考，這套邏輯能不能搬到 Claude Code Skill 優化上。
直到我看到了個叫達爾文.skill 的工具，邏輯比我想像中簡單：讓 AI 自動掃你所有的 skill，找到得分最低的維度，針對它改一個具體的東西，然後讓獨立的 agent 打分。
分數漲了就 git commit 保留，沒漲就 git revert 當沒發生過。不管跑幾輪，你的 skill 只會越來越好。

我拿了自己最常用的幾個 skill 跑了一遍，一個幫我做每天做複利工程的 skill 從 65 分跑到了 85 分，中間那次退步被乾淨回滾，不留下任何痕跡。
而這個skill，也從我想像不到的角度變得更強大了。很多時候並不是技術跟不上，而是想法跟不上。
對我來說，比這套工具本身更有意思的是這個模式。
棘輪可以套在任何有評估標準的東西上。Prompt 是棘輪，工作流是棘輪，你對某個領域的判斷也是棘輪，每次踩坑都在收窄錯誤邊界。
只要你有辦法評估「這次比上次變得更好還是更差」，時間就自然站在你那邊。
「當你給任何創造性工作加上只保留改進的約束時，時間就站在了你這邊。你不需要每一步都走對，你只需要確保走錯的那步不留痕跡。」
GitHub：github.com/alcha…
安裝：npx skills add alchaincyf/darwin-skill
github.com
GitHub - alchaincyf/darwin-skill: 达尔文.skill —— 一个让你的Skill无限进化的系统：评估→改进→测试→保留或回滚 | Autoresearch-inspired autonomous skill optimization for Claude Code. Evaluate, improve, test, keep or re

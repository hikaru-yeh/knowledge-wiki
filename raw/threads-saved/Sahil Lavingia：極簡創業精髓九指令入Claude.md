---
base: "[[收藏清單_DB.base]]"
url: "https://www.threads.com/@ayueliu/post/DWSRs3LEmjH"
author: "ayueliu"
clip_type: "Claude Code"
date_added: 2026-04-21T12:58:00
---

[https://www.threads.com/@ayueliu/post/DWSRs3LEmjH](https://www.threads.com/@ayueliu/post/DWSRs3LEmjH)

## 主文

ClaudeCode
03/25/26
9 個指令，把整本《極簡創業家》裝進 Claude

Gumroad 創辦人 Sahil Lavingia 把《極簡創業家》（The Minimalist Entrepreneur）的方法論打包成 9 個 Claude Code 指令，上傳 GitHub。不到 24 小時，830 個 star、57 個 fork。

這本書真的非常勵志，如果你看過的話應該會非常興奮。更令人興奮的是，他推出了 Skill。

項目連結、貼文、佈署方式見以下👇

## 作者留言

ClaudeCode
03/25/26
·
Author
🟩 關於 Sahil Lavingia
Sahil 2011 年 19 歲創辦 Gumroad，數位商品販售平台。剛開始創業走矽谷模式，做瘋狂擴張、做閃電擴張，公司規模上來了，但是營運卻沒有帶來多大的收益。

後來他直接把全公司的人都 lay off，只剩下他一位，所有的工作業務全部外包了。到現在 $10M ARR，還是只有他 1 名員工。

ClaudeCode
03/25/26
·
Author
🟩 讀完書，然後呢？

多數人讀完書就放書架。卡的不是看懂沒有，是「怎麼用？」這一步。

其實，大部分關於書的知識，很少有可以發揮的場景。

Skill 給了這個場景：需要做決策時，直接呼叫對應指令，AI 用書裡的框架拆你的問題。不用記住書全部的知識或架構。

ClaudeCode
03/25/26
·
Author
🟩 《極簡創業家》被拆成 9 個指令（安裝方式我放留言區👇），按創業路徑排列：

 - /find-community — 找社群
 - /validate-idea — 驗證想法
 - /mvp — 最小可行產品
 - /first-customers — 第一批客戶
 - /pricing — 定價
 - /marketing-plan — 行銷計畫
 - /grow-sustainably — 可持續成長
 - /company-values — 公司文化
 - /minimalist-review — 極簡主義複盤

ClaudeCode
03/25/26
·
Author
🟩 同一行指令，差在哪？

Skill 不是照抄就有用。一個普通人寫的 /validate-idea，叫出來就是幾個通用問題。

Sahil 的版本背後是他從 Pinterest 第 2 號員工、到 Gumroad 創辦、融資、失敗轉型、出書，15 年積累下來的判斷。你的Skill名稱可能跟他一樣，但細節肯定差很多。

Y Combinator 的 gstack 爆紅也是同樣邏輯：不是工具厲害，是工具背後的知識積累。

ClaudeCode
03/25/26
·
Author
🟩 他怎麼做出這個 plugin

整個 repo 6 個 commit，共同作者是 Claude Opus 4.6，只花一天。

技術架構：9 個 Markdown 檔 + 1 個 plugin.json，零依賴，幾乎沒有技術門檻。

這個 repo 本身就在示範書裡那套邏輯：有個問題（沒有可以呼叫的創業顧問），用最少的工作量解決它，放到 github 上面開源。

ClaudeCode
03/25/26
·
Author
🟩 這種文最常出現的坑

「一個人靠 AI 賺了 $1 千萬美金」看起來很有說服力，但這一路上都是坑。

哪些坑？試錯幾次、工具壞掉時怎麼辦、哪些決策不能丟給 AI、學習曲線要燒多久。這些是你實際要付出的成本：時間、金錢、機會成本，都算進去。

效果常被放大。看這類文章，先把結果打折，再問自己願意支付什麼。

ClaudeCode
03/25/26
·
Author
作者的 X：x.com/shl/s…
Github：github.com/slavi…
佈署：
git clone github.com/slavi… ~/.claude/plugins/skills
在 Claude Code 輸入 /plugin install，9 個指令上線。
github.com
GitHub - slavingia/skills: Based on The Minimalist Entrepreneur by Sahil Lavingia

·
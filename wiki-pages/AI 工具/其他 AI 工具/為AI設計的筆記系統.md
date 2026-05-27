---
網址: https://www.threads.com/@mukiwu/post/DYcUedzlBE7
作者: ["@mukiwu"]
tags: [AI]
status: wiki
---

## Main Content

從分類資料夾轉向檔案扁平化
​
2025 年我還在使用 Obsidian 的時候，我是用 PARA 這個資料夾結構來整理我的筆記。但隨著 AI 的興起，後來幾個月我一直想要重新調整他的結構，所以誕生了 Hyday 這套筆記軟體
​
Hyday 的出現，也讓我意識到了一個深層的設計問題：「我還在用人類大腦整理筆記的方式設計資料庫，但實際上每天最常翻我筆記的是 AI」
​
我們人腦習慣的是「把檔案放在哪個資料夾」這樣的視覺分類，但 AI 不需要，AI 要的是 frontmatter、tag、index 這類能一次掃完的東西。
​
如果我繼續用人腦的思維去設計 Hyday，等於每次跟 AI Agent 互動時，都要他重複 grep 整個資料夾，耗時耗力，也耗 token
​
而以下這篇文章就是我以 Hyday 為例，重新整理後的資料結構，與大家分享

◆ 各司其職的三種索引
​
我的 Hyday 最後的架構如下：
​
📁 Hyday/
├ sources/　　　　　外部素材（AI 只讀不寫）
│　├ books/
│　├ articles/
│　└ pdfs/
├ 根目錄 *.md　　　　我親手寫的筆記，沒有資料夾分類，全扁平化
├ wiki/　　　　　　　AI 編譯後的主題知識
│　├ _schema.md　　 wiki 規範
│　├ _tags.md　　　 全 vault tag 詞彙表
│　├ _index.md　　　全 vault 元資料索引
│　├ INDEX.md　　　 wiki/topics/ 主題索引
│　├ log.md　　　　 變更紀錄
│　└ topics/　　　　編譯後主題頁
└ journal/　　　　　日記

三份索引各自的角色：
​
→ _tags.md
索引什麼：全 vault 所有 tag 詞彙表
給誰用：AI 加 tag 時必查、防止自創
​
→ _index.md
索引什麼：全 vault 筆記的元資料
給誰用：AI 找東西時的快速入口
​
→ INDEX.md
索引什麼：只索引 wiki/topics/
給誰用：找「我整理過的主題知識」
​
每份索引只負責一件事，各司其職、不會重疊

◆ Wiki 的核心原則：指向不複製
​
參考 Andrej Karpathy 的 LLM wiki 概念，我對 wiki 的定義是「重新整合、用自己的話寫、底下附來源連結」的內容。他不是純索引，也不是抄原文，而是整合與收斂的產物
​
我把具體的規則寫到 wiki/_schema.md 中，其中包括可以和不可以做的事：
​
✅ 可以：用自己的話組織、整合多個來源、加 mermaid 表格
✅ 可以：引用原文金句
❌ 不可以：大段抄原文，當超過 50 字時要改寫
❌ 不可以：只列「相關筆記」卻沒有實質內容，因為那就變成是純索引了
​
而每個 wiki/topics/*.md 結尾都要附上「來源」
​
如此以來，我的原始筆記始終是獨立的觀點，不會被 wiki 所覆寫，而 wiki/topics 是該主題的最新整合視角，可以進行校對更新，讓兩個層級乾淨分離
​

◆ 建立自己的 tag 詞彙表
整理筆記時，也順便整理自己使用過的 tag，並請 AI 掃描整個資料庫，包含 frontmatter、inline，把所有用過的 tag 列成一份詞彙表 wiki/_tags.md
_tags.md 的格式長這樣（節錄）：
→ areas/思維模型
fm：140　inline：1　總計：141
→ projects/Hyday
fm：18　inline：213　總計：231
→ 開發日誌
fm：3　inline：458　總計：461
校對與合併後，詞彙表就變成專屬的合約，要新增 tag 時必須先登記到詞彙表，才能用到筆記裡
同理，可以將這條規則寫進 CLAUDE.md，從此 AI 加 tag 前會先查 _tags.md，避免自創標籤

◆ 調整後的流程與架構
​
調整後的架構,變成了包含扁平化、三份獨立索引，以及 AI 自動規則的系統
​
我在 CLAUDE.md 裡寫了要讓 AI 自動做的事：
❶ 有新的 tag 必須先登記到 _tags.md 才能用
❷ 資料庫內引用 wikilink，不用 markdown link
❸ 用整合的視角來撰寫 wiki/topics/，不大段抄原文
❹ 我動到的筆記如果是某 wiki 頁的來源，AI 會提醒 wiki 可能要更新
未來,我只會讓人腦（自己）做兩件事：
❶ 產生想法並寫到筆記裡
❷ 做判斷
・AI 可以建議我文章要標哪些 tag，但依然由我拍板決定
・這個主題是否累積夠多的文章？是否要編譯到 wiki/topics？
剩下的索引、關聯、跨筆記整合、維護，通通交給 AI，我給他的定位是編譯人員，幫我把散落的素材編譯成結構化的知識，再隨時更新維護

◆ 小結
​
如果你也有一個「檔案很多但都找不到、想整理但不知從哪開始」的資料庫，歡迎參考以上文章，建立屬於自己的流程體系
​
最好的整理工具不是更好的分類系統，而是讓 AI 接手整理這件事
​
剩下的就交給時間了
​
━━━━━━━━━━━━━━━━━━━━━━━
​
📱 關於 Hyday：本文提到的 Hyday 是我自己開發的筆記軟體，更多介紹與下載請到 hyday.tw
​
完整網頁版（含表格與 code 排版）：
👉 muki.tw/from… 顯示較少

## Sources

- [為AI設計的筆記系統](https://www.threads.com/@mukiwu/post/DYcUedzlBE7) | 作者: mukiwu

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

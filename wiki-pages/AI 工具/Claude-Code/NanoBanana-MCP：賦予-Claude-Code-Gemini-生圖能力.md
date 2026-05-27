---
網址: https://www.threads.com/@ci.fullstack/post/DWt_vBwk6h0
作者: ["@ci.fullstack"]
tags: []
status: wiki
---

## Main Content

先講 NanoBanana MCP 是什麼
MCP 是 Model Context Protocol
簡單說就是讓 AI 可以接外部工具的橋樑
Claude Code 本身只能讀寫檔案、跑終端機
裝了 MCP server 之後，它就能做更多事
查文件、讀 Notion、操作瀏覽器 — 都靠 MCP
NanoBanana MCP 做的事情是
把 Google Gemini 的圖片生成模型接進來
所以你跟 Claude Code 說「幫我生一張圖」
它就會透過 NanoBanana 去呼叫 Gemini
然後把圖片存到你的電腦上
不用開瀏覽器、不用另外登入、不用離開終端機

安裝只要一行指令
claude mcp add nanobanana-mcp -- npx -y
@ycse
/nanobanana-mcp -e GOOGLE_AI_API_KEY=你的key
就這樣。裝完重開 Claude Code 就能用了
API key 要去 aistudio.google.com 申請
Google 的 Gemini API 有免費額度
一般個人用量完全夠
裝完之後 Claude Code 會多出幾個工具：
set_aspect_ratio — 設定圖片比例
set_model — 切 flash（快）或 pro（精細）
gemini_generate_image — 生圖
gemini_edit_image — 改圖
gemini_chat — 多輪對話微調
我自己最常用的是 generate 和 chat
生一張不滿意，用 chat 跟它說「顏色再深一點」就好

Prompt 怎麼寫才出好圖
我一開始也是亂寫
「幫我生一張科技風的圖」
出來的東西每次都不一樣，品質也不穩定
後來摸出一個公式：主體 + 風格 + 構圖 + 色彩
比如這篇的封面圖，我給的描述是：
「科技綠暗底，電路板背景，大標題白字，品牌標籤左上角」
Claude Code 會自動把中文翻成英文 prompt
因為 Gemini 對英文 prompt 的生成品質比較好
然後幫你呼叫 API 生圖
有個重點：AI 生的圖裡面的文字常常有錯
所以不要在 prompt 裡塞太多精確文字
標題 + 一段副文就好，多了容易出錯
想找靈感的話可以看 awesome-nano-banana-pro-prompts
上面有一萬兩千多個 prompt 模板，按風格和用途分類

我後來把整個流程寫成了一個 Skill
叫 /ig-carousel
以前每次生 IG 圖文要手動做這些事：
設定比例 1:1 → 想英文 prompt → 指定風格 → 生圖 → 清除 AI 標記
現在我只要打一句：
/ig-carousel Claude Code 教學 — 科技綠暗底
它就會自動：
自動設定 1:1 比例
自動把我的中文描述翻成英文 prompt
自動套上品牌排版（標籤、簽名位置）
自動清除 C2PA metadata（不然 IG 會貼「Made with AI」）
這篇的 5 張圖就是這樣出來的
老實說這個方法有明顯的優缺點
適合的場景：
快速出圖、風格一致的系列圖、每天要發文但沒時間開設計軟體
我的系列 48 天的配圖全靠這個撐下來的
不太適合的場景：
需要像素級精準排版、品牌設計稿、或是圖裡有大量精確文字
AI 生的文字偶爾會有錯字，複雜佈局也不一定每次到位
簡單說就是「夠用、夠快、但不完美」
對我來說每天發文這個節奏，速度比完美重要

感謝大家的回饋和支持！
看到不少人想要這個 /ig-carousel skill
我決定直接開源放 GitHub + 寫一篇完整教學文
內容會包含：
- 安裝設定（一行指令）
- Prompt 怎麼寫才穩定
- Skill 原始碼完整公開
- 以及一些避坑經驗
同時也在研究 HTML 排版 + AI 背景圖的混合做法
文字精準度會比純 AI 生圖好很多
做好了會當 v2 分享出來
教學文近幾天發，敬請期待～
有問題都歡迎留言聊

哈哈每個人喜好不同，skill 完全可以照自己喜好調整，重點在於流程跟方法喔～

感謝XD

感覺可以寫一篇詳細的教學文了，等我發一篇～

感謝支持～坦白說這是我目前最常使用的產圖工作流XD

很好的問題～這個就牽扯到 MCP 的概念，差別在於 MCP 是 Claude Code 原生懂的協定，agentic 流程裡 Claude 能正確處理 tool call 的來回跟錯誤，直接包 API 的話語義上 Claude 對執行過程不太清楚
不過單純產圖這種 one-shot 場景兩個差異不大，選哪個都行XD

對啊，所以我自己還是會轉成英文的 Prompt 丟進去

感謝支持~晚點來整理一下

感謝支持哈哈，持續學習中～

MCP 是個好東西

很讚～

沒錯～

好啊～等我發一篇

感謝支持～我目前也是用這個工做流完成很多工作真的很方便
這個很適合有買 google AI Pro 的朋友們，一天有 250 張可以花XD

好感動～感謝支持～

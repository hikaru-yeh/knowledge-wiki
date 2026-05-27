---
網址: https://www.threads.com/@isaac_shekht/post/DW6KekREWw7
作者: ["@isaac_shekht"]
tags: []
status: wiki
---

## Main Content

五天前，Andrej Karpathy（OpenAI 的早期成員）在 X 上第一次分享他的知識管理系統「LLM Wiki」
在短短幾天就獲得了超過 1800 萬次觀看
受到啟發，我也開始建立自己的「AI 第二大腦」—— 一個由 AI 自主維護的知識庫，涵蓋我人生中接觸過的每一個領域
→ 把散亂的素材，整合成一個結構化的 Wiki
→ 節省 95% 的 tokens = 省錢 + 提高輸出質量
→ 適用於 Claude Code、Codex，或任何 LLM
→ 除了第二大腦，也能用來管理代碼庫或大型 Research
以下是最簡單的應用方法👇🏻

在開始之前，我超級建議你先理解它的原理，再思考如何套用在你的生活中
→ Karpathy 的原始 Tweet：x.com/karpa…
→ 這條 YouTube 影片解釋了整個概念，建議先看完再動手：youtu.be/sboNw…
youtube.com
Andrej Karpathy Just 10x’d Everyone’s Claude Code

三步開始：
1. 建立一個資料夾，放入你的文章、筆記、代碼
2. 打開 Claude Code（或者其他 LLM 也行）
3. 輸入指令：
（先到以下連結拷貝 Karpathy 寫的指引）
gist.github.com/karpa…
再拷貝以下的 prompt👇🏻
gist.github.com
llm-wiki

You are now my LLM Wiki agent. Implement this exact idea file as my complete second brain. Guide me step-by-step: Read everything in raw/. Then compile a wiki in wiki/ following the rules by creating the CLAUDE.md [按照你選擇的 AI 使用 Agents.md 還是 README.md 都可以。重要的不是檔案名稱，而是裡面的內容] schema file with full rules, set up index.md and log.md. Next, create one .md file per major topic, define folder conventions, tag and link related topics.
（下串繼續👇🏻）

[原創 但十分重要，這會影響你的Tags 系統的一致性）
For tags, create a tags.md file at the vault root listing all approved tags with descriptions. Add a rule in CLAUDE.md requiring agents to check tags.md before creating new tags. So that we can prevent duplicates and inconsistencies (e.g., #goal-setting vs #goals, #self-development vs #personal-growth)

[原創 - 讓 AI 幫你儲存重要的對話紀錄]
Create wiki/conversations/ as a new subfolder
∙ Add a conversation page type to CLAUDE.md with frontmatter like date, topic, key-insights
∙ Add a workflow rule: when the user says “save this conversation” (or similar trigger phrase), the LLM compacts the conversation into a wiki page with key takeaways, decisions made, and links to related wiki pages
∙ Add it to index.md as a new section
∙ Only save when explicitly asked — not automatic

[最後分享一個我很喜歡的做法：建立一個 disagreements/ 資料夾，專門紀錄持相反意見/立場的理據（參考自 Ali Abdaal）]
Create a disagreements/ subfolder. When sources conflict — researcher A says do X, researcher B says the opposite — create a page documenting both positions with their supporting evidence. This is far more useful than a clean summary when deciding what to teach or write or build in the future.
x.com/aliab…

不想讓 80 歲的自己後悔？
不想每年都在訂同樣的目標，卻從未完成過？
你還未成功，不是因為你不夠自律 —— 而是你從來沒有設定一套系統，幫你把目標拆解成「今天該做什麼」
我用了 5 年時間建立了一套系統
90 天為一個週期
每天只需 5 分鐘就能知道下一步要做什麼
每週六我會把其中一個框架寫成電子報
一個主題 ➕ 一個行動
讀完就能直接使用
免費訂閱👇🏻

真的，一開始感覺要用很多Token有點不捨得，但後來看到 Claude 的回應真的有質量提升，就覺得一切都值得🙌🏻
現在感覺都不需要 Claude/GPT 裡面的 project 了，這個 setup 又省 token，又能幫 AI 精準找到重點
長期來說真的很值得投資

Yea, it is 🙌🏻
I’ve been playing around with it for several days on 3+ cases. I really found unlimited possibilities here.
Definitely worth trying!

謝謝你的支持🙌🏻

## 圖片文字

Graph view
X +
< >
> assets
v raw
> 01-Projects
> 02-Area
> 03-Resources
> archived
Plan
Projects
> templates
v wiki
> comparisons
> concepts
> conversations
> entities
> overviews
> summaries
> syntheses
CLAUDE
index
log
tags

CANVAS
BASE

goals-course-content

Shek's Vault

Canvas mindmap
Smart v2.4.0

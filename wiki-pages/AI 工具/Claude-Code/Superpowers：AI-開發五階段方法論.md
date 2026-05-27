---
網址: https://www.threads.com/@ci.fullstack/post/DYH_K6vnSWf
作者: ["@ci.fullstack"]
tags: []
status: wiki
---

## Main Content

Anthropic 官方 plugin marketplace 上架的東西
有一個是個人開發者一個人寫的
obra/superpowers 184k stars
7 個月
跨 Claude Code、Codex、Cursor、OpenCode、Copilot、Gemini 都能裝
我 4/16 介紹 gstack 那篇有提到他
但只有一行帶過
老實說當時就想好好寫一篇
拖到今晚
為什麼 gstack 是「工作站」
Superpowers 是「方法論」
我兩個都裝
核心 5 個 stage：
Brainstorm → Plan → TDD → Debug → Review
不是技術新意
是把該做的步驟固化到 AI 身上
不會跳過 brainstorm 就寫 code
不會省略 plan 就 debug
下面展開 5 stages、和 gstack 的差別、我設成 mandatory 的幾個
你裝了之後回不去的 Claude Code skill 有哪些？

Superpowers 5 個 stage 拆開講：
1. Brainstorm
寫 code 前先把想法聊清楚
AI 會反問需求、邊界、edge case
聊到夠清楚才往下走
2. Plan
任務拆成 2-5 分鐘可完成的細項
寫成 plan 檔案
不是 todo list
是有 acceptance criteria 的 spec
3. TDD
RED → GREEN → REFACTOR
強制先寫測試
80%+ coverage
4. Debug
4 phase 根因分析
不准跳過 investigation 直接 fix
5. Review
多層驗證
verification-before-completion 是最後一道 gate
每個 stage 對應一個 SKILL.md
AI 跑到那步會自動觸發
你不用記

不太能直接取代——定位不一樣
SpecKit / OpenSpec 是 spec-driven dev 框架（先寫規格再做）
Superpowers 是 workflow 紀律層（確保 agent 不跳步驟）
有重疊但比較像疊著用
要找 SpecKit / OpenSpec 的同類，GSD 比較對位
我前天剛發一篇

plan 跟 verification 我也是這兩個感受最強～
GSD 切 phase 那塊今晚剛發了一篇

我裝完 superpowers 後，這幾個設成必觸發：
using-superpowers
這是 entry point
每次對話開頭強制檢查有沒有其他 skill 適用
沒這個其他都不會自動觸發
brainstorming
寫 code 前必跑
我太常一句話丟給 AI 然後拿到一坨偏掉的東西
brainstorming 逼你先聊清楚再動手
writing-plans
複雜任務必跑
不寫 plan 直接 do 是 AI 加速失控的最快方式
test-driven-development
新 feature 跟 bug fix 必跑
讓 AI 先定義什麼叫對
verification-before-completion
做完前必跑
AI 最會 over-claim 自己「完成了」
這個 skill 是最後一道 gate
14 個 skill 我大概用 10 個
看任務挑

為什麼說 gstack 是工作站、Superpowers 是方法論：
gstack
13 個 slash command
產品規劃 → 架構 → code review → QA → 發佈
內建 Playwright 瀏覽器引擎
高度綁 Garry Tan 跟 YC 文化
裝了就是一整套團隊文化包
Superpowers
14 個核心 skill
brainstorm → plan → TDD → debug → review
不綁任何業務 context
只是把「軟體工程師該做什麼」結構化
裝完之後 AI 會記得這些步驟
gstack 解決「我沒有團隊」
Superpowers 解決「AI 跳過該做的步驟」
兩個層次不衝突
我同時裝
gstack 跑流程、Superpowers 守紀律

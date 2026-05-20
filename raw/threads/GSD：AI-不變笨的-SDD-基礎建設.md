---
url: "https://www.threads.com/@ci.fullstack/post/DYKb48qHf4z"
author: "@ci.fullstack"
clip_type: "Claude Code"
---

昨晚講 Superpowers 的紀律層
今晚講 GSD 的基礎建設層
gsd-build/get-shit-done 61k stars
TÂCHES 5 個月寫的
4 天一個 minor release
它解的不是「AI 該做什麼」
是「AI 用滿 context 就笨」這個物理上限
GSD 把品質衰退量化 4 段：
PEAK 0-30% → GOOD 30-50% → DEGRADING 50-70% → POOR 70%+
整套設計就是把 main session 鎖在 50% 以下
fresh subagent context per task
orchestrator 限 10-15%
規模 66 commands / 33 agents / 90 workflows
老實說我研究完才理解
GSD 不是工具
是 SDD 的基礎建設
下面展開衰退表、6 phase、跟 Superpowers 怎麼互補
你 Claude session 跑到一半變笨過嗎？

GSD 6 phase 一條龍：
/gsd-new-project
建 PROJECT md / REQUIREMENTS md / ROADMAP md / STATE md
進入 .planning/ 把 state 外化
/gsd-discuss-phase
找 gray area 鎖決策
寫進 CONTEXT md
讓後面的 planner 不用重問
/gsd-plan-phase
研究 → 規劃 → 驗證循環
產 PLAN md
XML 結構 task + accept_criteria
/gsd-execute-phase
Wave 並行
每個 task 用 git worktree 隔離
fresh 200K context per task
/gsd-verify-work
4 層驗證：existence → content → integration → functionality
含 stub 偵測
/gsd-ship
自動生成 PR description

Claude 品質衰退 4 tier（GSD 把它寫死）：
PEAK 0-30%
全速、能讀 body、能 spawn 多 agent
GOOD 30-50%
正常、優先 frontmatter、開始 delegate
DEGRADING 50-70%
省著用、只讀 frontmatter、警告 user
POOR 70%+
緊急、立刻 checkpoint
不再讀新檔案
衰退預警三訊號（早於 panic 閾值）：
- silent partial completion 看起來做完其實沒做完
- increasing vagueness 開始講「適當處理」而不是具體 code
- skipped steps 該做 8 步只做 5 步
orchestrator 5 條鐵則：
不讀 agent 定義、不 inline 大檔、delegate 重活、主動警告 budget、按 context window 縮放讀深

GSD 跟 Superpowers 不同層次：
Superpowers
紀律層 — 5 stage（Brainstorm/Plan/TDD/Debug/Review）
解的是「AI 跳過該做的步驟」
14 個 skill auto-trigger
GSD
基礎建設層 — phase 切分 + fresh subagent context
解的是「AI 用滿 context 就笨」物理上限
.planning/ 把 state 外化
66 commands 形成 SDD lifecycle
兩個正交不衝突
Superpowers 管 AI 的「行為紀律」
GSD 管 AI 的「工作環境」
我兩個都裝
再配 RalphLoop
就是 5/8 那篇講的「一夜 100+ session」組合

感謝推薦耶～
這類之前寫過 Graphify 跟 Code-Review-Graph
我習慣跑過再寫，這個我研究完可以發一篇～

沒問題～有任何想法也歡迎交流～

謝謝

.planning 放 root 可以，但 6-phase 偏 single-project 思維
我沒在 monorepo 實測過，不敢打包票
單一 package 的開發倒是沒問題

subagent 不是重點
GSD 是每個任務都開 fresh context，跑 wave 並行，才比較燒
它有給 --wave 分批、--interactive 不開並行，可以控
我自己覺得多花 token 換後面不變笨，還算划算

---
url: "https://www.threads.com/@andrew54068/post/DXuJ1pGmux7"
author: "@andrew54068"
clip_type: "Claude Code"
---

Day 119 你的 Claude Code 每次對話都在偷吃 context。
不是 API 費用——是那些掛 global 的 skill。
skill 如果全掛 global，每次對話都得付稅。
就算 90% 的 skill 跟當下任務無關。
或者你同時在用 Claude Code 和 Codex，想讓兩邊共用同一套 skill。
我在 Day 117 提到用 /skills-manager 解這個問題。
今天把它開源到 GitHub，兩條指令就能裝。
Translate
58
7
9
97
andrew54068
ClaudeCode
04/29/26
·
Author
【安裝（兩條指令）】
在 Claude Code 輸入：
/plugin marketplace add github.com/andre…
/plugin install skills-manager@andrew54068
裝完在任何專案輸入 /skills-manager。
會跳出互動選單，勾選哪些 skill 要在這個專案啟用。
裝完外掛還不夠——要讓 AI 自動走這套流程，得加一條 rule。
Claude Code：在 ~/.claude/CLAUDE.md 加一段 Skills Management。
Codex：同樣的內容貼到 ~/.codex/AGENTS.md。
Codex 不讀 rules/*.md，AGENTS.md 是唯一入口。
github.com
GitHub - andrew54068/claude-plugins
2
1
3
andrew54068
ClaudeCode
04/29/26
·
Author
【為什麼 bullpen 放在 ~/.agents 而不是 ~/.claude？】
兩個工具讀的入口不同：
Claude Code 只讀 ~/.claude/skills/
Codex 讀 ~/.agents/skills/
要讓一個 skill 在兩邊都 global，得在兩個入口各建一條 symlink，都指回 bullpen 裡同一份真檔。
toggle-global.sh <skill> on 一次建好兩條，不用手動。
我測過：只建 ~/.agents/skills/ 的 symlink，~/.claude/skills/ 沒建。
Claude Code 看不到那個 skill。
兩條都要建，缺一不可。
寫一次（在 bullpen），兩邊都吃得到。
Translate
toggle-global.sh
toggle-global.sh
2
1
andrew54068
ClaudeCode
04/29/26
·
Author
【你會拿到什麼？】
/skills-manager 背後是 11 支 bash script，常用的：
state.sh <project> — JSON 快照，列出所有可用、已啟用的 skill
browse.sh — fzf（終端機互動選單工具）介面，空白鍵切換、enter 存檔
reconcile.sh [--fix] — 檢查（或修復）.globals 跟 symlink 的 drift
toggle-global.sh on|off — 一鍵把某個 skill 升降為 global
migrate.sh — 第一次跑，把舊 skill 全部搬進 bullpen
Translate
migrate.sh
migrate.sh
1
1
andrew54068
ClaudeCode
04/29/26
·
Author
【第一次跑的小坑】
第一次執行會偵測到 bullpen 不存在，提示你跑 migrate.sh，它會：
1. 把 ~/.claude/skills/ 的真資料夾搬進 bullpen
2. 已是 symlink 的維持原樣
3. 掃 settings.json hooks，自動把被 hook 引用的 skill 標為 global
4. 在兩邊建好 global symlink
過程備份舊的 settings.json 為 .bak，遇到問題可以還原。
Translate
1
1
1
andrew54068
ClaudeCode
04/29/26
·
Author
【filesystem as state】
整套設計沒有 daemon、IPC、SQLite。
不會壞——根本沒有東西會壞。
用 ls -la 就能看到當下狀態。
換機器：rsync 整個 bullpen 目錄過去就好。
skills-manager 壞了，你的 skill 都還在 bullpen。
跨工具共享 skill 的痛點，你遇過嗎？留言聊聊。
想知道需求從哪來？翻前一篇：Day 117
GitHub: github.com/andre…
Translate
github.com
GitHub - andrew54068/claude-plugins
1

---
網址: https://www.threads.com/@andrew54068/post/DXmUXSbGnA6
作者: ["@andrew54068"]
tags: []
status: wiki
---

## Main Content

Day 116 把 Claude Code 的 ralph-loop 移植到 Codex，一開始就卡關了
上一篇寫了 Claude Code 的 ralph-loop 為什麼能自動跑。
靠 plugin 系統在啟動時讀 hooks/hooks.json，把 Stop hook 合進記憶體。
Codex 沒有這個機制。
Plugin hook 不會自動載入。
ralph-loop 沒辦法直接複製過去。
所以我得自己選路線——而且有兩條路線差很多。
Translate
5
7
2
4
andrew54068
ClaudeCode
04/26/26
·
Author
【路線 A：自製 Stop hook（project-local）】
最快讓 loop 跑起來的方式。
用 codex_ralph.py 在專案目錄裡裝一個 Stop hook，之後由 Codex 自己觸發。
指令長這樣：
python3 ~/.agents/skills-bullpen/codex-ralph-loop/scripts/codex_ralph.py start \
--project . \
--prompt-file .codex/ralph-prompt.md \
--max-iterations 50 \
--completion-promise TASK_COMPLETE
Translate
codex_ralph.py
codex_ralph.py
1
1
andrew54068
ClaudeCode
04/26/26
·
Author
跑完會在專案裡產生五個關鍵檔案：
.codex/hooks.json → 把 Stop hook 註冊進去
.codex/hooks/codex_ralph_stop.py → hook 本體
.codex/ralph-loop.local.json → loop 狀態（on/off 開關）
.codex/ralph-prompt.md → 每次重新注入的 prompt
.codex/ralph-loop.last.json → loop 結束後才產生，記錄最終結果
Translate
1
1
andrew54068
ClaudeCode
04/26/26
·
Author
【Stop hook 的判斷邏輯】
每次 Codex 想結束，hook 就跑一次：
1. 找不到 ralph-loop.local.json → exit 0，放行
2. 找到了 → 看最後一則 assistant message 有沒有 <promise>TASK_COMPLETE</promise>
3. 有 → 停止，把結果寫進 ralph-loop.last.json，刪掉 state 檔案
4. 沒有但已達 max_iterations → 同上停止
5. 都不是 → 回傳 decision:"block"，Codex 繼續跑
Codex 接到 decision: "block" 就把 reason 當新的 user message 重新注入。
行為和 Claude Code 的 ralph-loop 完全一樣。
Translate
1
1
andrew54068
ClaudeCode
04/26/26
·
Author
【on/off 開關】
State 檔案 = 開關。
start → 建立 ralph-loop.local.json → loop ON
completion promise → 刪掉 state 檔案 → loop OFF
cancel → python3 codex_ralph.py cancel → 刪掉 state 檔案 → loop OFF
想臨時做一件跟 loop 無關的事？
刪掉 ralph-loop.local.json，做完再重建。
這比 Claude Code 的版本更透明——狀態就是一個 JSON 檔案。
隨時可以打開看當前 iteration 和 prompt。
Translate
codex_ralph.py
codex_ralph.py
1
1
andrew54068
ClaudeCode
04/26/26
·
Author
【路線 B：CodexPotter】
完全不同的方向。
CodexPotter 是一個獨立的 Rust binary。
不靠 Stop hook，而是直接包住 codex app-server protocol（Codex 的內部通訊介面），從外部驅動 Codex。
npm install -g codex-potter
codex-potter --yolo # 自動確認所有操作
它的核心設計是"round"概念：每個 round 是一個全新的 Codex session，刻意不共享上下文。
"every follow up prompt turns into a new task, not sharing previous contexts"
這是故意的——目的是避免 context poisoning。
長任務跑下去，早期的錯誤決策會一直污染後面的輸出。
Translate
1
1
andrew54068
ClaudeCode
04/26/26
·
Author
每個 round 結束後，靠 MAIN.md 做跨 round 記憶。
Codex 每次啟動都去讀這份 MAIN.md，知道目前做到哪、下一步做什麼。
停止方式：agent 認為任務完成時，自動在 MAIN.md 的 front matter 寫入 finite_incantatem: true。
或用 --rounds 限制執行輪數。
【兩條路線的核心差異】
自製 Stop hook：hook 攔截同一 session，context 持續累積，靠 prompt 檔案記憶。
CodexPotter：外部 process 包 app-server，每 round 重置 context，靠 MAIN.md 記憶。
選哪條的簡單原則：
重視結果 → CodexPotter（每 round 清空，不怕 context 累積壞掉）
擔心資安 → 自製 Stop hook（不裝全域 binary，不碰 app-server protocol）
Translate
main.md
main.md
1
1
andrew54068
ClaudeCode
04/26/26
·
Author
這是踩坑系列第二篇。
第一篇（Day 115）搞清楚 Claude Code 的 hook 機制，第二篇選定 Codex 路線。
下一個坑：Claude Code 的 rules 系統在 Codex 裡沒有完整對應物。
AGENTS.md 能做到什麼、做不到什麼，繼續寫。
你現在用 Codex 跑 agent loop 嗎？或是還在 Claude Code？
兩條路線你會選哪條，留言聊聊
CodexPotter 原始碼：github.com/breez…
Translate
agents.md
agents.md
1

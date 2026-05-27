---
網址: https://www.threads.com/@ai.tech.share/post/DYUy8GeE2e4
作者: ["@ai.tech.share"]
tags: [Claude Code]
status: wiki
---

## Main Content

Agent View 就像幫 Claude Code 加了一個機場塔台。
🛬 進主題之前先補位
・Claude Code 是 Anthropic 出的 AI 寫程式工具，跑在終端機裡。
・一個 session 就是一段對話、一個任務，跟在 ChatGPT 開一個新對話的概念差不多。
・「背景跑」就是任務交給電腦自己做，你不用盯著螢幕。
老手請快轉，下一段才是主菜。
💡 是什麼
Agent View 是 Claude Code 從昨天（2026/5/11）開始多出來的一張表格。把所有在背景跑的 session 收進一個畫面：每一列一個 session，狀態（在做事、卡住等你回、做完、失敗、停了）一目了然，按一個鍵就能切進去看完整對話、再按一個鍵切回來。
在終端機輸入 claude agents 就會打開，需要 Claude Code v2.1.139 以上。
🛠 怎麼用
並行跑多個任務：開一個讓 Claude Code 修 bug、另一個寫測試、第三個 review PR，全部背景跑，一張表追蹤。

長時間任務：機器睡了會停，但醒來輸入 claude respawn --all 可以全部喚回。
寫檔自動隔離：每個背景 session 自動進一個獨立的 git worktree（路徑：.claude/worktrees/ 底下），多任務並行不會撞檔。這條我覺得是這次最低調但實用的設計。
開了 PR 直接顯示連結與 CI 狀態，等於把「review PR」這個動作也收進總控台。
🧪 跟誰像
如果你用過 tmux 或 VS Code 多終端，Agent View 取代的是「自己排版多視窗」這層工作——但它比 tmux 多了一層 AI session 的狀態語意（誰要回應、誰開了 PR），不只是版面分割輔助。
跟 OpenAI 同期推的 Codex Desktop 並行控制中心思路類似，但 Codex 走桌面 GUI、Anthropic 走 CLI。這是兩種對「開發者人在哪」的不同假設。
🎯 我的第一印象（觀點）
最有意思的不是表格本身，是它讓 Claude Code 的 session 第一次能在背景活著：不綁 terminal、自動進 worktree、CI 狀態回顯。

這比 UI 更像一個「agent 平台」的雛型。
它目前仍是 Research Preview，企業 admin 也能一個設定（disableAgentView）關掉，還沒到「預設體驗」那層。我會先拿它跑 2–3 個並行的小任務試水溫，再決定要不要把日常開發整個搬上去。
順帶提醒：每個背景 session 各自吃 quota，跑 10 個 ≈ 10 倍消耗，這是要記住的成本。
🗳 一個提問
你會把哪幾種任務丟到背景跑？留言告訴我，我下一篇來做一個「適合背景化的 AI 任務清單」。
💡 ai.tech.share｜不會讓你看不懂的 AI 技術頻道
#ClaudeCode #AgentView #Anthropic #AICoding #開發者工具

## Sources

- [Claude Code Agent View：你的 AI 程式碼塔台](https://www.threads.com/@ai.tech.share/post/DYUy8GeE2e4) | 作者: ai.tech.share

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

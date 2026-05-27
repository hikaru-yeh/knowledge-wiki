---
網址: https://www.threads.com/@hei_ai.automation/post/DYLxTGaEVXd
作者: ["@hei_ai.automation"]
tags: []
status: wiki
---

## Main Content

Harness Engineering 是什麼？感覺好像很複雜？
但其實如果你寫過 CLAUDE md、裝過 skills、加過 hooks，你做的東西已經是 Harness Engineering 了
簡單說：AI 大語言模型本身以外的一切 — 規則、skills、hooks、MCP servers、記憶系統、回饋迴圈 — 加起來就是你的 harness
只是之前沒人幫這部分工作命名
Mitchell Hashimoto 2026 年 2 月提出公式：Agent = Model + Harness
Harness Engineering 就是設計、實施、維護這套 AI agent 周邊系統的工程紀律

怎麼用？比你想的簡單
第一，audit 你現有的 harness — 打開 ~/.claude 目錄，列 CLAUDE.md、skills、hooks、settings.json，這就是你已經有的雛形
第二，CLAUDE md 寫規則 — Addy Osmani 建議短於 60 行，當作 pilot 的 checklist，重複出現的失敗就成為新規則
第三，skills 寫重複任務 — 放 ~/.claude/skills/ 讓 AI 自動觸發
第四，hooks 寫機械化攔截 — PreToolUse 階段 grep 違規。口頭規則加 AI 自審永遠靠不住，hook 才是強制執行
需要連外部工具？再加 MCP servers
設定一次，永久執行

為什麼這個很值得學？
每個人用的 LLM 都一樣 — GPT-5.5、Claude Opus、Gemini，公開接 API 任何人用得到
那真正拉開差距的，就是你的 harness
如果你只用模型，輸出就跟所有人差不多
如果你有 harness，輸出就是你獨家的
對你來說
個人 — harness 是你可累積、模型升級也不貶值的資產
AI agency — harness 是你向客戶收費的可見資產，是客戶留存的護城河
公司 — 每間用 AI 的公司都需要精通 harness，控制 AI 輸出的可預測性
2026 年的 AI 不是比誰用更強模型，是比誰把模型周邊設計成不可能犯同一個錯的系統

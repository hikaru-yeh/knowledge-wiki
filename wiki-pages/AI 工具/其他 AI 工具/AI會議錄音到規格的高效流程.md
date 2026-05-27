---
網址: https://www.threads.com/@poopoo_stitch/post/DX55VOSCbRF
作者: ["@poopoo_stitch"]
tags: []
status: wiki
---

## Main Content

分享個上週我實測過，覺得蠻讚的工作流程！
這套流程主要是這樣串的：
會議錄音 ➡️ NotebookLM ➡️ notebooklm-mcp-cli ➡️ 任何 AI Agent (Codex/Gemini CLI 等) ➡️ Spectra
（下方 NotebookLM 簡稱 nlm）
前置準備
1. 安裝 Spectra App 與操作的 agent skills。
2. 安裝 notebooklm-mcp-cli 這個套件，與操作的 agent skills。
3. 用 nlm login 登入自己的帳號，它可以分開設定工作與個人環境：
• nlm login --profile work
• nlm login --profile personal
這樣工具就都安裝完成了，後續就可以直接用自然語言呼叫 nlm 跟產出 spec 文件！
具體操作流程
1. 錄音轉文字： 開完會後，把錄音檔丟到 NotebookLM 去產生逐字稿。
2. 白嫖運算力整理重點： 在本機上使用 Codex 或 Gemini CLI 等 AI 工具，叫它去 nlm 上面找那一份筆記，並請它節錄會議重點。

(💡 這邊是最讚的地方：整理幾萬字會議的 Token 消耗會全部算在 nlm 上，完全不會吃掉你本機 AI 工具的額度！而且還可以直接透過 CLI 呼叫 nlm 幫你製作簡報或影片並下載下來。)
3. 產出初步規格： 拿到會議記錄後，繼續用 AI 工具呼叫 Spectra 的 skills，讓它根據剛剛的重點，生出初步的 Spec 規格文件或是待辦事項。
4. 人工確認與開發： 等文件生出來後，我們再稍微人工看一下 Spec 規劃有沒有問題或需要調整的地方。確認沒問題，就可以直接跟 AI 說：「根據這份 Spec 去做後續的程式開發吧！」
相關連結
• NotebookLM MCP CLI: github.com/jacob…
• Spectra: spectra.5xcamp.us
spectra.5xcamp.us
Spectra — Spec-Driven Development

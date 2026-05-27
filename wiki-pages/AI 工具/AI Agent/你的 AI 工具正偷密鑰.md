---
網址: https://www.threads.com/@buildthink.ai/post/DXEe-fKj4nq
作者: ["@buildthink.ai"]
status: wiki
---

# 你的 AI 工具正偷密鑰？三步自保

**LiteLLM 後門事件（2026/03）：**  
LiteLLM（340 萬次下載的 Python 套件）被駭客植入後門。安裝者的 SSH 鑰、雲端憑證、.env 檔案、加密錢包全部被盜取。更可怕的是：有人從未安裝 LiteLLM，只是使用了一個 Cursor MCP plugin，就被自動引入而中招。

**MCP 工具的系統性風險：**  
MCP 協議本身不包含身份驗證，第三方 server 可以在工具描述中隱藏指令，AI agent 讀取後會靜默執行。

**三步今天做：**
1. 檢查確認沒有 LiteLLM 1.82.7 / 1.82.8
2. 列出所有 MCP server，閉源或來歷不明的立即停用
3. 每個工具使用獨立 API Key，在 console 設定 daily spending cap

使用的 AI 工具越強大，攻擊面就越大。

## Cross References

- [[MCP 工具]]: MCP 工具清單與安全使用原則
- [[AI 多模型協作審碼抓漏]]: 多模型協作與審碼


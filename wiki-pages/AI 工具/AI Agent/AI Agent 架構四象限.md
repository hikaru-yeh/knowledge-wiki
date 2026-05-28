---
網址: https://www.threads.com/@ainotes0313/post/DYRkRCWidl9
作者: ["@ainotes0313"]
tags: [AI]
status: wiki
---

## Main Content

一個 AI 功能，應該被設計成哪種類型的 Agent 架構？
最近看到一個新詞彙Harness Engineering
參考大神文章畫了這張圖 可以當作問題的答案

AI 架構可以用兩個維度來理解：
1️⃣ Context Correlation（上下文關聯性）
簡單說：
這個任務需不需要理解前面的對話？
低：
查資料
單次任務
不需要記憶聊天
高：
長對話
多步驟 workflow
要理解使用者目前狀態
2️⃣ Context Impact（上下文影響性）
簡單說：
這個任務結果，會不會改變後續流程？
低：
輔助功能
小工具
不影響主流程
高：
決定下一步
改變 workflow
影響整個 agent 行為
然後就能分成四種類型👇
🟦 RAG
（低關聯、低影響）
本質：
AI 查資料
適合：
文件 QA
FAQ
PDF 搜尋
API文件問答
AI 去文件找答案即可。
這類不需要複雜 agent。
🟦 Agent Skill
（高關聯、低影響）
本質：
Agent 的小技能
需要理解聊天上下文，
但不改變整個流程。
例如：
幫你整理會議
根據前文翻譯
改寫 email
自動摘要
像 function/tool 的概念。

🟦 Sub-agent
（低關聯、高影響）
本質：
專業工具人 agent
不太需要聊天上下文，
但負責重要專業任務。
例如：
Data analysis agent
Graph generation agent
收到任務後專心執行。
結果會影響後續流程。
🟦 Recursive Orchestrator
（高關聯、高影響）
最核心的大腦。
本質：
AI 總指揮 / PM
負責：
拆解任務
分配 agent
管理 workflow
根據結果調整策略

一句話總結：
🟦 RAG = 查資料
🟦 Skill = 小功能
🟦 Sub-agent = 專家工具人
🟦 Orchestrator = AI 總指揮

## 圖片文字

### 圖片 1

Agent Architecture Decision Matrix

Y 軸：Context Impact

Does the task result change the overall flow?

- High：上方
- Low：下方

X 軸：Context Correlation

Does the task need to understand previous dialogue?

- Low：左側
- High：右側

四象限：

- 左上：Sub-agent（High Context Impact / Low Context Correlation）
- 右上：Recursive Orchestrator（High Context Impact / High Context Correlation）
- 左下：RAG（Low Context Impact / Low Context Correlation）
- 右下：Agent Skill（Low Context Impact / High Context Correlation）

## Sources

- [AI Agent 架構四象限](https://www.threads.com/@ainotes0313/post/DYRkRCWidl9) | 作者: ainotes0313

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

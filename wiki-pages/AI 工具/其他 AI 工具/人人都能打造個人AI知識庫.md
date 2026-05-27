---
網址: https://www.threads.com/@a65041230/post/DYT7kyxgbTQ
作者: ["@a65041230"]
tags: [AI]
status: wiki
---

## Main Content

AI Threads
05/14/26
其實現在人人都能建立自己的小型 AI 資料庫。
很多人平常用 AI，最怕的不是不會用
這邊整理了一下區別
現在越來越多人開始建立：
自己的小型知識庫、文件搜尋、AI 工作流，SQLite 就能做到很多事，最有趣的是，它其實能變成你專業領域的小助手，舉例
業務 — 可以直接搜尋客戶歷史對話、報價單
設計師 —可以搜尋以前的提案與素材
工程師 —可以搜尋自己的技術筆記、API 文件
律師 —可以搜尋過往案例與合約內容
搭配N8n、Codex、Python、OpenAI API
它完全能變成自己的 AI 記憶庫。
例如：
Email→ 自動抓取更新 SQLite
PDF 報告→ 自動抓取整理進知識庫
Google 表單→ 自動抓取寫入客戶資料
甚至還能：
✔ 自動搜尋歷史資料✔ 查詢文件✔ 幫你填表✔ 整理客戶資訊✔ 建立個人工作流
很多個人 AI 系統，現在其實就是這樣運作的
一般人工作者，都能建立自己的
AI 筆記庫、PDF 搜尋、個人知識庫。
SQLite、Vector DB、PostgreSQL
其實是不同角色
不是誰取代誰

我整理了一張比較好懂的圖卡，
讓像我一樣剛開始很混亂的人，
能快速知道自己適合哪種架構。
一起往AI領域學習
有需要更詳細的實作流程圖卡的留言
「圖卡 」發給你

## 圖片文字

OCR 摘要：這張圖卡示範如何用 SQLite 搭配 `sqlite-vss`、OpenAI embedding 與 LLM，建立一個可查詢本地文件的個人 AI 知識庫 / RAG 系統。

- 環境需求包含 Python 3.10+，以及 `sqlite3-vss`、`openai`、`tiktoken` 等套件。
- 專案會建立 `my_knowledge` 資料夾與 `knowledge.db`，用 SQLite 作為本地知識庫資料庫。
- 透過 `sqlite-vss` 擴充 SQLite 的向量搜尋能力，讓本地資料庫能做語義檢索。
- 文件處理支援 PDF 與 TXT；若是掃描檔，需先經 OCR 轉成文字。
- `embed.py` 會把文件切成約 1000 字元的 chunks，並用 OpenAI `text-embedding-3-small` 產生 embedding；預算足夠可改用 `text-embedding-3-large`。
- `search.py` 會把使用者問題轉成向量，透過 `sqlite-vss` 從 `knowledge.db` 搜尋最相關的 `top_k` 片段。
- 檢索結果會交給 LLM，例如 `gpt-4o-mini`，由模型根據上下文回答；若上下文不足，應回覆不知道或要求更多資料。
- 整體流程是「文件匯入 → 切塊與 embedding → SQLite 向量檢索 → LLM 根據檢索內容回答」，適合建立個人 AI 筆記庫、PDF 搜尋或小型知識庫。

## Sources

- [人人都能打造個人AI知識庫](https://www.threads.com/@a65041230/post/DYT7kyxgbTQ) | 作者: a65041230

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

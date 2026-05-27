---
網址: https://www.threads.com/@_surendar._5/post/DXMQ1zGFF29
作者: ["@_surendar._5"]
tags: []
status: wiki
---

## Main Content

這頁原本只是 Threads 貼文中提到「有人把 AI 課程免費放到 GitHub」的短句，實質內容在 GitHub repo：

- GitHub: <https://github.com/rohitg00/ai-engineering-from-scratch>

`rohitg00/ai-engineering-from-scratch` 是一套開源 AI Engineering 課程，定位不是「快速學會呼叫 API」，而是從底層一路做到可交付的 AI 系統。README 說明課程包含 20 個 phase、435 lessons，估計約 320 小時，語言涵蓋 Python、TypeScript、Rust、Julia；每課都會產出可重用 artifact，例如 prompt、skill、agent 或 MCP server。

## 適合誰

適合想補 AI 工程底層的人，尤其是：

- 會寫程式，但想系統補 ML / Deep Learning / LLM 基礎。
- 已會使用 ChatGPT、Claude、Codex 等工具，但想理解 tokenizer、attention、RAG、agent loop 背後怎麼運作。
- 想做作品集，而不是只看影片或照抄 notebook。
- 想把 Claude / Codex 變成學習助教，逐課檢查理解、補練習、做小專案。

不太適合只想快速上手某個 SaaS 工具、只想拿 prompt 範本，或完全不想寫程式的人。

## 主要學習模組

課程以 20 個 phase 串成一條路線：

| 區段 | 內容 |
|---|---|
| Phase 0-3 | 開發環境、數學基礎、傳統 ML、Deep Learning core |
| Phase 4-6 | Computer Vision、NLP、Speech / Audio |
| Phase 7-10 | Transformers、Generative AI、RL、LLM from scratch |
| Phase 11-12 | LLM Engineering、Multimodal AI |
| Phase 13-14 | Tools / Protocols、MCP、Function Calling、Agent Engineering |
| Phase 15-16 | Long-horizon agents、self-improvement、multi-agent / swarms |
| Phase 17-18 | Infrastructure / Production、Ethics / Safety / Alignment |
| Phase 19 | 17 個 capstone projects，例如 coding agent、codebase RAG、production RAG chatbot、MCP server、multi-agent software engineering team |

README 也提供依背景選起點的建議：新手從 Phase 0；會 Python 但不熟 ML 從 Phase 1；熟 deep learning、想補 LLM 和 agent 可從 Phase 10；資深工程師若只想補 agent engineering，可從 Phase 14。

## 與付費課程相比的價值

這個 repo 的價值不在「免費」本身，而在它把 AI Engineering 拆成可追蹤的長課綱：

- **路線完整**：從 linear algebra、optimization、model evaluation 到 LLM、RAG、MCP、agent、production，不只教最新名詞。
- **偏實作**：課程設計強調先用原始數學和 code 建出小版本，再理解 PyTorch / sklearn 等框架在做什麼。
- **產出導向**：每課保留 artifact，最後可以累積 prompts、skills、agents、MCP servers，而不是只留下筆記。
- **可被 AI coding 工具輔助**：repo 內含可安裝到 Claude、Cursor、Codex、OpenClaw、Hermes 等工具的 skills / prompts，適合搭配 agent 做自學路線。

相對地，付費課程可能有老師答疑、社群、作業批改、更新承諾與學習節奏管理；這個 repo 比較像一份公開、龐大、偏工程師自學的 reference curriculum。

## 使用建議

1. 先打開 repo README 或網站版，依自己的背景選起點，不要從 Phase 0 硬啃到 Phase 19。
2. 每個 phase 先看 lesson list，挑一個能跑的 lesson，確認 `docs/en.md`、`code/`、`outputs/` 三件事都有對應。
3. 用 Claude / Codex 當助教，而不是代寫答案：
   - 請它先解釋該 lesson 的核心概念。
   - 自己先跑一次 repo 裡的 code。
   - 讓 Claude / Codex 出 3 個變體練習。
   - 把錯誤訊息貼回去，要求它只提示方向，不直接給完整答案。
4. 對 LLM / Agent 有經驗的人，可以優先看 Phase 10-14：LLM from scratch、LLM Engineering、MCP、tool use、agent loop、memory、planning、LangGraph、OpenAI / Claude Agent SDK 等。
5. 若目標是作品集，可直接挑 Phase 19 capstone project，把 repo 的專案題目改造成自己的小型可部署作品。

## 限制與注意事項

- 課程很長，約 320 小時，不適合當成週末速成包。
- lesson 數量多，品質與完成度可能不均；使用前要檢查目標 lesson 是否已有 docs、code、outputs。
- 有些 lesson 涉及 GPU、雲端、API key 或外部套件，實作成本不一定為零。
- repo 的 stars 與 lesson 數不代表每一課都已經穩定、最新或適合初學者。
- 若只是想學「如何用某個 AI 工具完成工作」，這份課綱可能太底層；若想理解 AI 工程本身，才比較值得投入。

## Sources

- Threads source: <https://www.threads.com/@_surendar._5/post/DXMQ1zGFF29>
- GitHub repo: <https://github.com/rohitg00/ai-engineering-from-scratch>

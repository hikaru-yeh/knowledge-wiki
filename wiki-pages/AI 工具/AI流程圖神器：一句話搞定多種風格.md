---
網址: https://www.threads.com/@software_ai_life/post/DYPDhiKmRju
作者: ["@software_ai_life"]
tags: []
status: reference
---

## 概述

fireworks-tech-graph 是 AI agent 技能，用自然語言描述即可產出 SVG + PNG 技術架構圖。支援 7 種視覺風格、14 種 UML 圖、40+ 技術 icon。

- 7.1k stars / MIT 授權
- 輸出：SVG（可編輯向量）+ PNG（1920px 高解析度）
- 支援中英文自然語言輸入

## 7 種視覺風格

| # | 風格 | 背景 | 適用場景 |
|---|------|------|----------|
| 1 | Flat Icon | 白 (#ffffff) | 部落格、投影片、文件 |
| 2 | Dark Terminal | 暗 (#0f0f1a) | GitHub README、開發文章 |
| 3 | Blueprint | 深藍 (#0a1628) | 架構文件、工程文件 |
| 4 | Notion Clean | 白 (#ffffff) | Notion、Confluence、wiki |
| 5 | Glassmorphism | 暗漸層 (#0d1117) | 產品官網、keynote |
| 6 | Claude Official | 暖米 (#f8f6f3) | Anthropic 風格圖表 |
| 7 | OpenAI Official | 純白 (#ffffff) | OpenAI 風格現代圖 |

## 14 種 UML 圖

Class / Component / Deployment / Package / Composite Structure / Object / Use Case / Activity / State Machine / Sequence / Communication / Timing / Interaction Overview / ER Diagram

## AI/Agent 領域內建模式

- RAG Pipeline & Agentic RAG
- Agentic Search
- Mem0 記憶層架構
- Agent 記憶類型（Sensory / Working / Episodic / Semantic / Procedural）
- Multi-Agent 編排
- Tool Call 執行流程

## 語意圖形詞彙

| 元素 | 圖形 |
|------|------|
| User/Human | 圓形 + 身體 |
| LLM/Model | 圓角矩形 + 雙邊框 |
| Agent | 六角形 |
| 短期記憶 | 虛線圓柱 |
| 長期記憶 | 實線圓柱 |
| Vector Store | 環狀圓柱 |
| Tool/Function | 矩形 + 齒輪 icon |
| Decision | 菱形 |

## 箭頭語意

| 流程類型 | 線型 |
|----------|------|
| 主要資料流 | 實線 2px |
| 控制/觸發 | 實線 1.5px |
| 記憶讀取 | 實線 |
| 記憶寫入 | 虛線 (5,3) |
| 非同步/事件 | 虛線 (4,2) |

## 產品 Icon 庫（40+）

- **AI/ML**：OpenAI、Anthropic、Gemini、LLaMA、Mistral、Cohere
- **框架**：Mem0、LangChain、LlamaIndex、LangGraph
- **向量 DB**：Pinecone、Weaviate、Qdrant、Chroma、Milvus
- **資料庫**：PostgreSQL、MongoDB、Redis、Neo4j
- **雲端**：AWS、GCP、Azure、Kubernetes、Docker
- **監控**：Grafana、Prometheus、Datadog

## 安裝

```bash
npx skills add yizhiyanhua-ai/fireworks-tech-graph
```

PNG 渲染器（擇一）：
- `pip install cairosvg`（推薦）
- `rsvg-convert`（系統套件，較輕量）
- Puppeteer（Node，最高保真度）

## 使用範例

觸發語句會自動啟動：

- "Draw a RAG pipeline flowchart"
- "Generate an Agentic Search architecture diagram"
- "Create a Mem0 architecture diagram, dark style"
- "畫一個多 Agent 協作架構圖"

## Sources

- GitHub repo：https://github.com/yizhiyanhua-ai/fireworks-tech-graph

---
網址: https://www.threads.com/@oneday0013/post/DYReUhdkvrU
作者: ["@oneday0013"]
tags: [Claude Code, AI Agent, Harness, 技術債, 架構]
status: wiki
source_blog: https://leehanchung.github.io/blogs/2026/05/08/hidden-technical-debt-agent-harness/
---

## 什麼是 Agent Harness？

Harness 是模型與執行環境之間的協調層，相當於 AI 的作業系統。組成元件：

- System prompt 與行為指令
- 工具集與可呼叫函式
- Rollout 協定（單輪 / 多輪 / ReAct loop）
- Context 管理與記憶層
- Sub-agent 拓撲與編排
- Guardrails、gates、驗證器
- 可觀測性與追蹤基礎設施

## 為何 Harness 會變成技術債

核心問題：「幾乎所有 harness 都會在下一代模型出來時溶解掉。」把 harness 當作永久產品表面，下次模型升級就要大規模重寫。

**Bitter Lesson 在 Agent 領域重演：**
- 2023：Harness 抓著整個記憶層（RAG）
- 2024：tool calling 不穩，寫一堆編排邏輯
- 2025+：模型內部整合推理、工具、反思，外部腳手架變成多餘負擔

## 正在溶解的元件

| 元件 | 被什麼取代 |
|------|------|
| n8n 這類 no-code 工作流 | 單一長壽 agent |
| 工具 wrapper | 模型直接讀 OpenAPI spec |
| Planner-executor 分離 | 模型內部交錯規劃與執行 |
| 向量記憶層 | 純文字 `progress.md` + git log |
| 複雜多 Agent 拓撲 | 單一模型處理複雜任務 |

## Thin Harness, Fat Skills 原則

**口訣：Harness 越薄越好、隨時能拔；領域知識放到 Skill 與 Prompt 層。**

- 設計目標：**90 天內可丟**，不要當永久產品在打造
- Skill 層迭代成本低（文字編輯），Harness 層迭代成本高（release）
- 犧牲小幅 benchmark 分數，換取更強的泛化能力與可維護性

## 訓練 Harness vs 生產 Harness

**這兩者應該是不同的東西：**

| 維度 | 訓練 Harness | 生產 Harness |
|------|------|------|
| Action space | 最大化（探索可能性） | 最小化（明確 allowlist） |
| 失敗 | 歡迎，是優化器信號 | 用 retry 邏輯壓制 |
| Guardrails | KL caps、curriculum gates | RBAC、審批分層、過濾器 |
| 網路 | 離線 / 記錄環境 | 嚴格 egress 政策的正式環境 |

## 實證：Harness 差距有多大

同樣跑 Opus 4.5：
- **Letta Code**（第三方，記憶層做得好）：**59.1%**
- **Claude Code**（官方）：**41.6%**
- 差距：**17.5 個百分點**

→ 即使第一方有先天優勢，第三方 Harness 若在關鍵軸線上投資更深，依然可以超越。

## 設計建議

1. **設計可移除性**：每個 harness 元件都應能在數小時而非數週內刪除
2. **分離關切點**：訓練、評估、生產三個 harness 各自獨立
3. **預設淘汰**：把 harness 當成每次模型發布前的 90 天臨時設施
4. **投資耐久底層**：訓練資料、評估框架、執行環境——這些比 harness 實作更持久

## Sources

- [leehanchung.github.io 博客](https://leehanchung.github.io/blogs/2026/05/08/hidden-technical-debt-agent-harness/) | 作者: Lee Han Chung

## Cross References

- [[AI Agent 效能關鍵：Harness Engineering]]：Harness Engineering 更廣泛討論
- [[Skill 設計]]：Fat Skills 設計原則
- [[工作流與配置]]：Agent 工作流架構設計

---
網址: https://www.threads.com/@futurecommerce_official/post/DWzmQVZCIgE
作者: futurecommerce_official
tags: [Claude-Code, 記憶, CLAUDE.md, 情境工程]
status: wiki
---

## 情境工程五步驟（三個 Markdown 讓 Claude 記住你）

建立五個核心檔案作為 Claude 的長期記憶：

| 檔案 | 用途 |
|------|------|
| `about-me.md` | 個人背景、技能、偏好風格 |
| `brand-voice.md` | 寫作語氣、品牌個性 |
| `working-rules.md` | 工作規則、禁止事項 |
| `project-state.md` | 當前專案狀態 |
| `knowledge/` | 領域知識庫（可多個子檔） |

## 模組化配置（杜絕記憶污染）

**核心策略：不開全域記憶**
- 不使用 Claude 的全域記憶功能，避免不同專案互相污染
- 改用 Obsidian vault 作為工作目錄
- 每個專案有獨立的 CLAUDE.md 定義上下文

**目錄結構示例：**
```
project/
├── CLAUDE.md          ← 專案級指令
├── .claude/
│   ├── about-me.md
│   └── working-rules.md
└── src/
```

## Claude-Mem（持久記憶 + RAG）

- GitHub: 48.5k Stars 熱門工具
- 功能：持久記憶跨 session 保存 + RAG 精準檢索
- 解決「每次開新對話都要重新解釋背景」的問題
- 可與任何 Claude 客戶端整合

## Obsidian × Claude 三層機制

| 層 | 機制 | 功能 |
|----|------|------|
| 輸入層 | UserPromptSubmit hook（fd + rg） | 自動搜尋相關筆記注入 context |
| 知識層 | obsidian-notes-rag MCP | 語義檢索 Obsidian vault |
| 輸出層 | Stop hook secretary | 對話結束自動整理並回寫 Obsidian |

## Sources

- [三個 Markdown 檔案讓 Claude 永遠記住你￼](https://www.threads.com/@futurecommerce_official/post/DWzmQVZCIgE) | 作者: futurecommerce_official
- [Claude 模組化配置，杜絕記憶污染](https://www.threads.com/@santin/post/DXI-v9BGvTQ) | 作者: santin

## Cross References

- [[Skill 設計]]：Skill 與 CLAUDE.md 的協作關係
- [[工作流與配置]]：整體工作流配置脈絡
- [[MCP 工具]]：Obsidian MCP 整合細節

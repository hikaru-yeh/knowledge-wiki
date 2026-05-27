---
網址: https://www.threads.com/@mukiwu/post/DYeE20qk6MR
作者: ["@mukiwu"]
tags: [AI, Claude Code, Skill, TDD, 工作流]
status: wiki
source_blog: https://muki.tw/
---

## 核心問題

用 AI 寫程式的三個常見痛點：
1. 跟 AI 講了一堆，產出完全不是自己要的
2. 架構越寫越像爛泥，充滿重複的 class/function
3. AI 一次丟幾百行，沒有好的驗證節奏，只好 let it go

解法：**Matt Pocock 的「Skills for Real Engineers」** — 一組小而專注的技能集合，讓你拼出自己的 AI 開發工作流。

## 四個核心 Skill

### 1. grill-with-docs

與 AI 建立共同語言，產出專案專屬的 **CONTEXT.md** 和 **ADR（Architecture Decision Records）**。

→ 解決「AI 不懂你的專案規範」問題

### 2. tdd

把 AI 強制踩煞車，一步步完成「寫測試 → 實作 → 重構」三步驟循環。

→ 解決「AI 一次丟大量未驗證程式碼」問題

### 3. diagnose

把 debug 變成有節奏的迴圈，而非無結構的瞎猜。

→ 解決「AI 隨機試錯，越改越亂」問題

### 4. improve-codebase-architecture

對整個 codebase 做定期健檢，對抗熵增（架構自然腐化）。

→ 解決「長期用 AI 後架構無人追蹤」問題

## 組合應用

```
Skills for Real Engineers
  + Superpowers（大流程自動化）
  + shipshape-skills（品質把關）
= 自動跑大流程 + 工程師保留架構與品質主導權
```

**核心哲學**：「現在用 AI 寫程式很快，但總覺得哪裡怪怪的」的解法不是用更多 AI，而是**在 AI 流程中植入工程師的驗證節奏**。

## Sources

- [muki.tw 博客](https://muki.tw/) | 作者: Muki Wu

## Cross References

- [[Vibe-Coding]]：Karpathy 四法則（先想再動 / 簡單優先 / 精準修改 / 目標驅動）
- [[Skill 設計]]：Skill 設計原則
- [[Claude Code 提案 HTML 化，審核更輕鬆]]：配合 /preview 提升審核品質

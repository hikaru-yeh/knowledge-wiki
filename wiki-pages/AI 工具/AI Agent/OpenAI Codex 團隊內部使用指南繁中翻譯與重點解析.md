---
網址: https://www.threads.com/@prompt_case/post/DYla5zOFA5I
作者: ["@prompt_case"]
tags: [Codex, OpenAI, 使用指南, 工作流]
status: wiki
---

## 摘要

OpenAI 釋出的「Codex 使用思維入門指南」PDF，揭示其工程團隊內部使用 Codex 的方式。作者（@prompt_case）翻譯成繁體中文並提取五個最值得學習的實踐。

核心定位：把 Codex 的用途從「幫我寫程式」擴展成「幫我理解、重構、測試、探索、維持開發節奏」的成熟使用方式。

## 五個最值得學的實踐

### 1. 先 Ask Mode 想清楚，再 Code Mode 執行

不要一開始就叫 Codex 改一堆檔案，先讓它分析、規劃、指出風險，確認方向後才進入實作。

### 2. 把 Prompt 寫得像 GitHub Issue

好的 prompt 格式：
```
- 檔案路徑
- 背景說明
- 期望行為
- 參考模組
- 限制條件
```

「幫我修一下」< 結構化的 Issue 格式

### 3. 用 Codex 理解陌生程式碼

Codex 不只是生成功能。更大的價值是快速讀懂陌生 repo、追資料流、找核心邏輯。這對接手別人的程式碼特別有用。

### 4. 用 Codex 補測試、找邊界案例

- 補缺少的測試覆蓋
- 找容易漏掉的 failure path
- 不確定哪裡該測時，讓 Codex 提議

### 5. AGENTS.md 是長期理解的關鍵

讓 Codex 長期理解專案規則、命名慣例、業務邏輯的檔案。有了它，Codex 不用每次從零開始猜測專案慣例。

（等同於 Claude Code 的 CLAUDE.md）

## 適用範圍

指南涵蓋多種使用場景：
- 理解程式碼
- 重構與遷移
- 效能最佳化
- 加快開發速度
- 探索與構思

## Sources

- [prompt_case Patreon 繁中翻譯](https://www.patreon.com/posts/158824884)

## Cross References

- [[CLAUDE.md 與記憶設定]]：CLAUDE.md 等同 AGENTS.md 的 Claude 版本
- [[Claude Code與Codex：開發工具怎麼選？]]：兩個工具的比較

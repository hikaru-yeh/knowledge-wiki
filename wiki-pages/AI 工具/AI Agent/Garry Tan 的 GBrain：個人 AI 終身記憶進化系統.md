---
網址: https://www.threads.com/@ray.realms/post/DYhf2imgejq
作者: ["@ray.realms"]
tags: [Claude Code, AI Agent, 記憶, 知識圖譜]
status: reference
---

**GitHub**: [garrytan/gbrain](https://github.com/garrytan/gbrain) ⭐ 18,476

Garry Tan（Y Combinator 執行長）親自設計並在生產環境運行的個人 AI 終身記憶系統，驅動其 OpenClaw 與 Hermes Agent。

## 生產規模（Garry 本人環境）

- **146,646 頁**筆記、**24,585 位**人物、**5,339 家**公司
- **66 個** cron job 全自動運行（會議、Email、推文、語音、想法持續攝入）

## 核心技術

- **自我連線知識圖譜**：每次寫入零 LLM 呼叫，自動提取並建立實體關聯（`attended` / `works_at` / `invested_in` / `founded` / `advises`）
- **混合搜尋**：向量搜尋 + BM25 全文搜尋 + 反向連結加權排名
- **BrainBench 效能**：P@5 **49.1%**、R@5 **97.9%**，比關閉圖譜版本高出 **+31.4 個百分點**；優於 ripgrep-BM25 + 純向量 RAG

## 預設嵌入（v0.36.2.0）

ZeroEntropy `zembed-1`（1280d Matryoshka）+ `zerank-2` 重排序：
- vs OpenAI：速度快 **2.2×**、成本低 **2.6×**、20 個查詢中 11 個勝出

## 使用方式

```bash
gbrain init --pglite
# 丟連結給 Agent：它會自動安裝
```

## Cross References

- [[CLAUDE.md 與記憶設定]]：Claude Code 記憶機制與 Obsidian 三層架構
- [[讓 AI coding 記得你的專案]]：agentmemory 跨 session 記憶方案

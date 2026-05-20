---
網址: https://www.threads.com/@weilian.will/post/DW83-tWktcR
作者: weilian.will
tags: [Claude-Code, MCP, 工具, 整合]
status: wiki
---

## Claude Code 必備五大 MCP

| MCP | 功能 | 使用場景 |
|-----|------|----------|
| **Markitdown** | 將網頁/PDF 轉成 Markdown | 資料擷取、文件整理 |
| **Context7** | 即時抓取函式庫最新文件 | 程式開發、API 查詢 |
| **Playwright** | 瀏覽器自動化 | 測試、網頁操作 |
| **GitHub** | Git/PR/Issue 操作 | 版本控制流程 |
| **Task Master** | 任務分解與追蹤 | 複雜專案管理 |

## Firecrawl — 解決爬蟲三大痛點

1. **403 封鎖**：自動輪換 User-Agent 和 IP，繞過基本封鎖
2. **JS 渲染**：等待 JavaScript 執行後再擷取，處理 SPA 網站
3. **批量爬取**：支援 sitemap 批量爬取，適合大規模資料收集

**整合方式**：透過 MCP 讓 Claude Code 直接呼叫 Firecrawl API

## Routines — 排程與事件驅動自動化

三種觸發模式：
- **Schedule（排程）**：cron 語法，例如 `0 9 * * 1` = 每週一早上 9 點
- **GitHub 事件**：PR opened/merged、Issue created 等
- **API 觸發**：外部系統透過 webhook 呼叫 Claude Code 工作流

## Obsidian MCP

透過 `obsidian-notes-rag` MCP 讓 Claude 讀寫 Obsidian vault：
- 語義搜尋：自然語言查詢找到相關筆記
- 雙向整合：Claude 可直接建立、修改 Obsidian 筆記

## Sources

- [Claude 必備 5 大 MCP：程式效率加速器](https://www.threads.com/@weilian.will/post/DW83-tWktcR) | 作者: weilian.will
- [Firecrawl 讓 Claude Code 輕鬆爬取網站](https://www.threads.com/@hei_ai.automation/post/DWxzgT-EzvC) | 作者: hei_ai.automation
- [Claude 自動化工程師：排程事件驅動](https://www.threads.com/@aiposthub/post/DXITbsPitMF) | 作者: aiposthub

## Cross References

- [[工作流與配置]]：MCP 在整體工作流的位置
- [[CLAUDE.md 與記憶設定]]：Obsidian MCP 與記憶系統整合
- [[其他 AI 工具/工具總覽]]：更多 AI 工具比較

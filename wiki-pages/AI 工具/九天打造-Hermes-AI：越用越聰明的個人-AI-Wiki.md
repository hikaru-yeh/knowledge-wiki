---
網址: https://www.threads.com/@krumjahn/post/DXg-sfymEnB
作者: ["@krumjahn"]
tags: []
status: wiki
---

## 概述

Hermes AI 是一套開源 Agent 系統，目標是打造 Andrej Karpathy 提出的「LLM Wiki」概念：一個持續運行、越用越聰明的個人 AI 助手。相較於 OpenClaw 缺乏持久記憶且每次對話重新開始，Hermes 透過 Souls / Agents / User 三層配置檔 + cron jobs 自動化，讓 AI 能累積個人脈絡並主動執行排程任務。

## 安裝與設定

- 執行 `hermes gateway setup` 啟動設定精靈
- 自動偵測既有 OpenClaw 安裝，可一鍵匯入 souls、profiles、skills
- Dashboard 啟動指令：`hermes dashboard`，存取 `127.0.0.1:1919`
- Dashboard 功能：session 歷史、已連接平台、token 用量、錯誤紀錄、cron jobs 管理、skills 開關、config 編輯器

## LLM 選擇

| Provider | 費用 | 特點 |
|----------|------|------|
| OpenAI Codex | $20/月 | 唯一不禁止 agent 層疊的主流 provider；自動偵測機器登入態 |
| OpenRouter | $10 最低儲值 | 每日 1,000 免費 requests、auto-routing、fallback 支援；免費模型 Elephant |
| Ollama（本地） | 免費 | `ollama launch hermes`；Qwen 3.5 9B 可用、Gemma 3 4B 不支援 tool calling |

Provider routing 可依任務複雜度切換：`mode cheap`（簡單任務用便宜模型）或 `mode plan`（複雜任務用高階模型），支援 fallback chain（Anthropic → OpenAI → 免費模型）。

## Telegram 整合

1. `hermes gateway setup` → 選 Telegram
2. BotFather 輸入 `/newbot` 建立 bot、取得 token
3. `@userinfobot` 取得 user ID（注意仿冒帳號）
4. BotFather → bot settings → Group Privacy → 關閉
5. 移除再重新加入 bot 到群組

啟用 Topics 功能可做工作流分流：Social Media / App Development / Analytics / Health 各自獨立對話區。

## 人格配置：三個 `.md` 檔

隱藏檔案需 `Cmd+Shift+.` 顯示：

| 檔案 | 用途 | 範例 |
|------|------|------|
| `Souls.md` | 人格定義 | 「concise technical expert, no fluff, just tactics」 |
| `Agents.md` | 指令與規則 | coding style、post format、行為限制 |
| `User.md` | 持久記憶 | 個人資料（姓名/家庭/地點/職業）；解決 OpenClaw 每天遺忘問題 |

## Cron Jobs 與排程

使用標準 cron 格式（分/時/日/月/週）：

- 每週一 8:30 發送 App Sales Report 到 Telegram
- 每小時 heartbeat：檢查工作進度、健康指標、業務改善建議
- 晨報：睡眠品質分數、日曆行程、標記 email、主動洞察

執行過的指令可儲存為可重用 skill。

## 實戰整合

| 服務 | 接法 | 能力 |
|------|------|------|
| Apple Health | Health Data AI Analyzer API | Python 提取睡眠數據（平均 7.59 hrs，含高低範圍） |
| Threads | 瀏覽器 cookie export | 單指令拉 34 篇貼文分析（likes / replies / reposts），作者已開源此 skill |
| Gmail + Calendar | Google Cloud Console → 建專案 → 啟用 API → 下載 OAuth JSON → 拖入 Hermes → 授權 | 交叉比對行程與睡眠數據 |
| Obsidian Vault | UGreen NAS 集中儲存 | 共享 markdown vault，兩個 Agent 共用 souls / agents / memory / emails / calendar / business notes |

## 雙 Agent 架構：Hermes + OpenClaw

兩者分工明確，共享同一個 Obsidian vault：

| 維度 | Hermes | OpenClaw |
|------|--------|----------|
| 強項 | 記憶、持久上下文、cron jobs、瀏覽器自動化、快速任務 | 多 Agent 工作流、深度研究、長時間複雜任務 |
| 角色 | 調度者 — 簡單推理 + 協調 | 執行者 — 多步驟工作流 + 深度研究 |

Prompt 設定：「Use Hermes for simple reasoning, quick tasks, coordination. Use OpenClaw for multi-step workflows, deep research, long-running tasks. Delegate complex tasks to OpenClaw, wait for response, return clean answer.」

## 成本與效果

| 項目 | 金額 |
|------|------|
| 舊方案（Claude API） | $64/週 |
| 新方案（OpenAI Codex） | $20/月 |
| VPS（DigitalOcean droplet，2 CPU + 4GB RAM） | $18/月 |
| **總範圍** | **$20-58/月**（依配置） |

關鍵改善：持久上下文（不再每天遺忘）、自動排程、瀏覽器自動化比 OpenClaw 穩定。

## Sources

- Substack guide: https://rumjahn.substack.com/p/complete-guide-to-mastering-hermes
- Threads 原帖: https://www.threads.com/@krumjahn/post/DXg-sfymEnB

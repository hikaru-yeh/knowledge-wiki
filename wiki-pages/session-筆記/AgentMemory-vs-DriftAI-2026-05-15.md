---
source: session | 2026-05-15
status: reference
tags: [agent-memory, drift-ai, 記憶管理, 多agent, MCP]
last_updated: 2026-05-15
---

# AgentMemory vs Drift AI — 全方面比較

> AgentMemory 是「讓 agent 永遠記得」的持久記憶庫；Drift AI 是「讓決策在 agent 之間流動」的交接 brief 工具。兩者不互斥。

## 核心定位

| 維度 | **AgentMemory** | **Drift AI** |
|------|-----------------|--------------|
| 核心問題 | Agent 跨 session 失憶、每次重頭解釋 | 切換不同 AI Agent 時喪失決策脈絡 |
| 解決策略 | 持久記憶庫，自動注入歷史上下文 | Handoff brief，打包交接任務給下一個 agent |
| 使用場景 | 長期專案、同一 agent 反覆工作 | 多 agent 切換、達到 rate limit / context 上限時 |
| 設計哲學 | 「讓 agent 永遠記得」 | 「讓知識在 agent 之間流動」 |

## 技術架構

| 維度 | **AgentMemory** | **Drift AI** |
|------|-----------------|--------------|
| 語言 | Node.js / TypeScript | Rust 1.85+ |
| 儲存 | SQLite（內建，無需外部 DB） | SQLite（`events.db`） |
| 記憶/索引引擎 | iii 分散式引擎（HTTP trigger + KV + WebSocket） | 本地事件 DB + 壓縮摘要 + Git notes |
| 搜尋方式 | BM25 + 向量嵌入 + 知識圖譜（RRF 融合） | 無語意搜尋，依靠摘要 + Git blame |
| LLM 依賴 | 可選（用於壓縮，預設關閉） | 必需（Anthropic API 壓縮摘要） |
| MCP 工具數 | 51 個（核心 + 擴展模式） | 5 個（唯讀） |
| 即時監控 | Web viewer（port 3113） | `drift watch` 背景 daemon（FSEvents/inotify） |

## 記憶模型

| 維度 | **AgentMemory** | **Drift AI** |
|------|-----------------|--------------|
| 記憶層次 | 4 層：working → episodic → semantic → procedural | 扁平：session → compacted summary → git notes |
| 記憶類型 | 觀察、程序知識、語意事實、工作記憶 | 決策、拒絕方案、檔案變更、進度狀態 |
| 記憶更新 | 12 個 lifecycle hooks 自動捕捉 | file-system 事件觸發 + 手動 `drift capture` |
| 記憶注入 | 自動（session 開始時智慧注入） | 手動（`drift handoff` 產生 brief 後貼入） |
| 跨 session | 是，無縫延續 | 是，透過 handoff brief |

## AI Agent 整合

| 維度 | **AgentMemory** | **Drift AI** |
|------|-----------------|--------------|
| 支援工具 | Claude Code、Cursor、Gemini CLI、Codex CLI、Cline、Hermes 等 30+ | Claude Code、Codex（讀取本機 session 目錄） |
| 整合方式 | MCP server、REST API、hooks | MCP server（stdio）、session 目錄掃描 |
| 跨 agent 共享 | 是（同一個 memory server 服務所有 agent） | 是（透過 git notes 共享 blame DB） |
| 廠商鎖定 | 無（任何支援 MCP 的 client） | 無（vendor-neutral handoff） |

## 安裝與使用

| 維度 | **AgentMemory** | **Drift AI** |
|------|-----------------|--------------|
| 安裝 | `npx @agentmemory/agentmemory`（30 秒） | Homebrew / Cargo / 預編譯 binary |
| 設定檔 | `~/.agentmemory/.env` | `~/.config/drift/config.toml` + repo `.prompts/config.toml` |
| 主要指令 | 自動（hooks），搜尋透過 MCP | `drift init / capture / watch / handoff / blame / trace` |
| Windows 支援 | 需要預編譯 iii binary 或 Docker Desktop | 提供預編譯 binary |
| 上手難度 | 低（安裝後全自動） | 中（需理解 handoff 流程） |

## Token 效率與成本

| 維度 | **AgentMemory** | **Drift AI** |
|------|-----------------|--------------|
| Token 用量 | ~170K tokens/年（vs 貼完整 context 的 19.5M+） | 依 handoff 頻率，每次 handoff ~$0.10–0.30（Opus） |
| LLM 呼叫費用 | 壓縮預設關閉；可用本地嵌入（免費） | 每次壓縮必須呼叫 Anthropic API |
| 成本控制 | 可調搜尋權重、關閉 LLM 壓縮 | 切換 Haiku 可省 ~19x 費用（$0.15 vs $2.91） |
| 費用追蹤 | 無內建 | `drift cost` 指令，逐 session 顯示 USD |

## 隱私與安全

| 維度 | **AgentMemory** | **Drift AI** |
|------|-----------------|--------------|
| 資料存放 | 本機（SQLite），不強制外傳 | 本機優先；`db_in_git=true` 時 blame DB 推上 repo |
| 敏感資訊風險 | 未明確提及 sanitize | 明確警告：session 內容（含意外貼入的 secrets）會鏡像到 `.prompts/` |
| Secrets 防護 | 無 | 建議搭配 gitleaks/trufflehog；regex redaction 列入 roadmap |
| 雲端依賴 | 可選（embeddings / LLM 壓縮） | 必要（Anthropic API 壓縮） |

## 專案成熟度

| 維度 | **AgentMemory** | **Drift AI** |
|------|-----------------|--------------|
| 版本 | 發布於 npm（穩定） | v0.4.2（活躍開發中） |
| 程式碼規模 | 21,800 LOC、118 檔案、800+ 測試 | Rust codebase |
| 授權 | Apache 2.0 | Apache 2.0 |

## 選擇建議

| 你的需求 | 推薦 |
|----------|------|
| 同一個 agent 長期工作，想自動記憶 | **AgentMemory** |
| 常切換多個 AI 工具（Claude → GPT → local LLM） | **Drift AI** |
| 想了解「為何做這個決定 / 拒絕哪些方案」 | **Drift AI** |
| 想要零配置、全自動 | **AgentMemory** |
| 重視 git 整合（blame、audit trail） | **Drift AI** |
| 預算敏感，不想付 LLM API 費 | **AgentMemory**（可用本地嵌入） |
| 需要語意搜尋歷史記憶 | **AgentMemory** |

兩者不互斥——Drift 管跨 agent 交接，AgentMemory 管單一 agent 記憶延續。

## 相關資源

- GitHub: https://github.com/rohitg00/agentmemory
- GitHub: https://github.com/ShellFans-Kirin/drift_ai
- [[AgentMemory-Windows-Setup-2026-05-15]]

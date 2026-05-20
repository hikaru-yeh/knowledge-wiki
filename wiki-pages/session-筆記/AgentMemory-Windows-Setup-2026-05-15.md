---
source: session | 2026-05-15
status: reference
tags: [agent-memory, MCP, windows, claude-code, codex, hooks]
last_updated: 2026-05-15
---

# AgentMemory — Windows 安裝與整合指南

> AI agent 持久記憶系統，支援 BM25+向量+知識圖譜三層搜尋，~$10/年 token 成本，51 個 MCP tools，支援 Claude Code / Codex / Cursor 等 30+ agent。

## 定位與用途

- **解決問題**：agent 跨 session 失憶，每次重頭解釋
- **運作方式**：12 個 lifecycle hooks 自動捕捉 session，智慧注入相關歷史
- **Token 效率**：~170K tokens/年 vs 貼完整 context 的 19.5M+（省 99%）
- **搜尋精度**：LongMemEval-S R@5 = 95.2%

## 安裝（Windows）

### Step 1：iii engine binary

Windows 需要 iii engine 才能執行完整功能：

1. 下載 prebuilt binary：https://github.com/iii-hq/iii/releases/tag/iii%2Fv0.11.2
2. 解壓 `iii.exe`
3. 放到 `%USERPROFILE%\.local\bin\`（或任何在 PATH 的目錄）

### Step 2：啟動 Memory Server

開一個**長駐 terminal**（不要關）：

```powershell
npx @agentmemory/agentmemory
```

驗證：

```powershell
curl http://localhost:3111/agentmemory/health
```

Real-time viewer：瀏覽器開 `http://localhost:3113`

### Step 3（選做）：執行 Demo

```powershell
npx @agentmemory/agentmemory demo
```

## Claude Code 整合

### 方法 A：Plugin（推薦，自動設定一切）

在 Claude Code 對話框輸入：

```
/plugin marketplace add rohitg00/agentmemory
/plugin install agentmemory
```

自動完成：
- 註冊 12 個 lifecycle hooks
- 加入 4 個 skills（`/recall`、`/remember`、`/session-history`、`/forget`）
- 設定 MCP server（51 個 tools）

### 方法 B：手動 MCP

編輯 `%USERPROFILE%\.claude\settings.json`，合併加入：

```json
{
  "mcpServers": {
    "agentmemory": {
      "command": "npx",
      "args": ["-y", "@agentmemory/mcp"],
      "env": {
        "AGENTMEMORY_URL": "http://localhost:3111"
      }
    }
  }
}
```

## Codex CLI 整合

### 背景

Codex plugin install 在 Windows 可能遇到 PermissionDenied（code 5）錯誤，改走 MCP 路線。

### 設定方式

編輯 `%USERPROFILE%\.codex\config.toml`，加入：

```toml
[mcp_servers.agentmemory]
command = "npx"
args = ["-y", "@agentmemory/mcp"]

[mcp_servers.agentmemory.env]
AGENTMEMORY_URL = "http://localhost:3111"
```

### Codex vs Claude Code 差異

| | Claude Code | Codex |
|--|-------------|-------|
| Hooks 數量 | 12 | 6 |
| 缺少的 hooks | — | SubagentStart/Stop、SessionEnd、Notification、TaskCompleted、PostToolUseFailure |
| Plugin 指令 | `/plugin` | `codex plugin` |
| 自動捕捉 | 完整 | 需確認 `codex_hooks = true` |

> Codex config.toml 中若有 `codex_hooks = false`，自動捕捉不會觸發，只有 MCP tools 可手動呼叫。

## 設定（.env）

設定檔位置：`%USERPROFILE%\.agentmemory\.env`

### LLM 壓縮（選擇一個，或都不設 = 免費 BM25 模式）

```env
ANTHROPIC_API_KEY=sk-ant-...
# 或
GEMINI_API_KEY=...
# 或
OPENROUTER_API_KEY=...
```

### 推薦開啟的功能

```env
AGENTMEMORY_SLOTS=true          # 固定記憶槽（persona、偏好、pending）
AGENTMEMORY_REFLECT=true        # session 結束自動更新記憶槽
AGENTMEMORY_INJECT_CONTEXT=true # session 開始自動注入上下文
GRAPH_EXTRACTION_ENABLED=true   # 知識圖譜建立
```

### 搜尋權重調整

```env
BM25_WEIGHT=0.4    # 關鍵字搜尋權重
VECTOR_WEIGHT=0.6  # 語意搜尋權重
TOKEN_BUDGET=2000  # 每 session 注入 token 上限
```

### 開啟全部 51 個 MCP Tools

```env
AGENTMEMORY_TOOLS=all
```

### 中文支援（必裝）

```powershell
npm install @node-rs/jieba tiny-segmenter
```

## MCP Tools 與 Skills

### 核心 11 個 Tools（預設啟用）

| Tool | 用途 |
|------|------|
| `memory_smart_search` | 混合語意+關鍵字搜尋（主力工具） |
| `memory_recall` | 搜尋過去觀察 |
| `memory_save` | 手動存入記憶 |
| `memory_file_history` | 查某個檔案的操作歷史 |
| `memory_profile` | 顯示整個專案的知識摘要 |
| `memory_timeline` | 時間軸瀏覽記憶 |
| `memory_sessions` | 列出近期 sessions |
| `memory_compress_file` | 壓縮 markdown 檔案 |
| `memory_export` | 匯出所有資料 |
| `memory_audit` | 操作審計軌跡 |
| `memory_governance_delete` | 附審計紀錄的刪除 |

### 擴展 Tools（需 `AGENTMEMORY_TOOLS=all`）

- `memory_graph_query`：知識圖譜查詢
- `memory_claude_bridge_sync`：同步 MEMORY.md
- `memory_lease`：多 agent 操作鎖
- `memory_snapshot_create`：Git 版本化快照
- `memory_signal_send/read`：agent 間訊息

### Skills（Plugin 安裝後可在對話框使用）

| 指令 | 功能 |
|------|------|
| `/recall <關鍵字>` | 語意搜尋歷史記憶 |
| `/remember <內容>` | 手動存入記憶 |
| `/session-history` | 列出最近 sessions 摘要 |
| `/forget <內容>` | 刪除特定記憶 |

## Hooks 系統（Claude Code Plugin）

| Hook | 自動捕捉 |
|------|----------|
| SessionStart | 初始化 + 注入上下文 |
| UserPromptSubmit | 使用者意圖 |
| PreToolUse | 執行前上下文 |
| PostToolUse | 工具名稱、輸入輸出（核心） |
| PostToolUseFailure | 錯誤 pattern |
| PreCompact | 重新注入記憶（防止 context 壓縮時遺失） |
| SubagentStart/Stop | 子 agent 生命週期 |
| Stop | session 結束摘要與整合 |
| SessionEnd | session 完成標記 |
| Notification | agent 通知事件 |
| TaskCompleted | 完成工作項目 |

## 匯入舊的 Claude Code 紀錄

```powershell
# 自動偵測所有 jsonl
npx @agentmemory/agentmemory import-jsonl

# 指定檔案
npx @agentmemory/agentmemory import-jsonl "$env:USERPROFILE\.claude\projects\my-project\abc123.jsonl"
```

## 常見問題 / 踩坑

| 問題 | 解法 |
|------|------|
| Windows PermissionDenied（code 5）安裝 plugin | 改走 MCP 路線，直接編輯 config.toml |
| Port 3111 被佔用 | `netstat -ano \| findstr :3111` → kill 該 PID |
| iii engine timeout（15s） | `npx @agentmemory/agentmemory --verbose` 查原因 |
| 中文搜尋不準 | `npm install @node-rs/jieba tiny-segmenter` |
| iii.exe 找不到 | 確認放在 PATH 目錄，重開 terminal |
| Codex hooks 不觸發 | 確認 config.toml 中 `codex_hooks = true` |

## 重要注意事項

- Memory server 必須長駐；建議用 Windows Task Scheduler 開機自動啟動
- LLM 壓縮預設關閉（`AGENTMEMORY_AUTO_COMPRESS=false`）；不設 API key 仍可免費使用 BM25
- Claude Code Plugin 和 Codex MCP 共用同一個 memory server，記憶互通

## 相關資源

- GitHub: https://github.com/rohitg00/agentmemory
- npm: `@agentmemory/agentmemory`
- [[AgentMemory-vs-DriftAI-2026-05-15]]

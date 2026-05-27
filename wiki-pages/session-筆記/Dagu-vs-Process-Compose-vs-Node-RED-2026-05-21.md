---
source: session | 2026-05-21
status: reference
tags: [windows, process-manager, watcher, dashboard, automation]
last_updated: 2026-05-21
---

# Dagu vs Process Compose vs Node-RED

> Windows 本機 watch 腳本與常駐命令的 dashboard 管理選型筆記。

## 核心定位 (比較表)

| 工具 | 適合度 | 核心定位 | 適合情境 |
| --- | --- | --- | --- |
| Dagu | 很適合 | 單機 DAG / job runner，有 Web UI、YAML、logs/history、手動 rerun/stop | 把散落在各專案的 watch / run command 收成一個本機腳本 dashboard |
| Semaphore UI | 很適合 | Web UI/API 跑 PowerShell、Shell、Python、Ansible、Terraform | 想把個人或小團隊腳本整理成任務中心，偏 runbook 管理 |
| Process Compose | 適合 | 像 docker-compose，但管理本機非容器 processes；有 TUI、REST API、logs、restart policy | 長期開很多常駐命令，需要 start/stop/restart 與集中 logs |
| Node-RED | 適合事件流 | 低程式碼 flow editor，適合「資料夾事件 -> 執行命令 -> 通知/分流」 | 想用 dashboard/flow 視覺化檔案事件與命令觸發 |
| Rundeck | 可以但偏重 | 成熟 runbook automation，有 Web UI、logs、權限、Windows nodes | 多人、權限、遠端機器、審計紀錄需求明確時 |
| PM2 | 部分適合 | Node 生態 process manager，可管理常駐命令、logs、restart | 管理 `npx @agentmemory/agentmemory` 這類常駐命令；dashboard 不夠本機化 |
| watchexec | 配角 | 專門監看檔案變動後執行命令 | 包進 Dagu / Process Compose / PM2 裡，處理資料夾 watch 邏輯 |

## 技術架構 (比較表)

| 類型 | 工具 | Dashboard | Watch 能力 | Process supervision | Windows 友善度 | 重量 |
| --- | --- | --- | --- | --- | --- | --- |
| Job / DAG runner | Dagu | Web UI | 可搭配 `watchexec` 或 job 排程 | 中 | 高 | 中低 |
| Runbook automation | Semaphore UI | Web UI | 可透過腳本或外部 watcher | 中 | 高 | 中 |
| Local process manager | Process Compose | TUI / REST API | 可直接跑 watcher command | 高 | 高 | 低 |
| Flow automation | Node-RED | Web editor / dashboard | 高，適合事件流 | 中低 | 高 | 中 |
| Enterprise runbook | Rundeck | Web UI | 可透過 job / script | 中高 | 中高 | 高 |
| Node process manager | PM2 | CLI / pm2.io | 可跑 watcher command | 高 | 中 | 低 |
| File watcher | watchexec | 無 | 高 | 低 | 高 | 低 |

## 選擇建議

- 如果目標是「本機 dashboard 管所有散落腳本」，優先試 Dagu。
- 如果主要是長期開很多常駐命令，Process Compose 會很舒服，特別適合集中管理 start/stop/restart/logs。
- 如果核心需求是「資料夾事件 -> 執行程式 -> 通知或分流」，Node-RED 比較像控制台。
- 如果未來要多人使用、權限控管、遠端節點、審計紀錄，再考慮 Rundeck。
- PM2 適合管理 `npx`、Node-based daemon 或一般長跑命令，但不是最理想的本機 dashboard。
- watchexec 不取代 dashboard，它是 watch 腳本的底層積木。

## 各工具詳細筆記

### Dagu

- 單一工具把腳本定義成 YAML job / DAG，提供 Web UI、執行紀錄、logs、手動 rerun/stop。
- 很適合把「各專案資料夾裡的 watch script」集中成一個 dashboard。
- 可把資料夾監看交給 `watchexec`，Dagu 只負責啟動、停止、查看 logs。

### Semaphore UI

- Web UI/API，可跑 PowerShell、Shell、Python、Ansible、Terraform。
- 比 Dagu 更像 runbook / 任務中心。
- 若之後要把個人腳本擴充成小團隊可用的任務系統，Semaphore UI 值得評估。

### Process Compose

- 類似 `docker-compose`，但管理的是本機 process，而不是 container。
- 適合常駐命令，例如 agentmemory server、watcher、local service。
- 重點能力：start/stop/restart、集中 logs、process dependency、restart policy、TUI、REST API。

### Node-RED

- 最適合事件流與視覺化控制台。
- 對「資料夾有新檔 -> 執行某命令 -> 成功/失敗通知 -> 可能移動檔案」這種流程很自然。
- process supervision 不是主場；若命令要長期穩定常駐，可能還是要搭配 Process Compose / PM2 / Windows service。

### Rundeck

- 成熟但偏重。
- 當需求包含多人、權限、遠端 Windows nodes、審計、審批、排程與 runbook catalog 時才比較划算。
- 個人電腦單機 watcher 管理一開始不建議先上。

### PM2

- 對 Node / npx 類常駐命令很好用，例如：`npx @agentmemory/agentmemory`。
- 可管理 logs、restart、startup。
- 但 dashboard 體驗不是最貼近「本機所有 watch 腳本總控台」。

### watchexec

- 輕量、跨平台，專門做「監看檔案變動後執行命令」。
- 適合作為 Dagu / Process Compose / PM2 裡的 command。
- 本身沒有 dashboard，也不負責完整 process 管理。

## 範例命令與設定

原本散落的 Windows Terminal 啟動命令：

```powershell
wt.exe -d "D:\shane_yeh\Documents\_Claude_Code\assignment-pipeline" cmd /k python run_assignment_pipeline.py --watch-dir "D:\shane_yeh\Downloads\New comer"
```

用 `watchexec` 把資料夾監看包成 command：

```powershell
watchexec -w "D:\shane_yeh\Downloads\New comer" -- python run_assignment_pipeline.py --watch-dir "D:\shane_yeh\Downloads\New comer"
```

Process Compose 範例：

```yaml
version: "0.5"

processes:
  assignment_pipeline:
    working_dir: "D:/shane_yeh/Documents/_Claude_Code/assignment-pipeline"
    command: 'python run_assignment_pipeline.py --watch-dir "D:\shane_yeh\Downloads\New comer"'
    availability:
      restart: "always"

  agentmemory:
    command: "npx @agentmemory/agentmemory"
    availability:
      restart: "always"
```

注意：如果這段 YAML 之後轉成 `.toml` 設定檔，Windows 反斜線路徑必須用 TOML 單引號字串，避免 `\W`、`\S`、`\v` 被雙引號字串解讀為跳脫序列。

## 相關資源

- [Dagu GitHub](https://github.com/dagu-org/dagu)
- [Semaphore UI Docs](https://semaphoreui.com/docs)
- [Process Compose Docs](https://f1bonacc1.github.io/process-compose/)
- [Node-RED Docs](https://nodered.org/docs/)
- [Rundeck Features](https://www.rundeck.com/features)
- [PM2 Quick Start](https://pm2.keymetrics.io/docs/usage/quick-start/)
- [watchexec GitHub](https://github.com/watchexec/watchexec)

---
type: project
status: legacy
last_updated: 2026-05-13
time: 2025-01
tech_stack:
  - Python
  - PyYAML
  - watchdog
  - AnythingLLM REST API
  - MarkItDown
  - fire-pdf
  - Tkinter
depends_on: []
feeds_into:
  - AnythingLLM (social_brain workspace)
  - personal_wiki (via Raw_Sources)
superseded_by: data_preprocess
---

# data_pipeline

社群媒體匯出資料、郵件、PDF 統一轉 Markdown → AnythingLLM 向量化 → Raw_Sources 的三段式管線。已由 `data_preprocess` 取代。

## 専案任務

Shane 建立個人知識庫（personal_wiki）的第一個前置基礎設施。需要把散落在多個平台的個人資料（Gmail、LINE、IG、FB、Threads、PDF）轉成 LLM 可讀的 Markdown，並上傳 AnythingLLM 向量資料庫，讓 AI 助手可查詢個人社群記憶。

## Briefing（原始需求）

把 Gmail 匯出、LINE 記錄、IG/FB/Threads 匯出、PDF 文件統一轉成 Markdown，批次上傳到 AnythingLLM `social_brain` workspace，再把轉換結果同步到 Raw_Sources 供 personal_wiki ingest。

## 成品描述

三段式管線，命令列執行：
1. `process_all.py`：各平台 processor（Gmail/LINE/IG/FB/Threads）+ `OthersProcessor`（通用文件），將 `original_input/` 轉出 Markdown 到 `md_output_for_AnythingLLM/`
2. `anythingllm_sync.py`：upload → embed → verify → sync，確保所有文件都進入 workspace
3. 轉換結果同步到 `Raw_Sources/` 供 personal_wiki ingest

另有 `service_pipeline.py` 背景服務模式（watchdog 監聽），可持續處理新檔案。

## 技術與架構

使用技術：Python、PyYAML、watchdog、AnythingLLM REST API、MarkItDown、fire-pdf

```
original_input/
    ↓ process_all.py（各平台 processor + OthersProcessor）
md_output_for_AnythingLLM/
    ↓ anythingllm_sync.py（upload → embed → verify → sync）
AnythingLLM workspace: social_brain
    ↓
Raw_Sources/ → personal_wiki ingest
```

主要元件：DataPipeline（主流程協調器）、SyncPipeline（同步管線）、SyncCache（快取層）、OthersProcessor（通用文件處理器）、PipelineRunWindow（Tkinter GUI，舊版）

## 可複用的元件

- `SyncCache`（`sync/sync_cache.py`）：size+mtime 快速路徑 + hash 慢路徑的雙層檔案級 cache。任何需要增量同步的管線都可直接複用
- `OthersProcessor`（`processors/others_processor.py`）：全域文件遞迴掃描、PDF/MarkItDown 分流，image-based PDF fallback（pdf_inspector）。通用文件轉換邏輯

## 學到什麼 / 踩過的坑

- AnythingLLM embed 不能只看 upload 成功，必須回查 workspace 文件清單確認已向量化 → 在 `anythingllm_sync.py` 加入 embed-verify loop
- `/api/v1/workspace/{slug}` 回傳的 `workspace` key 是 list，不是 dict（API 早期版本問題）→ 在 sync 邏輯中加 isinstance 判斷
- Windows cp950 主控台下 Unicode 警告字元會直接爆掉 → 所有錯誤訊息改用 ASCII 輸出
- image-based PDF（如掃描件）MarkItDown 無法轉出文字 → fallback 用 `pdf_inspector` 萃取圖像描述

## 遺留問題 / 未完成

- `Aufgabe_KW17.pdf`：image-based PDF，MarkItDown 無法處理，根因未完整追查
- stem collision（同名不同副檔名的來源檔）在舊管線設計下未處理，由 `data_preprocess` 解決

## Cross References

- [[專案管理/projects/data_preprocess]]：取代本管線的新版本
- [[專案管理/_overview]]：跨專案總覽

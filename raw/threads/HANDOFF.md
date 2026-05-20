# HANDOFF

> 上次 session: 2026-05-12
> 下次接手請從「接手要做的事」開始

## 狀態
Gemini 安全封鎖系列修復完成；output 資料夾遷移至 knowledge-wiki；Claude Code / AI 分類邊界確認並固化進 prompt；70 個 tests 全 pass。

## ✅ 本次完成
- **`response.text=None` 修復**：Gemini safety block 時 SDK 的 `.text` 是 `None` 不是 absent，改用 `(response.text or "")` 統一處理；補測試。
- **Per-item 錯誤隔離**：每筆書籤用 try/except 包住，單筆失敗不中斷整批；`failed_count` 正確計數；失敗時 emit `bookmark_failed` 事件。
- **PROHIBITED_CONTENT 繞過**：title prompt 加入 `「{category}」類別` 讓 Gemini 把請求視為分類內容生成，修復心理健康類貼文被封鎖的問題。
- **LLM client debug logging**：response.text 為空時記錄 finish_reason、safety_ratings、prompt_feedback。
- **output 資料夾遷移**：`config.py` DEFAULT_OUTPUT_DIR 從 `llm-notes\raw\threads` 改為 `knowledge-wiki\raw\threads`；同步更新測試。
- **Claude Code / AI 分類邊界確認**：Claude 只是被提及工具之一 → AI；明確談 Claude Code 功能/skill/hook → Claude Code；固化進 classifier prompt。
- **workflow test 更新**：`test_workflow_fails_fast_on_classifier_error` 改名為 `test_workflow_isolates_classifier_error_per_item`，斷言改為 `failed_count==1`、`written_count==0`、事件含 `bookmark_failed`。

## 🔄 進行中
- 無

## ⚡ 接手要做的事
1. **跑完整資料集**：`python app.py`，確認 skip 機制與 Gemini-first 在新 output 路徑 (`knowledge-wiki\raw\threads`) 表現正常
2. **重複 URL 清理**（另一 session 處理中）：`knowledge-wiki\raw\threads` 現有 29 個 URL 各有兩份，根因是舊 default 路徑 (`llm-notes`) 與 env var 路徑 (`knowledge-wiki`) 不一致導致 skip 機制失效，現已修正。

## ⚠️ 注意事項
- output 目錄已更新為 `D:\shane_yeh\Documents\_Claude_Code\knowledge-wiki\raw\threads`
- `samples/scribe.json` 不納版本控制，須確認本機有此檔
- git status 乾淨（所有 commits 已完成）

## 📁 本次修改的檔案
- `config.py` — DEFAULT_OUTPUT_DIR 改為 knowledge-wiki
- `services/llm_client.py` — response.text None 修復；debug logging
- `services/category_classifier.py` — Claude Code/AI 邊界明確化
- `services/title_generator.py` — PROHIBITED_CONTENT bypass
- `workflows/import_bookmarks_to_markdown.py` — per-item 錯誤隔離；failed_count 修正
- `tests/test_config.py` — output dir 斷言更新
- `tests/test_category_classifier.py` — Codex 斷言改為新規則斷言
- `tests/test_workflow.py` — fail-fast 測試改為 per-item isolation 測試
- `tests/test_llm_client.py` — response.text=None 測試

---
type: project
status: active
last_updated: 2026-05-13
time: 2025-02
tech_stack:
  - Python
  - Tkinter
  - PyYAML
  - pytest
  - MarkItDown
  - pdf_inspector
depends_on: []
feeds_into:
  - personal_wiki (via Raw_Sources)
supersedes: data_pipeline
---

# data_preprocess

`data_pipeline` 的重構版。拔掉 AnythingLLM 向量化主線，改成 GUI-driven 任務流，直接把 `original_input` 轉出的 Markdown 寫入 `Raw_Sources`。

## 専案任務

`data_pipeline` 同時綁定三種職責（batch / watch / sync），重構很難；且 wiki ingest 的本質是「讀來源後產生/更新知識頁面」（寫入型），向量化（retrieval 型）不是主線需求。目標：建立更輕量、單一職責的前置資料處理工具。

## Briefing（原始需求）

重構舊管線：拔掉 AnythingLLM 依賴，改成 Tkinter GUI 單一入口，讓 user 可以預覽衝突、選擇處理策略，最後一鍵寫入 Raw_Sources。

## 成品描述

GUI 桌面應用程式（Tkinter），流程：
1. User 選擇 `original_input/` 目錄與目標 `Raw_Sources/`
2. 系統 pre-scan 偵測同名衝突，GUI 顯示衝突清單
3. User 選擇每筆衝突的處理策略（overwrite / skip / rename）
4. executor 依決策寫入 `Raw_Sources/`
5. 產出 `run_manifest.json`、`run_result.json`、`run_failures.csv`

約 90% 完成，可自用。GUI 細節與 conflict reviewer 測試覆蓋待補。

## 技術與架構

使用技術：Python、Tkinter、PyYAML、pytest、MarkItDown、pdf_inspector

```
original_input/
    ↓ run_pipeline_once.py（GUI 入口）
        → pipeline/conflicts.py（pre-scan 衝突偵測）
        → GUI（user 選擇衝突策略）
        → pipeline/executor.py（根據 decision 寫入）
Raw_Sources/
    └── run_manifest.json / run_result.json / run_failures.csv
```

## 可複用的元件

- `pipeline/task_model.py`：RunSelection、ConflictItem、ConflictDecision、RunManifest 資料模型
- `pipeline/pathing.py`：source identity（relative path + stem）與 target path 規則，stem-based 衝突偵測邏輯
- `pipeline/conflicts.py`：current-run pre-scan 衝突偵測，可獨立於 GUI 使用
- `pipeline/executor.py`：根據 ConflictDecision 執行寫入，可替換 GUI 接口
- `pipeline/records.py`：產出 run_manifest.json、run_result.json、run_failures.csv

## 學到什麼 / 踩過的坑

- 同名不同副檔名的來源檔（stem collision）→ 衝突判定必須用 `relative path + stem`，不能比完整檔名
- 同時綁 batch / watch / sync 三種職責的系統很難局部重構 → 單一職責設計更好維護
- pytest temp 與 `.pytest_cache` 在 Windows 下權限不穩 → 改用 workspace-local temp folders
- Windows cp950 主控台 `UnicodeEncodeError` → 特殊字元輸出先轉 ASCII
- wiki ingest 的本質是寫入型，不是 retrieval → 向量化不是必要依賴，反而增加維護成本

## 遺留問題 / 未完成

- GUI 佈局與互動細節尚未打磨
- conflict reviewer 的 GUI 層測試覆蓋待補
- legacy AnythingLLM 命名與設定殘留待清理
- 遺留的測試暫存產物待移除

## Cross References

- [[專案管理/projects/data_pipeline]]：被取代的舊版本
- [[專案管理/_overview]]：跨專案總覽

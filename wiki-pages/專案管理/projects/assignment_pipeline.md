---
type: project
status: active
last_updated: 2026-05-13
time: 2025-04
tech_stack:
  - Python
  - Gemini CLI
  - Google Docs API
  - Google Workspace MCP
  - fire-pdf
depends_on: []
feeds_into:
  - Google Docs
---

# assignment_pipeline

PDF 作業題目 → Gemini 分析 → Google Docs 輸出的自動化管線。支援 watch mode 監聽資料夾自動處理新下載的 PDF。

## 専案任務

課程作業題目都是 PDF，每次需要手動開 PDF、閱讀、思考、再打開 Google Docs 記錄分析結果，流程繁瑣。自動化 PDF 解析 → AI 分析 → 文件輸出，把重複性操作壓縮到最低。

## Briefing（原始需求）

給一個 PDF（或 watch 一個資料夾），自動：
1. fire-pdf 解析 PDF 文字
2. Gemini CLI 分析作業內容
3. 建立 Google Doc，輸出分析結果
4. 支援 watch 模式，新下載的 PDF 自動觸發

## 成品描述

Python CLI 工具（`run_assignment_pipeline.py`）：
- 單次模式：`--pdf` 指定 PDF 路徑
- Watch 模式：`--watch` 監聽資料夾，新 PDF 自動處理
- 輸出：archived markdown + prompt artifact + Gemini output + Google Doc URL

基本功能完成，可自用。

## 技術與架構

使用技術：Python、Gemini CLI、Google Docs API、Google Workspace MCP、fire-pdf

```
PDF 檔案（--pdf 參數或 watch 模式）
    ↓ fire-pdf（PDF 文字解析）
    ↓ Gemini CLI（作業內容分析）
    ↓ Google Docs API（建立輸出文件）
輸出：archived markdown + prompt artifact + Gemini output + Google Doc URL
```

執行方式：
```powershell
# 單次
python run_assignment_pipeline.py --pdf "path/to/file.pdf"

# Watch 模式
python run_assignment_pipeline.py --watch "D:\Downloads"
```

相依工具：`gws`（Google Workspace CLI）、`gemini`（Gemini CLI）、`fire-pdf`

## 學到什麼 / 踩過的坑

（此專案較新，踩坑記錄待補）

## 遺留問題 / 未完成

- Watch 模式穩定性有待長期使用驗證
- image-based PDF 的處理能力取決於 fire-pdf + Gemini 的 multi-modal 能力

## Cross References

- [[專案管理/_overview]]：跨專案總覽

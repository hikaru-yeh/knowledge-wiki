---
source: session | 2026-05-15
status: wiki
tags: [skill-design, backward-compatibility, document-format]
last_updated: 2026-05-15
---

# Migration Guard Pattern

> 當文件/skill 格式升版時，自動偵測舊格式並就地 migrate，不破壞現有內容。

## 問題描述

Skill 或工具升版後新增欄位（例如 Markdown 表格加一欄），導致舊格式文件與新版 skill 的輸出不相容：

- 舊 header：4 欄
- 新 skill 追加的行：5 欄
- 結果：Markdown table 欄位錯位，渲染破掉

## 解法

在「追加新行」之前，先執行格式版本偵測：

```
追加前先檢查 header 欄位數：
- 舊格式（N 欄）→ 先 migrate header，再補全所有現有資料行，再追加新行
- 新格式（N+1 欄）→ 直接追加
```

### 實例：agent-handoff 架構決策表格

舊格式（4 欄）：
```markdown
| 決策 | 選擇 | 原因 | 日期 |
|------|------|------|------|
| 資料庫 | SQLite | 單機使用 | 2025-01-01 |
```

新格式（5 欄）加入「狀態」欄，migrate 步驟：
1. Header 改為 `| 決策 | 選擇 | 原因 | 狀態 | 日期 |`
2. 所有現有資料行在「原因」欄後插入 `active`
3. 再追加新行

## 適用場景

- Markdown 表格新增欄位
- Frontmatter 新增必填 key
- Skill 文件格式跨版本升級（新版 skill 讀取舊版產出）

## 注意事項

- **不刪舊行**：migrate 只補欄位，不改內容
- **預設值**：補入的欄位填合理預設（`active`、`unknown`、空字串），不留空
- **冪等**：同一文件執行兩次 migrate 結果相同（偵測到新格式直接跳過）

## 目前使用專案

- `agent-handoff` skill MEMORY.md（2026-05-15）：架構決策表格 4→5 欄

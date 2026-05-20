# 専案管理規則

knowledge-wiki 的 `wiki-pages/専案管理/` 操作規則。被 `CLAUDE.md` / `AGENTS.md` 的 `### 専案管理` section 引用。

---

## 事實來源

兩條更新路徑：

1. **Ingest 路徑**（project-wrap skill 產出）：
   `raw/cc_projects/` → `wiki-pages/専案管理/projects/`

2. **直接更新路徑**（從對話提供資訊）：
   對話 → `wiki-pages/専案管理/projects/` 或 `adr/` / `patterns/` / `errors/`

---

## 全域忽略

`wiki-pages/専案管理/*/README.md` 為格式說明文件，不列入知識頁計數，不 ingest。

---

## 専案快照頁格式（projects/*.md）

### Frontmatter

```yaml
---
type: project
status: active | legacy | archived | paused
last_updated: YYYY-MM-DD
time: YYYY-MM
tech_stack:
  - Python
  - Claude API
depends_on:
  - project_a
feeds_into:
  - project_b
---
```

### 正文段落（依序）

**## 専案任務**
為什麼做這個？要解決什麼問題？背景脈絡？

**## Briefing（原始需求）**
從 session 對話或文件中提取的最初需求描述。
多階段專案可加「後續調整」子段落記錄需求演變。

**## 成品描述**
最終做出來的東西長什麼樣？目前完成度？主要功能？

**## 技術與架構**
```
使用技術：[list]
架構說明：text diagram 或流程步驟
```

**## 可複用的元件**（選填）
project-level 元件紀錄，比 `patterns/` 更細，含 file path。
- `ComponentName`（`path/to/file.py`）：用途與複用方式

**## 學到什麼 / 踩過的坑**
- 問題描述 → 解法或結論

**## 遺留問題 / 未完成**
- 功能或問題：現況說明

**## Cross References**
- [[専案管理/_overview]]
- [[専案管理/projects/related]]（如有依賴關係）

---

## ADR 格式（adr/adr_<slug>.md）

```yaml
---
type: adr
status: active | superseded | deprecated
last_updated: YYYY-MM-DD
---
```

正文：背景 → 決策 → 後果 → 目前狀態

---

## Pattern 格式（patterns/pattern_<slug>.md）

格式：問題描述 → 解法 → 程式碼片段（選填）→ 目前使用專案

---

## Error log 格式（errors/error_<slug>.md）

格式：症狀 → 根因 → 修法 → 預防措施 → 出現過的專案

---

## 操作模式

### Ingest（raw/cc_projects → wiki-pages/専案管理/projects）

`raw/cc_projects/` 由 project-wrap skill 寫入，LLM 將其 ingest 為結構化 wiki 頁。

1. 讀取 `raw/cc_projects/project_<name>.md`。
2. 依「専案快照頁格式」建立或更新 `wiki-pages/専案管理/projects/<name>.md`。
   - 已存在 → Merge（見「Merge 規則」），不覆蓋。
   - 不存在 → 依格式建立新頁，**draft-first**（見下）。
3. 同步索引（見「索引同步規則」）。
4. log：`## [YYYY-MM-DD] 専案管理 ingest | project_<name>`

### 手動更新（從對話直接寫入）

觸發詞：「更新 X 狀態」「記錄這個 ADR」「把這個 pattern 存」「記錄這個坑」「新增專案 Y」

1. 確認類型（projects/ / adr/ / patterns/ / errors/）。
2. 提出變更摘要（新增什麼、更新哪些欄位）。
3. 等待使用者核准（well-specified 任務可直接執行）。
4. 寫入對應位置。
5. 同步索引（視變更範圍）。
6. log：`## [YYYY-MM-DD] 専案管理 update | <類型> | <名稱>`

---

## Draft-first 規則

建立或大幅改寫 `projects/` 頁面前，必須先給使用者確認草稿，再寫入。
ADR / pattern / error 頁面變更量小時，可直接執行。

---

## Merge 規則（既有頁面）

若 `wiki-pages/専案管理/projects/<name>.md` 已存在：
- 讀取現有內容。
- 新 session 資訊（新 Briefing 段落、成品更新、踩坑、遺留問題）**追加**，不刪除舊段落。
- 更新 `last_updated`。
- 只有使用者明確要求時才刪除舊段落。

---

## 索引同步規則

每次新增或更新 `projects/` 頁面時，同步以下四個位置：

| 檔案 | 更新內容 |
|------|---------|
| `wiki-pages/専案管理/_overview.md` | 狀態表格列 |
| `wiki-pages/index/専案管理-索引.md` | 專案表格 |
| `wiki-pages/index/總索引.md` | 専案管理列計數 |
| `_Claude_Code/PROJECTS.md` | 對應列（AI context 層） |

---

## Ingest 保留度例外

`専案管理/` 頁面不套用「Ingest 保留度分級」規則。
`raw/cc_projects/` 來源稿套用本文件的「専案快照頁格式」，而非一般 ingest 規則。

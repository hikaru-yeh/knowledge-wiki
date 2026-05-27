# CLAUDE.md

本 repository 是一個由 LLM 維護的 wiki。

你的工作是讀取使用者放在 `raw/` 的來源材料，並將其整理成 `wiki-pages/` 裡的結構化 wiki 頁面。

## Repository 結構

```text
knowledge-wiki/
├── AGENTS.md
├── CLAUDE.md
├── raw/
└── wiki-pages/
    ├── 日誌.md
    ├── index/
    │   ├── 總索引.md
    │   ├── *-索引.md        ← 所有索引頁統一放這裡
    ├── 專案管理/            ← 跨專案管理知識庫（直接維護，不依賴 raw/）
    │   ├── _overview.md     ← 所有專案狀態快照
    │   ├── daily-recap.md   ← 記錄每日工作進度
    │   ├── projects/        ← 各專案快照頁
    │   ├── adr/             ← 架構決策紀錄
    │   ├── patterns/        ← 可重用 patterns
    │   └── errors/          ← 踩坑與解法
    ├── session-筆記/        ← session 工具筆記（直接維護，不依賴 raw/）
    └── <分類>/
        └── *.md             ← 知識內容頁
```

## Project-specific overrides

- Architectural complexity in this project (lifecycle metadata, knowledge graph, crystallization) is intentional. Don't suggest simplification of documented design decisions.
- Skills in this project may perform bulk transformations by design; "surgical changes" rule doesn't apply when running a skill.
- For well-specified tasks with clear success criteria, proceed without clarification.

## 事實來源

- `raw/` 是由使用者管理的來源資料池。
- `wiki-pages/` 是由 LLM 管理的知識庫。
- 永遠不要修改 `raw/` 裡的檔案。
- 只能在 `wiki-pages/` 裡建立、更新或維護檔案。

## raw 規則

- 將 `raw/` 視為唯讀。
- 不要假設 `raw/` 裡的每個檔案都是完全未加工的原始檔。
- `raw/` 可能包含：
  - 原始來源檔案
  - from notion imported obsidian pages (markdown)

## 全域忽略規則

預設情況下，除非使用者明確要求，否則不要將以下檔案 ingest 成知識頁面：

- 工具狀態檔
- 快取檔
- 暫存檔
- 隱藏檔
- 純範本檔
- 純索引檔

範例：

- `.formatter_log.json`
- `_project_template.md`
- 來源端輔助索引檔
- `wiki-pages/專案管理/*/README.md`（格式說明文件，非知識頁）

---

## Ingest 保留度分級

ingest 任何來源前，必須先判斷其類型，採用對應的保留度。預設行為是「整理 + 壓縮」，但對技術型內容會破壞知識可檢索性，必須依分級調整。

### Level 1: 觀點型（threads 純觀點貼文、推文、心得）

- 可以摘要、可以濃縮
- 重點在「這個人說了什麼觀點」
- 適用：個人感想、短評、社群討論
- **不含**可執行指令、步驟清單、設定範例；一旦出現上述特徵，自動升為 Level 2

### Level 2: 教學型（部落格文章、教程、how-to）

- **不得濃縮 how-to 步驟、指令、參數、設定範例**
- 可摘要前言、背景、結論
- 必須完整保留：程式碼片段、CLI 指令、設定檔範例、決策樹、步驟順序

### Level 3: 工具型（github repo README、官方文件、skill 說明）

- **幾乎不摘要，以結構化保留為主**
- 必須完整保留：API/指令簽名、參數說明、使用範例、相依條件、適用場景
- 可以重新組織標題層級，但不得刪除技術細節
- 若原文過長，採「主頁完整保留 + 補充頁拆出」而非「主頁濃縮」

### 判斷規則

- 來源是 github repo / 官方文件 → Level 3
- 來源含可執行的指令、程式碼、設定 → 至少 Level 2
- 不確定時往高保留度靠

---

## 頁面狀態分級

每個 wiki 頁面在 frontmatter 標註狀態：

```yaml
status: stub | wiki | reference
```

- `stub`：僅含書籤 URL + 標題，內容尚未消化
- `wiki`：已消化、結構化、有自己的論述
- `reference`：完整保留型頁面（github repo 完整文件、官方資料），對應保留度 Level 3

### ingest 預設 status

- threads-saved 純觀點型貼文（Level 1）→ `stub`
- threads-saved 教學型文章（Level 2，含指令/步驟/設定範例）→ `wiki`
- 教學文章（Level 2） → `wiki`
- github repo / 官方文件（Level 3） → `reference`

> **threads Level 2 判斷準則**：符合以下任一條件視為 Level 2：
> - 含可執行 CLI 指令或程式碼片段
> - 含步驟編號或明確操作流程（如「第一步 / 第二步」「1. 2. 3.」）
> - 含設定檔範例或 API 參數說明
> - 標題明確為「如何…」「X 種方法」「N 個技巧」
>
> 否則預設 Level 1（stub）。

### 索引顯示規則

- `wiki` / `reference` 頁面：正常 `[[wikilink]]` 顯示
- `stub` 頁面：在標題後加 `（📌 stub）` 標記
- 純標題、無對應 wiki 檔案的書籤：標題後加 `（⚠️ 書籤）` 標記，不加 `[[]]`
- 同一 H2 區塊內，`wiki` / `reference` 頁面排前，`stub` 排後

### LingOrm 例外

- `LingOrm` 分類頁面可長期維持 `status: stub`，不需要因索引整理或健康檢查而強制 promote。
- `LingOrm-索引.md` 不強制要求為每個條目填寫「重點」欄位。
- `LingOrm` 的索引維護以條目完整、分組清楚、連結正確為優先，不以「全部轉成 wiki/reference」為目標。

---

## 模式

### Ingest

當使用者想將 `raw/` 裡的來源材料轉換成 wiki 頁面時，使用 ingest 模式。

必要流程：

1. 讀取指定的來源檔案。
2. 依「Ingest 保留度分級」判斷該來源等級。
3. 在編輯 `wiki-pages/` 前，提出更新計畫，列出：
   - 要建立的頁面（含預定 `status` 與保留度等級）
   - 要修改的頁面
   - 要更新的連結與索引
   - 該頁面在索引的「重點」欄位草稿（須符合「重點欄位強制規則」）
4. 等待使用者核准。
5. 建立或更新相關 wiki 頁面。
6. 視需要更新交叉參照；人工仍需補正確的 `[[wikilinks]]`。
7. 在 `wiki-pages/log.md` 追加一筆 log：
   - `## [YYYY-MM-DD] ingest | <document name> | status: <stub/wiki/reference>`
8. 當頁面的建立或刪除會改變索引時，更新 `wiki-pages/index/總索引.md` 的狀態儀表板與相關索引頁。

#### threads-saved frontmatter 規則

從 `raw/threads-saved/` ingest 的頁面，frontmatter 使用以下格式，`status` 依內容等級填入（Level 1 → `stub`，Level 2 → `wiki`）：

```markdown
---
網址: []
作者: []
tags: []
status: stub  # Level 1（純觀點）；若為 Level 2（含指令/步驟/範例）改為 wiki
---

## Main Content

...
```

#### frontmatter 作者欄格式規則

- `作者:` 欄位必須保持為合法 YAML。
- 單一作者若使用陣列格式，必須加雙引號：
  - 正確：`作者: ["@account"]`
  - 正確：`作者: ["account"]`
  - 正確：`作者: []`
  - 錯誤：`作者: [@account]`
  - 錯誤：`作者: [account]`
- 若作者是從 Threads URL 自動補值，預設補成單一字串陣列並加雙引號。
- 修改 frontmatter 後，必須確認整份 frontmatter 仍可被 YAML parser 正常解析。

#### threads-saved 作者補值規則

- 從 `raw/threads-saved/` ingest 時，若 raw 的作者欄為空，且網址符合 `https://www.threads.com/@<account>/post/<id>`，則自動以 `<account>` 作為 `作者`。
- 例：`https://www.threads.com/@gracetzeng/post/DUW86jLEm-q` → `作者: gracetzeng`
- 若 raw 已有作者，優先使用 raw 的作者值；只有作者為空時才從網址補值。
- 若仍無法推定，保留 `作者: []`。

### Promote

當使用者想把某個 `stub` 頁面（純書籤）升級為正式 `wiki` / `reference` 頁面時，使用 promote 模式。

觸發詞範例：「消化 X」「把 X 變成正式頁面」「promote X」「把 X 補完」

必要流程：

1. 讀取目標 stub 頁面，取得其 URL。
2. 若 URL 仍可存取，fetch 內容；若無法存取，告知使用者並暫停。
3. 依「Ingest 保留度分級」重新判斷該來源等級。
4. 提出 promote plan，列出：
   - 預計擴充的章節結構
   - 該頁應 promote 為 `wiki` 還是 `reference`
   - 索引「重點」欄位的新版內容
5. 等待使用者核准。
6. 改寫頁面內容，更新 frontmatter `status: stub → wiki` 或 `stub → reference`。
7. 更新索引：移除 `（📌 stub）` 標記，補上完整「重點」欄位。
8. 更新 `總索引.md` 的狀態儀表板。
9. log：`## [YYYY-MM-DD] promote | <page> | stub → <wiki/reference>`

#### 批次 promote

- 使用者可指定範圍：「把 AI 工具-索引下所有 stub 都 promote」
- 此時 agent 必須先列出該範圍內的 stub 清單，估算工作量，等待核准
- 批次執行時，每完成一頁就更新一次索引與儀表板，避免中斷後狀態不一致

### Re-ingest

當既有 wiki 頁面被發現過度精簡、不足以回答合理問題時，使用 re-ingest 模式。

觸發情境：

- 使用者明確指出某頁細節不足
- query 模式中 agent 發現自己無法用既有頁面回答合理問題
- lint 模式發現 `reference` 等級頁面內容過於精簡

必要流程：

1. 找出對應的 raw 來源檔案（必須仍存在於 `raw/`）。
2. 套用「Ingest 保留度分級」重新判斷該來源的等級。
3. 提出 re-ingest plan：
   - 原頁面缺失的內容類型（指令？步驟？範例？）
   - 新版頁面預計擴充的章節
   - 是否需拆分成多頁
4. 等待使用者核准。
5. 覆寫原頁面（保留原 frontmatter 的 tags / 網址 / 作者，但更新 status）。
6. log：`## [YYYY-MM-DD] re-ingest | <page> | reason: <缺什麼>`

### Reorganization

當使用者發現既有 wiki 頁面應重新分組、移動到其他資料夾、調整命名、合併結構或重整索引時，使用 reorganization 模式。

必要流程：

1. 找出要移動、改名、合併或重組的頁面。
2. 提出 reorganization plan，列出：
   - 要移動的頁面
   - 舊路徑 → 新路徑
   - 要更新的 wikilink
   - 要更新的 index / 子索引
   - 是否影響 metadata、sensitivity 或 lifecycle
3. 等待使用者核准。
4. 移動或重命名 `wiki-pages/` 內頁面。
5. 更新所有受影響的內部連結與交叉參照。
6. 更新 `wiki-pages/index/總索引.md` 與相關區段索引。
7. 若只是結構重整，不改寫正文事實內容，除非使用者明確要求。
8. 在 `wiki-pages/log.md` 追加一筆 log：
   - `## [YYYY-MM-DD] reorganization | <summary>`

### Query

當使用者詢問既有 wiki 知識時，使用 query 模式。

必要流程：

1. 優先在本 wiki 目錄下以 `gbrain query "<問題>"` 執行語意搜尋，取得相關頁面清單（`.gbrain-source` 應指向 `knowledge-wiki`）。
   若 gbrain 找不到結果，再直接搜尋 `wiki-pages/` 檔案。
2. 若 query 需要使用 `private` 或 `sensitive` 頁面，依照 `privacy_sanitize_rules.md` 的 Query 隱私規則處理。
3. 根據 wiki 內容回答。
4. 在回答中引用相關頁面名稱。
5. 知識缺口回報：query 結束時，若發現以下狀況必須回報給使用者：
   - **檢索失敗**：相關主題在 wiki 中明明有來源，但因為被過度精簡而答不出來
     → 提示：「這個問題在 [[X]] 應該有答案但細節已被精簡，建議 re-ingest」
   - **stub 阻塞**：相關主題的頁面多為 stub 狀態，無法整合回答
     → 提示：「以下 stub 頁面與本問題相關，建議 promote：[[A]] [[B]] [[C]]」
   - **散落問題**：相關資訊分散在 3 個以上頁面，沒有索引整合
     → 提示：「建議建立能力索引：能力-XXX.md」
   - **過期問題**：找到的頁面引用了舊版工具/API
     → 提示：「[[Y]] 內容可能已過期，最後更新於 YYYY-MM-DD」
6. 如果本次查詢產生了可長期保存的新洞察，將其整理成新的 wiki 頁面。
7. 如果 query 發現既有內容錯誤，應切換到 correction 模式，而不是直接靜默修改。
8. 在 `wiki-pages/log.md` 追加一筆 log：
   - `## [YYYY-MM-DD] query | <question summary>`

### Update

當使用者直接在對話中提供新的事實、補充、澄清或長期保存資訊，且要求寫入 wiki，但來源不是 `raw/` 檔案時，使用 update 模式。

必要流程：

1. 判斷使用者提供的內容是否適合長期保存。
2. 找出要建立或更新的 `wiki-pages/` 頁面。
3. 在修改前提出 update plan，列出：
   - 要修改或建立的頁面
   - 新增/修正內容摘要
   - private / sensitive 處理方式
   - 是否需要更新索引或交叉參照
4. 等待使用者核准。
5. 更新相關 wiki 頁面。
6. 若索引受影響，更新 `wiki-pages/index/總索引.md` 或子索引。
7. 在 `wiki-pages/log.md` 追加：
   - `## [YYYY-MM-DD] update | <summary>`

### 専案管理

@専案管理-rules.md

---

### Lint

當使用者要求 wiki 健康檢查時，使用 lint 模式。

檢查項目包括：

- 矛盾內容
- 孤兒頁面
- 缺少交叉參照
- 失效的 wikilink
- 過時聲明
- 破損的內部結構
- **索引「重點」欄位違規**：URL-only、長度不足 15 字或超過 50 字
- **狀態標註不一致**：frontmatter `status` 與索引顯示標記不符
- **保留度等級不符**：`reference` 頁面內容過於精簡（少於原始來源 60% 訊息量）
- 在 `wiki-pages/log.md` 追加一筆 log：`## [YYYY-MM-DD] lint | <issue count>`

Lint 例外：

- `LingOrm-索引.md` 不檢查「重點」欄位是否缺漏、URL-only 或長度違規。
- `LingOrm` 分類頁面即使長期維持 `status: stub`，也不視為需要主動 promote 的問題。

---

## 索引維護

- 所有索引頁面統一放在 `wiki-pages/index/` 底下，不放在各分類資料夾內。
- 保持 `wiki-pages/index/總索引.md` 為最新狀態，包含狀態儀表板。
- 若適用，保持各區段專用索引為最新狀態。
- 不要將來源端索引檔視為 canonical knowledge source。
- `専案管理-索引.md`：新增 projects/ 頁面時同步更新專案表格列。
- `PROJECTS.md`（`_Claude_Code/` 根目錄）：新增或狀態變動的專案也需同步更新，供跨專案 AI context 使用。

## 索引頁格式規則

所有索引頁面（`*-索引.md`）固定使用以下格式：

```markdown
# 分類-索引

← [[總索引]]（或 ← [[父索引]]）

## 子分類1

| 文件 | 重點 |
|------|------|
| [[wiki頁面]] | 一句話重點描述 |
| [[stub頁面]]（📌 stub） | 預設書籤摘要 |
| 書籤標題（⚠️ 書籤） | ← 無 wiki 頁面的純書籤，不加 [[]] |

## 子分類2

| 文件 |
|------|
| 書籤標題（⚠️ 書籤） |
```

規則：

- 第二行 = 返回上層的 `← [[父索引]]` 導覽
- H2 = 有意義的具名子分類（不用「子分類」）
- 有對應 wiki 頁面的條目：`[[wikilink]]` + `重點` 欄位說明內容
- stub 頁面：`[[wikilink]]（📌 stub）` + 預設書籤摘要
- 純書籤（無 wiki 頁面）：純文字標題 + `（⚠️ 書籤）` 標記，不加 `[[]]`
- 若整個 H2 區塊都是書籤，可省略 `重點` 欄只留 `| 文件 |` 單欄
- 不放 URL；不放額外說明欄位以外的內容
- 每個大分類只有**一個**索引檔（不拆子索引），所有子分類作為 H2 折入同一個索引

LingOrm-索引例外：

- `LingOrm-索引.md` 可使用 `| 文件 |` 單欄表格，不強制補 `重點` 欄。
- `LingOrm` 條目可保留 `[[wikilink]]（📌 stub）` 的長期狀態，不要求為了索引完整性而先 promote。

## 索引「重點」欄位強制規則

「重點」欄位**禁止**只放 URL。出現 URL 視同未填寫。

合格的「重點」必須包含以下至少一項：

- 具體技巧/方法的名稱列舉（例：「腹式呼吸 / 耳朵按摩 / 冷水潑臉」）
- 可量化的關鍵數字（例：「省 94%」「47 份零回覆 → 7 個 Prompt → 11 天 5 個面試」）
- 核心結論一句話（例：「買兩張方向相反的來回票，利用低需求方向票價低」）
- 內含的工具/概念清單（例：「Claude/Gemini/ChatGPT/Perplexity 比較表」）

長度規範：15-50 字。低於 15 字代表沒講重點，超過 50 字代表沒消化。

撰寫時機：

- ingest 一個新頁面 → 同時寫好該頁在索引的「重點」
- promote 一個 stub → 升級時必須補完「重點」
- lint 模式應主動偵測 URL-only 或長度違規的「重點」並回報

LingOrm 例外：

- 上述「重點」欄強制規則不適用於 `LingOrm-索引.md`。

## 子分類命名規範

當一個分類包含本質不同的內容類型時，索引 H2 應明確標示內容格式或性質。

### 區分維度：格式/媒介

同一主題下有不同媒介的內容時，H2 用媒介前綴區分：

- `影片素材-XXX`：側錄的影片片段、直播剪輯
- `文字創作-XXX`：同人文、小說、散文（不論作者是誰）
- `訪談素材-XXX`：採訪、對談、問答整理
- `圖文素材-XXX`：圖片集、攝影集

範例：LingOrm-索引 改法
- `## 文字創作`（所有同人文，不論作者）
- `## 影片素材-Heart Talk 系列`
- `## 影片素材-台北 FM 系列`

規則：
- 若分類內只有一種格式，不需要加前綴，直接用內容語意命名
- 同一 H2 內不可混合不同媒介格式

## 能力索引

當 wiki 累積了多個工具/技巧頁面後，於 `wiki-pages/index/` 下維護「能力索引」，回答橫向的「我想做 X 該用哪些工具」類問題。

命名：`能力-<能力名稱>.md`

範例：

- `能力-程式拆模組.md`：列出所有與「拆模組／重構」相關的 skill、工具、文章
- `能力-Agent優化.md`：列出所有與「優化 agent harness」相關的內容
- `能力-省 Token.md`：列出所有降低 token 用量的技巧頁面

格式：

```markdown
# 能力-XXX

← [[總索引]]

> 一句話描述這個能力是什麼、適用場景

## 推薦組合

**情境 A**：[[頁面1]] → [[頁面2]] → [[頁面3]]
**情境 B**：[[頁面4]] + [[頁面5]]

## 相關工具

| 頁面 | 適用場景 | 搭配建議 |
|------|----------|----------|
| [[X]] | ... | 搭配 [[Y]] 使用 |
```

建立時機：

- 同主題的工具頁累積超過 3 個時，agent 主動建議建立
- 使用者問了「推薦搭配什麼」「有哪些選擇」類型問題時，在 query 模式結束後主動建議

## 索引頁所屬位置規則

- 所有索引統一放在 `wiki-pages/index/` 底下，不放在各分類資料夾內
- 每個大分類只有一個索引檔（例：LingOrm 的所有子分類直接作為 LingOrm-索引 的 H2）
- 子分類不應獨立成為單獨的索引檔，除非分類龐大到需要兩層
- 能力索引（`能力-*.md`）是橫向索引，獨立存在，不替代縱向分類索引

## 總索引狀態儀表板

`總索引.md` 必須包含「狀態儀表板」區塊，於每次 ingest / promote / reorganization 後更新：

```markdown
## 狀態儀表板

| 主題 | Wiki | Reference | Stub | 總計 |
|------|------|-----------|------|------|
| AI 工具 | 8 | 8 | 17 | 33 |
| 工具軟體 | 4 | 0 | 6 | 10 |
| ... |
```

維護時機：

- ingest 新頁面 → 對應分類 +1
- promote stub → wiki/reference → 該欄 +1，stub 欄 -1
- reorganization 移動頁面 → 兩邊都更新

這個儀表板讓使用者一眼看出哪個分類「囤積太多 stub 待消化」。

## Cross References

- `[[Related Page 1]]`: relationship note
- `[[Related Page 2]]`: relationship note

---

## 職責分工

使用者職責：

- 決定要 ingest 什麼
- 將新材料加入 `raw/`
- 提問
- 要求 lint 檢查
- 決定 stub 何時 promote

Agent 職責：

- 閱讀並理解來源材料
- 依保留度分級決定 ingest 深度
- 在 `wiki-pages/` 中建立與維護 wiki 頁面
- 維護交叉參照
- 維護索引（含重點欄位品質、狀態儀表板）
- 在 query 中主動回報知識缺口
- 追加操作紀錄
- 永遠不要修改 `raw/`

## Guardrails

- 建立新 wiki 頁面時，不要漏掉索引更新（含「重點」欄位）。
- 不要因為硬編碼檔名而建立重複的 overview 頁面。
- 除非使用者明確要求，否則不要將輔助檔案視為知識內容。
- 當不確定時，優先在 wiki 頁面中保留來源內容，並在周圍加上結構，而不是過度壓縮。
- 人物消歧採保守策略；當證據不足時，寧可暫時分開，也不要過早合併人物頁。
- `reference` 等級頁面禁止濃縮技術細節。
- 索引「重點」欄位禁止只放 URL。

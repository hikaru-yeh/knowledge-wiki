# MEMORY
> 這個 project 的長效記憶，每次 session 累積更新
> 最後更新：2026-05-12

## 專案概覽
這個 project 會把 Threads 書籤匯出資料轉成 Markdown 筆記，輸出到本地筆記資料夾。主要流程是讀取 `scribe.json` 類型的書籤輸入，必要時用 Playwright 補抓原作者續貼，再做 Gemini 分類、Gemini 標題生成，最後寫成固定格式的 Markdown。技術棧以 Python 為主，測試用 `pytest`，LLM 目前使用 Gemini。

## 架構決策
| 決策 | 選擇 | 原因 | 日期 |
|------|------|------|------|
| 輸入最小必要欄位 | `postUrl`、`authorHandle`、`contentText` | 其餘欄位不影響 v1 主流程 | 2026-05-09 |
| 內容補完策略 | 書籤為主，Playwright 補抓原作者留言 | 很多 Threads 內容是主文 + 作者續貼才完整 | 2026-05-09 |
| Playwright 失敗策略 | fallback 到原始 `contentText` | 不因單篇抓取失敗中斷整體匯入 | 2026-05-09 |
| Gemini 失敗策略 | per-item 隔離，不 fail-fast | 單筆失敗不中斷整批；failed_count 正確計數 | 2026-05-12 |
| Markdown 輸出方式 | 全部平鋪到固定輸出資料夾 | 使用者要求不要按分類或作者分資料夾 | 2026-05-09 |
| 檔名衝突策略 | 自動加尾碼 | 保留所有輸出，不覆蓋舊檔 | 2026-05-09 |
| 作者留言抽取 | 同時支援 `@handle` block 與 logged-out `plain handle + timestamp + · + Author` | Threads 頁面文字形狀已變，單一路徑會漏抓 | 2026-05-11 |
| 主文選擇策略 | 若已成功抽到作者 blocks，第一個 block 優先作為主文 | 書籤 seed 常帶 `1/5` 或與 live text 有些微差異 | 2026-05-11 |
| 分類優先規則 | LingOrm / AI / 職場 先做 rule-based hints | 降低常見誤判，提高穩定性 | 2026-05-11 |
| Gemini SDK | `google.genai` | `google.generativeai` 已棄用，需遷移到官方新 SDK | 2026-05-11 |
| 分類策略 | Gemini-first | 本地 rule-based 會因寬鬆字串命中造成系統性誤判，改由 Gemini 做最終分類 | 2026-05-11 |
| 輸出去重策略 | 依 markdown 內的 `url:` 欄位判斷是否已處理過 | 不能只靠標題檔名；同 URL 每次標題不同會累積多份輸出 | 2026-05-11 |
| output 目錄 | `D:\shane_yeh\Documents\_Claude_Code\knowledge-wiki\raw\threads` | 從 llm-notes 遷移；config.py DEFAULT_OUTPUT_DIR 已更新 | 2026-05-12 |

## 規範
### 命名
- 分類名稱必須來自固定清單，不允許自由字串漂移。
- `Ling` / `Orm` / `LingOrm` / `00k` 在標題中應保留拉丁字母寫法，不要翻成中文。

### Claude Code / AI 分類邊界（已確認）
- 內容明確談論 Claude Code 功能、skill、hook 的具體用法 → `Claude Code`
- 內容談論多種 AI 工具 / agent 生態，或 Claude 只是被提及的工具之一而非主角 → `AI`

### 格式 / 流程
- Markdown frontmatter 採英文 snake_case key + 引號值：
  ```
  ---
  url: "https://..."
  author: "@handle"
  clip_type: "分類名稱"
  ---
  ```
- 作者留言抽取採寬鬆策略：只要是原作者在該貼文下的留言就收進來，不做過度聰明的 `1/3`、`2/3` 判讀。
- 事件日誌同時保留 console log 與 `threads_events.jsonl`。
- 本地 `samples/scribe.json` 是使用者環境樣本，不納入版本控制。
- 直接跑 `app.py` 時，預設 input 是 `samples/scribe.json`。
- 清理重複輸出時，優先移到 timestamped backup 資料夾，不直接刪除。

## 踩過的坑
- **Threads logged-out body shape 改變**（2026-05-11）：整批作者留言都抓不到 → 原因是 extractor 只認舊的 `@handle` block → 解法是新增 `plain handle + timestamp + · + Author` 路徑並保留舊路徑。
- **續貼 marker 污染主文**（2026-05-11）：書籤 seed 常含 `1/5`，導致主文升級失敗或主文重複 → 解法是清理獨立一行與行尾黏著的 continuation marker，並在成功抽到作者 blocks 時優先使用第一個 block 作主文。
- **LingOrm 標題被翻成中文**（2026-05-11）：Gemini 會把 `Ling` / `Orm` 翻成中文 → 解法是在 title prompt 明確禁止，並對 LingOrm 類別做已知 transliteration 還原。
- **CARL / STAR 類內容被誤歸到 AI**（2026-05-11）：因為有英文框架詞，容易被模糊判成工具內容 → 解法是新增 `面試 / behavioural / STAR / CARL / recruiter / hiring manager` 的 `職場` 規則。
- **寬鬆子字串規則污染分類**（2026-05-11）：`formulas` 命中 `orm`、`mcp` 命中 `cp`、`SessionStart` / GitHub stars 命中 `star`，導致本地 rule-based 在 Gemini 之前先誤判 → 解法是放棄 rule-first，改成 Gemini-first。
- **同 URL 會留下多個不同檔名版本**（2026-05-11）：rerun 時只靠標題生成檔名，沒有用 `source_url` 去重；只要標題每次稍有變化就會產生新檔 → 解法是先掃 output 中 markdown 的 `url:` 欄位，已存在的 URL 直接 skip。
- **output dir 不一致導致 skip 失效**（2026-05-12）：舊 default (`llm-notes`) 和 env var (`knowledge-wiki`) 不同，skip 機制讀錯目錄，導致 knowledge-wiki 累積 29 個重複 URL → 解法是 DEFAULT_OUTPUT_DIR 改為 `knowledge-wiki`；另一 session 負責清理已存在的重複。
- **Gemini `response.text` 是 `None` 不是 absent**（2026-05-12）：`getattr(response, 'text', '')` 無效，屬性存在但值為 `None`，呼叫 `.strip()` 會 AttributeError → 解法是改用 `(response.text or "")`。
- **心理健康類貼文觸發 PROHIBITED_CONTENT**（2026-05-12）：Gemini 把純標題生成請求視為有問題的內容生成 → 解法是 title prompt 加入 `「{category}」類別` 讓 Gemini 理解這是分類任務。

## 排除的方向
- 不走自由生成分類字串：會造成分類飄移、難以管理。
- 不把 Gemini 產生的標題寫進 Markdown 正文：使用者只要檔名用途。
- 不把輸出按分類或作者分資料夾：使用者要求全部平鋪。
- 不再採用本地 rule-based 先決定分類：即使可降低成本，也會在真實內容中放大錯誤。

## 環境 / 依賴
- 專案根目錄 `.env` 會自動載入，提供 `GEMINI_API_KEY` 與模型設定。
- 目前 LLM client 使用 `google.genai`。
- Playwright 需要能正常抓取 Threads 公開頁面的 `body` text。
- output 目錄：`D:\shane_yeh\Documents\_Claude_Code\knowledge-wiki\raw\threads`（config.py DEFAULT_OUTPUT_DIR，可用 `THREADS_MARKDOWN_OUTPUT` env var 覆蓋）。

## 未解決的問題
- [ ] 仍有 6 篇 `random20` 樣本是 `reply_fetch_no_author_replies`，需要人工確認是真沒有作者續貼，還是尚有未覆蓋的新頁面 text shape。
- [ ] knowledge-wiki\raw\threads 現有 29 個重複 URL（另一 session 處理中）。

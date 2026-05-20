---
status: wiki
last_updated: 2026-05-15
---

# Daily Recap

Short-term working memory for tomorrow-you. Entries are grouped by project, with newest entries first inside each project.

## Inbox / Misc / Harness

### 2026-05-15 18:33 - Codex 安全設定文件改寫

#### 快速掃讀
- 現在狀態: 已把 Claude Code 版安全設定指引改寫成 Codex 版，輸出成工作區內的 `codex-safety-setup-guide.md`。
- 今天做完: 用 Context7 查 `/openai/codex`，再用官方 Codex docs 交叉確認 `config.toml`、`approval_policy`、`sandbox_mode`、`rules/default.rules`、Windows TOML 路徑引號規則。
- 明天第一步: 如果要實際套用到本機，先檢查 `~/.codex/config.toml` 和 `~/.codex/rules/default.rules` 現況，再備份後合併，不要整檔覆蓋。
- 卡住或待決: 尚未實際修改使用者的 `~/.codex/config.toml` 或 `~/.codex/rules/default.rules`；目前只是產出改寫後的指引文件。
- 重要路徑/連結: `C:\Users\shane_yeh\Documents\Codex\2026-05-15\codex-settings-json-config-toml-contex7\codex-safety-setup-guide.md`；官方文件包含 `https://developers.openai.com/codex/config-reference`、`https://developers.openai.com/codex/config-basic`、`https://developers.openai.com/codex/agent-approvals-security`、`https://developers.openai.com/codex/rules`。

#### 完整脈絡
**原始目標 / 為什麼做**
- 使用者貼了一份 Claude Code 安全三件套安裝指引，要求把路徑、名稱與語法改成適合 Codex 的內容，特別提醒 `settings.json` 的語法不能直接照搬進 `config.toml`，並要求使用 Context7 查正確寫法。
- 背景坑點是 Claude Code 的 `~/.claude/settings.json`、`permissions.deny`、`Bash(...)` deny list 與 Codex 的設定模型完全不同。Codex 使用 `~/.codex/config.toml` 管 sandbox/approval，命令 allow/deny 則用 `~/.codex/rules/default.rules` 的 `prefix_rule`。

**今天的推理與決策**
- 決策: 把 Claude 的 `permissions.deny = ["Bash(...)"]` 改寫成 Codex rules 檔。
  原因: Context7 與官方 Codex docs 顯示 Codex rules 用 `prefix_rule(pattern = [...], decision = "forbidden")`，且 rules 檔不是 TOML，也不是 JSON。
  排除: 沒有把 deny list 塞進 `config.toml`，因為那會是錯誤語法與錯誤設定模型。
- 決策: 把權限模式改成 `approval_policy` + `sandbox_mode` 對照，而不是 `permissions.defaultMode`。
  原因: Codex 官方 config reference 寫的是 `approval_policy = "untrusted" | "on-request" | "never"` 與 `sandbox_mode = "read-only" | "workspace-write" | "danger-full-access"`。
  排除: 沒有保留 Claude 的 Accept Edits / Default / Plan / Bypass 原語義；只保留對應說明。
- 決策: Windows 路徑範例強制用 TOML 單引號字串。
  原因: 使用者的 AGENTS.md 明確要求 Windows 反斜線路徑必須用單引號；雙引號會把 `\n`、`\U` 等當成跳脫序列或導致 TOML parse error。
  排除: 沒有使用 `command = "C:\path\to\exe"` 這類會壞的範例。
- 決策: 對 `Bash(: >*)` 類 shell redirection 不假裝能直接用 prefix rule 完整阻擋。
  原因: Codex rules 比對 argv prefix，`>` 是 shell redirection，不是一般 argv；官方 rules docs 說 shell wrapper 遇到 redirection 等進階語法時會保守處理。
  排除: 沒有寫出假的 `pattern = [":", ">"]` 保護。

**做過的事**
- 讀取並套用 `context7-mcp` skill。
- 透過 Context7 查 `/openai/codex`，取得 `approval_policy`、`sandbox_mode`、`sandbox_workspace_write.network_access` 等 config 範例。
- 另外用官方 Codex docs 查 `Configuration Reference`、`Config basics`、`Agent approvals & security`、`Rules`，確認:
  - user config 在 `~/.codex/config.toml`
  - project config 可在 `.codex/config.toml`
  - rules 在 `~/.codex/rules/default.rules`
  - `prefix_rule` 支援 `allow`、`prompt`、`forbidden`
  - workspace-write 預設網路關閉，可用 `[sandbox_workspace_write] network_access = true/false`
- 新增 `codex-safety-setup-guide.md`，內容包含:
  - Claude → Codex 對照表
  - TOML Windows 路徑單引號規則
  - Windows PowerShell 資源回收筒版 `rm` 保護
  - macOS/Linux/WSL 的 trash 方案
  - Codex `.rules` forbidden 規則
  - Codex 權限模式選擇與 `config.toml` 範例
  - MCP server Windows path 正確範例
  - 踩坑紀錄與官方參考連結
- 用 `rg` sanity check，確認 `~/.claude/settings.json`、`permissions.deny`、`Bash(...)` 只出現在警示與對照段落，不是安裝步驟。
- 用 `where.exe codex` 確認本機有 Codex executable，但沒有實際跑 `execpolicy check`，因為目前只是文件改寫。

**已試過但不要重試**
- 不要用 `jq` 修改 `~/.codex/config.toml`；那是 TOML，不是 JSON。
- 不要把 Claude Code 的 `permissions.deny` 陣列貼進 Codex。
- 不要把 rules 內容貼進 `config.toml`；rules 檔是 `~/.codex/rules/default.rules`。
- 不要在 TOML 裡用雙引號包 Windows 反斜線路徑。
- 不要假設 `Bash(: >*)` 可以一比一翻成 Codex prefix rule。

**檔案 / 指令 / 測試**
- `C:\Users\shane_yeh\Documents\Codex\2026-05-15\codex-settings-json-config-toml-contex7\codex-safety-setup-guide.md` - 新增的 Codex 版安全設定指引。
- `Get-Content -Raw C:\Users\shane_yeh\.agents\skills\context7-mcp\SKILL.md` - 讀取 Context7 skill 使用方式。
- `mcp__context7__.resolve_library_id` - 查到官方 `/openai/codex`。
- `mcp__context7__.query_docs` - 查 Codex config/sandbox/approval 寫法。
- `rg -n "\.claude|settings\.json|permissions\.deny|Bash\(|jq|AskUserQuestion|config\.toml|default\.rules" codex-safety-setup-guide.md` - 結果: 殘留 Claude 字樣只在警示、對照、踩坑段落。
- `where.exe codex` - 結果: 找到 `C:\Users\shane_yeh\AppData\Local\OpenAI\Codex\bin\codex.exe` 等 Codex executable。

**未完成與下一步**
- [ ] 若使用者要「實際安裝」而不是文件改寫，先讀取現有 `~/.codex/config.toml` 與 `~/.codex/rules/default.rules`。
- [ ] 實際改本機設定前，先建立 timestamp backup。
- [ ] 合併 rules 時要避免重複 table 或重複規則，尤其 Codex app 對 duplicate TOML table 可能不友善。
- [ ] 實際套用後用 `codex execpolicy check --pretty --rules ~/.codex/rules/default.rules -- rm -rf test-folder` 驗證 forbidden。
- [ ] 視使用者平台決定是否套用 PowerShell `rm` 到資源回收筒，或 WSL/macOS/Linux 的 `trash-cli`。

**明天恢復狀態時要記得**
- 這次成果是「改寫文件」，不是「已套用到本機 Codex 設定」。
- `codex-safety-setup-guide.md` 是主要產物，可以直接打開續改。
- Codex 正確心智模型: `config.toml` 管預設模型、sandbox、approval、MCP；`.rules` 管命令前綴 allow/prompt/forbidden。
- 使用者特別在意 TOML Windows 路徑引號，未來任何 `config.toml` 例子都要用單引號包反斜線路徑。

### 2026-05-15 17:19 - PROJECT_Shane Wiki「Prompt is too long」根因修復

#### 快速掃讀
- 現在狀態: 兩個重複載入 bug 已修復，context 節省 ~18.4KB/session。
- 今天做完: 找到 3 個根因、修復 2 個，加上操作性建議 /compact。
- 明天第一步: 開新 PROJECT_Shane Wiki session 驗證不再溢出。
- 卡住或待決: 無。
- 重要路徑/連結:
  - `D:\shane_yeh\Documents\_Claude_Code\CLAUDE.md` — 已移除 `@gemini-usage.md`
  - `D:\shane_yeh\Documents\_Claude_Code\PROJECT_Shane Wiki\AGENTS.md` — 已 stub 為 3 行

#### 完整脈絡
**原始目標 / 為什麼做**
- PROJECT_Shane Wiki session 中送出單字 prompt 就出現 `API Error: Prompt is too long`。
- 需要找到是什麼讓 base context 或 session context 溢出，並修復。

**今天的推理與決策**
- 決策: 移除 `_Claude_Code/CLAUDE.md` 中的 `@gemini-usage.md`。
  原因: `gemini-usage.md`（6,443 bytes）完全相同的內容被載入兩次——一次從全域 `~/.claude/CLAUDE.md`，一次從 parent `_Claude_Code/CLAUDE.md`；diff = 0 行差異。
  排除: 刪除其中一個檔案（保留 @ 引用路徑彈性）。
- 決策: 將 `PROJECT_Shane Wiki/AGENTS.md` stub 為 3 行 redirect。
  原因: Claude Code 同時自動載入 `CLAUDE.md` 與 `AGENTS.md`（cross-agent 相容性）。兩者只有第一行標題不同，12,402 bytes 幾乎完全重複。
  排除: 完全刪除 AGENTS.md（其他 agent 可能需要讀它）。
- 決策: 建議長 session 中使用 `/compact`（操作性建議，未自動設定）。
  原因: 讀取多個 rule file（lifecycle 5KB、privacy 8KB、course_project 14KB）+ source file + skill injection 後，history 逐漸逼近上限。

**做過的事**
- 用 diff 確認 AGENTS.md vs CLAUDE.md 只有第一行不同。
- 用 diff 確認兩份 gemini-usage.md 完全相同（0 行差異）。
- 確認 `_Claude_Code/CLAUDE.md` 的 `@gemini-usage.md` 行，移除之。
- 將 `AGENTS.md` 覆寫為 3 行 stub。

**已試過但不要重試**
- 無錯誤嘗試。

**檔案 / 指令 / 測試**
- `D:\shane_yeh\Documents\_Claude_Code\CLAUDE.md` — 刪除 `@gemini-usage.md` 行，節省 6.4KB/session。
- `D:\shane_yeh\Documents\_Claude_Code\PROJECT_Shane Wiki\AGENTS.md` — stub：`See CLAUDE.md for full wiki agent instructions.`，節省 12KB/session。

**未完成與下一步**
- [ ] 開新 session 在 PROJECT_Shane Wiki 做一次 wiki operation，確認不再溢出。
- [ ] 若仍有問題，考慮將 `course_project_ingest_rules.md`（13.9KB）改為懶載入（只在 ingest 時 read，不放入 CLAUDE.md @ 引用）。

**明天恢復狀態時要記得**
- `gemini-usage.md` 現在只從全域 `~/.claude/` 載入一次。
- `AGENTS.md` 在 PROJECT_Shane Wiki 是 stub，內容不再重複 CLAUDE.md。
- 長 session 做 wiki ingest 前，先 `/compact` 壓縮 history。
- rule file 讀取都計入 session context history，每個 Read tool call 的結果都留在 conversation 中。

### 2026-05-15 - Codex skill YAML 修復（agent-handoff + gemini-use）

#### 快速掃讀
- 現在狀態: 兩個 Codex skill 的 YAML frontmatter 已修復，可正常載入。
- 今天做完: 修復 `agent-handoff/SKILL.md` 多行 description 語法錯誤；補齊 `gemini-use/SKILL.md` 缺少的 frontmatter 分隔符。
- 明天第一步: 無待續任務；若 Codex 還報其他 skill 錯誤，照相同模式處理。
- 卡住或待決: 無。
- 重要路徑/連結: `C:\Users\shane_yeh\.codex\skills\agent-handoff\SKILL.md`；`C:\Users\shane_yeh\.agents\skills\gemini-use\SKILL.md`

#### 完整脈絡
**原始目標 / 為什麼做**
- Codex 報了兩個 skill 載入錯誤，導致這兩個 skill 無法使用。

**今天的推理與決策**
- 決策: `agent-handoff` description 用 YAML 折疊區塊純量 `>-` 處理多行。
  原因: 原始 description 跨兩行但沒有縮排，YAML parser 把第二行視為新 key 卻找不到 `:`，報 `could not find expected ':'`。
  排除: 合併成單行（太長）、雙引號包裹（需 escape 中文標點內的特殊字元）。
- 決策: `gemini-use` 補上完整 frontmatter block（name + description + 上下 `---`）。
  原因: 該檔案直接從 `# LLM Wiki...` 開始，完全沒有 frontmatter，Codex skill loader 找不到必要欄位。
  排除: 無其他選項，必須加 frontmatter。

**做過的事**
- 讀兩個檔案，確認各自錯誤根因。
- `agent-handoff/SKILL.md` line 3-4: 將 `description: ...` 改為 `description: >-\n  ...\n  ...`。
- `gemini-use/SKILL.md` 第一行前: 插入 `---\nname: gemini-use\ndescription: ...\n---`。

**已試過但不要重試**
- 無。

**檔案 / 指令 / 測試**
- `C:\Users\shane_yeh\.codex\skills\agent-handoff\SKILL.md` - YAML `>-` folded block 修復 description。
- `C:\Users\shane_yeh\.agents\skills\gemini-use\SKILL.md` - 新增 frontmatter `---` block。

**未完成與下一步**
- [ ] 無，若 Codex 仍報其他 skill 錯誤再處理。

**明天恢復狀態時要記得**
- YAML frontmatter 中 description 跨行必須用 `>-` 或 `|` block scalar 並縮排，不能直接換行。
- Codex skill loader 嚴格要求 frontmatter `---` 分隔符存在。

---

### 2026-05-15 00:47 - daily-recap skill 設計與安裝

#### 快速掃讀
- 現在狀態: 已建立並安裝 `daily-recap` skill，目標是給隔天的我快速恢復工作狀態。
- 今天做完: 用 `interview-me` 釐清需求、閱讀 knowledge-wiki 架構、決定固定單一頁與 project 分組格式、建立 skill 與插入 helper。
- 明天第一步: 用 `/daily-recap` 或要求「daily recap」時，檢查 `D:\shane_yeh\Documents\_Claude_Code\knowledge-wiki\wiki-pages\專案管理\daily-recap.md` 是否有最新 entry。
- 卡住或待決: 無重大 blocker；之後可視使用習慣調整 section 名稱或 project 分組規則。
- 重要路徑/連結: `C:\Users\shane_yeh\.codex\skills\daily-recap`；`D:\shane_yeh\Documents\_Claude_Code\knowledge-wiki\wiki-pages\專案管理\daily-recap.md`

#### 完整脈絡
**原始目標 / 為什麼做**
- 我有 ADHD，可以同時處理多個 projects、harness 問題或零散工作，但隔天可能忘記做過的決策、進度與原因。
- 既有工具已有 `project-wrap` 和 `agent-handoff`，但缺少「隔天的我本人」每天短期看的工作記憶。
- 這個 skill 的目的不是長期沉澱知識，也不是給 agent 接手，而是讓明天的我能不用重新推理昨天的脈絡。

**今天的推理與決策**
- 決策: 讀者是隔天的我本人。
  原因: `agent-handoff` 已服務 agent，這個缺口是 human-facing working memory。
  排除: 不以 agent 或長期 wiki 讀者為主要對象。
- 決策: recap 固定寫入單一頁 `wiki-pages/專案管理/daily-recap.md`。
  原因: 單一入口比每天資料夾更容易找到，降低 ADHD 的搜尋與分類成本。
  排除: `raw/`、`wiki-pages/日誌.md`、每日資料夾、每 project 分檔。
- 決策: 頁面內容用 project 做 H2 分組，每個 project 底下新的 daily recap 放最上方。
  原因: 可以沿著同一條工作線回看，但仍維持單一入口。
  排除: 依日期分組或日期資料夾。
- 決策: 不屬於明確 project 的內容放固定 `## Inbox / Misc / Harness`。
  原因: harness、工具設定、臨時研究和 meta-work 不應被迫歸類，否則會增加紀錄摩擦。
- 決策: 每篇 entry 同時包含 `快速掃讀` 和 `完整脈絡`。
  原因: 我不想依賴 AI 判斷何者是「必要時」才需要保留；寧可多記，也不要明天接不起來。
- 決策: skill 直接寫入，不先產草稿確認。
  原因: 結束對話時要低摩擦，否則容易不做；這是短期工作記憶，不是長期正式知識頁。

**做過的事**
- 讀取並套用 `interview-me` skill，逐步確認真正需求。
- 閱讀 `D:\shane_yeh\Documents\_Claude_Code\knowledge-wiki\AGENTS.md`、wiki 目錄架構、`専案管理-rules.md`、`專案管理-索引.md`、`_overview.md`、`日誌.md`。
- 判斷 daily recap 最適合放在 `wiki-pages/專案管理/`，但不放入 `projects/`、`adr/`、`patterns/`、`errors/`。
- 讀取 `project-wrap` 與 `agent-handoff`，確認新 skill 的邊界。
- 使用 `skill-creator` / `write-a-skill` 指南建立 skill。
- 初始化並安裝 `daily-recap` skill 到 `C:\Users\shane_yeh\.codex\skills\daily-recap`。
- 新增 `scripts/insert_daily_recap.py`，用來建立目標頁、建立 H2 project heading，並把新 entry 插到該 heading 下方最上面。

**已試過但不要重試**
- 不要把這類短期 recap 放進 `wiki-pages/日誌.md`；那是 wiki 操作日誌。
- 不要放進 `raw/cc_projects/`；那是 `project-wrap` 的來源稿入口。
- 不要拆成每天資料夾；使用者已明確拒絕。
- 不要只做快速摘要；使用者明確要求同時保留完整脈絡。

**檔案 / 指令 / 測試**
- `C:\Users\shane_yeh\.codex\skills\daily-recap\SKILL.md` - 新 skill 主指令。
- `C:\Users\shane_yeh\.codex\skills\daily-recap\scripts\insert_daily_recap.py` - Markdown 插入 helper。
- `python ...\quick_validate.py ...\skill-staging\daily-recap` - 第一次因 Windows 預設 cp950 讀 UTF-8 中文失敗。
- `$env:PYTHONUTF8='1'; python ...\quick_validate.py ...\daily-recap` - 驗證通過。
- `insert_daily_recap.py` staging 測試 - 成功建立測試 recap，並插入 `## Inbox / Misc / Harness`。

**未完成與下一步**
- [ ] 未來使用幾次後，觀察 `快速掃讀` / `完整脈絡` 的欄位是否需要微調。
- [ ] 若 entries 變多，可以再加固定索引或 archive 規則，但現在先保持單一檔案。

**明天恢復狀態時要記得**
- 這個 skill 的核心價值是「不要讓 AI 替我過度篩選」，所以完整脈絡要保留 WHY、替代方案、排除原因、已試過的路徑。
- 如果之後要叫它，最自然的觸發詞是 `/daily-recap`、`daily recap`、`幫我記到明天看的 recap`、或「把這段存進 daily recap」。


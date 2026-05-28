---
status: wiki
---

# Wiki 操作日誌

## [2026-05-28] promote | 7 AI 工具 stubs batch promoted | stub→wiki

Pages: AI-企業作業系統降臨：一人公司時代來了、AI進化超速，專業者們辛苦了、Paperclip：你的-AI-虛擬公司，預算全自動、Vibe-Coding-亂象與工程師的心累、擺脫糊字！AI簡報組合技、用Obsidian建立你的LLM知識庫、開發者，別再浪費-tokens。總索引儀表板 AI 工具 Wiki 209→216，Stub 12→5。

## [2026-05-28] ingest | 工程師最常用的 12 個 Claude Code 指令 | status: wiki

來源：raw/threads-iphone/threads-unknown-20260511-120328.md 與 threads-unknown-20260511-120523.md（兩個 raw 檔指向同一 URL）。WebFetch 成功抓取部分內容：帖文可見文字、互動數據、主題確認（12 個 Claude Code 指令快捷鍵）；速查表以圖片呈現無法抽取文字。合併成一頁 wiki，存於 wiki-pages/AI 工具/Claude-Code/工程師最常用的 12 個 Claude Code 指令.md，作者 @this.web，Level 2（含指令/速查表），status: wiki。AI 工具-索引 Claude Code 社群帖子區塊新增條目。

## [2026-05-28] reorganization | Delete 3 empty wiki pages; promote 擲杯技巧 stub→wiki; keep 有用免費證照 & 職涯分析Prompt as stubs (Threads auth required, raw files empty)

Deleted: wiki-pages/AI 工具/147個AI員工，一鍵部署玩轉.md、wiki-pages/健康生活/壺鈴運動.md、wiki-pages/健康生活/練肩.md。Promoted: wiki-pages/生活雜記/擲杯技巧.md（stub→wiki，用戶已手動補全內容）。Updated indexes: AI 工具-索引（移除 147 條目）、健康生活-索引（移除壺鈴運動 & 練肩）、生活雜記-索引（擲杯技巧升格並補重點欄）。

## [2026-05-27] qa | Post-cleanup QA closeout

AI 工具直層 content quality cleanup 完成收斂。已完成批次：D1（5 stub）/ D2（8 頁：2 enriched + 1 noise-cleaned + 5 stub）/ E0（2 index fix）/ E1（9 作者欄）/ E2（2 off-topic → 生活雜記）/ E3B（3 stub）/ E4A-1（4 re-ingest：3 reference + 1 wiki）/ E4A-2（1 Substack re-ingest）。Final state：Wiki 357 / Reference 28 / Stub 99 / Total 484；AI 工具 208/23/13=244。Remaining 3 頁 blocked on Threads refetch（AI專家員工庫 / Obsidian-+-Claudian / Claude-整合-10-大工具）+ 5 blocked content gap stubs + index duplicate H2 tooling follow-up。

## [2026-05-27] repair | frontmatter 作者欄 YAML 修復

全站掃描並修復 `wiki-pages/**/*.md` 的 frontmatter `作者:` 欄：將 `作者: [@handle]` 與 `作者: [handle]` 統一改為合法 YAML 格式 `作者: ["@handle"]`，保留 `作者: []` 不變。完成後以 YAML parser 驗證 `wiki-pages/` 下 510 個含 frontmatter 的 Markdown 檔，結果為 0 parse error。同步在 `CLAUDE.md` 補充作者欄 frontmatter 格式規則，避免後續再次寫出非法 YAML。

## [2026-05-27] qa | E4A-2：1 頁 Substack source re-ingest

`九天打造-Hermes-AI` 用 Keith Rumjahn Substack 完整教學（rumjahn.substack.com/p/complete-guide-to-mastering-hermes）補齊內容：安裝設定、LLM 三選項、Telegram 整合、Souls/Agents/User 三層配置、cron jobs、Apple Health/Gmail/Calendar 實戰、Hermes+OpenClaw 雙 Agent 架構、成本 $64/week→$20/month。Status 維持 wiki（教學型 Level 2）。AI 工具-索引 2 條目改 MD relative link + 更新重點。總索引不變。

## [2026-05-27] qa | E4A-1：4 頁 public-source re-ingest

4 頁用公開來源補齊內容：`guizang-ppt-skill`（github.com/op7418/guizang-ppt-skill → reference）、`AI-管家養成`（farceurliu.github.io/ai-butler-handbook → wiki）、`AI流程圖神器`（github.com/yizhiyanhua-ai/fireworks-tech-graph → reference）、`AI-Agent-範本大補帖`（github.com/Shubhamsaboo/awesome-llm-apps → reference）。AI 工具-索引 8 條目改 MD relative link + 更新重點。總索引：AI 工具 Wiki 211→208, Ref 20→23。全域 Wiki 360→357, Ref 25→28。

## [2026-05-27] qa | E3B：3 頁 borderline thin wiki → stub

3 頁從 `status: wiki` 降回 `status: stub`：`Paperclip：你的-AI-虛擬公司，預算全自動`（極短，只描述一個功能）、`超好看開源日式風格Skill`（~5 行，無 repo 連結/步驟）、`擺脫糊字！AI簡報組合技`（3 工具名稱 + 一行說明）。AI 工具-索引 6 條目改 MD relative link + `（📌 stub）`。總索引：AI 工具 Wiki 214→211, Stub 10→13。全域 Wiki 363→360, Stub 96→99。

## [2026-05-27] qa | E2：off-topic reorganization（WBC台灣 + 測你文字 → 生活雜記）

2 頁從 `wiki-pages/AI 工具/` 搬到 `wiki-pages/生活雜記/`：`WBC台灣：地獄開局湘北魂不滅`（棒球，非 AI）、`測你文字的語感色溫`（心理測驗，非 AI 工具）。AI 工具-索引刪 4 條目（duplicate sections 各 2），生活雜記-索引新增 2 條目（Markdown relative link，raw/ 同名）。總索引：AI 工具 Wiki 216→214 / 244，生活雜記 Wiki 20→22 / 23。Status 不變（wiki）。

## [2026-05-27] qa | E1：作者欄 @ 前綴修正（8 頁）

8 頁 frontmatter `作者:` 欄從 `[handle]` 修正為 `[@handle]`：AI助頂尖研究員（daydayaitools）、WBC台灣（hellokenneth）、Mac離線AI字幕（mtmcy_ig）、Awesome Design System（ai_cpocoder）、簡報地獄有救（___o.h.___）、擺脫糊字（yofish.read）、測你文字（mosan_form）、NotebookLM 10大框架（futurecommerce_official）。A1 全 9 頁完成（含 D2 已修 用Obsidian/iiaiuii）。

## [2026-05-27] qa | E0：AI-免費課程 + Claude-整合 index wikilink → MD relative link

AI 工具-索引 4 處 bare `[[wikilink]]` 改為 Markdown relative link（AI-免費課程驚豔登場 ×2、Claude-整合-10-大工具 ×2）。原因：兩頁皆有 `raw/threads/` 同名檔，需避免 Obsidian 連結歧義。Status 不變（皆 wiki），總索引不動。

## [2026-05-27] qa | D2 完成：AI-員工速成 / Threads-API / 開發者別再浪費tokens 降 stub

Batch D2 最後 3 頁全部從 `status: wiki` 降回 `status: stub`：`AI-員工速成：Claude-+-Obsidian-密技大公開`（1 句 teaser，無外部連結）、`Threads-API`（GitHub URL 截斷）、`開發者，別再浪費-tokens`（3 個 GitHub URL 全截斷）。`AI 工具-索引` 六處條目改為 Markdown relative link 並補 `（📌 stub）`。總索引：AI 工具 Wiki 219→216、Stub 7→10；全域 Wiki 366→363、Stub 93→96。Batch D2 全 8 頁處理完畢。

## [2026-05-26] qa | D2：Google-AI-Agents 公開來源補 wiki + 用Obsidian 降 stub

`Google-AI-Agents-Vibe-Coding-攻略與報名` fetch Netlify 頁成功，頁面含完整課程資訊（五日主題 / 7 步報名 / 工具清單 / Capstone 證書），已補成正式 wiki 內容，保持 `status: wiki`。`用Obsidian建立你的LLM知識庫` fetch CF Pages 結果為 portfolio landing page，無 PDF 或教學內容，從 `status: wiki` 降回 `status: stub`，順修作者欄 `@` 前綴。`AI 工具-索引` 四處條目更新（含 raw 同名 Markdown relative link）。總索引：AI 工具 Wiki 220→219、Stub 6→7；全域 Wiki 367→366、Stub 92→93。D2 剩餘 3 頁未動。

## [2026-05-26] qa | D2：AI-企業作業系統降臨 downgrade + Claude-整合-10-大工具 noise-clean

`AI-企業作業系統降臨：一人公司時代來了` 從 `status: wiki` 降回 `status: stub`（X URL 不明，無法 refetch，內容純 hype 無步驟）；`AI 工具-索引` 兩處條目改為 Markdown relative link 並補 `（📌 stub）`。`Claude-整合-10-大工具，AI-幫你做` 維持 `status: wiki`，移除 20+ 重複導流留言噪音，保留主文 10 工具清單；索引重點欄更新。總索引更新：AI 工具 Wiki 221→220、Stub 5→6；全域 Wiki 368→367、Stub 91→92。D2 其餘 5 頁未動；raw/ 未修改；未 stage/commit。

## [2026-05-26] qa | Batch D2：AI 免費課程頁補 GitHub repo 內容

將 `AI-免費課程驚豔登場，付費課程情何以堪` 從 3 句 Threads 摘要補成基於 `rohitg00/ai-engineering-from-scratch` README 的 wiki 頁，清掉截斷 `github.com/rohit…`，新增完整 GitHub source link。頁面維持 `status: wiki`，並更新 `AI 工具-索引.md` 中兩處既有條目的重點欄；未處理其他 D2 頁、未改 raw、未更新總索引。

## [2026-05-26] qa | Batch D1 direct downgrade：AI 工具 5 頁 wiki → stub

依 `tasks/content-quality-audit.md` 的 Batch D1，將 `147個AI員工，一鍵部署玩轉`、`AI伴學：知識壁壘已破`、`AI寫文口頭禪`、`AI進化超速，專業者們辛苦了`、`Vibe-Coding-亂象與工程師的心累` 由 `status: wiki` 降回 `status: stub`。`AI 工具-索引.md` 對應條目補回 `（📌 stub）`，且因 raw/ 同名風險改為 Markdown relative link。總索引重算為 Wiki 368 / Reference 25 / Stub 91；未處理 D2、off-topic、作者欄格式或邊緣案例。

## [2026-05-26] final | Wiki cleanup final scan passed

- duplicate URL = 0（全輪已解消）
- Task 7 links fixed：生活雜記 / 旅遊美食 / 健康生活 / 求職履歷 / 動漫 raw-ambiguous bare wikilink 全數轉為 Markdown relative link
- promote-ready non-LingOrm stubs completed：Batch A 29 + Batch B 52 = 81 頁已 promote
- remaining non-LingOrm stubs = 6 blocked content gaps（擲杯技巧 / 壺鈴運動 / 練肩 / 有用免費證照 / 職涯分析Prompt / Thariq-在-X）
- LingOrm stubs = 80 retained（永久豁免）
- 總索引：Wiki 373 / Reference 25 / Stub 86
- raw/ dirty 為 separate pipeline，commit 時需 selective add 排除 raw/ 路徑

## [2026-05-26] update | Finding 4：AI 工具-索引 19 個 < 15 字重點欄批次更新，涵蓋 AI 工具社群帖子（14）、Claude Code 社群帖子（3）、Github 參考倉庫（1）、其他 AI 工具（1）

## [2026-05-26] correction | LingOrm-索引 P'Eclair apostrophe：display text 與 link target 從 U+0027 → U+2019，與實際檔名一致

## [2026-05-26] review-fix | Review council fixes：AI 工具 raw-ambiguous links、LingOrm P'Eclair link、Thariq downgrade、log order、todo parent tasks

## [2026-05-26] dashboard | Task 13c：總索引最終重算

依 `wiki-pages/` 當前實際檔案狀態重算 `wiki-pages/index/總索引.md` 的頂部摘要與狀態儀表板。更新後總數為 `Wiki 374 / Reference 25 / Stub 85`，快速導覽總頁數仍與 dashboard 加總一致為 `484`。Non-LingOrm stubs 僅剩 5 個 blocked content gaps（`擲杯技巧`、`壺鈴運動`、`練肩`、`有用免費證照`、`職涯分析Prompt`），LingOrm stubs 維持 `80`；專案管理仍只統計 `status: wiki` 的 3 頁，active/legacy 未混入儀表板。

## [2026-05-26] promote | Task 12 Batch B-3b：求職履歷 12 stubs → wiki

依 `tasks/stub-promote-inventory.md` 的剩餘清單 promote 求職履歷通過 preflight 的 12 頁：`Sherlock：數位足跡清查神器`、`Thariq-在-X`、`vibe-hardening：Vibe-Coder-一鍵資安掃描`、`中高階面試：用-HERO-展現決策者思維`、`展現影響力，突破職場天花板`、`履歷 LinkedIn AI Prompt`、`德國B2B-SaaS行銷：白話文溝通勝過技術詞彙`、`求職被拒黃金回覆：讓「不」變「是`、`為什麼離開上一份工作`、`美國求職必備四大證照`、`行天宮開條件：完美職缺神降臨`、`誰來決定？軟體業的責任黑洞`。`status: stub` 全部改為 `wiki`；`求職履歷-索引` 移除 12 個 `（📌 stub）` 並補 10 個過短重點。`有用免費證照` 與 `職涯分析Prompt` 因只有重複 `## Main Content` 轉列 blocked content gaps，保留 `status: stub`。Non-LingOrm stubs `17→5`，Blocked `3→5`，Batch B promote-ready 清空。未處理健康生活、LingOrm，也未更新 `總索引`。

## [2026-05-26] promote | Task 12 Batch B-3a：求職履歷 14 stubs → wiki

依 `tasks/stub-promote-inventory.md` 的 Batch B 順序 promote 求職履歷前 14 頁：`AI履歷，HR一眼看穿`、`AI郵報徵AI自動化研究員`、`AI模擬資深HR面試Prompt`、`AI讀寶典，為你量身打造職涯建議`、`AI驅動求職，多平台職缺匯整Notion`、`AI-爬蟲新神器-Obscura`、`Addy-Osmani-Agent-Skills-助-AI-開發更專業`、`AgentHub：下載AI員工，從此變老闆`、`Claude新手指南：你的前30分鐘`、`Codex-ralph-loop-移植：Stop-hook與CodexPotter兩條路`、`graphify-知識圖譜讓-AI-懂程式碼「為什麼」，Token-消耗狂降`、`LLM面試題遊戲化，AI即時回饋創商機`、`LinkedIn-也不想你知道：Claude-的-8-大求職利器`、`STAR與CARL面試技巧：展現適應力與反思`。`status: stub` 全部改為 `wiki`；`求職履歷-索引` 移除 14 個 `（📌 stub）` 並補 7 個過短重點。Non-LingOrm stubs `31→17`，求職履歷 Batch B `28→14`，Batch B `30→16`。未處理健康生活、LingOrm、blocked content gaps，也未更新 `總索引`。

## [2026-05-26] promote | Task 12 Batch B-2b：健康生活 9 stubs → wiki。保加利亞分腿蹲 / 大腦的四小時定律 / 年輕時就該吃的保健品 / 快速入睡方法，想像自己不斷下樓梯 / 思緒卡關？試試這些「蠢」方法，讓大腦不內耗 / 改善肩頸僵硬 / 爛痘救星！日本洗面乳大推 / 這本書的魔力與共鳴 / 高敏感：把天線插對地方。健康生活-索引 移除 9 個 stub 標記，補 8 個過短重點。壺鈴運動與練肩轉列 blocked content gaps，保留 status: stub。Non-LingOrm stubs 40→31，Batch B 39→30

## [2026-05-26] promote | Task 12 Batch B-2a：健康生活前 10 stubs → wiki。每天5分鐘，身體有感大不同 / Dayvigo：安心助眠新選擇 / 熬夜救急，肌酸補腦 / 台灣人與歐洲人的覺察差異 / 關係中的情緒課題 / 90%久坐族都不知道的腰痛真相 / ADHD女生：這些徵兆你也有嗎？ / Claude百變創作交流 / Disease- Disorder 差別 / THINK-The-user-wants-a-short,-natural-Traditional-Chinese-title-based-on-the-pr。健康生活-索引 移除 stub 標記，補 5 個過短重點。Non-LingOrm stubs 50→40，健康生活 Batch B 21→11，Batch B 49→39

## [2026-05-26] promote | Task 12 Batch B-1：動漫 3 stubs → wiki。神聖無碼帝國萬歲！ / 《直情真氣》：R-18動畫第一人稱神作 / 只是....覺得好像做了一場很長很長的夢￼。動漫-索引 移除 stub 標記，補 2 個過短重點。Non-LingOrm stubs 53→50，Batch B 52→49

## [2026-05-26] update | Task 7 Batch 2C：動漫-索引 3 個 stub 條目 bare wikilink → Markdown relative link；Task 7 Batch 2 累計 52/52 完成；僅更新 index 連結格式，保留 stub 標記與重點欄，不 promote、不改內容頁

## [2026-05-26] update | Task 7 Batch 2B：求職履歷-索引 28 個 stub 條目 bare wikilink → Markdown relative link；僅更新 index 連結格式，保留 stub 標記與重點欄，不 promote、不改內容頁

## [2026-05-26] update | Task 7 Batch 2A：健康生活-索引 21 個 stub 條目 bare wikilink → Markdown relative link；僅更新 index 連結格式，保留 stub 標記與重點欄，不 promote、不改內容頁

## [2026-05-26] update | Task 13b：總索引 dashboard 重算。Wiki 298→326（+28），Stub 162→133（-29）。健康生活 total 28→27（-1 壺鈴運動-2 刪除）。快速導覽健康生活 28→27

## [2026-05-26] promote | Task 12 Batch A-3：Batch A 最後 2 stubs → wiki。Claude 生態系指南（AI 工具/Claude-Code/）/ 自製萬用HEIC轉檔器免費送（工具軟體/）。AI 工具-索引 + 工具軟體-索引 移除 stub 標記。Batch A 清空，Non-LingOrm stubs 55→53

## [2026-05-26] promote | Task 12 Batch A-2：旅遊美食 11 stubs → wiki。台灣美食 / 泰國糯米炒飯，老饕激推！ / 生活妙招 / 口袋名單App上線，全台好店輕鬆存 / Google地圖排行程，原來可以這樣用！ / 奶茶控本命無雷推薦 / 東京大阪女同志地圖：PIAMY小冊 / 根昆布漬豆腐 / 泰國超好吃甜點奶油麵包 / 謝謝我很好吃嗎？ / 高雄美食。旅遊美食-索引 移除 stub 標記 + 補 重點。Non-LingOrm stubs 66→55，Batch A 剩 2 頁

## [2026-05-26] update | 擲杯技巧 標記為 blocked content gap：wiki page 與 raw source 皆空白，Facebook share URL 暫不 fetch，保留 status: stub；inventory 更新（Non-LingOrm stubs 81→66，Batch A 29→13，Blocked 1）

## [2026-05-26] promote | Task 12 Batch A-1：生活雜記 15 stubs → wiki。手機搶拓元攻略 / 遺產繼承不踩雷 / CIA物理學家 / Staatlichkeit / 精選網軍蟑螂黑名單 / 親台YouTube頻道 / 進擊的巨人 / 高端疫苗 / Faker / たら、ば、と、なら / 台灣原民版 / 廚房當裝飾 / 眼肉芽 / 租屋族看這 / 跑咖構圖法。擲杯技巧內容空白（雙空標題），保留 stub。生活雜記-索引 移除 stub 標記 + 補 重點，stub 排至最後

## [2026-05-26] update | Task 11C：refresh stub promote inventory。81 stubs（-1 壺鈴運動-2）。Batch A 29 / Batch B 52 / Batch C 0。台灣美食、生活妙招、自製萬用HEIC 從 Batch C 升至 Batch A（11A 已修 index lint）

## [2026-05-26] reorganization | Task 11B：刪除 壺鈴運動-2.md（duplicate orphan）。保留 壺鈴運動.md（在 健康生活-索引 ## 社群帖子）。壺鈴運動-2 無 index 條目、無 wiki cross-ref、內容近空白、URL 為同 reel 加 ?igsh 追蹤參數

## [2026-05-26] update | Task 11A：pre-promote hygiene。旅遊美食-索引：台灣美食補 stub 標記；生活妙招轉 MD relative link + stub 標記；曼谷茶冰淇淋移除誤植 stub 標記（頁面實為 wiki）。工具軟體-索引：自製萬用HEIC轉檔器免費送轉 MD relative link + stub 標記（raw 同名風險已隔離）。壺鈴運動 duplicate precheck：壺鈴運動.md（empty stub，在 index）與壺鈴運動-2.md（near-empty stub，不在 index，無 cross-ref）為同一 reel URL；建議刪除 壺鈴運動-2.md，保留 壺鈴運動.md；待使用者確認

## [2026-05-26] update | Task 11：重新產生 stub promote inventory。82 non-LingOrm stubs → Batch A 26（promote-ready）/ Batch B 52（需 Task 7 Batch 2）/ Batch C 4（需 index 修正）。80 LingOrm stubs excluded。發現壺鈴運動-2 疑似重複、旅遊美食-索引曼谷茶冰淇淋 status/標記不一致

## [2026-05-25] update | Task 13：重算總索引儀表板。3 頁補 status: stub（壺鈴運動、台灣美食、生活妙招）；專案管理 active/legacy 排除統計，加註記；全面 Grep 交叉驗證 10 分類計數

## [2026-05-25] update | post-review orphan fix：台灣美食.md 加入旅遊美食-索引 ## 台北美食（Markdown relative link）；review council 發現 orphan 後補正

## [2026-05-25] reorganization | Task 10E-2：Group 10E-2 — 刪除 台北漢堡排名.md（canonical: 臺北市漢堡）；台灣美食.md 移除 frontmatter 網址（multi-source hub）；dup groups 1→0

## [2026-05-25] reorganization | Task 10E-3：Group 10E-3 — 刪除 海外飲食.md（薄殼、不在索引、Sources 與 canonical 曼谷喝的泰奶們 完全相同）；台灣美食.md 移除 [[海外飲食]] cross ref；dup groups 2→1

## [2026-05-25] reorganization | Task 10E-1：Group 10E-1 — 生活妙招.md 移除 frontmatter 網址（多來源 hub，canonical 為 離不開的不鏽鋼小工具；Sources 保留 3 URL）；dup groups 3→2

## [2026-05-25] reorganization | Task 10D-3：Group 9 — 合併迷走神經30秒重置術進身心保健 | Vagal Tone 背景段 + 5 補充動作（TRE/輕拍/漱口/手掌遮眼/嗅聞精油）；刪除迷走神經30秒重置術.md；健康生活-索引刪 1 列；腸道失衡 cross ref 刪 1 列；dup groups 4→3

## [2026-05-25] reorganization | Task 10D-2：Group 1 — 旅遊省錢.md 移除 frontmatter 網址（多來源 hub 無單一 primary URL，Sources 保留 2 URL）；兩頁皆保留；dup groups 5→4

## [2026-05-25] reorganization | Task 10D-1：Group 13 — 刪除孤兒 健身動作.md + 核心運動.md（無 status、不在索引、0 active ref）；canonical 每天10-20分鐘把核心練起來 保留；dup groups 6→5

## [2026-05-25] reorganization | Task 10C-2：Group 2 duplicate URL cleanup | 刪除沈浸式翻譯外掛雙語字幕.md（thin shell）；日常數位工具.md 移除 frontmatter 網址（多來源 hub 無單一 primary URL，Sources 保留 3 URL）；工具軟體-索引刪 1 列；dup groups 7→6

## [2026-05-25] reorganization | Task 10C-1：合併 `減少 AI 幻覺` 進 `提示詞技巧` | 個人化 System Prompt 英文原文 2 段 + 80% 幻覺降低 + 指令品質提醒合併；刪除減少 AI 幻覺.md；AI 工具-索引刪 1 列；GPT不要順著我 cross ref [[減少 AI 幻覺]]→[[提示詞技巧]]；dup groups 8→7

## [2026-05-25] reorganization | Task 10B-3：合併 `自動化應徵工作流程` 進 `求職自動化` | 數位大腦三件套、AI Agent 自動執行、職缺篩選指令三段合併；刪除自動化應徵工作流程.md；求職履歷-索引刪 1 列、求職自動化重點更新；dup groups 9→8

## [2026-05-25] reorganization | Task 10B-2：合併 `面試流程化` 進 `面試準備` | 草案 A（六步清單 +履歷一致性/hiring manager）B（敏感問題準備）C（面試當天 Checklist）三段合併；刪除面試流程化.md；求職履歷-索引刪 1 列、面試準備重點更新；dup groups 10→9

## [2026-05-25] reorganization | Task 10B-1：刪除 `AI 助攻履歷從0面試到5面試`（canonical: 履歷優化）；求職履歷-索引刪 1 列；AI寫履歷 + AI攻略履歷 cross ref 更新；dup groups 11→10

## [2026-05-25] reorganization | Task 10A：刪除 2 個 stale duplicate URL 薄頁 | `Mac 還有什麼必裝神奇軟體`（canonical: Mac 工具）+ `開發工具`（canonical: MCP 工具）；工具軟體-索引刪 2 列；duplicate URL groups 13→11

## [2026-05-25] reorganization | Task 9：政治-索引併入生活雜記 | 5 頁 政治/ → 生活雜記/；生活雜記-索引新增 ## 時事政治（5 列 Markdown relative link）；刪除政治-索引.md + 空資料夾 政治/；總索引刪政治列、生活雜記目前 21 篇（Wiki 5、Stub 16）；Staatlichkeit cross ref 更新

## [2026-05-25] reorganization | AI 工具分類 Batch 4B：6 頁 Claude-Code/ → AI Agent/ | Hermes、Google-Agents-CLI、AI-Agent技能生態系、AI-Agent跨儲庫盲區、Harness Engineering ×2；Claude Code 社群帖子刪 6 列、AI 工具社群帖子新增 6 列（Markdown relative link）

## [2026-05-25] reorganization | AI 工具分類 Batch 4A：4 頁 Claude-Code/ → 其他 AI 工具/ | VSCode/Zed、Mac-mini-LLM、Naval AI 預言、AI會議錄音到規格；Claude Code 社群帖子刪 4 列、其他 AI 工具新增 4 列（Markdown relative link）

## [2026-05-25] reorganization | AI 工具分類 Batch 3 前置檢查完成 | 6 頁 Knowledge/RAG 類（2026年RAG、長Context RAG、人人AI知識庫、PostgreSQL打天下、AI知識庫新解方、為AI設計的筆記系統）暫不搬移，保留在其他 AI 工具/；4/6 有 raw/ 同名衝突

## [2026-05-25] reorganization | AI 工具分類 Batch 2：4 頁錯位修正 | 其他 AI 工具 → Prompt 工程（AI提示詞破除迷信、ChatGPT精煉指令、擺脫AI腔調）+ Gemini 與 NotebookLM（Shinkansen）；索引已更新

## [2026-05-25] reorganization | Task 8 Batch 1：Claude 生態系指南 | 生活雜記/ → AI 工具/Claude-Code/；生活雜記-索引刪一列、AI 工具-索引 Claude Code 社群帖子新增一列（📌 stub）；採漸進方案 C，資料夾重構延後

## [2026-05-25] reorganization | Task 8 LingOrm 搬移 | LOLO的蛋蛋大翻桌 + P'Eclair-跌櫈笑死 從 生活雜記/ 移至 LingOrm/泰百其他/；生活雜記-索引刪除兩列、LingOrm-索引泰百其他新增兩列（📌 stub）

## [2026-05-25] reorganization | 刪除 stale 工具軟體索引.md | 合併 [[開發工具]] + [[Mac 還有什麼必裝神奇軟體]] 進 canonical 工具軟體-索引.md 後刪除無 hyphen 舊檔

## [2026-05-25] reorganization | Task 7 Batch 1：修正 ambiguous bare wikilinks | 生活雜記-索引.md (19 條) + 旅遊美食-索引.md (15 條) bare [[STEM]] → [[CATEGORY/STEM|STEM]] 分類路徑別名；掃描驗證 0 ambiguous remaining；所有 34 個別名目標檔案存在；gbrain sync 已停用不再執行

## [2026-05-24] reorganization | Checkpoint A：清理還原舊檔、合併日誌與索引 | 刪除 3 個還原舊檔（神聖無碼帝國萬歲！-2.md、鄺玲玲-索引.md、AI 工具索引.md）；合併 日誌.md 歷史條目進 log.md（2026-05-07~18）後刪除 日誌.md；建立 tasks/ 執行清單（url-dedupe-inventory.md、raw-link-inventory.md、stub-promote-inventory.md）；raw-link 掃描乾淨（0 筆）；非 LingOrm stub 計數 82 個確認

## [2026-05-24] update | 索引更新 | 15個stub→wiki：生活雜記(5)+旅遊美食(4)+求職履歷(6)移除📌標記補完重點；工具軟體/AI工具各2條重點補強；儀表板 Wiki 294→309，Stub 176→161

## [2026-05-24] update | 批量注入 pending-digest-app-output 內文 | 39 個 wiki stub 頁面塞入消化後內容；17 頁 status 升為 wiki，22 頁維持 stub（純觀點 Level 1）；2 個含 U+FFFC 檔名頁面以 PowerShell 驗證寫入成功

## [2026-05-24] reorganization | Git 三大流程：廚房管理術 | 求職履歷 → 工具軟體/開發工具，status: stub → wiki

## [2026-05-24] promote | 批量 206 篇 | stub → wiki — AI 工具(192) + 工具軟體(14) | 索引已更新，儀表板 Wiki 88→294，Stub 382→176

## [2026-05-24] ingest | 批量 295 篇 raw/threads + raw/threads-saved | status: stub — AI 工具(156) / LingOrm(44) / 求職履歷(33) / 生活雜記(17) / 健康生活(16) / 旅遊美食(12) / 工具軟體(11) / 政治(4) / 動漫(2)

## [2026-05-24] promote | 批量 20 篇 | stub → wiki（8）/ reference（12）— 從 GitHub README 與部落格全文補完

### → reference（12 篇）
- Hallmark：開源設計技能 | nutlope/hallmark 1.7K stars，22 主題 + 65 slop gates
- Garry Tan GBrain | garrytan/gbrain 18.5K stars，P@5 49.1%，146K 頁生產規模
- AI 影片理解神器 | sonpiaz/watch-cli，yt-dlp+ffmpeg+Whisper 三合一
- AI寫程式架構亂？Axiom | fatelvx/axiom，靜態架構合約 4 指令 CI 攔截
- Google Skills | google/skills 10.4K stars，官方 20+ 技能模組
- 技能包大總管 | Jiang-Yude/skill-curator，4 模式 Skill 庫治理
- Claude Code 提案 HTML 化 | hanamizuki/solopreneur，/preview 互動 HTML 審核
- AI 知識庫新解方 | nashsu/llm_wiki 9K stars，4 信號圖譜 + Louvain 偵測
- OpenHuman | tinyhumansai/openhuman 26.3K stars，118 app 接入每 20 分鐘同步
- AI 工具設定管理 | skills-manager 1.6K + Plexus，15+ 工具統一管理
- 5個必裝 Codex Skill | awesome-codex 11K / repomix 25K / follow-builders 4.7K / codex++ / keep-fast
- 9 個 Claude Code 神器 | claude-mem 77.7K / ECC 189K / GSD 63K 等 9 repo

### → wiki（8 篇）
- Claude Code 的啟示 Harness | leehanchung 部落格，Thin Harness Fat Skills 原則
- AI寫程式不失控 | muki.tw，grill-with-docs / tdd / diagnose / 架構健檢 4 技能
- AI導入工程團隊 | Production vs Review vs Validation Capacity 平衡
- Shinkansen | Gemini API 翻譯，本地隱私不過第三方，保留排版 + YouTube 字幕
- Tubelens | Claude AI 一鍵摘要 / 心智圖 / 雙語字幕，免費擴充
- AI時代的閱讀系統 | raw→wiki→output 三層 + qmd 本地搜尋 + HTML 視覺化
- OpenAI Codex 使用指南 | Ask Mode 先規劃，Prompt 寫成 GitHub Issue，AGENTS.md
- Claude Code 白話入門 | 50 張 ELI5 投影片，CLAUDE.md / Hooks / MCP 比喻解說

## [2026-05-23] promote | 我的 AI 日常：多 Agent CLI 設定 | stub → wiki — 以 Arthur Yau 部落格全文補完（tmux + Tailscale + vmux PWA 設定細節）

## [2026-05-23] ingest | raw/threads/ 78 個新 threads 貼文 | status: stub (76 建立 / 2 略過：Faker、神聖無碼帝國萬歲！-2)
分類：AI 工具 AI Agent ×43、AI 工具其他 ×14、LingOrm ×2、健康生活 ×5、旅遊美食 ×2、求職履歷 ×2、工具軟體 ×3、生活雜記 ×3（新）、政治 ×1（新）、動漫 ×1（新）

## [2026-05-21] session-capture | Dagu vs Process Compose vs Node-RED | status: reference

## [2026-05-20] session-capture | Shane Wiki 人物消歧 | status: reference

## [2026-05-19] session-capture | GitHub Portfolio Repo Workflow | status: reference

## [2026-05-18] 専案管理 reorganization | 移除非本人專案頁

依使用者確認，刪除 `wiki-pages/専案管理/projects/career_ops.md` 與 `wiki-pages/専案管理/projects/claude_context_graphify_coexist.md`，因這兩者不是 Shane 自己的專案。同步移除 `_overview.md`、`専案管理-索引.md`、`總索引.md` 與 `PROJECTS.md` 中對應的專案列。

## [2026-05-18] 専案管理 update | project | scribe_treads_saved

調查 `D:\shane_yeh\Documents\_Claude_Code\PROJECT_scribe_treads_saved`，新增專案快照頁 `wiki-pages/專案管理/projects/scribe_treads_saved.md`。同步更新 `_overview.md`、`専案管理-索引.md`、`總索引.md` 與跨專案 `PROJECTS.md`。

## [2026-05-15] delete | 鄺玲玲-索引

刪除 `wiki-pages/鄺玲玲-索引.md`。LingOrm-索引 中鄺玲玲系列條目保持直接列表，無失效 wikilink。

## [2026-05-15] session-capture | AgentMemory + Drift AI | status: reference

新增兩頁至 `wiki-pages/session-筆記/`：AgentMemory vs Drift AI 全方面比較表（8 維度）、AgentMemory Windows 安裝與整合指南（iii engine、Claude Code plugin、Codex config.toml MCP 設定、51 tools、hooks、踩坑）。建立 `session-筆記-索引.md`，更新 `總索引.md`（新增 session-筆記 分類，Reference +2）。

## [2026-05-15] update | daily-recap skill 與初始短期工作記憶頁

新增 `wiki-pages/専案管理/daily-recap.md` 作為固定單一頁的短期工作記憶，供隔天的使用者依 project 分組恢復工作脈絡；同步更新 `専案管理-索引.md` 與 `總索引.md` 計數。

## [2026-05-14] 専案管理 update | adr | 5 筆架構決策紀錄

新增 5 個 ADR 頁面至 `wiki-pages/専案管理/adr/`：跨專案 KB 選址、雙層架構、橋接頁模式、規則抽離、橋接頁建立方式。同步更新 `専案管理-索引.md` 和 `_overview.md`。

## [2026-05-13] 専案管理 update | projects | 9 頁全面補全模板段落

為 `wiki-pages/専案管理/projects/` 下所有 9 個專案頁補全完整 7 段結構：専案任務、Briefing（原始需求）、成品描述、技術與架構、可複用的元件、學到什麼/踩過的坑、遺留問題/未完成。同步統一 frontmatter 加入 `type: project` 與 `time: YYYY-MM`，並將舊版「踩坑」及「下一步」改寫合入對應新段落。涉及頁面：data_pipeline、data_preprocess、threads_saved_v2、claude_context_graphify_coexist、career_ops、shane_wiki、shane_wiki_v2、assignment_pipeline、knowledge_wiki。

## [2026-05-13] update | 新增能力-多 Agent 協作與能力-Token 優化索引

建立 `wiki-pages/index/能力-多 Agent 協作.md` 與 `wiki-pages/index/能力-Token 優化.md`，從 `AI 工具-索引` 挑出與多 Agent 分工、handoff、搜尋擴充、自動循環、上下文壓縮、記憶管理與低成本工作流相關的頁面，依「新手入門 → 進階配置 → 進階技巧 → 參考實作」分組整理；同步在 `wiki-pages/index/總索引.md` 的能力索引區塊新增兩個入口。

## [2026-05-13] update | 新增能力-Agent 優化索引

建立 `wiki-pages/index/能力-Agent 優化.md`，從 `AI 工具-索引` 挑出與 Claude Code / Codex harness、配置、工作流相關的頁面，依「新手入門 → 進階配置 → 進階技巧 → 參考實作」分組整理；同步在 `wiki-pages/index/總索引.md` 新增能力索引入口，方便後續查找與 stub promote 規劃。

## [2026-05-13] update | 健康生活-索引重點欄修正

掃描 `wiki-pages/index/健康生活-索引.md`，在刪除 `[[壺鈴運動]]` 後，修正剩餘 2 個「重點」欄為 URL-only 的條目，改寫為符合 15-50 字規則的有效摘要：`起床降低皮質醇五步`、`雙下巴消失運動`。

## [2026-05-13] reorganization | 刪除健康生活索引中的壺鈴運動條目

`wiki-pages/index/健康生活-索引.md` 中的 `[[壺鈴運動]]` 僅為索引條目，實際不存在對應 wiki 頁面，因此依使用者要求將該條目刪除。保留其他頁面中的外部來源引用，不改動 `raw/`。

## [2026-05-12] update | 求職履歷-索引重點欄修正

掃描 `wiki-pages/index/求職履歷-索引.md`，修正 3 個「重點」欄為 URL-only 的條目，改寫為符合 15-50 字規則的有效摘要：`面試流程化`、`面試到最後被問到 WhyShouldWeHireYou`、`自動化應徵工作流程`。

## [2026-05-12] update | 工具軟體-索引重點欄修正

掃描 `wiki-pages/index/工具軟體-索引.md`，修正 3 個「重點」欄為 URL-only 的條目，改寫為符合 15-50 字規則的有效摘要：`MacBook Superpower 多功能視窗切換`、`沈浸式翻譯外掛雙語字幕`、`Gmail 進階搜尋字串`。

## [2026-05-12] update | AI 工具-索引重點欄修正與補建缺頁

掃描 `wiki-pages/index/AI 工具-索引.md`，修正 4 個「重點」欄為 URL-only 的條目，改寫為符合 15-50 字規則的有效摘要。同步補建缺失頁面 `wiki-pages/AI 工具/Prompt 工程/GPT 不要順著我指令技巧.md`；因 `raw/threads-saved/` 僅保留標題與網址，頁面正文以保守主題整理方式落成，並明記來源缺口。

## [2026-05-12] reorganization | 索引檔命名統一為 *-索引

將 `wiki-pages/index/AI 工具索引.md` 改名為 `wiki-pages/index/AI 工具-索引.md`，`wiki-pages/index/工具軟體索引.md` 改名為 `wiki-pages/index/工具軟體-索引.md`，統一與其餘索引頁的 `*-索引.md` 命名風格。同步更新全站對 `AI 工具索引` 與 `工具軟體索引` 的 wikilink 引用，以及 `總索引.md` 的快速導覽連結。

## [2026-05-12] promote | 非 LingOrm stub 批次 promote 與同源去重 | stub → wiki

將 `LingOrm` 以外 11 個 `status: stub` 頁面批次處理：7 頁直接升級為 `wiki`，4 頁與既有正式頁同源者完成 canonical 去重。保留 `MCP 工具`、`Mac 工具`、`臺北市漢堡`、`每天10-20分鐘把核心練起來` 作為正式頁名；刪除重複頁 `最受歡迎的5大Claude MCPs`、`Mac 還有什麼必裝神奇軟體`、`台北漢堡排名`、`核心運動`。同步更新 `AI 工具索引`、`工具軟體索引`、`旅遊美食-索引`、`健康生活-索引` 與 `總索引` 狀態儀表板。

## [2026-05-07] reorganization | 索引頁集中至 wiki-pages/index/，統一表格格式

移動：21 個 `*-索引.md` 從各分類資料夾移至 `wiki-pages/index/`。
格式：所有索引頁改用 `## 子分類 / | 文件 |` 表格格式。
規則更新：CLAUDE.md 新增索引頁格式規則與目錄位置規範。

## [2026-05-07] reorganization | 索引頁格式全面對齊參考 wiki 樣式

依照 `ai-tips & notes\wiki\索引\` 的格式規範重寫全部索引：
- 加入 `← [[父索引]]` 返回導覽
- 有 wiki 頁面條目改為 `| 文件 | 重點 |` 雙欄，加入一句話重點描述
- 純書籤條目標記 `（⚠️ 書籤）`
- LingOrm 的 9 個子索引折入 LingOrm-索引 單一檔（刪除子索引）
- 總索引改為綜合概覽格式（含精選文章、快速導覽、概念地圖）
- CLAUDE.md 格式規則同步更新

## [2026-05-07] reorganization | 合併 6 個索引為 AI 工具索引 + 工具軟體索引

將 `AI 工具-索引`、`Claude-Code-索引`、`Gemini 與 NotebookLM-索引`、`Github 參考倉庫-索引`、`Prompt 工程-索引`、`工具軟體-索引` 合併為兩個平面索引：`AI 工具索引`、`工具軟體索引`。消除子索引層級，Github 參考倉庫內容整合為 AI 工具索引末尾 H2 區塊。更新 `總索引` 連結。

## [2026-05-07] ingest | 所有索引頁文件欄位修復（wiki 頁面建立）

修復全部索引頁中無連結的書籤條目，步驟：搜尋 wiki-pages 對應頁面 → 建立 wikilink；無對應頁面則從 raw ingest；raw 只有作者或 URL 者，將資訊寫入 wiki 頁面，URL 填入索引 重點 欄。
新增頁面涵蓋：AI 工具、工具軟體、求職履歷、旅遊美食、健康生活、LingOrm 共約 60+ 頁。LingOrm-索引 全面改寫，Heart Talk / LingOrm / Orm / 台北 FM / 鄺玲玲 / 巴黎時裝周 / 寵溺日常 / 同人創作 / 其他各節書籤全數轉為 [[wikilink]]。

## [2026-05-07] reorganization | LingOrm 頁面分類至 7 個子資料夾

將 `wiki-pages/LingOrm/` 下 48 個頁面移入子資料夾：同人創作（3）、Heart Talk 系列（11）、LingOrm 系列（7）、Orm 系列（9）、台北 FM 系列（11）、鄺玲玲系列（5）、泰百其他（1）。刪除舊 `鄺玲玲/` 子資料夾。更新 `LingOrm-索引.md` 補上原先未列入的 10 個條目。

## [2026-05-07] lint | 3 issues

無斷鏈、無矛盾。問題：Gemini/Claude-Code 3 組頁面缺交叉參照；raw/ 173 個未 ingest 檔（13 GitHub 倉庫 + 160 threads）。詳見 `list-to-be-repaired.md`。

## [2026-05-07] update | threads-saved frontmatter 補完與多來源來源清單

補完既有 wiki 頁面的 `threads-saved` frontmatter：既有 Threads 網址但 `作者: []` 的頁面依網址帳號回填作者；缺少 `網址` / `作者` frontmatter 的整理頁與單篇頁補上主要來源。整理頁、書籤集、多來源合併頁同步新增 `## Sources` 區塊，將所有使用到的來源作者與網址寫入正文。`AGENTS.md` 追加相同規則，明定多來源頁需同時保留 frontmatter 主來源與正文來源清單。

## [2026-05-07] reorganization | 中文與英文間距規則套用至全部頁面

`AGENTS.md` 新增頁面命名與內容撰寫規則：當中文與英文相鄰時，中間需加一個半形空白。此規則已批次套用至 `wiki-pages/` 現有頁面，包含頁名、標題、正文、wikilink、索引與來源清單，同步更新相關連結指向。

## [2026-05-07] update | 總索引文章數與概念文章地圖更新

更新 `索引/總索引.md` 的快速導覽統計，依目前實際 wiki 頁面數重算 AI 工具、工具軟體、求職履歷、旅遊美食、健康生活、LingOrm 六大主題的文章數；同步重寫概念文章地圖，改為反映目前知識庫的 AI 工具主線、Prompt 與研究支線、求職履歷支線與健康生活支線。

## [2026-05-07] reorganization | 索引資料夾改名為 index

將 `wiki-pages/索引/` 重命名為 `wiki-pages/index/`。同步更新 `AGENTS.md`、`lint.md` 與相關日誌中的明文路徑描述，讓索引目錄位置與維護規則一致。

## [2026-05-07] update | 台北 FM 系列 3 頁 stub 測試補文

針對 `wiki-pages/Lingorm/台北 FM 系列/` 中 3 個只有 frontmatter 的 Threads stub 頁面進行測試補文：`台北 FM 下班路`、`台北 FM 小寶幫 jeje 拉椅子`、`台北 FM 不嘻嘻`。依 frontmatter 的 `網址` 與 `作者`，參考外部 `socialcrawl_client.py` 與 `playwright_threads_client.py` 的邏輯，抽取作者主文與作者留言後回填正文；同時在 repo 內新增可重用工具腳本 `tools/fill_threads_stub_pages.py`，保留既有 frontmatter 並加入來源與交叉參照區塊，供後續批次處理其他空白頁面使用。

## [2026-05-07] update | 批次補全文站 Threads stub 頁面

延續 `台北 FM 系列 3 頁 stub 測試補文`，使用 `tools/fill_threads_stub_pages.py` 批次掃描 `wiki-pages/` 中只有 frontmatter、且 `網址` 指向 `threads.com` 的空白頁面，依 `網址` 與 `作者` 抽取作者主文與作者留言後回填正文。此次批次補完 AI 工具、工具軟體、求職履歷、旅遊美食、健康生活與 LingOrm 等分類的大多數 Threads stub；工具腳本同步補強為可依分類自動加入對應索引交叉參照，並在 `SocialCrawl` 404 時自動降級改用 `Playwright` 抽取。剩餘未補的空白頁為非 Threads 來源或單篇抽取失敗的例外頁。

## [2026-05-07] reorganization | 刪除 LingOrm 舊索引空檔並修正鄺玲玲條目

刪除殘留在 `wiki-pages/LingOrm/LingOrm-索引.md` 的 0-byte 舊索引空檔，保留正式索引 `wiki-pages/index/LingOrm-索引.md` 作為唯一 canonical 版本；同步修正正式索引中 `[[空鄺玲玲台北場 FM]]` 的錯誤條目名稱為 `[[鄺玲玲台北場 FM]]`，避免失效 wikilink。

## [2026-05-07] update | 清理 wiki 頁面重複標題與 Main Content

批次移除 wiki-pages/ 內容頁中與檔名重複的開頭 H1，以及不必要的 ## Main Content 區塊標記；不變更索引、交叉參照與 raw 來源。

## [2026-05-07] ingest | raw/threads-saved 全批（219 檔）

分類結果：
- AI 工具（Claude Code 42 篇、Gemini/NotebookLM、Prompt 工程、其他 AI 工具、Github 參考倉庫）
- 工具軟體（Mac、開發、日常數位）
- 求職履歷（履歷優化、求職自動化、面試準備）
- 旅遊美食（台灣美食、海外飲食、旅遊省錢、生活妙招）
- 健康生活（健身動作、身心保健）
- LingOrm（Heart Talk 11篇、LingOrm 系列 5篇、Orm 系列 7篇、台北 FM 12篇、鄺玲玲 3篇、巴黎時裝周 3篇、同人創作 3篇、寵溺日常 2篇、泰百其他 1篇）

備註：
- 113 個 stub 檔（僅有 frontmatter，無內文）以書籤形式列於各索引
- 91 個有實際內容的檔案整理為 wiki 頁面
- 結構參照 `ai-tips & notes\wiki\` 現有分類

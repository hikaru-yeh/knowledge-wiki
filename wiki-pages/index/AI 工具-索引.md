---
status: wiki
---

# AI 工具-索引

← [[總索引]]

## AI Agent 核心

| 文件 | 重點 |
|------|------|
| [[工作流與配置]] | 穩定工作流架構、四種 Agent 模式、危險指令識別、ADHD 七指令、Routines 排程 |
| [[Claude Code 白話入門：非工程師必看]] | 50 張白話 ELI5 投影片，CLAUDE.md / Hooks / MCP / Subagent 比喻解說 |
| [[Claude Code 自動開發15訣]] | Boris Cherny 親授：/loop 排程、Hooks、Git Worktrees、/voice |
| [[Claude Code 脆文實作50招]] | 100+ 篇脆文提取，8 大類 Skill / Token / CLAUDE.md / 工具整合 |
| [[everything-claude-code 冠軍配置]] | GitHub 12 萬 Stars，冠軍配置包含 Agent / Skills / MCP 完整設定 |
| [[OpenAI Codex 團隊內部使用指南繁中翻譯與重點解析]] | Ask Mode 先規劃再 Code，Prompt 寫成 GitHub Issue，AGENTS.md 關鍵 |
| [[Claude Code與Codex：開發工具怎麼選？]] | Claude Code 與 Codex 優缺點與適用場景比較 |
| [[Claude Code與Codex的同步與協作]] | Claude Code 與 Codex 同步工作與協作方式探討 |
| [[手機操控 AI：Claude Code、Codex 與 OpenCode 的 3T 應用]] | Tailscale / Termius / Tmux 手機遠端操控 AI 工具 |

## Harness、Skills 與記憶

| 文件                                              | 重點                                                                                            |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [[Claude Code 的啟示：AI Agent Harness 的技術債與薄型化設計]] | Thin Harness Fat Skills，90 天可丟，Letta 59.1% vs Claude 41.6%                                    |
| [[AI Agent 效能關鍵：Harness Engineering]]           | Agent = Model + Harness；Ratchet 把錯誤變規則；Hooks 強制 pre/post 執行；harness 不消亡只移動                    |
| [[AI Agent 架構四象限]]                              | Context Correlation × Impact 二維矩陣：RAG 查資料 / Skill 小技能 / Sub-agent 專家工具人 / Orchestrator AI 總指揮 |
| [[Skill 設計]]                                    | Adversarial Reviewer 三步驟、免費 Skill 設計課、Darwin-Skill 進化框架                                       |
| [[Claude 蒸餾 Skill-Set 大禮包]]                     | 蒸餾他人腦力成 Skill，丟網址給 Claude Code / Codex 直接抽技能                                                  |
| [[免費 Skill 助你建智能設計部]]                           | 10 人設計部門 Skill 組，模組化 Skill 維護效率更高                                                             |
| [[5個必裝 Codex Skill 體驗升級]]                       | awesome-codex 11K / repomix 25K / follow-builders / codex++ / keep-fast                       |
| [技能包大總管](<../AI 工具/AI Agent/技能包大總管.md>)         | 4 模式：觸發詞健檢 / Skill 快篩 / 整併拆分 / 更新檢查                                                           |
| [[Google Skills：官方 AI 產品技能庫]]                   | 官方 10K stars，npx skills add google/skills，Gemini/Cloud/BigQuery                               |
| [[CLAUDE.md 與記憶設定]]                             | 情境工程五步驟、模組化配置、Claude-Mem、Obsidian 三層機制                                                        |
| [[讓 AI coding 記得你的專案]]                          | agentmemory 為 AI coding 提供長期專案記憶                                                              |
| [[Garry Tan 的 GBrain：個人 AI 終身記憶進化系統]]           | P@5 49.1%，146K 頁生產規模，自我連線知識圖譜                                                                 |
| [[codex $mirgate to codex skill 超方便]]           | Codex 技能遷移指令，方便轉換到 Codex 平台                                                                   |

## Agent 安全與執行環境

| 文件 | 重點 |
|------|------|
| [[MCP 工具]] | 必備五大 MCP（Markitdown / Context7 / Playwright / GitHub / Task Master）、Firecrawl、Routines |
| [[你的 AI 工具正偷密鑰]] | LiteLLM 後門事件，MCP 隱式執行風險，三步自保 |
| [[別把 API Key 直接給 AI！]] | 使用 .env 保護 API Key，不應直接傳給 AI |
| [[AI 代碼有毒？microsandbox 硬件隔離]] | microsandbox 硬件沙盒隔離，安全執行 AI 代碼 |
| [[Claude Code：30秒搞定套件CVE]] | NVD MCP 接進 Claude Code，30 秒檢查 npm 套件 CVE |
| [[Claude Code 桌面自動遠端接管]] | remoteControlAtStartup 讓桌機自動成遠端後端 |

## 多 Agent 與長任務

| 文件 | 重點 |
|------|------|
| [AI 多模型協作審碼抓漏](<../AI 工具/AI Agent/AI 多模型協作審碼抓漏.md>) | Claude Octopus 8 模型，75% 共識門檻，Claude 指揮 / Codex 實作 / Gemini 資安 |
| [[Claude Code：AI開發團隊的Agent分工術]] | Agent / Sub-agent 分工架構與四層成熟使用方式 |
| [[Claude Code Agent View：你的 AI 程式碼塔台]] | `claude agents` 總控台：多 session 背景並行、自動 git worktree 隔離、CI 狀態回顯，v2.1.139+ |
| [[Claude Code goal：工程師長任務自動化救星]] | /goal 設完成條件，AI 自動循環執行直到完成 |
| [[AI Agent 24-7 持續運作]] | watchdog + heartbeat 讓 Codex / Claude Code 24/7 持續輪轉，backlog 優先序驅動，額度耗盡自動等待恢復 |
| [[我的 AI 日常：多 Agent CLI 設定]] | tmux + Tailscale + 自訂 PWA 面板同時管理 10+ CLI Agent，附完整安裝步驟與 config |
| [AI們的對話實驗](<../AI 工具/AI Agent/AI們的對話實驗.md>) | 多個 AI 互相討論與迭代對話的實驗設計 |
| [[GitHub推出Agentic AI Developer證書]] | GitHub 新認證正式定義 Agentic AI Developer 為獨立學科 |
| [[AI 數位員工崛起]] | AI Agent 從工具演進為數位員工的浪潮觀察 |

## Coding Agent 工程化

| 文件 | 重點 |
|------|------|
| [[Vibe-Coding]] | Karpathy→周加恩→Muse 三層知識系統；先想再動、簡單優先、精準修改、目標驅動 |
| [AI寫程式不失控：工程師的開發工作流](<../AI 工具/AI Agent/AI寫程式不失控：工程師的開發工作流.md>) | 4 技能：grill-with-docs / tdd / diagnose / 架構健檢，防 AI 帶著跑 |
| [AI寫程式架構亂？Axiom幫你看見。](<../AI 工具/AI Agent/AI寫程式架構亂？Axiom幫你看見。.md>) | 靜態架構合約 axi check/observe/infer/diff，CI 攔截 TS/JS 漂移 |
| [AI導入工程團隊：實戰加速交付](<../AI 工具/AI Agent/AI導入工程團隊：實戰加速交付.md>) | Production / Review / Validation Capacity 平衡，先制度再寫 CODE |
| [[AI Agent工程化工具趨勢]] | 本週 GitHub 前 10 AI 工程化工具趨勢整理 |
| [[AI 工具設定管理痛點與解方]] | skills-manager 15+ 工具統一 + Plexus 一鍵同步，Git 版控 |
| [[9 個你可能不知道的 Claude Code 神器]] | claude-mem 77K / ECC 189K / GSD 63K 等 9 個高星 repo |
| [[Thariq的Claude Code施工日誌Prompt]] | implementation-notes 施工日誌 Prompt 方法論 |
| [[Matt Pocock Claude 技能公開：AI 工作流效率升級]] | TDD / 診斷等三大高效 Claude Code 技能分享 |
| [[Hallmark：開源設計技能，讓 Claude Code UI 預設美觀]] | 22 主題 + 65 slop gates，npx skills add nutlope/hallmark |
| [[Impeccab 讓 AI 前端更完美]] | UX 審查 / 無障礙檢查技能，提升 AI 前端輸出品質 |
| [[Claude Code 提案 HTML 化，審核更輕鬆]] | /preview 技能，互動 HTML + 留言審核，Vercel 手機預覽 |

## Token 與上下文

| 文件 | 重點 |
|------|------|
| [[Token 優化]] | 四步省 94%（198k→10k）、Caveman Skill 省 75%、bu-ketao 省 72% |
| [[Claude ADHD 模式七個高效指令]] | Brain Dump、Task Untangler、Hyperfocus Hijacker、Body Double Bot 等 7 個指令 |
| [[Claude 高手用法設定即執行]] | CLAUDE.md + Skills + Subagents + Hooks 四大進階功能 |
| [[Claude Code：用 NotebookLM 讓 Claude 不再重複讀取 PDF]] | NotebookLM MCP 避免 Claude Code 重複讀 PDF 浪費 token |
| [AI時代的閱讀系統：好奇心驅動的知識長途駕駛](<../AI 工具/AI Agent/AI時代的閱讀系統：好奇心驅動的知識長途駕駛.md>) | raw→wiki→output 三層 + qmd 25K stars 本地搜尋 + HTML 視覺化 |
| [AI：你的專屬生命作業系統](<../AI 工具/AI Agent/AI：你的專屬生命作業系統.md>) | Claude Code 化身個人 Personal AI Infrastructure |

## Gemini 與 NotebookLM

| 文件 | 重點 |
|------|------|
| [[指令與整合]] | 五個實戰指令（骨架 / 三層深挖 / 摘要卡 / 跨本整合 / 思考歷程）、十大深度框架 |
| [Gemini 個人化指令設定](<../AI 工具/Gemini 與 NotebookLM/Gemini 個人化指令設定.md>) | 避免工作與私人情境混線，靠個人化指令切換 AI 人設 |
| [Gemini 同步 NotebookLM](<../AI 工具/Gemini 與 NotebookLM/Gemini 同步 NotebookLM.md>) | 3 本 notebook 分工：客戶專案 / 內容企劃 / 自學工具，減少重貼背景 |
| [[NotebookLM 外掛李宏毅24小時家教]] | YouTube to NotebookLM 外掛，一次匯入課程清單 |
| [Shinkansen 擴充：Gemini 高品質翻譯，隱私排版兼顧](<../AI 工具/Gemini 與 NotebookLM/Shinkansen 擴充：Gemini 高品質翻譯，隱私排版兼顧.md>) | Gemini API，不過第三方伺服器，保留排版，YouTube 字幕翻譯 |

## Prompt 工程

| 文件 | 重點 |
|------|------|
| [[提示詞技巧]] | 減少幻覺策略、Chain-of-Thought、Octopus 八模型 75% 共識門檻 |
| [[卡帕西破解 LLM 編碼陷阱心法]] | Karpathy 四法則：先想再動、簡單優先、精準修改、目標驅動，29.7k Stars |
| [[Google 官方 AI 提示詞寶典]] | 角色 / 任務 / 背景 / 格式公式，外加 6 大提示原則 |
| [[GPT 不要順著我指令技巧]] | 要求 GPT 別盲目附和，資訊不足就直說並指出論證漏洞 |
| [AI提示詞：破除迷信咒語，結構才是王道](<../AI 工具/Prompt 工程/AI提示詞：破除迷信咒語，結構才是王道.md>) | 提示詞迷思破解，結構化框架勝於咒語技巧 |
| [ChatGPT 精煉指令：告別廢話](<../AI 工具/Prompt 工程/ChatGPT 精煉指令：告別廢話.md>) | 5 個技巧讓 ChatGPT 輸出更簡潔有力 |
| [擺脫AI腔調](<../AI 工具/Prompt 工程/擺脫AI腔調.md>) | 6 種 Prompt 技巧去除 AI 文字明顯特徵讓內容更自然 |

## Github 參考倉庫

| 文件 | 重點 |
|------|------|
| [[obra-superpowers]] | Claude Code Skill 框架 |
| [[agent-skills]] | 多 IDE 適用 Agent Skill 集合 |
| [[cablate-llm-atomic-wiki]] | 584 posts → 630 atoms → 83 wiki pages，四層改進架構 |
| [[graphify]] | 任意輸入轉知識圖譜 |
| [[ralph-loop]] | Stop Hook 實作 while-true 無限循環 Agent 框架 |
| [[planning-with-files]] | 多平台 /plan、/start、/status 工作流 |
| [[drift_ai]] | AI 決策 git blame 追蹤，廠商中立 handoff |
| [[kinggyusuh-gemini-search-cc]] | Gemini + Claude Code，7 個 /gemini: 指令含 audit guard hook |

## 其他 AI 工具

| 文件 | 重點 |
|------|------|
| [[工具總覽]] | 沈浸式翻譯（雙語字幕 / 網頁對照）、Claude / Gemini / ChatGPT / Perplexity 比較表 |
| [2026年RAG還需要嗎？](<../AI 工具/其他 AI 工具/2026年RAG還需要嗎？.md>) | 2026 年 RAG 需場景判斷，MCP 讓 AI 自決搜索 |
| [長Context時代，RAG還需要嗎？](<../AI 工具/其他 AI 工具/長Context時代，RAG還需要嗎？.md>) | 長 Context 模型與 RAG 的應用場景與成本效益比較 |
| [人人都能打造個人AI知識庫](<../AI 工具/其他 AI 工具/人人都能打造個人AI知識庫.md>) | SQLite / 向量資料庫，個人 AI 知識庫建立指南 |
| [[AI 知識庫：一套 PostgreSQL 打天下]] | pgvector 成為 AI 知識庫與 RAG 系統核心基礎 |
| [[AI 知識庫新解方：告別碎片化，打造越用越聰明的 AI Wiki]] | nashsu/llm_wiki 9K stars，4 信號知識圖譜，Louvain 盲區偵測 |
| [為AI設計的筆記系統](<../AI 工具/其他 AI 工具/為AI設計的筆記系統.md>) | Hyday 筆記軟體的 AI 友善設計與三層索引系統 |
| [[AI 影片理解神器]] | sonpiaz/watch-cli，yt-dlp+ffmpeg+Whisper，5 種 Prompt 模板 |
| [[Tubelens + Claude AI：YouTube 影片秒變摘要，免費懶人救星！]] | Claude AI 一鍵摘要 / 心智圖 / 留言分析 / 雙語字幕，免費 |
| [[Notion AI 大招：從筆記到作業系統]] | Notion AI Agent 平台，筆記工具升級為 AI 作業系統 |
| [OpenHuman：開箱即用，懂你的個人AI](<../AI 工具/其他 AI 工具/OpenHuman：開箱即用，懂你的個人AI.md>) | 118 app 接入每 20 分鐘同步，本地加密，80% token 節省 |
| [AI八字免費解析](<../AI 工具/其他 AI 工具/AI八字免費解析.md>) | 個人化 AI 八字命盤解析，五行喜神等命理分析 |
| [AI指令：從對話紀錄規劃自媒體副業](<../AI 工具/其他 AI 工具/AI指令：從對話紀錄規劃自媒體副業.md>) | 5 個指令從對話分析自媒體方向與變現策略 |
| [VSCode-太臃腫？試試極速-AI-編輯器-Zed-1.0](<../AI 工具/其他 AI 工具/VSCode-太臃腫？試試極速-AI-編輯器-Zed-1.0.md>) | VSCode 太臃腫？試試極速 AI 編輯器 Zed 1.0 |
| [Mac-mini-LLM-應用請益](<../AI 工具/其他 AI 工具/Mac-mini-LLM-應用請益.md>) | Mac mini LLM 應用請益 |
| [Naval-的-AI-軟體預言：Vibe-Coding-與-Apple-危機](<../AI 工具/其他 AI 工具/Naval-的-AI-軟體預言：Vibe-Coding-與-Apple-危機.md>) | Naval 的 AI 軟體預言：Vibe Coding 與 Apple 危機 |
| [AI會議錄音到規格的高效流程](<../AI 工具/其他 AI 工具/AI會議錄音到規格的高效流程.md>) | AI會議錄音到規格的高效流程 |

## AI 工具社群帖子

| 文件 | 重點 |
|------|------|
| [90天AI工程師速成：10個GitHub專案](<../AI 工具/90天AI工程師速成：10個GitHub專案.md>) | 90天AI工程師速成：10個GitHub專案 |
| [AI-Agent-接入-Trello，開啟真實工作流](<../AI 工具/AI-Agent-接入-Trello，開啟真實工作流.md>) | AI Agent 接入 Trello，開啟真實工作流 |
| [AI-Agent-範本大補帖：100+-即用專案幫你抄作業](<../AI 工具/AI-Agent-範本大補帖：100+-即用專案幫你抄作業.md>) | Awesome LLM Apps：100+ 即用 Agent/RAG 模板，13 分類，Apache-2.0，112k stars |
| [AI-企業作業系統降臨：一人公司時代來了](<../AI 工具/AI-企業作業系統降臨：一人公司時代來了.md>) | Agent Stack 行銷貼文，介紹 ADK / MCP / Vertex AI / A2A 四個概念，無程式碼或步驟 |
| [AI-免費課程驚豔登場，付費課程情何以堪](<../AI 工具/AI-免費課程驚豔登場，付費課程情何以堪.md>) | GitHub 免費 AI Engineering 課程，涵蓋 LLM、RAG、Agent 與實作專案，適合自學補底層 |
| [AI-員工速成：Claude-+-Obsidian-密技大公開](<../AI 工具/AI-員工速成：Claude-+-Obsidian-密技大公開.md>)（📌 stub） | Claude + Obsidian playbook 一句 teaser，外部連結未 ingest |
| [AI-影分身：Meta-Meta-Prompting-打造個人大腦](<../AI 工具/AI-影分身：Meta-Meta-Prompting-打造個人大腦.md>) | AI 影分身：Meta Meta Prompting 打造個人大腦 |
| [AI-管家養成：免費中英文版](<../AI 工具/AI-管家養成：免費中英文版.md>) | 22 章免費教材：把 AI 訓練成能交辦、可驗收、能累積的工作夥伴，含 4 實戰案例 |
| [AI下一波：瓶頸才是舞台](<../AI 工具/AI下一波：瓶頸才是舞台.md>) | AI下一波：瓶頸才是舞台 |
| [AI伴學：知識壁壘已破](<../AI 工具/AI伴學：知識壁壘已破.md>)（📌 stub） | AI伴學：知識壁壘已破 |
| [AI助你高效規劃，告別瞎忙！](<../AI 工具/AI助你高效規劃，告別瞎忙！.md>) | AI助你高效規劃，告別瞎忙！ |
| [AI助頂尖研究員，化身一人團隊](<../AI 工具/AI助頂尖研究員，化身一人團隊.md>) | AI助頂尖研究員，化身一人團隊 |
| [AI寫文口頭禪](<../AI 工具/AI寫文口頭禪.md>)（📌 stub） | AI寫文口頭禪 |
| [AI專家員工庫，Github-81萬收藏！](<../AI 工具/AI專家員工庫，Github-81萬收藏！.md>) | AI專家員工庫，Github 81萬收藏！ |
| [AI流程圖神器：一句話搞定多種風格](<../AI 工具/AI流程圖神器：一句話搞定多種風格.md>) | fireworks-tech-graph：自然語言→SVG+PNG，7 風格、14 種 UML、40+ 技術 icon |
| [AI進化超速，專業者們辛苦了](<../AI 工具/AI進化超速，專業者們辛苦了.md>) | AI 話題每年換名詞：LLM→RAG→Agent→Harness，追新術語是從業者日常 |
| [Agent-試錯學習迴路](<../AI 工具/Agent-試錯學習迴路.md>) | Agent 試錯學習迴路 |
| [Awesome Design System](<../AI 工具/Awesome Design System.md>) | GitHub 20K stars，55個大廠設計系統：Google Material/Apple HIG/Microsoft Fluent/Airbnb/Shopify |
| [Chandra：文件解析神器，完美保留結構](<../AI 工具/Chandra：文件解析神器，完美保留結構.md>) | Chandra：文件解析神器，完美保留結構 |
| [ChatGPT監督Claude：開啟新世界](<../AI 工具/ChatGPT監督Claude：開啟新世界.md>) | ChatGPT監督Claude：開啟新世界 |
| [ChatGPT私人加速學習教練](<../AI 工具/ChatGPT私人加速學習教練.md>) | ChatGPT私人加速學習教練 |
| [ChatGPT腦袋整理術](<../AI 工具/ChatGPT腦袋整理術.md>) | ChatGPT腦袋整理術 |
| [Chrome-Skills：Gemini-變身數位員工](<../AI 工具/Chrome-Skills：Gemini-變身數位員工.md>) | Chrome Skills：Gemini 變身數位員工 |
| [Claude Code 換到 Codex，無痛遷移清單](<../AI 工具/Claude Code 換到 Codex，無痛遷移清單.md>) | Claude Code 換到 Codex，無痛遷移清單 |
| [Claude-Cowork-+-byCrawl：社群動態一手掌握](<../AI 工具/Claude-Cowork-+-byCrawl：社群動態一手掌握.md>) | Claude Cowork + byCrawl：社群動態一手掌握 |
| [Claude-實戰-Justin-Welsh-框架：一人公司獲利咒語](<../AI 工具/Claude-實戰-Justin-Welsh-框架：一人公司獲利咒語.md>) | Claude 實戰 Justin Welsh 框架：一人公司獲利咒語 |
| [Claude-整合-10-大工具，AI-幫你做](<../AI 工具/Claude-整合-10-大工具，AI-幫你做.md>) | Claude 直接整合 Notion / n8n / Calendar / Canva / Gamma 等 10 工具，無需 plugin 即可調用 |
| [Claude助你輕鬆讀懂深度英文長文](<../AI 工具/Claude助你輕鬆讀懂深度英文長文.md>) | Claude助你輕鬆讀懂深度英文長文 |
| [Claude的7個航班省錢提示](<../AI 工具/Claude的7個航班省錢提示.md>) | Claude的7個航班省錢提示 |
| [Claude高效自學術：少走彎路四倍快](<../AI 工具/Claude高效自學術：少走彎路四倍快.md>) | Claude高效自學術：少走彎路四倍快 |
| [Copilot-妙招：Claude-Opus-用不完](<../AI 工具/Copilot-妙招：Claude-Opus-用不完.md>) | Copilot 妙招：Claude Opus 用不完 |
| [Dataview：告別-Obsidian-筆記土法煉鋼](<../AI 工具/Dataview：告別-Obsidian-筆記土法煉鋼.md>) | Dataview：告別 Obsidian 筆記土法煉鋼 |
| [GPT生圖不撞款指令](<../AI 工具/GPT生圖不撞款指令.md>) | GPT生圖不撞款指令 |
| [Gemini-Notebooks：懂你的-AI-智慧筆記](<../AI 工具/Gemini-Notebooks：懂你的-AI-智慧筆記.md>) | Gemini Notebooks：懂你的 AI 智慧筆記 |
| [Google-AI-Agents-Vibe-Coding-攻略與報名](<../AI 工具/Google-AI-Agents-Vibe-Coding-攻略與報名.md>) | Google × Kaggle 免費五日 AI Agent 課程：Vibe Coding / Function Calling / 多 Agent 通訊 / 部署，附 7 步報名 |
| [Hermes-Agent記憶術：AI越用越便宜的秘密](<../AI 工具/Hermes-Agent記憶術：AI越用越便宜的秘密.md>) | Hermes Agent記憶術：AI越用越便宜的秘密 |
| [MIT生靠NotebookLM-2天搞定一學期](<../AI 工具/MIT生靠NotebookLM-2天搞定一學期.md>) | MIT生靠NotebookLM 2天搞定一學期 |
| [Mac離線AI字幕，精準繁中翻譯](<../AI 工具/Mac離線AI字幕，精準繁中翻譯.md>) | Mac離線AI字幕，精準繁中翻譯 |
| [NotebookLM-×-Gemini：AI-文獻指揮官](<../AI 工具/NotebookLM-×-Gemini：AI-文獻指揮官.md>) | NotebookLM × Gemini：AI 文獻指揮官 |
| [NotebookLM-終極指令集：高手都在用的-5-招](<../AI 工具/NotebookLM-終極指令集：高手都在用的-5-招.md>) | NotebookLM 終極指令集：高手都在用的 5 招 |
| [NotebookLM：10大框架解鎖深度洞察](<../AI 工具/NotebookLM：10大框架解鎖深度洞察.md>) | NotebookLM：10大框架解鎖深度洞察 |
| [Obsidian-+-Claudian：你的-24-小時-AI-個人秘書](<../AI 工具/Obsidian-+-Claudian：你的-24-小時-AI-個人秘書.md>) | Obsidian + Claudian：你的 24 小時 AI 個人秘書 |
| [Obsidian-必備神級插件](<../AI 工具/Obsidian-必備神級插件.md>) | Obsidian 必備神級插件 |
| [PageIndex：RAG-不一定要向量](<../AI 工具/PageIndex：RAG-不一定要向量.md>) | PageIndex：RAG 不一定要向量 |
| [Paperclip：你的-AI-虛擬公司，預算全自動](<../AI 工具/Paperclip：你的-AI-虛擬公司，預算全自動.md>) | Paperclip AI 虛擬公司：多 Agent 組織架構 + Auto-Budgeting 自動分配 API 額度 |
| [Printing-Press：AI-Agent-的-CLI-瑞士刀](<../AI 工具/Printing-Press：AI-Agent-的-CLI-瑞士刀.md>) | Printing Press：AI Agent 的 CLI 瑞士刀 |
| [Threads-API](<../AI 工具/Threads-API.md>)（📌 stub） | 官方 API 僅限自己帖子；GitHub 開源替代截斷，需 Threads refetch |
| [Vibe-Coding-亂象與工程師的心累](<../AI 工具/Vibe-Coding-亂象與工程師的心累.md>) | Vibe Coding 亂象與工程師的心累 |
| [guizang-ppt-skill：AI-高質感雜誌風-PPT-神器](<../AI 工具/guizang-ppt-skill：AI-高質感雜誌風-PPT-神器.md>) | 單檔 HTML 簡報技能：Editorial Magazine / Swiss International 兩套風格、32 種版面、WebGL 動畫 |
| [ralph-loop plugin 原理](<../AI 工具/ralph-loop plugin 原理.md>) | ralph loop plugin 原理 |
| [vibe-coding-app-資安問題總整理](<../AI 工具/vibe-coding-app-資安問題總整理.md>) | vibe coding app 資安問題總整理 |
| [一人到整個團隊](<../AI 工具/一人到整個團隊.md>) | 一人到整個團隊 |
| [三周24-7-AI-Agent開發團隊：架構與演進](<../AI 工具/三周24-7-AI-Agent開發團隊：架構與演進.md>) | 三周24 7 AI Agent開發團隊：架構與演進 |
| [不是所有經驗都能成為-AI-Skill](<../AI 工具/不是所有經驗都能成為-AI-Skill.md>) | 不是所有經驗都能成為 AI Skill |
| [九天打造-Hermes-AI：越用越聰明的個人-AI-Wiki](<../AI 工具/九天打造-Hermes-AI：越用越聰明的個人-AI-Wiki.md>) | Hermes Agent 完整教學：三層 .md 人格配置、Telegram/Gmail/Health 整合、雙 Agent 架構 |
| [史丹佛-Vibe-Coding：告別感覺寫程式](<../AI 工具/史丹佛-Vibe-Coding：告別感覺寫程式.md>) | 史丹佛 Vibe Coding：告別感覺寫程式 |
| [實測了上百個skill後，我只留下了這10個skill](<../AI 工具/實測了上百個skill後，我只留下了這10個skill.md>) | 實測了上百個skill後，我只留下了這10個skill |
| [擺脫糊字！AI簡報組合技](<../AI 工具/擺脫糊字！AI簡報組合技.md>) | NotebookLM→Nanobanana→LightPDF 三步解決 AI 簡報糊字不能編輯 |
| [框架工程：AI優先，重塑你的組織](<../AI 工具/框架工程：AI優先，重塑你的組織.md>) | 框架工程：AI優先，重塑你的組織 |
| [用Obsidian建立你的LLM知識庫](<../AI 工具/用Obsidian建立你的LLM知識庫.md>) | Obsidian 搭建 LLM Wiki 教學；作者 PDF 站已改版為 portfolio，無教學內容 |
| [簡報地獄有救！AI免費轉PPT無痛編輯](<../AI 工具/簡報地獄有救！AI免費轉PPT無痛編輯.md>) | 簡報地獄有救！AI免費轉PPT無痛編輯 |
| [超好看開源日式風格Skill](<../AI 工具/超好看開源日式風格Skill.md>)（📌 stub） | 開源日式風格 Skill，含 agent 設計指南；個人免費、商用需授權 |
| [部署平台怎麼選？Vercel、Railway、GitHub-Actions-成本與應用場景](<../AI 工具/部署平台怎麼選？Vercel、Railway、GitHub-Actions-成本與應用場景.md>) | 部署平台怎麼選？Vercel、Railway、GitHub Actions 成本與應用場景 |
| [開發者，別再浪費-tokens](<../AI 工具/開發者，別再浪費-tokens.md>) | 3 個 GitHub repo（CLI 壓縮 / 結構化 context / prompt 控制）連結全截斷，需 refetch |
| [Hermes-AI-Agent：會自己進化的懶人助手](<../AI 工具/AI Agent/Hermes-AI-Agent：會自己進化的懶人助手.md>) | Hermes AI Agent：會自己進化的懶人助手 |
| [Google-Agents-CLI：AI-助手專屬雲端-Agent-開發](<../AI 工具/AI Agent/Google-Agents-CLI：AI-助手專屬雲端-Agent-開發.md>) | Google Agents CLI：AI 助手專屬雲端 Agent 開發 |
| [AI-Agent-技能生態系成形-2](<../AI 工具/AI Agent/AI-Agent-技能生態系成形-2.md>) | AI Agent 技能生態系成形 2 |
| [AI-Agent跨儲庫盲區與解方](<../AI 工具/AI Agent/AI-Agent跨儲庫盲區與解方.md>) | AI Agent跨儲庫盲區與解方 |
| [Harness-Engineering：AI-應用致勝之道](<../AI 工具/AI Agent/Harness-Engineering：AI-應用致勝之道.md>) | Harness Engineering：AI 應用致勝之道 |
| [Harness-Engineering：AI-時代工程師的新核心](<../AI 工具/AI Agent/Harness-Engineering：AI-時代工程師的新核心.md>) | Harness Engineering：AI 時代工程師的新核心 |

## Claude Code 社群帖子

| 文件                                                     | 重點                                                                      |
| ------------------------------------------------------ | ----------------------------------------------------------------------- |
| [Claude 生態系指南](<../AI 工具/Claude-Code/Claude 生態系指南.md>) | Claude / Claude Code / Cowork、Skills、Connectors、Plugins 與 Skill 安裝指南    |
| [25-個-Claude-Code-日常指令](<../AI 工具/Claude-Code/25-個-Claude-Code-日常指令.md>)                              | 25 個 Claude Code 日常指令                                                   |
| [[工程師最常用的 12 個 Claude Code 指令]]                        | @this.web 分享 12 個最常用 Claude Code 快捷鍵與指令，附完整速查表（圖表版）                       |
| [4-招寫好-CLAUDE.md-降低-token-消耗](<../AI 工具/Claude-Code/4-招寫好-CLAUDE.md-降低-token-消耗.md>)                        | 4 招寫好 CLAUDE.md 降低 token 消耗                                             |
| [ADHD-友善的-Claude-Code-狀態列](<../AI 工具/Claude-Code/ADHD-友善的-Claude-Code-狀態列.md>)                           | ADHD 友善的 Claude Code 狀態列                                                |
| [AI-Skill-優化：達爾文式棘輪進化法](<../AI 工具/Claude-Code/AI-Skill-優化：達爾文式棘輪進化法.md>)                              | AI Skill 優化：達爾文式棘輪進化法                                                   |
| [AI-實用評估-GitHub-專案：打破迷思](<../AI 工具/Claude-Code/AI-實用評估-GitHub-專案：打破迷思.md>)                             | AI 實用評估 GitHub 專案：打破迷思                                                  |
| [AI助理不給答案，卻讓我改變最多](<../AI 工具/Claude-Code/AI助理不給答案，卻讓我改變最多.md>)                                   | AI助理不給答案，卻讓我改變最多                                                        |
| [AI外接硬碟：Claude-Mem解決記憶斷片](<../AI 工具/Claude-Code/AI外接硬碟：Claude-Mem解決記憶斷片.md>)                            | AI外接硬碟：Claude Mem解決記憶斷片                                                 |
| [AI寫程式：品質、穩定與基礎功](<../AI 工具/Claude-Code/AI寫程式：品質、穩定與基礎功.md>)                                    | AI寫程式：品質、穩定與基礎功                                                         |
| [AI工具：Cowork工作流與Claude技能](<../AI 工具/Claude-Code/AI工具：Cowork工作流與Claude技能.md>)                            | AI工具：Cowork工作流與Claude技能                                                 |
| [AI新OS：設計系統雙鏡片思考](<../AI 工具/Claude-Code/AI新OS：設計系統雙鏡片思考.md>)                                    | AI新OS：設計系統雙鏡片思考                                                         |
| [AI開發：深究細節，方能致用](<../AI 工具/Claude-Code/AI開發：深究細節，方能致用.md>)                                     | AI開發：深究細節，方能致用                                                          |
| [AI點子30-5精煉法](<../AI 工具/Claude-Code/AI點子30-5精煉法.md>)                                        | AI點子30 5精煉法                                                             |
| [Anthropic-Claude-技能包：文件排版神器](<../AI 工具/Claude-Code/Anthropic-Claude-技能包：文件排版神器.md>)                        | Anthropic Claude 技能包：文件排版神器                                             |
| [CLAUDE.md-太長反效果](<../AI 工具/Claude-Code/CLAUDE.md-太長反效果.md>)                                    | CLAUDE.md 太長反效果                                                         |
| [CLAUDE.md-的精準寫法：注意力經濟學](<../AI 工具/Claude-Code/CLAUDE.md-的精準寫法：注意力經濟學.md>)                             | CLAUDE.md 的精準寫法：注意力經濟學                                                  |
| [CLI-更新檢查，試試-effort](<../AI 工具/Claude-Code/CLI-更新檢查，試試-effort.md>)                                 | CLI 更新檢查，試試 effort                                                      |
| [Claude Agent：權限管理與自動化進程](<../AI 工具/Claude-Code/Claude Agent：權限管理與自動化進程.md>)                            | Claude Agent：權限管理與自動化進程                                                 |
| [Claude Code 對話 Recap：一眼掌握進度](<../AI 工具/Claude-Code/Claude Code 對話 Recap：一眼掌握進度.md>)                        | Claude Code 對話 Recap：一眼掌握進度                                             |
| [Claude Code 技能達爾文式進化](<../AI 工具/Claude-Code/Claude Code 技能達爾文式進化.md>)                               | Claude Code 技能達爾文式進化                                                    |
| [Claude Code 指令風險判讀術](<../AI 工具/Claude-Code/Claude Code 指令風險判讀術.md>)                                | Claude Code 指令風險判讀術                                                     |
| [Claude Code：打造你的第二大腦](<../AI 工具/Claude-Code/Claude Code：打造你的第二大腦.md>)                               | Claude Code：打造你的第二大腦                                                    |
| [Claude Pro開發對話額度不足？](<../AI 工具/Claude-Code/Claude Pro開發對話額度不足？.md>)                                | Claude Pro開發對話額度不足？                                                     |
| [Claude Skill 設定教學推薦？](<../AI 工具/Claude-Code/Claude Skill 設定教學推薦？.md>)                               | Claude Skill 設定教學推薦？                                                    |
| [Claude 模組化配置，杜絕記憶污染](<../AI 工具/Claude-Code/Claude 模組化配置，杜絕記憶污染.md>)                                | Claude 模組化配置，杜絕記憶污染                                                     |
| [Claude+Zotero：文獻圖書館速成術](<../AI 工具/Claude-Code/Claude+Zotero：文獻圖書館速成術.md>)                             | Claude+Zotero：文獻圖書館速成術                                                  |
| [Claude-Code-Codex-Skill-管理：告別-Context-偷吃，輕鬆共享](<../AI 工具/Claude-Code/Claude-Code-Codex-Skill-管理：告別-Context-偷吃，輕鬆共享.md>)      | Claude Code Codex Skill 管理：告別 Context 偷吃，輕鬆共享                           |
| [Claude-Code-串接-Threads-API-廣告後台卡關](<../AI 工具/Claude-Code/Claude-Code-串接-Threads-API-廣告後台卡關.md>)                  | Claude Code 串接 Threads API 廣告後台卡關                                       |
| [Claude-Code-實戰：4-天開發-Picnote-上架-iOS-App](<../AI 工具/Claude-Code/Claude-Code-實戰：4-天開發-Picnote-上架-iOS-App.md>)            | Claude Code 實戰：4 天開發 Picnote 上架 iOS App                                 |
| [Claude-Code-效率提升：Slack-通知](<../AI 工具/Claude-Code/Claude-Code-效率提升：Slack-通知.md>)                          | Claude Code 效率提升：Slack 通知                                               |
| [Claude-Code-設定外掛教學](<../AI 工具/Claude-Code/Claude-Code-設定外掛教學.md>)                                 | Claude Code 設定外掛教學                                                      |
| [Claude-Code-避坑守則](<../AI 工具/Claude-Code/Claude-Code-避坑守則.md>)                                   | Claude Code 避坑守則                                                        |
| [Claude-Code必學8招：Boris-Cherny進階與避雷](<../AI 工具/Claude-Code/Claude-Code必學8招：Boris-Cherny進階與避雷.md>)                  | Claude Code必學8招：Boris Cherny進階與避雷                                       |
| [Claude-Code：AI-Agent-五層架構剖析](<../AI 工具/Claude-Code/Claude-Code：AI-Agent-五層架構剖析.md>)                        | Claude Code：AI Agent 五層架構剖析                                            文字/文件自動轉知識圖譜，支援繁中等多語言；任意輸入均可結構化處理 |
| [[ralph-loop]] | Stop Hook 實作 while-true 無限循環 Agent 框架 |
| [[planning-with-files]] | 多平台 /plan、/start、/status 工作流 |
| [[drift_ai]] | AI 決策 git blame 追蹤，廠商中立 handoff |
| [[kinggyusuh-gemini-search-cc]] | Gemini + Claude Code，7 個 /gemini: 指令含 audit guard hook |

## 其他 AI 工具

| 文件 | 重點 |
|------|------|
| [[工具總覽]] | 沈浸式翻譯（雙語字幕 / 網頁對照）、Claude / Gemini / ChatGPT / Perplexity 比較表 |
| [2026年RAG還需要嗎？](<../AI 工具/其他 AI 工具/2026年RAG還需要嗎？.md>) | 2026 年 RAG 需場景判斷，MCP 讓 AI 自決搜索 |
| [長Context時代，RAG還需要嗎？](<../AI 工具/其他 AI 工具/長Context時代，RAG還需要嗎？.md>) | 長 Context 模型與 RAG 的應用場景與成本效益比較 |
| [人人都能打造個人AI知識庫](<../AI 工具/其他 AI 工具/人人都能打造個人AI知識庫.md>) | SQLite / 向量資料庫，個人 AI 知識庫建立指南 |
| [[AI 知識庫：一套 PostgreSQL 打天下]] | pgvector 成為 AI 知識庫與 RAG 系統核心基礎 |
| [[AI 知識庫新解方：告別碎片化，打造越用越聰明的 AI Wiki]] | nashsu/llm_wiki 9K stars，4 信號知識圖譜，Louvain 盲區偵測 |
| [為AI設計的筆記系統](<../AI 工具/其他 AI 工具/為AI設計的筆記系統.md>) | Hyday 筆記軟體的 AI 友善設計與三層索引系統 |
| [[AI 影片理解神器]] | sonpiaz/watch-cli，yt-dlp+ffmpeg+Whisper，5 種 Prompt 模板 |
| [[Tubelens + Claude AI：YouTube 影片秒變摘要，免費懶人救星！]] | Claude AI 一鍵摘要 / 心智圖 / 留言分析 / 雙語字幕，免費 |
| [[Notion AI 大招：從筆記到作業系統]] | Notion AI Agent 平台，筆記工具升級為 AI 作業系統 |
| [OpenHuman：開箱即用，懂你的個人AI](<../AI 工具/其他 AI 工具/OpenHuman：開箱即用，懂你的個人AI.md>) | 118 app 接入每 20 分鐘同步，本地加密，80% token 節省 |
| [AI八字免費解析](<../AI 工具/其他 AI 工具/AI八字免費解析.md>) | 個人化 AI 八字命盤解析，五行喜神等命理分析 |
| [AI指令：從對話紀錄規劃自媒體副業](<../AI 工具/其他 AI 工具/AI指令：從對話紀錄規劃自媒體副業.md>) | 5 個指令從對話分析自媒體方向與變現策略 |
| [VSCode-太臃腫？試試極速-AI-編輯器-Zed-1.0](<../AI 工具/其他 AI 工具/VSCode-太臃腫？試試極速-AI-編輯器-Zed-1.0.md>) | VSCode 太臃腫？試試極速 AI 編輯器 Zed 1.0 |
| [Mac-mini-LLM-應用請益](<../AI 工具/其他 AI 工具/Mac-mini-LLM-應用請益.md>) | Mac mini LLM 應用請益 |
| [Naval-的-AI-軟體預言：Vibe-Coding-與-Apple-危機](<../AI 工具/其他 AI 工具/Naval-的-AI-軟體預言：Vibe-Coding-與-Apple-危機.md>) | Naval 的 AI 軟體預言：Vibe Coding 與 Apple 危機 |
| [AI會議錄音到規格的高效流程](<../AI 工具/其他 AI 工具/AI會議錄音到規格的高效流程.md>) | 錄音→NotebookLM→Spectra 生 Spec；Token 消耗全算在 nlm 不佔本機 |

## AI 工具社群帖子

| 文件 | 重點 |
|------|------|
| [90天AI工程師速成：10個GitHub專案](<../AI 工具/90天AI工程師速成：10個GitHub專案.md>) | 90天AI工程師速成：10個GitHub專案 |
| [AI-Agent-接入-Trello，開啟真實工作流](<../AI 工具/AI-Agent-接入-Trello，開啟真實工作流.md>) | AI Agent 接入 Trello，開啟真實工作流 |
| [AI-Agent-範本大補帖：100+-即用專案幫你抄作業](<../AI 工具/AI-Agent-範本大補帖：100+-即用專案幫你抄作業.md>) | Awesome LLM Apps：100+ 即用 Agent/RAG 模板，13 分類，Apache-2.0，112k stars |
| [AI-企業作業系統降臨：一人公司時代來了](<../AI 工具/AI-企業作業系統降臨：一人公司時代來了.md>) | Agent Stack 行銷貼文，介紹 ADK / MCP / Vertex AI / A2A 四個概念，無程式碼或步驟 |
| [AI-免費課程驚豔登場，付費課程情何以堪](<../AI 工具/AI-免費課程驚豔登場，付費課程情何以堪.md>) | GitHub 免費 AI Engineering 課程，涵蓋 LLM、RAG、Agent 與實作專案，適合自學補底層 |
| [AI-員工速成：Claude-+-Obsidian-密技大公開](<../AI 工具/AI-員工速成：Claude-+-Obsidian-密技大公開.md>)（📌 stub） | Claude + Obsidian playbook 一句 teaser，外部連結未 ingest |
| [AI-影分身：Meta-Meta-Prompting-打造個人大腦](<../AI 工具/AI-影分身：Meta-Meta-Prompting-打造個人大腦.md>) | AI 影分身：Meta Meta Prompting 打造個人大腦 |
| [AI-管家養成：免費中英文版](<../AI 工具/AI-管家養成：免費中英文版.md>) | 22 章免費教材：把 AI 訓練成能交辦、可驗收、能累積的工作夥伴，含 4 實戰案例 |
| [AI下一波：瓶頸才是舞台](<../AI 工具/AI下一波：瓶頸才是舞台.md>) | GPU 之外，電力/散熱/HBM/網路才是瓶頸股；VRT/MU/ANET/奇鋐/汎銓選股分析 |
| [AI伴學：知識壁壘已破](<../AI 工具/AI伴學：知識壁壘已破.md>)（📌 stub） | AI 24 小時待機不吐槽，學生知識壁壘已破；反思教育現場空缺 |
| [AI助你高效規劃，告別瞎忙！](<../AI 工具/AI助你高效規劃，告別瞎忙！.md>) | 4 個 Claude Prompt：四象限週任務分類、拖延偵測、任務拆解、30 分鐘週規劃模板 |
| [AI助頂尖研究員，化身一人團隊](<../AI 工具/AI助頂尖研究員，化身一人團隊.md>) | AI助頂尖研究員，化身一人團隊 |
| [AI寫文口頭禪](<../AI 工具/AI寫文口頭禪.md>)（📌 stub） | 列出 AI 寫文高頻詞「穩、撐、懂」，幫助識別 AI 腔調具體語言特徵 |
| [AI專家員工庫，Github-81萬收藏！](<../AI 工具/AI專家員工庫，Github-81萬收藏！.md>) | AI專家員工庫，Github 81萬收藏！ |
| [AI流程圖神器：一句話搞定多種風格](<../AI 工具/AI流程圖神器：一句話搞定多種風格.md>) | fireworks-tech-graph：自然語言→SVG+PNG，7 風格、14 種 UML、40+ 技術 icon |
| [AI進化超速，專業者們辛苦了](<../AI 工具/AI進化超速，專業者們辛苦了.md>) | AI 話題每年換名詞：LLM→RAG→Agent→Harness，追新術語是從業者日常 |
| [Agent-試錯學習迴路](<../AI 工具/Agent-試錯學習迴路.md>) | hermes-agent 任務後背景 fork review，只存試錯路徑，防止 skill base 膨脹 |
| [Awesome Design System](<../AI 工具/Awesome Design System.md>) | GitHub 20K stars，55個大廠設計系統：Google Material/Apple HIG/Microsoft Fluent/Airbnb/Shopify |
| [Chandra：文件解析神器，完美保留結構](<../AI 工具/Chandra：文件解析神器，完美保留結構.md>) | Chandra：文件解析神器，完美保留結構 |
| [ChatGPT監督Claude：開啟新世界](<../AI 工具/ChatGPT監督Claude：開啟新世界.md>) | ChatGPT監督Claude：開啟新世界 |
| [ChatGPT私人加速學習教練](<../AI 工具/ChatGPT私人加速學習教練.md>) | ChatGPT私人加速學習教練 |
| [ChatGPT腦袋整理術](<../AI 工具/ChatGPT腦袋整理術.md>) | 5 個 ChatGPT 指令：腦袋清空整理、行動規劃、決策簡化、混亂變清晰、專注衝刺建構 |
| [Chrome-Skills：Gemini-變身數位員工](<../AI 工具/Chrome-Skills：Gemini-變身數位員工.md>) | Chrome Skills：Gemini 變身數位員工 |
| [Claude Code 換到 Codex，無痛遷移清單](<../AI 工具/Claude Code 換到 Codex，無痛遷移清單.md>) | Claude Code 換到 Codex，無痛遷移清單 |
| [Claude-Cowork-+-byCrawl：社群動態一手掌握](<../AI 工具/Claude-Cowork-+-byCrawl：社群動態一手掌握.md>) | Claude Cowork + byCrawl：社群動態一手掌握 |
| [Claude-實戰-Justin-Welsh-框架：一人公司獲利咒語](<../AI 工具/Claude-實戰-Justin-Welsh-框架：一人公司獲利咒語.md>) | Claude 實戰 Justin Welsh 框架：一人公司獲利咒語 |
| [Claude-整合-10-大工具，AI-幫你做](<../AI 工具/Claude-整合-10-大工具，AI-幫你做.md>) | Claude 直接整合 Notion / n8n / Calendar / Canva / Gamma 等 10 工具，無需 plugin 即可調用 |
| [Claude助你輕鬆讀懂深度英文長文](<../AI 工具/Claude助你輕鬆讀懂深度英文長文.md>) | Claude助你輕鬆讀懂深度英文長文 |
| [Claude的7個航班省錢提示](<../AI 工具/Claude的7個航班省錢提示.md>) | Claude的7個航班省錢提示 |
| [Claude高效自學術：少走彎路四倍快](<../AI 工具/Claude高效自學術：少走彎路四倍快.md>) | Claude高效自學術：少走彎路四倍快 |
| [Copilot-妙招：Claude-Opus-用不完](<../AI 工具/Copilot-妙招：Claude-Opus-用不完.md>) | Copilot 妙招：Claude Opus 用不完 |
| [Dataview：告別-Obsidian-筆記土法煉鋼](<../AI 工具/Dataview：告別-Obsidian-筆記土法煉鋼.md>) | Dataview：告別 Obsidian 筆記土法煉鋼 |
| [GPT生圖不撞款指令](<../AI 工具/GPT生圖不撞款指令.md>) | 先讓 GPT 分析視覺風格、配色偏好與受眾，提三組設計方向後再生圖，避免撞款 |
| [Gemini-Notebooks：懂你的-AI-智慧筆記](<../AI 工具/Gemini-Notebooks：懂你的-AI-智慧筆記.md>) | Gemini Notebooks：懂你的 AI 智慧筆記 |
| [Google-AI-Agents-Vibe-Coding-攻略與報名](<../AI 工具/Google-AI-Agents-Vibe-Coding-攻略與報名.md>) | Google × Kaggle 免費五日 AI Agent 課程：Vibe Coding / Function Calling / 多 Agent 通訊 / 部署，附 7 步報名 |
| [Hermes-Agent記憶術：AI越用越便宜的秘密](<../AI 工具/Hermes-Agent記憶術：AI越用越便宜的秘密.md>) | Hermes Agent記憶術：AI越用越便宜的秘密 |
| [MIT生靠NotebookLM-2天搞定一學期](<../AI 工具/MIT生靠NotebookLM-2天搞定一學期.md>) | MIT生靠NotebookLM 2天搞定一學期 |
| [Mac離線AI字幕，精準繁中翻譯](<../AI 工具/Mac離線AI字幕，精準繁中翻譯.md>) | Mac離線AI字幕，精準繁中翻譯 |
| [NotebookLM-×-Gemini：AI-文獻指揮官](<../AI 工具/NotebookLM-×-Gemini：AI-文獻指揮官.md>) | NotebookLM × Gemini：AI 文獻指揮官 |
| [NotebookLM-終極指令集：高手都在用的-5-招](<../AI 工具/NotebookLM-終極指令集：高手都在用的-5-招.md>) | NotebookLM 終極指令集：高手都在用的 5 招 |
| [NotebookLM：10大框架解鎖深度洞察](<../AI 工具/NotebookLM：10大框架解鎖深度洞察.md>) | NotebookLM：10大框架解鎖深度洞察 |
| [Obsidian-+-Claudian：你的-24-小時-AI-個人秘書](<../AI 工具/Obsidian-+-Claudian：你的-24-小時-AI-個人秘書.md>) | Obsidian + Claudian：你的 24 小時 AI 個人秘書 |
| [Obsidian-必備神級插件](<../AI 工具/Obsidian-必備神級插件.md>) | Obsidian 必備神級插件 |
| [PageIndex：RAG-不一定要向量](<../AI 工具/PageIndex：RAG-不一定要向量.md>) | PageIndex：RAG 不一定要向量 |
| [Paperclip：你的-AI-虛擬公司，預算全自動](<../AI 工具/Paperclip：你的-AI-虛擬公司，預算全自動.md>) | Paperclip AI 虛擬公司：多 Agent 組織架構 + Auto-Budgeting 自動分配 API 額度 |
| [Printing-Press：AI-Agent-的-CLI-瑞士刀](<../AI 工具/Printing-Press：AI-Agent-的-CLI-瑞士刀.md>) | Printing Press：AI Agent 的 CLI 瑞士刀 |
| [Threads-API](<../AI 工具/Threads-API.md>)（📌 stub） | 官方 API 僅限自己帖子；GitHub 開源替代截斷，需 Threads refetch |
| [Vibe-Coding-亂象與工程師的心累](<../AI 工具/Vibe-Coding-亂象與工程師的心累.md>) | Vibe Coding 亂象與工程師的心累 |
| [guizang-ppt-skill：AI-高質感雜誌風-PPT-神器](<../AI 工具/guizang-ppt-skill：AI-高質感雜誌風-PPT-神器.md>) | 單檔 HTML 簡報技能：Editorial Magazine / Swiss International 兩套風格、32 種版面、WebGL 動畫 |
| [ralph-loop plugin 原理](<../AI 工具/ralph-loop plugin 原理.md>) | ralph loop plugin 原理 |
| [vibe-coding-app-資安問題總整理](<../AI 工具/vibe-coding-app-資安問題總整理.md>) | vibe coding app 資安問題總整理 |
| [一人到整個團隊](<../AI 工具/一人到整個團隊.md>) | Claude 扮演七角色（CEO/CPO/QA 等）依序審核，solo founder 打造開發流水線 |
| [三周24-7-AI-Agent開發團隊：架構與演進](<../AI 工具/三周24-7-AI-Agent開發團隊：架構與演進.md>) | 三周24 7 AI Agent開發團隊：架構與演進 |
| [不是所有經驗都能成為-AI-Skill](<../AI 工具/不是所有經驗都能成為-AI-Skill.md>) | 不是所有經驗都能成為 AI Skill |
| [九天打造-Hermes-AI：越用越聰明的個人-AI-Wiki](<../AI 工具/九天打造-Hermes-AI：越用越聰明的個人-AI-Wiki.md>) | Hermes Agent 完整教學：三層 .md 人格配置、Telegram/Gmail/Health 整合、雙 Agent 架構 |
| [史丹佛-Vibe-Coding：告別感覺寫程式](<../AI 工具/史丹佛-Vibe-Coding：告別感覺寫程式.md>) | 史丹佛 Vibe Coding：告別感覺寫程式 |
| [實測了上百個skill後，我只留下了這10個skill](<../AI 工具/實測了上百個skill後，我只留下了這10個skill.md>) | 實測了上百個skill後，我只留下了這10個skill |
| [擺脫糊字！AI簡報組合技](<../AI 工具/擺脫糊字！AI簡報組合技.md>) | NotebookLM→Nanobanana→LightPDF 三步解決 AI 簡報糊字不能編輯 |
| [框架工程：AI優先，重塑你的組織](<../AI 工具/框架工程：AI優先，重塑你的組織.md>) | 框架工程：AI優先，重塑你的組織 |
| [用Obsidian建立你的LLM知識庫](<../AI 工具/用Obsidian建立你的LLM知識庫.md>) | Obsidian 搭建 LLM Wiki 教學；作者 PDF 站已改版為 portfolio，無教學內容 |
| [簡報地獄有救！AI免費轉PPT無痛編輯](<../AI 工具/簡報地獄有救！AI免費轉PPT無痛編輯.md>) | 簡報地獄有救！AI免費轉PPT無痛編輯 |
| [超好看開源日式風格Skill](<../AI 工具/超好看開源日式風格Skill.md>)（📌 stub） | 開源日式風格 Skill，含 agent 設計指南；個人免費、商用需授權 |
| [部署平台怎麼選？Vercel、Railway、GitHub-Actions-成本與應用場景](<../AI 工具/部署平台怎麼選？Vercel、Railway、GitHub-Actions-成本與應用場景.md>) | 部署平台怎麼選？Vercel、Railway、GitHub Actions 成本與應用場景 |
| [開發者，別再浪費-tokens](<../AI 工具/開發者，別再浪費-tokens.md>) | 3 個 GitHub repo（CLI 壓縮 / 結構化 context / prompt 控制）連結全截斷，需 refetch |
| [Hermes-AI-Agent：會自己進化的懶人助手](<../AI 工具/AI Agent/Hermes-AI-Agent：會自己進化的懶人助手.md>) | Hermes AI Agent：會自己進化的懶人助手 |
| [Google-Agents-CLI：AI-助手專屬雲端-Agent-開發](<../AI 工具/AI Agent/Google-Agents-CLI：AI-助手專屬雲端-Agent-開發.md>) | Google Agents CLI：AI 助手專屬雲端 Agent 開發 |
| [AI-Agent-技能生態系成形-2](<../AI 工具/AI Agent/AI-Agent-技能生態系成形-2.md>) | AI Agent 技能生態系成形 2 |
| [AI-Agent跨儲庫盲區與解方](<../AI 工具/AI Agent/AI-Agent跨儲庫盲區與解方.md>) | AI Agent跨儲庫盲區與解方 |
| [Harness-Engineering：AI-應用致勝之道](<../AI 工具/AI Agent/Harness-Engineering：AI-應用致勝之道.md>) | Harness Engineering：AI 應用致勝之道 |
| [Harness-Engineering：AI-時代工程師的新核心](<../AI 工具/AI Agent/Harness-Engineering：AI-時代工程師的新核心.md>) | Harness Engineering：AI 時代工程師的新核心 |

## Claude Code 社群帖子

| 文件 | 重點 |
|------|------|
| [Claude 生態系指南](<../AI 工具/Claude-Code/Claude 生態系指南.md>) | Claude / Claude Code / Cowork、Skills、Connectors、Plugins 與 Skill 安裝指南 |
| [25-個-Claude-Code-日常指令](<../AI 工具/Claude-Code/25-個-Claude-Code-日常指令.md>) | 25 個 Claude Code 日常指令 |
| [4-招寫好-CLAUDE.md-降低-token-消耗](<../AI 工具/Claude-Code/4-招寫好-CLAUDE.md-降低-token-消耗.md>) | 4 招寫好 CLAUDE.md 降低 token 消耗 |
| [ADHD-友善的-Claude-Code-狀態列](<../AI 工具/Claude-Code/ADHD-友善的-Claude-Code-狀態列.md>) | ADHD 友善的 Claude Code 狀態列 |
| [AI-Skill-優化：達爾文式棘輪進化法](<../AI 工具/Claude-Code/AI-Skill-優化：達爾文式棘輪進化法.md>) | AI Skill 優化：達爾文式棘輪進化法 |
| [AI-實用評估-GitHub-專案：打破迷思](<../AI 工具/Claude-Code/AI-實用評估-GitHub-專案：打破迷思.md>) | AI 實用評估 GitHub 專案：打破迷思 |
| [AI助理不給答案，卻讓我改變最多](<../AI 工具/Claude-Code/AI助理不給答案，卻讓我改變最多.md>) | AI助理不給答案，卻讓我改變最多 |
| [AI外接硬碟：Claude-Mem解決記憶斷片](<../AI 工具/Claude-Code/AI外接硬碟：Claude-Mem解決記憶斷片.md>) | AI外接硬碟：Claude Mem解決記憶斷片 |
| [AI寫程式：品質、穩定與基礎功](<../AI 工具/Claude-Code/AI寫程式：品質、穩定與基礎功.md>) | AI寫程式：品質、穩定與基礎功 |
| [AI工具：Cowork工作流與Claude技能](<../AI 工具/Claude-Code/AI工具：Cowork工作流與Claude技能.md>) | AI工具：Cowork工作流與Claude技能 |
| [AI新OS：設計系統雙鏡片思考](<../AI 工具/Claude-Code/AI新OS：設計系統雙鏡片思考.md>) | AI新OS：設計系統雙鏡片思考 |
| [AI開發：深究細節，方能致用](<../AI 工具/Claude-Code/AI開發：深究細節，方能致用.md>) | AI開發：深究細節，方能致用 |
| [AI點子30-5精煉法](<../AI 工具/Claude-Code/AI點子30-5精煉法.md>) | 先讓 AI 爆 30 個想法再精煉 5 個，比直問效果更好；支援 Claude Code skills 安裝 |
| [Anthropic-Claude-技能包：文件排版神器](<../AI 工具/Claude-Code/Anthropic-Claude-技能包：文件排版神器.md>) | Anthropic Claude 技能包：文件排版神器 |
| [CLAUDE.md-太長反效果](<../AI 工具/Claude-Code/CLAUDE.md-太長反效果.md>) | CLAUDE.md 太長反效果 |
| [CLAUDE.md-的精準寫法：注意力經濟學](<../AI 工具/Claude-Code/CLAUDE.md-的精準寫法：注意力經濟學.md>) | CLAUDE.md 的精準寫法：注意力經濟學 |
| [CLI-更新檢查，試試-effort](<../AI 工具/Claude-Code/CLI-更新檢查，試試-effort.md>) | CLI 更新檢查，試試 effort |
| [Claude Agent：權限管理與自動化進程](<../AI 工具/Claude-Code/Claude Agent：權限管理與自動化進程.md>) | Claude Agent：權限管理與自動化進程 |
| [Claude Code 對話 Recap：一眼掌握進度](<../AI 工具/Claude-Code/Claude Code 對話 Recap：一眼掌握進度.md>) | Claude Code 對話 Recap：一眼掌握進度 |
| [Claude Code 技能達爾文式進化](<../AI 工具/Claude-Code/Claude Code 技能達爾文式進化.md>) | Claude Code 技能達爾文式進化 |
| [Claude Code 指令風險判讀術](<../AI 工具/Claude-Code/Claude Code 指令風險判讀術.md>) | Claude Code 指令風險判讀術 |
| [Claude Code：打造你的第二大腦](<../AI 工具/Claude-Code/Claude Code：打造你的第二大腦.md>) | Claude Code：打造你的第二大腦 |
| [Claude Pro開發對話額度不足？](<../AI 工具/Claude-Code/Claude Pro開發對話額度不足？.md>) | Claude Pro開發對話額度不足？ |
| [Claude Skill 設定教學推薦？](<../AI 工具/Claude-Code/Claude Skill 設定教學推薦？.md>) | Claude Skill 設定教學推薦？ |
| [Claude 模組化配置，杜絕記憶污染](<../AI 工具/Claude-Code/Claude 模組化配置，杜絕記憶污染.md>) | Claude 模組化配置，杜絕記憶污染 |
| [Claude+Zotero：文獻圖書館速成術](<../AI 工具/Claude-Code/Claude+Zotero：文獻圖書館速成術.md>) | Claude+Zotero：文獻圖書館速成術 |
| [Claude-Code-Codex-Skill-管理：告別-Context-偷吃，輕鬆共享](<../AI 工具/Claude-Code/Claude-Code-Codex-Skill-管理：告別-Context-偷吃，輕鬆共享.md>) | Claude Code Codex Skill 管理：告別 Context 偷吃，輕鬆共享 |
| [Claude-Code-串接-Threads-API-廣告後台卡關](<../AI 工具/Claude-Code/Claude-Code-串接-Threads-API-廣告後台卡關.md>) | Claude Code 串接 Threads API 廣告後台卡關 |
| [Claude-Code-實戰：4-天開發-Picnote-上架-iOS-App](<../AI 工具/Claude-Code/Claude-Code-實戰：4-天開發-Picnote-上架-iOS-App.md>) | Claude Code 實戰：4 天開發 Picnote 上架 iOS App |
| [Claude-Code-效率提升：Slack-通知](<../AI 工具/Claude-Code/Claude-Code-效率提升：Slack-通知.md>) | Claude Code 效率提升：Slack 通知 |
| [Claude-Code-設定外掛教學](<../AI 工具/Claude-Code/Claude-Code-設定外掛教學.md>) | Claude Code 設定外掛教學 |
| [Claude-Code-避坑守則](<../AI 工具/Claude-Code/Claude-Code-避坑守則.md>) | Claude Code 避坑守則 |
| [Claude-Code必學8招：Boris-Cherny進階與避雷](<../AI 工具/Claude-Code/Claude-Code必學8招：Boris-Cherny進階與避雷.md>) | Claude Code必學8招：Boris Cherny進階與避雷 |
| [Claude-Code：AI-Agent-五層架構剖析](<../AI 工具/Claude-Code/Claude-Code：AI-Agent-五層架構剖析.md>) | Claude Code：AI Agent 五層架構剖析 |
| [Claude-Code：五層架構，打造開發團隊](<../AI 工具/Claude-Code/Claude-Code：五層架構，打造開發團隊.md>) | Claude Code：五層架構，打造開發團隊 |
| [Claude-Code：神級-UI-UX-與-GSD-攻略](<../AI 工具/Claude-Code/Claude-Code：神級-UI-UX-與-GSD-攻略.md>) | Claude Code：神級 UI UX 與 GSD 攻略 |
| [Claude-Cowork-與-CLI-的功能落差](<../AI 工具/Claude-Code/Claude-Cowork-與-CLI-的功能落差.md>) | Claude Cowork 與 CLI 的功能落差 |
| [Claude-Opus-4.7-活用心法與性能爭議](<../AI 工具/Claude-Code/Claude-Opus-4.7-活用心法與性能爭議.md>) | Claude Opus 4.7 活用心法與性能爭議 |
| [Claude-減少幻覺的-3-個設定](<../AI 工具/Claude-Code/Claude-減少幻覺的-3-個設定.md>) | Claude 減少幻覺的 3 個設定 |
| [Claude-的心跳與監控清單](<../AI 工具/Claude-Code/Claude-的心跳與監控清單.md>) | Claude 的心跳與監控清單 |
| [Claude-自動化-NotebookLM](<../AI 工具/Claude-Code/Claude-自動化-NotebookLM.md>) | Claude 自動化 NotebookLM |
| [Claude.md-核心上下文管理術](<../AI 工具/Claude-Code/Claude.md-核心上下文管理術.md>) | Claude.md 核心上下文管理術 |
| [ClaudeBar：AI配額監控與Token精算](<../AI 工具/Claude-Code/ClaudeBar：AI配額監控與Token精算.md>) | ClaudeBar：AI配額監控與Token精算 |
| [Claude老員工交接，面試實戰攻略](<../AI 工具/Claude-Code/Claude老員工交接，面試實戰攻略.md>) | Claude老員工交接，面試實戰攻略 |
| [Claude：規劃後委派Codex](<../AI 工具/Claude-Code/Claude：規劃後委派Codex.md>) | Claude：規劃後委派Codex |
| [Firecrawl 讓 Claude Code 輕鬆爬取網站](<../AI 工具/Claude-Code/Firecrawl 讓 Claude Code 輕鬆爬取網站.md>) | Firecrawl 讓 Claude Code 輕鬆爬取網站 |
| [GSD：AI-不變笨的-SDD-基礎建設](<../AI 工具/Claude-Code/GSD：AI-不變笨的-SDD-基礎建設.md>) | GSD：AI 不變笨的 SDD 基礎建設 |
| [Gemma-4-+-Ollama：免費本地版-Claude-Code，別期待奇蹟](<../AI 工具/Claude-Code/Gemma-4-+-Ollama：免費本地版-Claude-Code，別期待奇蹟.md>) | Gemma 4 + Ollama：免費本地版 Claude Code，別期待奇蹟 |
| [GitHub榜首AI調度中心：多Agent協同開發](<../AI 工具/Claude-Code/GitHub榜首AI調度中心：多Agent協同開發.md>) | GitHub榜首AI調度中心：多Agent協同開發 |
| [LLM-Wiki 進階應用](<../AI 工具/Claude-Code/LLM-Wiki 進階應用.md>) | Karpathy LLM Wiki三步建立AI第二大腦，省95% token，含conversations/disagreements子資料夾 |
| [NanoBanana-MCP：賦予-Claude-Code-Gemini-生圖能力](<../AI 工具/Claude-Code/NanoBanana-MCP：賦予-Claude-Code-Gemini-生圖能力.md>) | NanoBanana MCP：賦予 Claude Code Gemini 生圖能力 |
| [NotebookLM-×-Claude-Code-×-Obsidian-自動知識庫](<../AI 工具/Claude-Code/NotebookLM-×-Claude-Code-×-Obsidian-自動知識庫.md>) | NotebookLM × Claude Code × Obsidian 自動知識庫 |
| [Obsidian x Claude：AI二腦讀寫守門術](<../AI 工具/Claude-Code/Obsidian x Claude：AI二腦讀寫守門術.md>) | Obsidian x Claude：AI二腦讀寫守門術 |
| [Obsidian-+-AI：打造-AI-讀得懂的第二大腦](<../AI 工具/Claude-Code/Obsidian-+-AI：打造-AI-讀得懂的第二大腦.md>) | Obsidian + AI：打造 AI 讀得懂的第二大腦 |
| [Obsidian賦予AI持久記憶](<../AI 工具/Claude-Code/Obsidian賦予AI持久記憶.md>) | Obsidian賦予AI持久記憶 |
| [PAPAYA Claude Code：小白秒上手AI開發](<../AI 工具/Claude-Code/PAPAYA Claude Code：小白秒上手AI開發.md>) | PAPAYA Claude Code：小白秒上手AI開發 |
| [Ryan-Mather-的-Claude-Design-實戰七招](<../AI 工具/Claude-Code/Ryan-Mather-的-Claude-Design-實戰七招.md>) | Ryan Mather 的 Claude Design 實戰七招 |
| [Sahil Lavingia：極簡創業精髓九指令入Claude](<../AI 工具/Claude-Code/Sahil Lavingia：極簡創業精髓九指令入Claude.md>) | Sahil Lavingia：極簡創業精髓九指令入Claude |
| [Subagent：省的不是錢，是-Claude-的-context](<../AI 工具/Claude-Code/Subagent：省的不是錢，是-Claude-的-context.md>) | Subagent：省的不是錢，是 Claude 的 context |
| [Superpowers：AI-開發五階段方法論](<../AI 工具/Claude-Code/Superpowers：AI-開發五階段方法論.md>) | Superpowers：AI 開發五階段方法論 |
| [`.claude-`：解決-Claude-代碼理解的代幣浪費](<../AI 工具/Claude-Code/`.claude-`：解決-Claude-代碼理解的代幣浪費.md>) | `.claude `：解決 Claude 代碼理解的代幣浪費 |
| [cc-switch：AI工具整合神器，省時又省力](<../AI 工具/Claude-Code/cc-switch：AI工具整合神器，省時又省力.md>) | cc switch：AI工具整合神器，省時又省力 |
| [claude-code-Hook：你的開發影分身](<../AI 工具/Claude-Code/claude-code-Hook：你的開發影分身.md>) | claude code Hook：你的開發影分身 |
| [gsd-skill：開發者救星，一鍵解決惱人-bug](<../AI 工具/Claude-Code/gsd-skill：開發者救星，一鍵解決惱人-bug.md>) | gsd skill：開發者救星，一鍵解決惱人 bug |
| [jardisTools讓Claude-Code精準理解PHP-Composer套件](<../AI 工具/Claude-Code/jardisTools讓Claude-Code精準理解PHP-Composer套件.md>) | jardisTools讓Claude Code精準理解PHP Composer套件 |
| [req-daemon：自動化-Claude-Codex-開發](<../AI 工具/Claude-Code/req-daemon：自動化-Claude-Codex-開發.md>) | req daemon：自動化 Claude Codex 開發 |
| [三分鐘讓Claude免費生圖](<../AI 工具/Claude-Code/三分鐘讓Claude免費生圖.md>) | 接 Hugging Face MCP，三步啟用 FLUX/Qwen-Image 等開源生圖模型，完全免費 |
| [三指令搞定 AI 工具搬家難題](<../AI 工具/Claude-Code/三指令搞定 AI 工具搬家難題.md>) | 三指令搞定 AI 工具搬家難題 |
| [不客套：砍掉中文AI客套話](<../AI 工具/Claude-Code/不客套：砍掉中文AI客套話.md>) | 不客套：砍掉中文AI客套話 |
| [免費-Claude-Code-技能：100-個爆紅短影音開頭公式](<../AI 工具/Claude-Code/免費-Claude-Code-技能：100-個爆紅短影音開頭公式.md>) | 免費 Claude Code 技能：100 個爆紅短影音開頭公式 |
| [台大李宏毅教授講解-Harness-Engineering：駕馭-AI-的關鍵祕密](<../AI 工具/Claude-Code/台大李宏毅教授講解-Harness-Engineering：駕馭-AI-的關鍵祕密.md>) | 台大李宏毅教授講解 Harness Engineering：駕馭 AI 的關鍵祕密 |
| [告別高昂-API-費！Free-Claude-Code-教學：NVIDIA-免費驅動-AI](<../AI 工具/Claude-Code/告別高昂-API-費！Free-Claude-Code-教學：NVIDIA-免費驅動-AI.md>) | 告別高昂 API 費！Free Claude Code 教學：NVIDIA 免費驅動 AI |
| [打造手機版-claude-code：Telegram-插件設定](<../AI 工具/Claude-Code/打造手機版-claude-code：Telegram-插件設定.md>) | 打造手機版 claude code：Telegram 插件設定 |
| [搞懂Claude最新版：10部YouTube影片實戰教學](<../AI 工具/Claude-Code/搞懂Claude最新版：10部YouTube影片實戰教學.md>) | 搞懂Claude最新版：10部YouTube影片實戰教學 |
| [活用 .claude 資料夾，優化工程師工作流](<../AI 工具/Claude-Code/活用 .claude 資料夾，優化工程師工作流.md>) | 活用 .claude 資料夾，優化工程師工作流 |
| [精選Threads Vibe Coding實戰訣竅](<../AI 工具/Claude-Code/精選Threads Vibe Coding實戰訣竅.md>) | 精選Threads Vibe Coding實戰訣竅 |
| [自製Agent開發與架構](<../AI 工具/Claude-Code/自製Agent開發與架構.md>) | Haiku router 分流執行模式，管家/秘書/智能體三層架構，含 Claude SDK 差異 |
| [Claude-Code：五層架構，打造開發團隊](<../AI 工具/Claude-Code/Claude-Code：五層架構，打造開發團隊.md>)                            | Claude Code：五層架構，打造開發團隊                                                 |
| [Claude-Code：神級-UI-UX-與-GSD-攻略](<../AI 工具/Claude-Code/Claude-Code：神級-UI-UX-與-GSD-攻略.md>)                      | Claude Code：神級 UI UX 與 GSD 攻略                                           |
| [Claude-Cowork-與-CLI-的功能落差](<../AI 工具/Claude-Code/Claude-Cowork-與-CLI-的功能落差.md>)                          | Claude Cowork 與 CLI 的功能落差                                               |
| [Claude-Opus-4.7-活用心法與性能爭議](<../AI 工具/Claude-Code/Claude-Opus-4.7-活用心法與性能爭議.md>)                          | Claude Opus 4.7 活用心法與性能爭議                                               |
| [Claude-減少幻覺的-3-個設定](<../AI 工具/Claude-Code/Claude-減少幻覺的-3-個設定.md>)                                 | Claude 減少幻覺的 3 個設定                                                      |
| [Claude-的心跳與監控清單](<../AI 工具/Claude-Code/Claude-的心跳與監控清單.md>)                                    | Claude 的心跳與監控清單                                                         |
| [Claude-自動化-NotebookLM](<../AI 工具/Claude-Code/Claude-自動化-NotebookLM.md>)                              | Claude 自動化 NotebookLM                                                   |
| [Claude.md-核心上下文管理術](<../AI 工具/Claude-Code/Claude.md-核心上下文管理術.md>)                                 | Claude.md 核心上下文管理術                                                      |
| [ClaudeBar：AI配額監控與Token精算](<../AI 工具/Claude-Code/ClaudeBar：AI配額監控與Token精算.md>)                           | ClaudeBar：AI配額監控與Token精算                                                |
| [Claude老員工交接，面試實戰攻略](<../AI 工具/Claude-Code/Claude老員工交接，面試實戰攻略.md>)                                 | Claude老員工交接，面試實戰攻略                                                      |
| [Claude：規劃後委派Codex](<../AI 工具/Claude-Code/Claude：規劃後委派Codex.md>)                                  | Claude：規劃後委派Codex                                                       |
| [Firecrawl 讓 Claude Code 輕鬆爬取網站](<../AI 工具/Claude-Code/Firecrawl 讓 Claude Code 輕鬆爬取網站.md>)                     | Firecrawl 讓 Claude Code 輕鬆爬取網站                                          |
| [GSD：AI-不變笨的-SDD-基礎建設](<../AI 工具/Claude-Code/GSD：AI-不變笨的-SDD-基礎建設.md>)                               | GSD：AI 不變笨的 SDD 基礎建設                                                    |
| [Gemma-4-+-Ollama：免費本地版-Claude-Code，別期待奇蹟](<../AI 工具/Claude-Code/Gemma-4-+-Ollama：免費本地版-Claude-Code，別期待奇蹟.md>)           | Gemma 4 + Ollama：免費本地版 Claude Code，別期待奇蹟                                |
| [GitHub榜首AI調度中心：多Agent協同開發](<../AI 工具/Claude-Code/GitHub榜首AI調度中心：多Agent協同開發.md>)                          | GitHub榜首AI調度中心：多Agent協同開發                                               |
| [LLM-Wiki 進階應用](<../AI 工具/Claude-Code/LLM-Wiki 進階應用.md>)                                      | Karpathy LLM Wiki三步建立AI第二大腦，省95% token，含conversations/disagreements子資料夾 |
| [NanoBanana-MCP：賦予-Claude-Code-Gemini-生圖能力](<../AI 工具/Claude-Code/NanoBanana-MCP：賦予-Claude-Code-Gemini-生圖能力.md>)          | NanoBanana MCP：賦予 Claude Code Gemini 生圖能力                               |
| [NotebookLM-×-Claude-Code-×-Obsidian-自動知識庫](<../AI 工具/Claude-Code/NotebookLM-×-Claude-Code-×-Obsidian-自動知識庫.md>)          | NotebookLM × Claude Code × Obsidian 自動知識庫                               |
| [Obsidian x Claude：AI二腦讀寫守門術](<../AI 工具/Claude-Code/Obsidian x Claude：AI二腦讀寫守門術.md>)                        | Obsidian x Claude：AI二腦讀寫守門術                                             |
| [Obsidian-+-AI：打造-AI-讀得懂的第二大腦](<../AI 工具/Claude-Code/Obsidian-+-AI：打造-AI-讀得懂的第二大腦.md>)                       | Obsidian + AI：打造 AI 讀得懂的第二大腦                                            |
| [Obsidian賦予AI持久記憶](<../AI 工具/Claude-Code/Obsidian賦予AI持久記憶.md>)                                   | Obsidian賦予AI持久記憶                                                        |
| [PAPAYA Claude Code：小白秒上手AI開發](<../AI 工具/Claude-Code/PAPAYA Claude Code：小白秒上手AI開發.md>)                       | PAPAYA Claude Code：小白秒上手AI開發                                            |
| [Ryan-Mather-的-Claude-Design-實戰七招](<../AI 工具/Claude-Code/Ryan-Mather-的-Claude-Design-實戰七招.md>)                   | Ryan Mather 的 Claude Design 實戰七招                                        |
| [Sahil Lavingia：極簡創業精髓九指令入Claude](<../AI 工具/Claude-Code/Sahil Lavingia：極簡創業精髓九指令入Claude.md>)                    | Sahil Lavingia：極簡創業精髓九指令入Claude                                         |
| [Subagent：省的不是錢，是-Claude-的-context](<../AI 工具/Claude-Code/Subagent：省的不是錢，是-Claude-的-context.md>)                  | Subagent：省的不是錢，是 Claude 的 context                                       |
| [Superpowers：AI-開發五階段方法論](<../AI 工具/Claude-Code/Superpowers：AI-開發五階段方法論.md>)                            | Superpowers：AI 開發五階段方法論                                                 |
| [`.claude-`：解決-Claude-代碼理解的代幣浪費](<../AI 工具/Claude-Code/`.claude-`：解決-Claude-代碼理解的代幣浪費.md>)                     | `.claude `：解決 Claude 代碼理解的代幣浪費                                          |
| [cc-switch：AI工具整合神器，省時又省力](<../AI 工具/Claude-Code/cc-switch：AI工具整合神器，省時又省力.md>)                           | cc switch：AI工具整合神器，省時又省力                                                |
| [claude-code-Hook：你的開發影分身](<../AI 工具/Claude-Code/claude-code-Hook：你的開發影分身.md>)                           | claude code Hook：你的開發影分身                                                |
| [gsd-skill：開發者救星，一鍵解決惱人-bug](<../AI 工具/Claude-Code/gsd-skill：開發者救星，一鍵解決惱人-bug.md>)                         | gsd skill：開發者救星，一鍵解決惱人 bug                                              |
| [jardisTools讓Claude-Code精準理解PHP-Composer套件](<../AI 工具/Claude-Code/jardisTools讓Claude-Code精準理解PHP-Composer套件.md>)          | jardisTools讓Claude Code精準理解PHP Composer套件                               |
| [req-daemon：自動化-Claude-Codex-開發](<../AI 工具/Claude-Code/req-daemon：自動化-Claude-Codex-開發.md>)                     | req daemon：自動化 Claude Codex 開發                                          |
| [三分鐘讓Claude免費生圖](<../AI 工具/Claude-Code/三分鐘讓Claude免費生圖.md>)                                     | 三分鐘讓Claude免費生圖                                                          |
| [三指令搞定 AI 工具搬家難題](<../AI 工具/Claude-Code/三指令搞定 AI 工具搬家難題.md>)                                    | 三指令搞定 AI 工具搬家難題                                                         |
| [不客套：砍掉中文AI客套話](<../AI 工具/Claude-Code/不客套：砍掉中文AI客套話.md>)                                      | 不客套：砍掉中文AI客套話                                                           |
| [免費-Claude-Code-技能：100-個爆紅短影音開頭公式](<../AI 工具/Claude-Code/免費-Claude-Code-技能：100-個爆紅短影音開頭公式.md>)                   | 免費 Claude Code 技能：100 個爆紅短影音開頭公式                                        |
| [台大李宏毅教授講解-Harness-Engineering：駕馭-AI-的關鍵祕密](<../AI 工具/Claude-Code/台大李宏毅教授講解-Harness-Engineering：駕馭-AI-的關鍵祕密.md>)          | 台大李宏毅教授講解 Harness Engineering：駕馭 AI 的關鍵祕密                               |
| [告別高昂-API-費！Free-Claude-Code-教學：NVIDIA-免費驅動-AI](<../AI 工具/Claude-Code/告別高昂-API-費！Free-Claude-Code-教學：NVIDIA-免費驅動-AI.md>)      | 告別高昂 API 費！Free Claude Code 教學：NVIDIA 免費驅動 AI                           |
| [打造手機版-claude-code：Telegram-插件設定](<../AI 工具/Claude-Code/打造手機版-claude-code：Telegram-插件設定.md>)                    | 打造手機版 claude code：Telegram 插件設定                                         |
| [搞懂Claude最新版：10部YouTube影片實戰教學](<../AI 工具/Claude-Code/搞懂Claude最新版：10部YouTube影片實戰教學.md>)                       | 搞懂Claude最新版：10部YouTube影片實戰教學                                            |
| [活用 .claude 資料夾，優化工程師工作流](<../AI 工具/Claude-Code/活用 .claude 資料夾，優化工程師工作流.md>)                            | 活用 .claude 資料夾，優化工程師工作流                                                 |
| [精選Threads Vibe Coding實戰訣竅](<../AI 工具/Claude-Code/精選Threads Vibe Coding實戰訣竅.md>)                          | 精選Threads Vibe Coding實戰訣竅                                               |
| [自製Agent開發與架構](<../AI 工具/Claude-Code/自製Agent開發與架構.md>)                                       | 自製Agent開發與架構                                                            |
| [讓 AI 說重點，省 75% Token](<../AI 工具/Claude-Code/讓 AI 說重點，省 75% Token.md>)                               | 讓 AI 說重點，省 75% Token                                                    |
| [達爾文技能：Claude Code自我進化](<../AI 工具/Claude-Code/達爾文技能：Claude Code自我進化.md>)                              | 達爾文技能：Claude Code自我進化                                                   |
| [雙模型協同與雲端自動修復：高效開發架構](<../AI 工具/Claude-Code/雙模型協同與雲端自動修復：高效開發架構.md>)                                | 雙模型協同與雲端自動修復：高效開發架構                                                     |

---
網址: https://www.threads.com/@cooljerrett/post/DYPZaPAm8pf
作者: ["@cooljerrett"]
tags: [AI]
status: wiki
---

## Main Content

Harness Engineering - Google工程師 Addy Osmani ：為什麼 AI Agent 的好壞，取決於模型以外的東西，這篇文章整理了很多做法值得參考
Agent Harness Engineering：為什麼 AI Agent 的好壞，取決於模型以外的東西，Addy Osmani 這篇文章整理了一個正在成形的概念，叫 Harness Engineering。簡單講就是：一個 coding agent 不是只有模型，而是「模型加上包在模型外面的整套工作系統」。
Addy Osmani 是知名軟體工程師、作家與技術領袖，目前在 Google 擔任 Google Cloud AI 總監。近年以 AI 代理人（AI Agents）開發而聞名於開發者社群，這篇連文章的幾個附圖都是資訊非常多，也一併翻成中文
━━━━━━━━━━━━━━━━━━━━
▍Harness engineering 把這套外層系統當成一個會持續演化的東西。每次 agent 犯錯，都不是單純重跑一次就算了，而是要把那次失敗變成一個永久修正，讓它下次不要再犯同樣的錯。
過去兩年，大家討論 AI 大多都在比模型：哪個最聰明、哪個寫 React 最乾淨、哪個比較不會亂講話。這些當然重要，但它只看到了系統的一半。
模型只是正在運作的 agent 的其中一個輸入。剩下那一整層就是 harness，包括 prompt（你怎麼交代它）、工具（它能用什麼）、context policy（它要記住什麼、忘掉什麼）、hook（自動檢查機制）、sandbox（安全的工作環境）、subagent（分工的小幫手）、feedback loop（做錯後怎麼回來修）、recovery path（出錯後怎麼補救）。它們共同決定模型能不能真的把事情做完。
所以一個普通模型加上好的 harness，常常會比一個強模型加上爛 harness 更穩。越來越多真正有價值的工程工作，不是在選哪個模型，而是在設計模型外面的支撐結構，也就是讓 AI 有一套更好的工作方法。
這個領域現在也開始有名字了。Viv Trivedy ，LangChain 的工程師提出 harness engineering 這個說法，HumanLayer 把 agent failure 視為 configuration skill issue，Anthropic 的工程團隊在談長時間 app design，Birgitta Böckeler 則從使用者端經驗切入。這些討論其實都在指向同一件事：agent 的表現，不只是模型本身，而是整個外層系統一起造成的。
━━━━━━━━━━━━━━━━━━━━
▍什麼是 Harness
Viv Trivedy 給了一個很乾淨的定義：
Agent = Model + Harness
If you're not the model, you're the harness.
也就是說，只要你做的事情不是模型本身，那幾乎都屬於 harness。
Harness 包含所有不是模型本體的程式碼、設定和執行邏輯。單獨一個 raw model 還不是 agent。模型只有在外層 harness 提供狀態、工具執行、回饋迴路和可被強制執行的限制之後，才會變成真正能做事的 agent。
具體來說，harness 包含下面這些東西。原文的技術詞可以先保留，但可以用更白話的方式理解：
System prompt、CLAUDE.md、AGENTS.md、skill files、subagent instructions
概念就是「工作說明書」。它告訴 agent 這個專案怎麼做事、有哪些規矩、遇到哪些情況要怎麼處理。就像新人到公司第一天拿到的 SOP。
Tools、skills、MCP servers，以及它們的工具描述
概念就是「工具箱」。Agent 不是只會聊天，它可以查資料、讀檔案、跑測試、操作瀏覽器、呼叫外部服務。工具描述則像工具上的標籤，告訴 agent 這個工具可以拿來做什麼。
檔案系統、sandbox、headless browser 這類基礎執行環境
概念就是「工作桌和安全實驗室」。檔案系統讓 agent 有地方放資料，sandbox 讓它可以安全地試錯，headless browser 則讓它可以在沒有打開視覺瀏覽器的情況下檢查網頁。
負責啟動 subagent、handoff、model routing 的 orchestration logic
概念就是「分工和派工機制」。什麼時候要叫另一個 agent 來幫忙？什麼時候要把任務交給別人？什麼任務該用哪個模型？這些都屬於 orchestration。
負責 deterministic execution 的 hook 和 middleware，例如 lint check、context compaction
概念就是「自動檢查和自動整理」。例如寫完 code 自動檢查格式，太長的對話自動整理摘要。它們的目的，是把一些不能只靠模型自覺完成的事情，變成系統自動執行。
logs、traces、cost、latency metering 這類 observability 工具
概念就是「監控儀表板」。你要知道 agent 做了哪些事、卡在哪一步、花了多少錢、跑得慢不慢。沒有這些紀錄，就很難知道問題到底出在哪裡。
從核心來看，agent 就是一個會在 loop 裡呼叫工具、觀察結果、繼續往目標前進的系統。白話說，它不是一次回答完就結束，而是像一個工作者：先做一步、看結果、再決定下一步。真正的工程能力，不只在於選模型，也在於設計工具和設計這個工作循環。
這也是為什麼 Claude Code、Cursor、Codex、Aider、Cline 都可以被看成不同的 harness。底層模型可能一樣，但你實際感受到的行為，很大部分是 harness 決定的。
━━━━━━━━━━━━━━━━━━━━
▍重新理解所謂的 Skill Issue
很多工程師看到 agent 做出奇怪的事情，第一反應會怪模型，然後把問題歸類成「等下一代模型變強就會解決」。
Harness engineering 的思維剛好相反。它會先問：這個錯誤是不是可以被讀懂？是不是可以被系統性修掉？也就是說，不是只罵「AI 怎麼又錯了」，而是把錯誤變成下一版系統的改進素材。
Agent 忽略了某個專案慣例，就把規則寫進 AGENTS.md。Agent 執行了危險指令，就寫 hook 去擋。Agent 在 40 步的長任務裡迷路，就把架構拆成 planner 和 executor，讓一個角色負責規劃，另一個角色負責執行。Agent 每次交出來的 code 都壞，就接一個 typecheck 的回饋機制，讓系統自動檢查錯誤，再把錯誤丟回去讓它自己修。
HumanLayer 的說法很直接：這不是模型的問題，是設定的問題（It's not a model problem. It's a configuration problem）。
同一個模型，放在不同 harness 裡，表現可能差很多。把模型放進一個有更好 codebase 工具、更緊的 prompt、更清楚 back-pressure 的環境裡，會把原本沒有被釋放出來的能力打開。
模型理論上能做到的事情，和你實際看到它做到的事情，中間那段落差，很多時候就是 harness gap。換句話說，不一定是「這個人不聰明」，也可能是「工作環境、流程和檢查機制沒有設計好」。
━━━━━━━━━━━━━━━━━━━━
▍Ratchet：每一次錯誤都變成規則
Harness engineering 最重要的習慣，是把 agent 的錯誤當成永久信號，而不是一次性的意外。
如果 agent 送出一個 PR（程式修改提案），裡面把測試註解掉，結果不小心被 merge（合併進正式程式碼），這不是「下次小心」就好。下一版 AGENTS.md 就應該寫清楚：不要註解掉測試，要刪掉或修好。pre-commit hook 應該自動抓出 diff 裡的 .skip(。reviewer subagent 也應該被更新，遇到這種情況就阻擋。白話說，每一次事故都要變成一條檢查清單，而不是只靠人或 AI 記得。
但規則也不是越多越好。Addy 的重點是：限制應該只在你真的觀察到失敗時才加入；當模型變強，某些限制已經不再必要時，也應該移除。
好的 system prompt 裡，每一條規則都應該能追溯到某個曾經發生過的失敗。這讓 harness engineering 不是一套通用框架，而是一個依照特定 codebase（專案程式碼庫）、特定團隊、特定失敗歷史長出來的紀律。
━━━━━━━━━━━━━━━━━━━━
▍從行為往回設計 Harness
設計 harness 最有效的方法，不是先列一堆工具，而是先問：我希望 agent 出現什麼行為？
也就是：
想要的行為 → 為了達成這個行為，需要什麼 harness 設計
每個 harness 元件都應該有明確工作。如果你說不出某個 prompt、hook、middleware、tool 或 subagent 到底在服務哪個具體行為，它就應該被移除。白話說，不要因為看起來很厲害就加功能；每個設定都要能回答「它幫 agent 變好在哪裡」。
這讓 harness engineering 更像產品設計，而不是單純堆設定。好的 harness 不是越複雜越好，而是每一塊都知道自己要解決什麼問題。
━━━━━━━━━━━━━━━━━━━━
▍Filesystem 和 Git：可持久化的狀態
檔案系統是 harness 最基礎的一層。可以把它想成 agent 的工作桌。
模型只能處理塞進 context window 裡的東西。檔案系統讓 agent 有地方讀資料、保存中間產出、卸載暫時不需要塞進 context 的資訊，也讓多個 agent 之間可以協作。
加上 Git 之後，就有了版本紀錄。這很像工作過程中的存檔點：Agent 可以追蹤進度、開分支實驗、保留可比較的變更，也能在出錯時 rollback。
這些東西看起來很基本，但對 agent 來說，它們就是把一次性的文字生成變成可追蹤工作流程的基礎。
━━━━━━━━━━━━━━━━━━━━
▍Bash 和 Code Execution：通用工具層
大部分 agent 都在一種 ReAct loop 裡運作：reason、呼叫工具、觀察結果、再繼續。白話說，就是「想一下、做一下、看結果、再調整」。
與其幫 agent 預先設計每一種可能會用到的工具，不如給它 bash 和 code execution 的能力，讓它能自己組合需要的解法。
這也是為什麼很多 coding agent 對 shell 指令特別依賴。因為 bash 是一種通用工具層，像是給 agent 一組基本工具：可以搜尋檔案、跑測試、轉換格式、檢查輸出、寫小工具，快速把問題拆成可以被執行的步驟。
━━━━━━━━━━━━━━━━━━━━
▍Sandbox 和預設工具
Bash 很有用，但前提是它必須跑在安全環境裡。
Sandbox 提供隔離邊界，讓 agent 可以執行程式碼、檢查檔案、驗證成果，而不會直接傷到主機環境。可以把它想成一個安全實驗室：裡面可以試錯，但不會把外面的正式環境弄壞。
好的 sandbox 不只是安全而已，還會預裝好常見語言環境、測試 CLI、headless browser。這樣 agent 才能自己看到自己做出來的結果，形成 self-verification loop，也就是「自己做完後，自己先檢查一次」。
如果 agent 只能寫，不能跑、不能看、不能驗證，那它很容易停在「看起來完成」而不是真的完成。
━━━━━━━━━━━━━━━━━━━━
▍Memory 和 Search：持續補上知識缺口
模型本身的知識只來自訓練資料和當前 context。Harness 需要用記憶和搜尋去補這個缺口。
像 AGENTS.md 這類 memory file，可以在每次 session 開始時注入專案知識、團隊慣例、過去踩過的坑。這就像把團隊經驗寫成備忘錄，讓 agent 不用每次都從零開始理解環境。
而即時資訊，例如新版 library、最新 API 文件、線上資料，則需要 web search 或 MCP tools。白話說，模型腦中的知識可能過期，所以 harness 要讓它能「上網查」或「接外部資料源」，才能處理最新資訊。
━━━━━━━━━━━━━━━━━━━━
▍對抗 Context Rot
模型有一個現實限制：context window 越塞越滿，推理品質通常會變差。Addy 稱這是 context rot。
Harness 主要用三種方式管理這件事。
第一是 compaction，把舊對話或中間過程整理成摘要，避免 context 爆掉，也避免模型被太多舊訊息干擾。這像是開會到一半先整理會議紀錄，不要把所有逐字稿都攤在桌上。
第二是 tool-call offloading。像 2000 行 log 這種大型工具輸出，不應該整段塞進 context，而是存在檔案系統裡，只保留必要的開頭、結尾和重點。這就像完整資料放進資料夾，桌面上只留摘要。
第三是 progressive disclosure（漸進式揭露）。工具、指令、文件不要一開始全部塞進去，而是在任務真的需要時才載入。這像教新人時不要第一天塞完整本公司手冊，而是在他做到某個任務時，再給對應章節。
━━━━━━━━━━━━━━━━━━━━
▍Long-Horizon Execution：長任務需要結構
長時間、自主執行的 agent 任務，常見兩個問題：太早停下來，以及不會好好拆解問題。這很像人做大型專案時，容易中途以為完成了，或一開始就沒有把工作切成清楚步驟。
Harness 會用幾種結構處理：
Loop 機制會攔截模型想提早結束的行為，讓它在新的 context window 裡繼續朝完成目標前進。白話說，就是系統會問：「你真的做完了嗎？還有沒有驗證？」
Planning 機制會要求模型先把目標拆成 step-by-step plan file，並且在每一步之後透過 self-verification hook 檢查自己的工作。這就像先寫工作清單，每完成一項就打勾並檢查成果。
Split 機制則把「產出」和「評估」拆給不同 agent。因為讓同一個模型自己評自己的作品，天生會有正面偏差。白話說，就是不要讓同一個人又當考生又當考官。
這些設計的目的都一樣：不要只期待模型自己有毅力、自己會規劃、自己會客觀檢查，而是把這些能力結構化到 harness 裡。
━━━━━━━━━━━━━━━━━━━━
▍Hooks 是執行層的強制機制
Hook 的作用，是把「請 agent 這樣做」變成「系統強制這樣做」。這可以想成自動門禁或自動檢查站。
它們會在特定生命週期自動執行，例如工具呼叫之前、檔案修改之後、commit 之前。Hook 可以阻擋危險指令、執行 auto-formatting 來節省 token、跑 test suite、做 typecheck。一般人可以把它理解成：每次 agent 做出關鍵動作前後，系統都會自動檢查一次。
好的 hook 設計原則是：成功時安靜，失敗時大聲。
Typecheck 通過，agent 不需要看到任何東西。Typecheck 失敗，錯誤訊息就直接注入回 loop，讓 agent 自己修正。
這就是 harness 的執行層價值：它不是建議，而是守門。不是提醒 agent「最好不要犯錯」，而是讓某些錯誤根本過不了關。
━━━━━━━━━━━━━━━━━━━━
▍Rulebook 和工具選擇
放在 repo 根目錄的一份 flat markdown file，目前仍然是最高槓桿的設定點。它可以是 AGENTS.md、CLAUDE.md，或其他類似的專案規則檔。
但這份文件應該像飛行員的檢查清單，不應該像一份冗長風格指南。它要短，每一條規則都要是從過去的失敗中賺來的。
工具選擇也是同樣邏輯。10 個職責清楚、描述精準的工具，永遠比 50 個功能重疊的工具更好用。就像工作現場，不是工具越多越專業，而是每個工具都要知道什麼時候用。
還有一個安全問題：工具描述會直接進到 prompt 裡。這代表一個品質很差、甚至有惡意的外部整合，例如未驗證的 MCP server，可能在 agent 開始工作之前，就已經把不該有的指令注入進去。白話說，工具不只是工具，它的說明文字也會影響 agent 的判斷，所以不能隨便接來路不明的工具。
━━━━━━━━━━━━━━━━━━━━
▍生產環境裡的 Harness 長什麼樣子
Addy 用 Fareed Khan 對 Claude Code 架構的估計拆解，來說明成熟 harness 在生產環境裡可能長什麼樣子。
前面提到的概念，幾乎都能在這種架構裡找到對應元件。
Context injection 是知識層，也就是把必要背景資料送進 agent 的地方。Loop state 會放在 memory store 和 worktree isolator 裡，白話說就是保存任務進度、隔離工作區。Destructive-action hooks 藏在 permission gate 後面，也就是危險操作前要先過安全檢查。Subagent context firewall 是多 agent 層的核心，用來避免不同 agent 之間看到不該看的資訊。Tool dispatch registry 則是 MCP servers 和 bash 接進來的地方，可以把它想成工具總機，負責把任務導向正確工具。
也就是說，Claude Code 這類 coding agent 的演進，不只是底層模型變強而已。它的軌跡至少同樣程度是 harness 的演進。
━━━━━━━━━━━━━━━━━━━━
▍Harness 不會變萎縮，只會移動
模型變強之後，harness 不會消失，只會移動。
很容易以為模型越強，外層 scaffolding 就越不需要。但實際上只是某些舊問題變少，新的問題又會出現。
例如新模型讓早期很多 context anxiety 的防護措施變得沒那麼必要。可是模型能力的地板提高之後，原本做不到的任務現在變得可能，這也會帶來全新的失敗模式。
Harness 裡每一個元件，本質上都編碼了一個假設：這件事模型自己做不好。白話說，每個外部輔助設計，背後都在說「這裡不能完全相信模型自己處理」。
當模型進步，過時的 scaffolding 要移除；同時，為了碰到下一個更高的任務邊界，也要建立新的 scaffolding。
━━━━━━━━━━━━━━━━━━━━
▍Training Loop：Harness 也會影響模型訓練
Harness 設計和模型訓練之間，有一個主動的 feedback loop。
Addy 提到，現在很多模型在 post-training 階段，其實會把特定 harness 放在 loop 裡。這會產生某種程度的 overfitting：模型會特別擅長 harness 設計者重視的動作，例如 filesystem ops、bash、subagent dispatch。白話說，模型不只是學一般知識，也會在特定工作環境裡被訓練，所以它會越來越熟悉那套環境的做事方式。
這代表 harness 不是靜態設定檔，而是一個會跟模型一起演化的 living system。
也因此，所謂「最好的 harness」不是抽象上的最好，而是最適合你的任務、你的 workflow（工作流程）、你的失敗模式的那一套。
━━━━━━━━━━━━━━━━━━━━
▍Harness-as-a-Service 正在成形
產業正在從「用 LLM API 寫東西」轉向「用 Harness API 跑東西」。
LLM API 提供的是 completion，也就是「給你一段回答」。Harness API 提供的是 runtime，也就是「給你一套能執行任務的工作環境」。
現在很多 SDK 已經把 loop、工具管理、context management、hook、sandbox 都包好了。工程師不一定要從零打造 orchestration，而是可以選一個 harness framework，設定核心模組，然後把心力放在自己領域的 prompt 和工具設計上。
這也讓 troubleshooting 變得比較可規模化。你不是每次都重造一套 agent 架構，而是在一個拆分良好的 configuration surface 上調整。白話說，以後做 agent 可能比較像調整一台機器，而不是每次都從零打造整座工廠。
━━━━━━━━━━━━━━━━━━━━
▍接下來會往哪裡走
Addy 的觀察是：現在排名前面的 coding agents，看起來彼此之間的相似度，甚至比它們底下使用的模型還高。
模型不同，但 harness pattern 正在收斂。整個產業正在快速辨認出：要把生成式文字變成可交付軟體，到底需要哪些真正承重的 scaffolding。
下一步更有趣的問題會超過單一 agent。例如多個 agent 並行協作、agent 自己分析自己的執行軌跡來修正 harness 層問題、以及環境能根據任務即時組裝工具。
最後，harness 會越來越不像靜態設定檔，而更像 compiler。白話說，它不只是放幾條規則給 agent 看，而是會根據任務，把工具、流程、限制和檢查機制組裝成一套可執行的工作系統。
ddy 也補充，如果你正在找 agent harness framework，可以看看 Fred K. Schott 做的 Flue。它顯然也受到這篇文章早期版本的啟發
Read more

x.com/addyo…

## Sources

- [AI Agent 效能關鍵：Harness Engineering](https://www.threads.com/@cooljerrett/post/DYPZaPAm8pf) | 作者: cooljerrett

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

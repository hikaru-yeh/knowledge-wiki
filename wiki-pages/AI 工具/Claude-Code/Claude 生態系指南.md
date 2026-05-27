---
網址: https://www.threads.com/@listentozapao/post/DXMWHkxlio1
作者: ["@listentozapao"]
tags: []
status: wiki
---

## Main Content

來源為 Anthropic 官方文件、與 Claude 的問答、Reddit/Youtube 影片等社群討論，截止日期 2026 年 4 月

這篇文章會寫：

- **Claude 有哪些產品？**
    
- **Claude 有哪些必安裝 Skills**
    
- **怎麼安裝 Skills**
    
- **延伸閱讀：如果你想動手寫 Skills**
    

> **！大問題所以寫在第一頁！！！**
> 
> 包含 ChatGPT、Claude 自己、Gemini，在回答 Claude 生態系相關問題時幾乎都是全錯。連最基本的「有哪些 Skill 是預設」都會答錯，hallucination 情況非常嚴重。建議你們一定要請它**指出資訊來源**，再自己到那個頁面去驗證！

> 這篇你讀完就好不用存，因為存了也不能幫你客製化自己的 Skill。真正有用的是理解概念之後，花時間把自己的工作方式寫進去。

---

## 基本架構

### Claude 有哪些產品？

Anthropic 官網把產品分成三類：**Claude, Claude Code, Cowork**。

_(Anthropic 自己網站的不同地方分類也不一樣，頂部導覽和頁尾的分法就不一樣了，這邊用頁首的分類)_

**三個核心產品：**

- **Claude**：就是 claude.ai，你現在用的這個。包含網頁版、手機 App、桌面 App。日常對話、寫作、分析都在這裡。`免費版和付費版都能用`
    
- **Claude Code**：給開發者寫程式用的工具。可以直接讀取你電腦裡的程式碼、修改檔案、執行指令。這是比較進階的用法且需要付費，但非常方便，其實沒有想像中難，可以用自然語言對話，也可以嘗試去用用 Claude Code。`需要付費方案`
    
- **Cowork**：讓 Claude 自動完成多步驟任務的工具，不需要懂寫程式。例如整理資料夾、從多份文件彙整資料、自動化重複性工作。`需要付費方案`
    

**那 Claude for Chrome/for Excel 那些算什麼？**

這些是**延伸功能**。概念是把 Claude 嵌入到你已經在用的工具裡，讓你不用切換視窗就能用 Claude。例如 **Claude for Chrome** 讓 Claude 直接幫你導覽網頁、填表單，**Claude for Excel** 可以在試算表裡用 Claude 分析資料、寫公式。

---

## 擴充機制

### Skills vs. Connectors vs. Plugins

**什麼是 Skills？**

Skills 本質就是**一串文字**，一個 Markdown 檔案。

但比「很詳細的 prompt」再精確一點的說法是：**它是給 Claude 讀的操作手冊**。一般 prompt 是你告訴 Claude「幫我做 X」，Skill 是在說「當你需要做 X 這類任務時，這是最佳實踐、注意事項、和範例」。

差別在於：

- **普通 prompt**：每次對話都要手動帶進去
    
- **Skill**：放在固定路徑，Claude 啟動時掃描名稱和描述，符合任務就自動載入，你不用每次提
    

所以 Skill 的魔法不在格式，而在**自動觸發的機制**和把**人類試錯累積的知識固化下來**的概念。Skill 之所以有效，是因為有人花時間總結出「什麼樣的 XX 會讓輸出變差」然後寫進去，那些知識本來只存在某人腦子裡，現在變成可以複用的文字。說穿了就是 prompt engineering 的模組化和自動化。

通常他會是一個資料夾，裡面有一個叫 `SKILL.md` 的文件。

**運作方式**：Claude 啟動時會讀每個 Skill 的名稱和描述，等你說的話符合某個 Skill 的描述時，才把完整內容載入，自動觸發。不需要你手動呼叫。_(但手動指定可以跳過自動偵測的判斷步驟，稍微省一點時間／token)_

> Skills 的格式是開放標準，不只 Claude 能用，OpenAI Codex、Cursor、Gemini CLI 也都支援，所以你寫一個 Skill，理論上可以在多個 AI 工具之間共用。

---

## 擴充機制

### 什麼是 Connectors？什麼是 Plugins？

**什麼是 Connectors？**

讓 Claude 能存取外部服務的整合工具。背後用的是 **MCP (Model Context Protocol)** 協議，透過 OAuth 認證（也就是那種「用 Google 帳號登入」的機制）連接到外部服務。

例子：連接 Google Drive 讓 Claude 能讀你的雲端文件、連接 Slack 讓 Claude 看你的工作訊息、串接 GitHub 讓 Claude 幫你管理程式碼。

**什麼是 Plugins？**

把 Skills、Connectors、斜線指令打包在一起的套件。2026 年 1 月隨 Cowork 一起推出，現在有 marketplace 可以瀏覽安裝。

如果 Skill 是一張食譜卡，**Plugin 就是整本食譜加上廚具組**。你安裝一個 Plugin，可能同時裝了好幾個 Skill 加上幾個 Connector 加上幾個斜線指令。

例子：法律 Plugin 裡面包含審閱合約的 Skill、連接文件系統的 Connector，還有 `/triage-nda`、`/review-contract` 等斜線指令。

---

## 安裝指南

### 所以應該安裝哪些 Skills？怎麼安裝？

**Skills 目前有三種安裝方式**

1. **直接從目錄選**
    
    在 Claude 網頁版的 chat 介面，點「Add skill」進入 Directory，瀏覽後直接點安裝。最簡單，適合大多數用戶。
    
2. **到官方 GitHub 下載後，從 Claude 網頁版上傳**
    
    前往 `github.com/anthropics/skills`，找到你要的 Skill 資料夾下載，再從 Claude 網頁版設定頁面手動上傳。適合目錄裡找不到、但 GitHub 上有的 Skill，例如 frontend-design。
    
3. **透過 Claude Code CLI 安裝**
    
    如果你有在用 Claude Code，可以在終端機下 npx 指令直接安裝，Skill 會存在 `~/.claude/skills/`。
    

> 注意：claude.ai Directory 和 Claude Code Marketplace 是兩個完全獨立的地方，各自決定上架哪些 Skill，不互通。同一個 Skill 名稱在兩邊都有，不代表內容一樣。

---

## 安裝指南

### 可以裝哪些 Skill？

|**名稱**|**他是幹嘛的**|**Remark**|
|---|---|---|
|**docx, xlsx, pptx, pdf**|處理各種辦公室文件格式，包含讀取、編輯、建立|預設的，任何新帳號都會有，不用安裝|
|**file-reading, pdf-reading**|讓 Claude 用正確方式讀取你上傳的各種檔案類型|預設的，應該也不用安裝，但沒有找到官方文件|
|**skill-creator**|帶你一步步把自己的工作方式封裝成新的 Skill|目前應該也是自動都有（昨天創了免費的新帳號，已經預設裝好）|
|**canvas-design**|做海報、單頁設計、視覺藝術品|目錄裡面有|
|**theme-factory**|10 套預設配色與字體主題，一句話換整套風格|這個真的蠻實用的但我自己還沒用過|
|**Frontend-design**|讓 Claude 做網頁、介面時有設計個性，不再千篇一律|必須自己去 github 下載，或從 powershell 裡面下指令，但我的環境裡他是預裝的不知道為什麼，可以問問自己的 Claude|
|**System-debugging**|強制 Claude 用有方法論的方式 debug|通常是工程師用，必須自己去 github 下載，或從 powershell 裡面下指令|
|**internal-comms**|寫週報、月報、事故報告、FAQ 等內部溝通文件的模板|可以在目錄找到，但其實只是模板，你要花時間自己客製化才有用|
|**brand-guidelines**|把公司的品牌色、字體、視覺規範存成 Skill|可以在目錄找到，但其實只是模板，你要花時間自己客製化才有用|
|**mcp-builder**|當市面上沒有你需要的 Connector 時，幫你自己做一個 MCP Server|一般情況下不會用到，但你可以裝來玩|

---

## 常見問題

### Q: Skills 越少越好？

這個說法不太精確。因為 Skills 並不是一啟動就讀完全部，而是三層架構：

1. 啟動時只讀**名稱和描述**（每個約 100 tokens）
    
2. 偵測到任務符合時，才載入**完整指令**
    
3. 執行中需要附帶腳本或文件，才把那些也載入
    

不過裝太多的話，描述可能被系統截斷，Claude 反而不知道什麼時候該觸發哪個。

> 但 Skill 的描述寫得精確，的確比裝得多更重要。另外，我看到「官方建議 2000 token 以內」的說法，不過官方文件裡沒找到這個數字。官方說的是 SKILL.md 建議控制在 **500 行以內**，超過就拆檔案。

閱讀完後你應該也能發現，**實際上 Skills 並不是萬靈丹**。除了通用 Skills，其他都需要你**客製化自己的**，才能發揮它的效用（例如你公司的常用語境、你喜歡的設計概念、你需要的寫作模式）。不然的話成果跟沒有 Skill 的 Claude 是一樣的。所以才說這篇你讀完就好不用存，因為存了也不能幫你客製化自己的 Skill。

---

## 額外閱讀

### 如果你打算自己寫 Skills...

來源：Claude API Docs — Skill authoring best practices

**所以寫 Skill 一定要：「寫得短、精準、只寫 AI 不知道的東西」**

1. **只寫 Claude 不懂的東西**：不要解釋 PDF、Python 是什麼。只需要補充「你這個專案的特定規則、偏好、流程」。
    
2. **SKILL.md 建議控制在 500 行以內**：超過就拆成多個檔案，讓 Claude 按需載入。
    
3. **Description 比內容更重要**：description 是 Claude 決定「要不要觸發這個 Skill」的依據。要寫「做什麼」加「什麼時候用」，用第三人稱，包含關鍵詞。
    

**怎麼寫，建議的流程是：**

1. 先自己做一次任務，注意自己對 Claude 重複說了什麼
    
2. 任務要寫清楚，越具體越好，方向跑掉也是在燒 token
    
3. 叫 Claude 幫你把那些東西整理成 Skill 初稿
    
4. 自己再審一遍，刪掉 Claude 本來就知道的廢話
    
5. 用小循環跑：實作 ➔ 測試 ➔ 修正，不要一次下超大任務
    

---

## 額外閱讀

### 有效 Skills 的檢查清單

分享 Skill 前，請確認：

**核心品質**

- [ ] 描述具體且包含關鍵詞
    
- [ ] 描述同時包含功能和使用時機
    
- [ ] SKILL.md 本文在 500 行以內
    
- [ ] 額外細節在獨立檔案中
    
- [ ] 無時效性資訊
    
- [ ] 全文使用一致的術語
    
- [ ] 範例具體，而非抽象
    
- [ ] 檔案參考只有一層深度
    
- [ ] 適當使用漸進式揭露
    
- [ ] 工作流程有清晰的步驟
    

**程式碼和腳本**

- [ ] 腳本解決問題，非推卸給 Claude
    
- [ ] 錯誤處理明確且有幫助
    
- [ ] 無「魔法常數」
    
- [ ] 所需套件已列並確認可用
    
- [ ] 腳本有清晰的文件說明
    
- [ ] 無 Windows 風格路徑
    
- [ ] 關鍵操作包含驗證步驟
    
- [ ] 品質關鍵任務包含回饋迴路
    

**測試**

- [ ] 已建立至少三個評估
    
- [ ] 已用 Haiku、Sonnet 和 Opus 測試
    
- [ ] 已用真實使用情境測試
    
- [ ] 已整合團隊回饋（如適用）

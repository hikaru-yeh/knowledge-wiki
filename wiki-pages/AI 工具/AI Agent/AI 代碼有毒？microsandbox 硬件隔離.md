---
網址: https://www.threads.com/@buildthink.ai/post/DYbOTe4D_IX
作者: ["@buildthink.ai"]
tags: [Claude Code]
status: wiki
---

## Main Content

上一篇講了 npm 套件可能有毒——今次講：就算代碼有毒，怎麼確保你的系統不受傷害
如果你正在用 Claude Code、Codex、Cursor 或任何 AI coding agent，有一件事你可能沒想過：
這些 agent 生成的代碼，是直接在你的電腦上執行的。沒有隔離，沒有沙盒，沒有保護
microsandbox 是一個讓 AI agent 在一個硬件隔離的微型虛擬機裡執行代碼。就算 AI 寫了惡意代碼、刪錯文件、或者被 prompt injection 攻擊，影響範圍只限於那個用完即棄的沙盒，你的真實系統完全不受影響
這篇整理了完整拆解：
→ 為什麼 AI agent 需要沙盒田
→ Docker 的隔離為什麼不夠用
→ microVM 和 container 到底差在哪
→ microsandbox 的核心設計：怎麼做到 100ms 啟動 + 硬件隔離
→ 實際怎麼用：CLI、SDK、MCP 三種接入方式
→ 同類工具對比：microsandbox vs E2B vs Daytona
儲存 💾
追蹤
@buildthink.ai
獲取更多 AI 工具實戰教學

多謝 👍 希望慳到大家查文檔嘅時間。
三個工具定位唔同——想自架免費用 microsandbox、想託管免煩惱用 E2B、需要完整開發環境用 Daytona，揀啱自己嘅場景就得。

## 圖片文字

### 圖片 1

| AI 工具速報

你的 AI Agent
正在你的電腦上裸奔

microsandbox — 6000+ star 的開源沙盒，
100ms 啟動，硬體級隔離

讓 Claude Code、Codex、Cursor 等
AI coding agent 在隔離的 microVM 裡安全執行代碼。

01                                02                                03
AI Agent                          microsandbox                      真實系統
生成代碼                            隔離執行                          不受影響
[Image: Code editor icon]         [Image: Shield/box icon]          [Image: Laptop with checkmark]

AI Agent 撰寫、調用                在 microVM 中執行代碼，            隔離環境內的變更
並準備執行程式碼                    硬體級隔離，快速啟動                不影響你的真實電腦

[Image: Star icon]                [Image: Lightning bolt icon]      [Image: Chip icon]                [Image: Open source icon]
6000+                             100ms                             5MB                               開源
star                              啟動                              記憶體                            自由、透明、可審計

• @buildthink.ai •

### 圖片 2

AI 工具速報
P9
安裝和第一次使用
5 分鐘跑起來

ⓘ 前提：Linux (需要 KVM) 或 macOS (Apple Silicon)

01
Step 1：安裝
curl -fsSL https://get.microsandbox.dev | sh

02
Step 2：跑第一個沙盒
msb run python -- python3 -c "print('Hello from microVM!')"

03
Step 3：用 SDK 嵌入你的應用
*   npm install microsandbox (TypeScript)
*   pip install microsandbox (Python)

04
Step 4：連接 MCP server
*   在 Claude 設定加入 microsandbox MCP
*   AI agent 自動在沙盒裡執行代碼

第一次拉鏡像會慢一些，之後用緩存，啟動 < 100ms

@buildthink.ai

### 圖片 3

AI 工具速報
microsandbox 核心設計
microsandbox 怎麼做到又快又安全?

01                                      02
        硬體隔離                                100ms
        (Hardware Isolation)                    以內啟動
    •   基於 Firecracker microVM            •   優化的內核鏡像 +
        技術 (AWS Lambda 同款)                  最小化設備模型 +
                                                VM 快照緩存
    •   每個沙盒有獨立 kernel、
        網路命名空間                        •   極快啟動

03                                      04
        極低資源消耗                            OCI 相容
    •   每個 VM 基礎佔                    •   Docker Hub、
        5MB 記憶體                              GHCR 上的標準鏡像
                                                直接用
    •   一台普通伺服器
        可以跑幾百個沙盒                    •   不用學新的打包格式

05
        Secret 不進入 VM
    •   密鑰通過代理注入，永遠不會出現在 VM 內部
    •   就算 VM 被攻破，密鑰也拿不到

P4                                      @buildthink.ai

### 圖片 4

AI 工具速報

### 圖片 5

AI 工具速報                                                              P8

同類工具對比
microsandbox vs E2B vs Daytona

microsandbox                                E2B                                     Daytona
本地自架 /                                  雲端託管 /                                  雲端或自架 /
開源 Apache 2.0 /                           開源核心 /                                  90ms 冷啟動
100ms 啟動                                  Firecracker                             (最快)
                                            microVM

5MB 基礎記憶體 /                            SDK 設計最成熟 /                            完整的開發環境
MCP 原生支援                                Code Interpreter                        (不只是沙盒)
                                            內建

免費 /                                      免費額度後                                  AGPL-3.0 授權
你控制所有                                  按用量收費 /                                (注意 copyleft)
基礎設施                                    Session 上限
                                            24 小時

限制：仍在 beta、                           適合：不想管                                適合：需要
目前不支援                                  基礎設施的團隊                              持久化開發環境
Windows                                                                             的場景


想自架 + 免費                               想託管 + 快速上手                           需要完整 CDE
→                                           →                                           →
microsandbox                                E2B                                         Daytona

                                            @buildthink.ai

### 圖片 6

AI 工具速報

### 圖片 7

AI 工具速報
P2 / 10
為什麼需要沙盒
AI Agent 生成的代碼，直接在你的電腦上跑

AI 生成一段代碼

代碼直接在你的本地環境執行

它能存取你的文件系統、環境變數、
SSH key、雲端憑證

沒有任何隔離

01 PocketOS 刪庫事件
*   Agent 自行決定刪除
    Railway volume
*   9 秒鐘清空生產資料庫
    + 所有備份
*   三年客戶數據消失

02 node-ipc 事件
*   惡意套件偷取
    100+ 種憑證
*   如果在沙盒裡執行，
    什麼都偷不到

不是 AI 有惡意，而是它有權限但沒有隔離

@buildthink.ai

### 圖片 8

P7 AI 工具速報

實際使用場景
什麼時候該用沙盒？

必須用沙盒的場景                                可以不用的場景

AI agent 自動生成                                你自己寫的、
並執行代碼                                        完全信任的代碼

執行從 npm / PyPI
下載的未經審查的套件                            只做 API 調用
                                                不執行代碼的 agent

處理用戶上傳的
文件或代碼

CI/CD pipeline                                  純文字生成的
中執行測試                                        AI 應用

分析可能有
惡意的代碼

簡單原則 —
如果代碼不是你寫的，
就不要在你的系統上裸跑

@buildthink.ai

### 圖片 9

P5 | AI 工具速報
三種接入方式
CLI、SDK、MCP —— 怎麼接入你的工作流

01
CLI (最快上手)

msb run python --
python3 -c "print('Hello')"

• 一行指令，在沙盒裡跑
  任何東西
• 適合：快速測試、手動操作

02
SDK (程式碼整合)

const sandbox = await
Sandbox.builder("my-sandbox")
.image("python")
.cpus(1)
.memory(512)
.create();

• TypeScript / Python SDK
• 適合：整合到你的 AI 應用中

03
MCP Server
(AI Agent 直接用)

Claude / GPT 透過
MCP 協議發現並調用沙盒

AI 生成代碼 → 發送到
microsandbox → 在
隔離環境執行 → 返回結果

AI 永遠不直接接觸
你的系統

快速接入
幾分鐘內開始使用

靈活整合
適配各種技術棧

安全隔離
始終在沙盒中執行

專為 AI 打造
與 AI Agent 無縫協作

@buildthink.ai

### 圖片 10

P10 | AI 工具速報

你的 AI Agent
不該有權限毀掉你的系統

microsandbox – 100ms 啟動・硬體隔離・開源・本地運行

理解風險                 用沙盒隔離                 保護真實系統
AI 工具能做很多事，         microsandbox 提供          真實系統不受影響，
也可能做錯很多事。         硬體級隔離，快速啟動，       安全用 AI，放心創造。
                         不牽連主機。

GitHub: github.com/superradcompany/microsandbox
Apache 2.0・6000+ star・MCP 原生支援

上一篇講了套件可能有毒 → 這次講怎麼讓毒藥傷不了你

追蹤 @buildthink.ai
獲取更多 AI 工具實戰教學

@buildthink.ai

## Sources

- [AI 代碼有毒？microsandbox 硬件隔離](https://www.threads.com/@buildthink.ai/post/DYbOTe4D_IX) | 作者: buildthink.ai

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

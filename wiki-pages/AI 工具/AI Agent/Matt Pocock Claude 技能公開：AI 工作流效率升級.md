---
網址: https://www.threads.com/@kai_ch_chen/post/DYbFsNlD2uh
作者: ["@kai_ch_chen"]
tags: [Claude Code]
status: wiki
---

## Main Content

mattpocock 把他自己的 .claude/skills 整包公開放上 GitHub。一週衝到 48,564 顆星，trending 第二名。
我挑出最值得裝的三個：
→ TDD：紅綠重構迴圈，一次切一片功能
→ Diagnose：debug 別亂猜，先複現再修
→ improve-codebase-architecture：把 shallow module 變 deep，AI 才看得懂
裝法一行：
npx skills@latest add mattpocock/skills --yes --global
我看到一個朋友的廣告投手 team，把 TDD 那條改成「先寫驗收 SQL，再讓 Claude 寫廣告抓取腳本」，bug 直接砍一半。
skills 不是新概念，是把你已經會的工作流寫成 SKILL.md 給 Claude 自動套。

## 圖片文字

### 圖片 1

AI 應用 🛠️ 工具教學
3 個 skill 把 Claude
mattpocock 公開他的 .claude/skills
/ GitHub trending #2 / 48,564 ⭐

1 TDD
先寫測試，再讓 Claude 補實作

2 Diagnose
先定位問題，再動手修

3 improve-codebase-architecture
整理架構，降低長期維護成本

@kai_ch_chen
更少重複，更多創造。

### 圖片 2

TDD — 紅綠重構
紅：先寫失敗測試 / 綠：寫最少 code 讓它過 / 重構：抽乾淨

1 紅
先寫失敗測試
測試檔案
> npm test
> FAIL
> 1 failing test

2 綠
寫最少 code 讓它過
function add(a, b) {
  return a + b;
}

3 重構
抽乾淨
雜亂程式
乾淨架構

@kai_ch_chen
更少重複，更多創造。

### 圖片 3

Diagnose — 結構化 debug
先復現問題 / 縮小範圍再修 / 別亂猜

1 先復現問題
   先把錯誤變成可重現案例，
   記錄輸入、環境與預期結果。
                                 $ npm test
                                 FAIL test/login.spec.ts
                                 Error: Expected 200
                                 Received 500
                                 ...

2 縮小範圍再修
   用最小測試、二分法與日誌
   定位根因，再動手修改。
                                 Log 測試案例 假設

3 別亂猜
   每次只驗證一個假設，
   讓 debug 變成有證據的流程。
                                 ✓ 假設 A
                                 ☐ 假設 B
                                 ☐ 假設 C
                                 — 觀察
                                 — 日誌
                                 — 結果

@kai_ch_chen
                                 更少重複，更多創造。

### 圖片 4

improve-codebase-architecture
shallow module → deep / 小介面 + 大實作 / AI 才看得懂結構

1 shallow module
先讓外層保持薄：
只放命名、邊界與流程。
Module
命名
邊界
流程

2 deep implementation
把複雜度收進深層模組，
讓大實作藏在穩定介面後。
Interface
Deep Implementation

3 AI 讀得懂結構
清楚的層次與小介面，
讓 AI 更容易定位、修改、驗證。
Module
A B C
AI

@kai_ch_chen
更少重複，更多創造。

### 圖片 5

朋友的廣告投手 team 案例
把 TDD 改成「先寫驗收 SQL」/ bug 砍一半 / Claude 寫廣告抓取腳本

1 先寫驗收 SQL
把 TDD 從「先寫測試」改成
能驗證成效的 SQL 驗收條件
SELECT *
FROM ads
WHERE ... ↑

2 bug 砍一半
抓資料、比對、匯入流程先有
可驗證規格，錯誤量下降 50%

3 Claude 寫廣告抓取腳本
讓 Claude 依驗收 SQL 補齊
抓取腳本，team 只審核結果

@kai_ch_chen
更少重複，更多創造。

### 圖片 6

一行裝完

`npx skills@latest add`
`mattpocock/skills --yes --global`

`npx skills@latest add`
`mattpocock/skills --yes --global`

你的 .claude/skills 裡幾個 SKILL.md?

先抓一個重點就好。

你最想先試哪一步？

追蹤 @kai_ch_chen 看更多實戰案例

@kai_ch_chen
更少重複，更多創造。

## Sources

- [Matt Pocock Claude 技能公開：AI 工作流效率升級](https://www.threads.com/@kai_ch_chen/post/DYbFsNlD2uh) | 作者: kai_ch_chen

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

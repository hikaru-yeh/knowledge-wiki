---
網址: https://www.threads.com/@one.minute.frontend/post/DW-91B5FOHY
作者: ["@one.minute.frontend"]
tags: []
status: wiki
---

## Main Content

一張圖搞懂 Git Flow vs GitHub Flow vs GitLab Flow
這三種 Git 流程就像是三種不同規模的廚房，管理食材（程式碼）的方式完全不同：

## 1. Git Flow：五星級飯店大餐廳

分工極其細膩，每樣食材都要經過好幾個廚房關卡才能上桌。

- `master`（出菜區）：只有準備好要端給客人的完美成品
- `develop`（大廚房）：所有廚師在這裡匯集做好的配菜
- `feature/*`（備料組）：專門切菜、熬湯的小組，做完送到大廚房
- `release/*`（試吃檢查區）：出菜前的最後擺盤與調味，確認沒問題才送到出菜區
- `hotfix/*`（緊急維修組）：客人吃到蟲了！立刻從出菜區抓回來緊急處理

**特點**：非常穩、非常慢，適合大工程。

## 2. GitHub Flow：熱血路邊攤

老闆兼廚師，講求現點現做、馬上出餐。

- `main`（攤位桌面）：桌面上放的永遠是能賣客人的東西
- `feature/*`（臨時砧板）：想出一道新菜就在旁邊小砧板弄一下
- Pull Request（老闆點頭）：弄好後老闆看一眼，覺得可以就直接倒進主鍋，立刻遞給客人

**特點**：極快、靈活，適合需要一直更新菜單的小店。

## 3. GitLab Flow：連鎖餐廳的中央廚房

覺得路邊攤太隨便、大餐廳太囉唆，改用「分店管理」。

- `main`（總部研發）：研發出新口味的菜色
- `pre-production`（實驗分店）：新菜送到這間店給員工試吃（測試環境）
- `production`（全台門市）：試吃過關，才正式在全台灣所有分店同步推出（正式環境）

**特點**：重視「在哪裡賣」，適合有多個測試關卡的企業。

## Sources

- [Git 三大流程：廚房管理術](https://www.threads.com/@one.minute.frontend/post/DW-91B5FOHY) | 作者: one.minute.frontend

## Cross References

- [[工具軟體-索引]]：工具軟體分類總覽
- [[npm 深度解析與安全指南]]：相關開發工具知識

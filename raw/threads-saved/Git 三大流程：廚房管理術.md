---
base: "[[收藏清單_DB.base]]"
url: "https://www.threads.com/@one.minute.frontend/post/DW-91B5FOHY"
author: "one.minute.frontend"
clip_type: "職場"
date_added: 2026-04-21T13:15:00
---

[https://www.threads.com/@one.minute.frontend/post/DW-91B5FOHY](https://www.threads.com/@one.minute.frontend/post/DW-91B5FOHY)

## 主文

![[IMG_3513.jpeg]]

一張圖搞懂 Git Flow vs GitHub Flow vs GitLab Flow
這三種 Git 流程就像是三種不同規模的廚房，管理食材（程式碼）的方式完全不同：

## 作者留言

·
Author
1. Git Flow：像「五星級飯店大餐廳」
這裡分工極其細膩，每樣食材都要經過好幾個廚房關卡才能上桌。
master (出菜區)： 只有準備好要端給客人的完美成品。
develop (大廚房)： 所有廚師在這裡匯集做好的配菜。
feature/* (備料組)： 專門切菜、熬湯的小組，做完把成品送到大廚房。
release/* (試吃檢查區)： 出菜前的最後擺盤與調味，確認沒問題才送到出菜區。
hotfix/* (緊急維修組)： 客人吃到蟲了！立刻從出菜區抓回來緊急處理。
特點： 非常穩、非常慢，適合大工程。

·
Author
2. GitHub Flow：像「熱血路邊攤」
老闆兼廚師，講求的是現點現做、馬上出餐。
main (攤位桌面)： 桌面上放的永遠是能賣客人的東西。
feature/* (臨時砧板)： 老闆想出一道新菜（比如加個蛋），就在旁邊小砧板弄一下。
Pull Request (老闆點頭)： 弄好後，老闆看一眼（PR），覺得可以就直接倒進主鍋裡，立刻遞給客人。
特點： 極快、靈活，適合需要一直更新菜單的小店。

·
Author
3. GitLab Flow：像「連鎖餐廳的中央廚房」
它覺得路邊攤太隨便、大餐廳太囉唆，所以改用「分店管理」。
main (總部研發)： 研發出新口味的菜色。
pre-production (實驗分店)： 先把新菜送到這間店給員工試吃，看看味道對不對（測試環境）。
production (全台門市)： 試吃過關了，才正式在全台灣所有分店同步推出（正式環境）。
特點： 重視「在哪裡賣」，適合有多個測試關卡的企業。

·
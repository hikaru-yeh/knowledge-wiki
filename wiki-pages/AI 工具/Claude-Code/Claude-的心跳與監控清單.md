---
網址: https://www.threads.com/@jungchun_/post/DXW94P_H0QF
作者: ["@jungchun_"]
tags: []
status: wiki
---

## Main Content

```
# Claude heartbeat
/loop 每 tick 重讀本檔。
## 每 tick 判斷（由上而下，處理完就停）
1. 用戶訊息未回 → 先回
2. 上輪被打斷的任務 → 推到斷點
3. 讀 `.claude/watchlist.md`：有條目就檢查對應外部狀態；可推進就推進
4. 都沒有的話 -> 休眠
## ScheduleWakeup 選值
- 有 active 任務要追：60–270s
- 純休眠：1200–1800s
## watchlist.md 維護
- 用戶明確交代或任務自然產生 → 新增條目
- 完成 / 放棄 → 刪除條目
- 只放「等外部系統 / 定期檢查」的事
```
在這裡面我又請 claude code 去讀 `.claude/watchlist.md`
這邊其實就是待辦清單, 有哪些工作需要他定時監控的
例如
> 看一下我的 threads 有沒有新留言
下面是 watchlist.md 樣板：

```
# /loop watchlist
Claude 目前在盯的外部等待任務。沒條目 = idle。
格式：`- [type] 描述`
## Active
- 看一下 slack 我老闆有沒有 tag 我, 有的話用 Line 叫我
```
這樣就可以讓 claude code 每隔一段時間自動醒來做事，更新狀態
當然如何讓 claude code 可以把一件事情做好，就需要你好好的設定工作流程在 skill 中了

哎呀...給你發現了呢

少來你才是我師父

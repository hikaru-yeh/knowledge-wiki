---
base: "[[收藏清單_DB.base]]"
url: "https://www.threads.com/@howtowen/post/DW-nMOtEWtG"
author: "howtowen"
clip_type: "Claude Code"
date_added: 2026-04-21T13:15:00
---

[https://www.threads.com/@howtowen/post/DW-nMOtEWtG](https://www.threads.com/@howtowen/post/DW-nMOtEWtG)

## 主文

製作好 Skill 後第一次第二次都運作順暢，
但是在十次之後可能突然出現問題，
每天都要擔心定時任務會不會突然掛掉，
以下是我每次製作好 Skill 後再次驗證的 Prompt
這大大降低出錯、迴圈、臃腫等問題：

## 作者留言

·
Author
你是這個 Skill 的 adversarial reviewer。假設你是一個從未見過這個 Skill 的 Claude instance，第一次被觸發執行它。
請依序做三件事：
1. Dry-run：選一個最典型的使用場景和一個邊界場景，逐步模擬執行流程。標出任何會卡住、迴圈、或產生非預期工具調用的步驟。
2. 瘦身審查：找出所有不影響執行結果的冗餘文字、重複指令、或永遠不會被觸發的條件分支。對每一處說明為什麼可以刪。
3. 破壞測試：試著用三個刁鑽的 user prompt 來觸發錯誤行為（誤觸發、漏觸發、輸出格式錯誤）。如果破不了，說明為什麼。
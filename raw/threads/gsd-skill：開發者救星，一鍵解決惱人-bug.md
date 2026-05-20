---
url: "https://www.threads.com/@matths.dev/post/DYOov-vERnc"
author: "@matths.dev"
clip_type: "Claude Code"
---

開發專案時，最煩的一種情況：
突然發現一個 bug，但你正在做別的 task，不能馬上修。
你通常怎麼處理？
• 寫備忘錄
→ 久了超難整理
• 開 GitHub Issues / 專案管理工具
→ 流程太重，很多時候懶得開
我現在都直接用 gsd skill 的 capture command
在 Claude Code 或其他 agentic coding tool 輸入：
/gsd-capture <問題描述>
通常打一行就夠了。
gsd 會自動整理：
- 相關檔案
- 問題上下文
- 更完整的描述
- TODO markdown
之後想回頭看待辦：
/gsd-capture --list
很多時候甚至不用重新解釋問題
它已經知道上下文，並且已經擬定好了solution
一鍵 fix，整天心情都舒服了 😌

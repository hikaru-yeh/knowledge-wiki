---
base: "[[收藏清單_DB.base]]"
url: "https://www.threads.com/@linmiepii/post/DXItJBMEwal"
author: "linmiepii"
clip_type: "Claude Code"
date_added: 2026-04-21T12:58:00
---

[https://www.threads.com/@linmiepii/post/DXItJBMEwal](https://www.threads.com/@linmiepii/post/DXItJBMEwal)

## 主文

Andrej Karpathy 在 X 上的隨手筆記，被整理成skill在github上爆火，累記29.7k star
github.com/forre…
他列出目前所有 LLM 都有這三個通病
1. AI 有歧義時不問你、直接猜
2. 100 行能解的問題它寫出 1000 行
3. 改 A 的時候順手動了 B，留下你找不到的 bug。
而他的對應法則分為以下4點：
先想再動 — 有歧義先問，不要猜。把假設說出來，讓人確認。
簡單優先 — 沒被要求的功能一律不加。自我檢查：資深工程師會說這段太複雜嗎？
精準修改 — 只碰該碰的地方。看到不相干的問題，提一下，但不要動。
目標驅動 — 不給模糊指令，給可驗證的目標。「修 bug」→「寫能重現這個 bug 的測試，讓它通過」。
#ClaudeCode #AndrejKarpathy

## 作者留言

·
Author
最讓我感同身受的是這句話 -「不要告訴它做什麼，給它成功標準，然後讓它跑。」，除了特定喜好外，如果你嘗試指導LLM怎麼做事，現在看來都有點太自大(雖然你可能沒有這種想法)，相當於以個人的認知去挑戰全世界。因此除了訓練外的資料，一意孤行只會得到差強人意的結果。
github.com
GitHub - forrestchang/andrej-karpathy-skills: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
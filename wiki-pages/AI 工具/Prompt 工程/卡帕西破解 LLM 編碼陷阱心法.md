---
網址: https://www.threads.com/@linmiepii/post/DXItJBMEwal
作者: linmiepii
status: wiki
---

Andrej Karpathy 在 X 的觀察被整理成 CLAUDE.md 格式的 Skill，在 GitHub 累積 29.7k Stars（[forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)）。

**所有 LLM 的三個通病：**
1. 有歧義時不問你、直接猜
2. 100 行能解的問題它寫出 1000 行
3. 改 A 的時候順手動了 B，留下找不到的 bug

**Karpathy 四法則：**

| 法則 | 說明 |
|------|------|
| 先想再動 | 有歧義先問，不要猜。把假設說出來讓人確認 |
| 簡單優先 | 沒被要求的功能一律不加。自我檢查：資深工程師會說這段太複雜嗎？ |
| 精準修改 | 只碰該碰的地方。看到不相干的問題，提一下，但不要動 |
| 目標驅動 | 不給模糊指令，給可驗證的目標。「修 bug」→「寫能重現這個 bug 的測試，讓它通過」 |

核心洞見：「不要告訴它做什麼，給它成功標準，然後讓它跑。」

## Cross References

- [[Vibe-Coding]]: Karpathy 四法則完整脈絡
- [[提示詞技巧]]: LLM 提示詞設計技巧

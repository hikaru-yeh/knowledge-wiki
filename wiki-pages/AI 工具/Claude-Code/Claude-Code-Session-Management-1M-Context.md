---
網址: https://claude.com/blog/using-claude-code-session-management-and-1m-context
作者: ["@trq212"]
tags: [claude-code, session-management, context, 1m-context]
status: wiki
---

# Claude Code Session Management 與 1M Context

> 1M context 不是「裝更多」，而是「管理更好」。

**出處**：Anthropic Blog / Thariq Shihipar (Member of Technical Staff at Anthropic)

---

## 核心概念：Context Rot

Context window 包含模型「一次能看到的所有東西」：system prompt、對話歷史、tool calls、輸出、讀取的檔案。

**Context rot（上下文腐化）**：context 愈堆愈大時，注意力分散到更多 token，舊的無關內容干擾當前任務，模型表現下降。

1M context 讓長任務可行，但 context rot 仍然存在——更大的 context 更需要主動管理。

---

## 5 種 Session 管理操作

每次 Claude 完成任務後，有 5 個選擇：

| 操作 | 說明 | 適用情境 |
|------|------|----------|
| **Continue** | 在同一 session 繼續送訊息 | 同一任務，context 仍有效 |
| **`/rewind` (Esc Esc)** | 跳回指定訊息重試 | Claude 走錯方向，想保留已讀檔案但丟掉失敗嘗試 |
| **`/clear`** | 開新 session，使用者自己寫交接 brief | 全新任務，想完全控制帶入的 context |
| **`/compact [hint]`** | 模型壓縮對話為摘要後繼續 | 中途 session 膨脹，低成本清理 |
| **Subagents** | 委派給子代理，只收結論 | 下一步產生大量中間輸出，只需要最終結果 |

---

## Rewind vs. Correction Message

**推薦用 `/rewind`，不要送 correction message。**

❌ 不好：「那樣行不通，試試 X 吧」
✅ 好：Rewind 到讀完檔案那步，重新 prompt：「不要用 A 方法，直接做 B」

也可以在 rewind 前，先請 Claude `"summarize from here"` 產出交接摘要，帶進新 session。

---

## Compact vs. Clear 選哪個

| | Compact | Clear |
|---|---|---|
| **誰寫摘要** | Claude | 使用者 |
| **精準度** | 有損（模型決定保留什麼） | 精準（使用者決定） |
| **工作量** | 低（一行指令） | 高（手寫 brief） |
| **可引導** | 是：`/compact focus on the auth refactor` | N/A |
| **風險** | 長時間 debug 後自動壓縮可能丟重要 context | 無 |

**Bad autocompact**：模型無法預測任務走向時，會在最需要智慧的時刻壓縮出差劣摘要（context rot 讓模型在壓縮時最笨）。

解法：主動用 `/compact <方向提示>` 引導壓縮方向，而非等自動觸發。

---

## Subagents 使用時機

判斷標準：**「我還需要這個 tool output，還是只需要結論？」**

- 需要中間輸出 → Continue/Compact
- 只需要結論 → Subagent（中間雜訊留在子 context，不污染主 session）

---

## 完整決策表

| 情境 | 操作 | 原因 |
|------|------|------|
| 同一任務，context 仍有效 | Continue | 內容仍是有效負載 |
| Claude 走錯方向 | Rewind | 保留已讀檔案；丟掉失敗嘗試；帶學到的重新 prompt |
| 中途 session 因 debug 膨脹 | `/compact <hint>` | 低成本；Claude 判斷相關性；可引導 |
| 全新任務 | `/clear` | 零 context rot；使用者控制帶入內容 |
| 下一步產出大量輸出，只需結論 | Subagent | 中間雜訊留在子 context |

---

## 何時開新 Session

> "When you start a new task, you should also start a new session."

即使有 1M context，任務間的 context 不一定有效。例外：相關任務（如「剛實作完，現在寫文件」）可考慮繼續同一 session。

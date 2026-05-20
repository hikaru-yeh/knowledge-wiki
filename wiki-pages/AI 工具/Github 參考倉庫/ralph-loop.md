---
網址: Ralph Loop Plugin（GitHub）
作者: []
status: reference
---

**Ralph Loop** 是一個 Claude Code Plugin，實作基於 Stop Hook 的無限迭代 Agent 循環。

**Ralph 是什麼？**  
來自 Geoffrey Huntley 描述的「Ralph Wiggum coding technique」：一個 `while true` 的 Bash 循環，不斷餵給 AI agent 同一個提示檔，讓它迭代改進直到完成。此 plugin 用 Stop Hook 在 Claude Code 內部實作這個循環，不需要外部 Bash 腳本。

**核心機制：**
```bash
# 你只執行一次：
/ralph-loop "你的任務描述" --completion-promise "DONE"

# 然後 Claude Code 自動：
# 1. 執行任務
# 2. 嘗試退出
# 3. Stop hook 攔截退出
# 4. Stop hook 重新餵入相同提示
# 5. 重複直到完成
```

**自我參照回饋迴路的特性：**
- 提示在每次迭代之間不變
- Claude 之前的工作（修改的檔案）持續存在
- 每次迭代都看到修改後的檔案和 git 歷史
- Claude 透過讀取自己過去的工作來自主改進

**指令：**
- `/ralph-loop "<prompt>" --max-iterations <n> --completion-promise "<text>"` — 開始循環
- `/cancel-ralph` — 取消循環

## Cross References

- [[工作流與配置]]: Hooks 與自動化工作流


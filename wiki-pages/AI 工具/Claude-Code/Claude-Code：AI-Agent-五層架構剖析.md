---
網址: https://www.threads.com/@vincent.chanw/post/DX5lV20GI_F
作者: ["@vincent.chanw"]
tags: []
status: wiki
---

## Main Content

Claude Code 真正值得學的，不只是 prompt，而是它把 agent development 拆成一套架構。
最底層是 CLAUDEmd：放 architecture rules、naming conventions、test expectations、repo map。這不是每次手動貼進 context 的提示詞，而是 agent 長期遵守的 constitution。
第二層是 Skills：把任務知識模組化。不是所有知識都塞進主 context，而是在需要時載入對應 SKILLmd、reference、scripts、templates，讓 agent 取得 task-specific knowledge。
第三層是 Hooks：這層最容易被忽略，但最像 production engineering。

PreToolUse、PostToolUse、SessionStart、Stop 這些事件可以觸發 deterministic shell commands，例如 Write 後自動 lint、阻擋 rm -rf、任務結束後通知。品質不是靠 prompt 祈禱，而是靠 infra enforce。
第四層是 Subagents：每個 subagent 有自己的 context window、model、tools、permissions。主 agent 只負責 delegation，拿結果回來，避免主 context 被污染。
第五層是 Plugins：把 skills、agents、hooks、commands 打包，讓整個 team 一次安裝同一套 agent behavior。

所以 agentic system 的成熟度，不是「模型多強」而已，而是有沒有記憶層、知識層、guardrail、delegation、distribution。
少一層，就會把系統問題錯怪成 prompt 問題。

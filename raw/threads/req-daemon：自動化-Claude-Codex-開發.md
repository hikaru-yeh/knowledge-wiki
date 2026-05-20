---
url: "https://www.threads.com/@vic849680/post/DXmZHYuCSWT"
author: "@vic849680"
clip_type: "Claude Code"
---

我每做一個 side project 平均切換 17 次 — 直到我寫了 req-daemon
你也每天在 Claude Code 跟 Codex CLI 之間切來切去、copy-paste 嗎？
我每做一個 side project 都這樣：
開 Claude → 寫 prompt 分析需求 → 複製 SPEC
切 Codex → 貼進去 review → 複製建議
切回 Claude → 貼建議改 → 生 code
切 Codex → review code → 複製 fix list
切回 Claude → 改 → 打包
某天我崩潰了，寫了 req-daemon。
現在我把需求寫成 request.md，丟進 inbox/ 資料夾，daemon 自動接手 — 兩個 CLI 都還在，我只是不用再切視窗。
下篇講內部 7 個 stage 怎麼分工。

接續上篇 → req-daemon 內部跑這 7 個 stage：
Stage 1 Claude 分析需求 → SPEC.md
Stage 1.5 Codex review SPEC（攔方向錯，省 implementation 錢）
Stage 2 Claude 照 SPEC 寫 deliverable/
Stage 2.5 regex linter 零成本掃 XSS / leak
Stage 3 Codex review 整包
Stage 4 Claude 照 review 修
Stage 5 壓 zip → 落到 done/
它們各做擅長的事：Claude 寫得好，Codex 抓問題狠。
4,862 行 TypeScript，本質就解決一件事 — 把我手動做的瑣事自動化。
#ClaudeCode #CodexCLI #vibecoding #AI #sideproject

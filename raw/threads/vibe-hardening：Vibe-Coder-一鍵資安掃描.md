---
url: "https://www.threads.com/@angletech2026/post/DXW_Gogk3fL"
author: "@angletech2026"
clip_type: "職場"
---

AI Threads
04/20/26
做了一個專門給 vibe coder 的一鍵資安掃描。
npx vibe-hardening scan
如果你的 code 是 Cursor / v0 / Lovable / Bolt / Claude Code 寫的 — 上線前跑這個。
一次掃出:
· 外洩 API key（OpenAI / Anthropic / Stripe / GitHub / Slack），加 --verify --own 可以即時驗證哪把還能用
· Supabase table 關掉 RLS
· Next.js API route 沒檢查登入
· SQL / command injection
· 套件有已知 CVE（OSV 資料庫）
· AI 幻覺出來的假 npm 套件
· NEXT_PUBLIC_ 不小心把 server secret 帶進瀏覽器
3 秒跑完，不用裝，支援離線。
→ vibe-hardening.io
vibe-hardening.io
vibe-hardening.io

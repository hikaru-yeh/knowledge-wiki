---
網址: https://www.threads.com/@aiondaily/post/DYJDjkkEqdX
作者: ["@aiondaily"]
tags: []
status: wiki
---

## Main Content

【 google/agents-cli：讓你的 AI 編程助手直接幫你 build、eval、deploy Google Cloud Agent 】
不是給人用的 CLI，是給 Agent 用的 CLI，Google 在 Cloud Next '26 正式推出。
Agents CLI 是 Google 專為 AI 編程助手（Claude Code、Gemini CLI、Codex 等）設計的統一工具鏈，把 Agent 開發生命週期（ADLC）的每個階段，建立、測試、部署、監控，整合成一個 CLI。 你只需要說自然語言，你的 AI 助手就知道該怎麼做每一步。
■ 七個核心 Skill 模組
- Workflow：整體流程協調，串接所有 skill
- ADK Code：寫 ADK Agent 程式碼
- Scaffold：從零建立 Agent 專案結構
- Evaluation：自動跑 eval，含 trajectory scoring
- Deployment：部署到 Cloud Run / GKE / Agent Runtime

- Publish：發布到 Gemini Enterprise 上架
- Observability：Cloud Trace、Logging、第三方整合
■ 支援的 AI 編程助手
Claude Code、Gemini CLI、Codex、Cursor 均支援，任選一個你熟悉的工具即可。
■ 三步驟開始
# Step 1：安裝 google-agents-cli
# Step 2：開啟你的 AI 助手（Claude Code / Gemini CLI / Codex）
# Step 3：直接說 > 幫我建一個可以分類 incident 的 agent
▋安全性檢查
前情提要：此檢查透過 AIOnDaily安全工具掃描。然而實際使用仍請自行經評估再用。
全項通過，Google 官方 repo，可安全使用。

■ 總結
這個工具最值得關注的設計理念是「它不是給人用的，是給你的 AI 用的」，Google 直接把 Google Cloud 的複雜知識（ADK、Cloud Run、GKE、Vertex AI 的正確用法）打包成 skills 注入你的 AI 助手，讓 Claude Code 或 Codex 不需要靠 token 摸索就能做對每一步。你只需要說需求，AI 幫你走完所有雲端基礎設施的細節。
而我相信這也是未來大框架軟體設計包含雲端服務都會走的流程，由 Agent 開始接手雲端操作細節，過去我們可能每次進入 GCP / AWS 就被繁瑣的 UI 操作搞愣了，未來這類情況將會逐步改善。

repo連結 - github.com/googl…
github.com
GitHub - google/agents-cli: The CLI and skills that turn any coding assistant into an expert at creating, evaluating, and deploying AI agents on Google Cloud.

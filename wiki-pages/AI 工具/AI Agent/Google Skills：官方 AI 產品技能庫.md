---
網址: https://www.threads.com/@tootiredbear/post/DYZRDaCH3Qt
作者: ["@tootiredbear"]
tags: [AI, Google, Cloud, Skill]
status: reference
---

**GitHub**: [google/skills](https://github.com/google/skills) ⭐ 10,436

Google 官方 AI Agent 技能庫，把 Google Cloud 產品知識、操作流程與最佳實務打包成 Agent 可調用的技能模組。

## 安裝

```bash
npx skills add google/skills
# 安裝後可互動選擇所需技能
```

## 包含技能

| 類別 | 技能 |
|------|------|
| **AI 平台** | Gemini API / Gemini Interactions API / Managed Agents API / Skill Registry API |
| **資料庫** | AlloyDB Basics / BigQuery Basics / Cloud SQL Basics |
| **運算與部署** | Cloud Run Basics / GKE Basics / Firebase Basics |
| **Well-Architected** | 安全性 / 可靠性 / 成本最佳化 / 卓越運營 / 效能 / 永續性 |
| **入門 Recipe** | Google Cloud Onboarding / 認證 / 網路可觀測性 |

## 使用說明

- 技能模組設計為 Agent Skill 格式，安裝後 Claude Code / Codex 可直接調用
- Gemini Gem 中可將 SKILL.md 作為自訂指令使用（注意：script 無法執行）

## Cross References

- [[Skill 設計]]：Skill 設計原則與框架
- [[MCP 工具]]：Google Cloud MCP 整合

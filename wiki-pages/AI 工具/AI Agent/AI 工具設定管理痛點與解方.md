---
網址: https://www.threads.com/@crazyaitools_/post/DYbr_zJEukO
作者: ["@crazyaitools_"]
tags: [Claude Code, Codex, Cursor, 工具管理, Skill]
status: reference
---

跨工具 AI 技能與配置統一管理方案，解決「工具越多、設定越混亂」的根本問題。推薦兩個互補工具：

---

## 1. Skills Manager

**GitHub**: [xingkongliang/skills-manager](https://github.com/xingkongliang/skills-manager) ⭐ 1,606

輕量桌面應用，集中管理、同步並組織 15+ 個 AI coding 工具的技能庫。

**解決什麼：** 跨工具（Claude Code / Codex / Cursor / Copilot 等）的技能版本不一致問題

**核心功能：**
- 集中管理所有 AI 工具的 Skill，一個地方統一編輯
- Git 版本控制：多台電腦同步，設定不會跑掉
- Marketplace 瀏覽安裝功能
- Global Workspace + Agent Workspace 雙層管理

---

## 2. Plexus

**GitHub**: [miniLV/Plexus](https://github.com/miniLV/Plexus) ⭐ 15

掃描現有 AI 工具配置，選定「單一真相來源」，一鍵同步規則、Skill、MCP 設定到各工具原生位置。

**解決什麼：** 同時使用多個 AI 工具時，手動同步配置耗時且容易出錯

**核心功能：**
- 掃描 Claude Code / Cursor / Codex / Gemini CLI / Qwen Code 等現有配置
- 每次寫入前自動快照，不怕設定出錯
- 一次點擊同步到所有工具

```bash
npx -y plexus-agent-config@latest start
```

---

## Cross References

- [[Skill 設計]]：Skill 設計與管理原則
- [[技能包大總管]]：Skill 庫內部關係治理
- [[工作流與配置]]：整體 Agent 配置架構

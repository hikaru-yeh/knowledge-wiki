---
網址: https://www.threads.com/@krumjahn/post/DYjZA0GE3VL
作者: ["@krumjahn"]
tags: [Claude Code, Skill, UI, 設計]
status: reference
---

**GitHub**: [Nutlope/hallmark](https://github.com/Nutlope/hallmark) ⭐ 1,710

Anti-AI-slop 設計技能，讓 Claude Code、Cursor、Codex 生成的 UI 拒絕千篇一律的 AI 樣板外觀。由 Together AI（roomgpt / llamacoder / blinkshot 作者）出品。

## 核心機制

- **22 種主題**：每次 build 隨機挑選不同主題，同一 brief 兩次產出外觀不同
- **65 個 slop-test gates + pre-emit self-critique**：輸出前自動偵測並拒絕 AI 默認樣板
- **四種指令（verbs）**：

| 指令 | 功能 |
|------|------|
| *(default)* | 新建 UI，挑選 macrostructure + 套用規則集 + 跑 slop test |
| `hallmark audit <target>` | 評分現有程式碼的 anti-pattern 程度，只出報告不修改 |
| `hallmark redesign <target>` | 保留文案與 IA，重新建構不同外觀 |
| `hallmark study <screenshot\|URL>` | 提取你欣賞設計的 DNA（macrostructure、字型配對、色彩錨點），輸出 `design.md` |

## 安裝

```bash
npx skills add nutlope/hallmark
```

## Cross References

- [[Skill 設計]]：Skill 框架設計原則
- [[免費 Skill 助你建智能設計部]]：10 人設計部門 Skill 組合

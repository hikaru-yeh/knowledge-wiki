---
網址: https://www.threads.com/@hanamizuki/post/DYedOBbim10
作者: ["@hanamizuki"]
tags: [Claude Code, Skill, 審核, HTML]
status: reference
---

**GitHub**: [hanamizuki/solopreneur](https://github.com/hanamizuki/solopreneur) ⭐ 52

solopreneur 是一套 Claude Code 插件集，提供 16 個核心技能（/preview、pipelines、思考夥伴等）與多個角色插件（marketer / designer / ios-dev / android-dev / ai-engineer）。

## /preview 技能：提案 HTML 化

解決問題：Claude Code 規劃提案量大，人類懶得看終端機中的純文字，導致 human-in-the-loop 形同虛設。

**做法：**
1. 輸入 `/preview` → Claude Code 把當前提案製作成 HTML
2. HTML 包含互動元件、圖表、表格，讓人快速掌握提案全貌
3. Comment 功能：像 Google Doc 留言，選取要調整的地方並附說明
4. 審核完後一次貼回 Claude Code 執行，流程輕量
5. 若設定 Vercel，自動生成預覽連結，手機也可審核

## 插件總覽

| 插件 | 內容 |
|------|------|
| `solopreneur` | 16 個核心技能 |
| `marketer` | 7 技能（GTM / 命名 / 文案 / X/LinkedIn 成長 / 投影片） |
| `designer` | `taste-*` 家族 + `impeccable` 共 10 技能 |
| `ios-dev` | iOS patterns + 23 vendored 技能 |
| `android-dev` | Android Compose + 39 vendored 技能 |
| `ai-engineer` | LangGraph + AI app templates |

## 安裝

```bash
claude plugin marketplace add hanamizuki/solopreneur
claude plugin install solopreneur@solopreneur
claude plugin install designer@solopreneur  # 按需安裝角色插件
```

## Cross References

- [[Skill 設計]]：Skill 設計框架
- [[AI寫程式不失控：工程師的開發工作流]]：工程師 AI 工作流設計

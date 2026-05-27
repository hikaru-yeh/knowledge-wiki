---
網址: https://www.threads.com/@howtowen/post/DW-nMOtEWtG
作者: ["@howtowen"]
tags: [AI Agent, Claude Code, Skill, 自動化, 驗證]
status: wiki
---

## Skill 防出錯驗證三步驟（Adversarial Reviewer）

設計 Skill 後，用以下三步驟測試健壯性：

1. **Dry-run（試跑）**：在空環境執行，確認無副作用
2. **瘦身測試**：移除每個步驟，確認哪些是真正必要的
3. **破壞測試**：給予邊界輸入（空值、超長輸入、特殊字元），確認不崩潰

## 免費 Skill 設計課

**核心原則：**
- Skill 是「可重複呼叫的工作流模板」
- 每個 Skill 應有：觸發詞、前置條件、執行步驟、成功標準
- 避免 Skill 過於泛化（「幫我做任何事」≠ Skill）

**結構範本：**
```markdown
## Trigger
[觸發關鍵詞或情境描述]

## Preconditions
[執行前需要滿足的條件]

## Steps
1. [步驟一]
2. [步驟二]
...

## Success Criteria
[完成的判斷標準]
```

## Darwin-Skill / Claude-Evolver

AI 進化式 Skill 框架概念：
- Skill 可以自我評估並提出改善版本
- 使用版本控制追蹤 Skill 演進歷史
- 結合測試結果自動篩選更優版本

## Sources

- [AI Skill 防出錯驗證 Prompt](https://www.threads.com/@howtowen/post/DW-nMOtEWtG) | 作者: howtowen
- [免費 Skill 助你建智能設計部](https://www.threads.com/@bibi._.0614/post/DWdjNPkETjt) | 作者: bibi._.0614

## Cross References

- [[工作流與配置]]：Skill 應用於整體工作流的脈絡
- [[CLAUDE.md 與記憶設定]]：Skill 存放位置與跨 session 載入
- [[Token 優化]]：Skill 執行時的 token 效率

---
網址: https://www.threads.com/@_prem.io/post/DXGDLiTAp8i
作者: ["@_prem.io"]
tags: [AI Agent, Claude Code, Token, 成本優化, 效率]
status: wiki
---

## 省 94% Token 四步驟

從 198k → 10k tokens 的實作方法：

1. **關記憶（60k 上限）**：關閉 Claude 記憶功能，或設定最大 memory token 上限
2. **改 Concise 模式**：回應風格設為簡潔，減少冗長解釋
3. **關 Web 搜尋**：不需要時關閉自動網路搜尋
4. **On-demand 工具**：只在需要時啟用工具，而非常態開啟

## Caveman Skill（省 75% Token）

透過限制 AI 回應格式省 Token：
- 使用穴居人式簡短回應風格
- arXiv 研究佐證：準確度提升 26 個百分點（同時減少 token）
- `bu-ketao` 模式可省 72% token 且不損失答題品質

**核心洞察**：AI 的冗長不等於品質，去除廢話通常同時提升準確度。

## Token 成本心法

- **Context 管理 > 硬體升級**：聰明管理上下文比換更大模型更有效
- **批次操作**：多個小請求合成一個大請求
- **快取利用**：重複的 system prompt 可利用 prompt caching 降費
- **工具選擇**：小模型 + 精準 prompt 常優於大模型 + 模糊 prompt

## Sources

- [Claude Token 爆燒？一招設定省94%](https://www.threads.com/@_prem.io/post/DXGDLiTAp8i) | 作者: _prem.io
- [讓 AI 說重點，省 75% Token](https://www.threads.com/@buildthink.ai/post/DXF7U1qD27S) | 作者: buildthink.ai
- [不客套：砍掉中文 AI 客套話](https://www.threads.com/@macdog/post/DXHr_Bgj_aW) | 作者: macdog

## Cross References

- [[工作流與配置]]：工作流設計影響 token 消耗
- [[CLAUDE.md 與記憶設定]]：記憶設定與 token 使用的關係
- [[Skill 設計]]：Skill 設計精良可大幅減少來回 token

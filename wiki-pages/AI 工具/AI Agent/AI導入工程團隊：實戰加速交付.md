---
網址: https://www.threads.com/@astolfo_proto/post/DYeb84Vka1_
作者: ["@astolfo_proto"]
tags: [AI, 工程團隊, PR Review, 交付, 開發流程]
status: wiki
source_blog: https://hackmd.io/@FortHsu/
---

## 核心洞察

**AI 擴大的是 Production Capacity，但真正決定交付速度的是 Review Capacity 與 Validation Capacity。**

引入 AI coding 工具後，工程師生成程式碼的速度大幅提升，卻常造成 PR Review 與驗證成為新瓶頸，導致「重工變多」而非「交付變快」。

## 三種 Capacity 的平衡

| Capacity | 說明 | AI 對此的影響 |
|------|------|------|
| **Production Capacity** | 寫出程式碼的速度 | AI 大幅提升 |
| **Review Capacity** | 審查 PR 的速度與品質 | AI 反而造成堆積 |
| **Validation Capacity** | 驗證功能正確性的速度 | AI 不穩定時反而增加 |

## 實戰落地建議（高流量白牌交易所實踐）

1. **先訂制度再寫 CODE**：不完善的制度會讓不穩定的代價在日後以高風險形式買單
2. **MVP 版本的取捨**：若需要先出 MVP，明確承認技術債範圍，事後補足驗證
3. **Review 自動化**：設定 Coding Agent 的 PR 輸出規格，配合自動化審查工具降低人工 Review 成本
4. **驗證節奏**：建立固定的驗證週期，讓 AI 生成的程式碼有明確的質量把關點

## 適用對象

- 工程師正在導入 AI coding 工具但不知道如何融入現有流程
- 管理層需要評估 AI 對交付速度的實際影響
- 需要「明天到公司立即可用」的可操作建議，而非理論性吹捧

## Sources

- [HackMD 文章](https://hackmd.io/@FortHsu/) | 作者: FortHsu (astolfo_proto)

## Cross References

- [[AI寫程式不失控：工程師的開發工作流]]：TDD + diagnose 解決驗證節奏問題
- [[Vibe-Coding]]：AI 輔助開發的工程化哲學

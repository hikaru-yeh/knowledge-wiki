---
網址: https://www.threads.com/@danielwchen0/post/DYgdaz9kaKv
作者: ["@danielwchen0"]
tags: [Claude Code, 閱讀, 知識庫, Obsidian, 個人系統]
status: wiki
---

## 核心問題

AI 時代每天要讀大量純文字資訊。AI 不會累，但人會。如何讓大量閱讀像在漂亮公路上長途駕駛一樣舒服？

## 個人閱讀系統（Long Drive）

### 三層知識架構（受 Karpathy 啟發）

```
raw（原料層）
  → wiki（AI 閱讀原料後撰寫的知識庫）
    → output（Q&A Agent 查閱 wiki 回答問題的產出）
```

- 第一層 **Raw**：所有優質文章、repo、影片、資料的未加工原料
- 第二層 **Wiki**：AI 閱讀原料後撰寫的結構化知識庫，以「好奇心」為中心持續完善
- 第三層 **Output**：Q&A Agent 查閱 wiki、產出 Obsidian + Marp Slide 沈浸式閱讀材料

### 知識視覺化系統

把不同類型的知識轉成更容易吸收的形式：
- 歷史脈絡 → timeline
- 概念關係 → mind map
- 程式說明 → HTML（受 Thariq 「HTML 比 Markdown 好」的展示論點啟發）

### 工具組合

| 工具 | 用途 |
|------|------|
| **Claude Code** | 將文章/影片轉成 Markdown + HTML |
| **Obsidian + Web Clipper** | 截取網路知識，本地知識庫管理 |
| **qmd** | 本地 CLI 搜尋引擎，全文搜尋 + 向量搜尋 + LLM 重排序 |

## qmd：本地 Markdown 搜尋引擎

**GitHub**: [tobi/qmd](https://github.com/tobi/qmd) ⭐ 25,475

```bash
npm install -g @tobilu/qmd
qmd collection add ~/notes --name notes
qmd embed                           # 生成向量嵌入
qmd query "quarterly planning process"  # 混合搜尋 + 重排序
```

三種搜尋：`qmd search`（BM25 關鍵字）/ `qmd vsearch`（向量語義）/ `qmd query`（混合 + LLM 重排序）

## 核心哲學

「你只要負責好奇與發問、你的知識庫會隨著你的學習，被 AI 整理越來越好用。」

讓自己一直待在心流與好奇心裡，AI 在背後持續讓 wiki 更完善、原料更新鮮。

## Sources

- [Thariq on X](https://x.com/trq212) | implementation-notes HTML 施工日誌啟發

## Cross References

- [[CLAUDE.md 與記憶設定]]：Obsidian 三層知識庫架構
- [[AI 知識庫新解方：告別碎片化，打造越用越聰明的 AI Wiki]]：llm_wiki 類似架構

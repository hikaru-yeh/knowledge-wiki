---
網址: https://www.threads.com/@kai_ch_chen/post/DYmL-vME7o-
作者: ["@kai_ch_chen"]
tags: [AI, 知識庫, Wiki, RAG, Obsidian]
status: reference
---

**GitHub**: [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) ⭐ 8,975

跨平台桌面應用，讓 LLM 從你的文件增量建構並維護一個有結構的 Wiki。對比傳統 RAG 每次查詢都從零檢索，llm_wiki 是「編譯一次、越用越聰明」。

## 核心機制

- **兩步驟 Chain-of-Thought 攝入**：LLM 先分析，再生成附來源追溯的 wiki 頁，增量快取
- **多模態圖像攝入**：從 PDF 提取嵌入圖像，視覺 LLM 生成事實說明，lightbox 預覽並跳至來源
- **4-Signal 知識圖譜**：直接連結 / 來源重疊 / 語義相似 / 引用頻率，四信號自動建立關聯
- **Louvain 社群偵測**：找出你自己都未意識到的知識盲區
- **Chrome 一鍵剪藏**：好網頁直接進知識庫
- **Obsidian 三欄相容**：生成的知識庫可直接在 Obsidian 使用

## 與傳統 RAG 的差異

| 維度 | 傳統 RAG | llm_wiki |
|------|------|------|
| 查詢方式 | 每次從零檢索碎片 | 查詢預建的結構化 wiki |
| 知識組織 | 碎片化、無關聯 | 圖譜連結、越用越完整 |
| 成長性 | 靜態 | 增量更新，越用越聰明 |

## Cross References

- [[CLAUDE.md 與記憶設定]]：Obsidian 三層知識庫架構
- [[AI時代的閱讀系統：好奇心驅動的知識長途駕駛]]：個人閱讀知識系統

---
網址: https://www.threads.com/@free.com.tw/post/DYZJSVkjlSK
作者: ["@free.com.tw"]
tags: [AI, 翻譯, 瀏覽器, Gemini, 隱私]
status: wiki
source_blog: https://free.com.tw/shinkansen/
---

## 摘要

台灣開發者（Jimmy Su）製作的瀏覽器擴充功能，使用 Google Gemini API 翻譯網頁，主打高品質、保留排版、不過第三方伺服器，是沉浸式翻譯的隱私友善替代方案。

## 核心特色

| 特點 | 說明 |
|------|------|
| **翻譯品質** | Gemini API 驅動，批次翻譯 + 漸進注入，邊讀邊等其他內容翻譯 |
| **隱私保護** | 資料只在使用者電腦與 Google API 之間流通，不過第三方伺服器 |
| **排版保留** | 原始字型、大小、顏色、超連結完全保留 |
| **YouTube 字幕** | 自動翻譯影片字幕，支援 Gemini 與 Google Translate 切換 |
| **開源** | 原始碼公開，可自行審查安全性 |

## 設定步驟

1. 從 Chrome 線上應用程式商店或 Firefox 附加元件安裝
2. 取得 Google Gemini API Key（需信用卡綁定，免費方案不收費）
3. 在 Shinkansen 設定頁貼入 API Key
4. 選擇模型（建議 `gemini-3.5-flash`，品質與成本平衡）
5. 設定用量配額防止超支

## 為什麼優於沉浸式翻譯

作者設計 Shinkansen 的原因是沉浸式翻譯的隱私問題。Shinkansen 資料不流出本機 + 架構輕量，同時提供使用量追蹤與快取降低成本。

## Sources

- [免費資源網 Shinkansen 介紹](https://free.com.tw/shinkansen/) | 作者: free.com.tw

## Cross References

- [[工具總覽]]：沉浸式翻譯與其他 AI 工具比較

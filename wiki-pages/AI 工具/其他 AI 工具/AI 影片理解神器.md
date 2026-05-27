---
網址: https://www.threads.com/@felix_c888/post/DYUle6tgKPq
作者: ["@felix_c888"]
tags: [AI, 影片, CLI, 工具]
status: reference
---

**GitHub**: [sonpiaz/watch-cli](https://github.com/sonpiaz/watch-cli) ⭐ 217

`yt-dlp + ffmpeg + Whisper` 三合一 CLI，讓 AI Agent 取得影片的原始幀與逐字稿，從「看摘要」升級為「真正理解影片」。

## 核心指令

```bash
watch https://twitter.com/anyone/status/12345
```

輸出三件素材：`VIDEO`（影片檔）+ `FRAMES`（均勻抽幀圖）+ `TRANSCRIPT`（逐字稿），直接餵給 LLM 自行推理，而非由工具預消化。

## 支援平台

YouTube / X（Twitter）/ LinkedIn / TikTok / Reddit / Vimeo / Facebook
（登入牆內容自動使用瀏覽器 Cookie 繞過）

## 五個現成 Prompt 模板

| 影片類型 | 產出成品 |
|------|------|
| 程式碼教學 | 可執行專案檔案 |
| 系統架構演講 | 互動架構圖 |
| UI / 動態展示 | 可執行 React 元件 |
| 論文 / 研究影片 | 可執行 Notebook |
| 長篇教學 | 步驟速查表 |

## Cross References

- [[工具總覽]]：其他 AI 工具比較

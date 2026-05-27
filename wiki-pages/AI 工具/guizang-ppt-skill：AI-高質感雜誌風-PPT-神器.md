---
網址: https://www.threads.com/@endman100/post/DXie0R2ClVV
作者: ["@endman100"]
tags: []
status: reference
---

## 概述

guizang-ppt-skill 是 AI agent 技能，可產出**單檔 HTML 橫向滑動簡報**。支援 Claude Code、Codex 等 agent 環境。不需 build、不需 server，一個 HTML 檔直接開瀏覽器即可呈現。

- 12.4k stars / MIT 授權
- 兩套完整視覺系統（Editorial Magazine / Swiss International）
- WebGL/Canvas 動畫 + 靜態降級模式（按 B 切換）

## 兩種視覺風格

### Style A — Editorial Magazine

「像 Monocle 雜誌配上程式碼」，適合敘事型演講、沙龍、個人觀點。

- **10 種版面**：封面、章節分隔、數據海報、圖文組合、網格版面、流程圖、比較頁等
- **5 套電子墨水色主題**：Ink Classic / Indigo Porcelain / Forest Ink / Kraft Paper / Dune

### Style B — Swiss International

網格優先、系統化資訊設計，適合事實呈現、產品分析、方法論。

- **22 種鎖定版面**（不可自由組合，強制使用指定 layout）
- **4 套高飽和主色**：Klein Blue IKB / Lemon Yellow / Lemon Green / Safety Orange
- 直角、髮線邊框、無陰影、無漸層
- 含 `validate-swiss-deck.mjs` 驗證腳本，自動抓置中標題、實驗版面、SVG 內嵌文字等違規

所有主題只能用預設色，禁止自訂 hex 值。

## 安裝

```bash
# 推薦（一行安裝）
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill

# 手動
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.claude/skills/guizang-ppt-skill
# 確認 SKILL.md、assets/、references/ 目錄存在
```

## 使用流程

1. 選擇視覺風格（Style A 或 B）
2. 回答七題釐清清單（觀眾、時長、素材、圖片需求、配色）
3. 複製對應模板（`template.html` 或 `template-swiss.html`）
4. 依 reference 文件的 layout skeleton 填入內容
5. 可選：透過 GPT-Image 2.0 / GPT-M 2.0 生成配圖（Codex 環境）
6. 用 `checklist.md` 自檢品質
7. 瀏覽器預覽，透過 inline CSS 迭代修改

## 圖片生成（Codex 整合）

支援圖片類型：紀實攝影、資訊圖表、流程圖、系統關係圖、UI 場景、數據海報、複合版面。圖片必須符合模板比例（主圖 21:9，替代 16:9 / 16:10），不可包含頁碼、頁尾、裝飾邊框。

## 多平台封面

| 平台 | 比例 |
|------|------|
| 微信公眾號頭圖 | 21:9 |
| 分享卡 | 1:1 |
| 小紅書封面 | 3:4 |
| 影片橫向封面 | 16:9 |

## 輸出規格

- **格式**：單一 HTML 檔
- **導航**：鍵盤 / 滾輪 / 觸控 / 介面按鈕
- **動畫**：WebGL/Canvas，靜態模式切換（按 B）
- **瀏覽器**：直接開啟，無需 server

## 適用場景

**適合**：線下簡報、產業內部演講、私人活動、AI 產品發表、demo day、風格化講座

**不適合**：大型數據表格、培訓課程、多人協作編輯、需頻繁修改結構的內容

## Sources

- GitHub repo：https://github.com/op7418/guizang-ppt-skill
- 實作範例：https://endman100.github.io/artic…（原帖連結，截斷）

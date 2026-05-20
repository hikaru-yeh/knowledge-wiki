# lint

定期執行（建議每月一次）。對 Claude 執行以下任務。

---

## 任務 1：掃描不一致

```
讀取 wiki-pages/ 下所有 wiki 頁面（排除索引頁），找出：
1. 相互矛盾的描述（同一概念有不同定義）
2. 來源連結失效（raw/ 中找不到對應文件）
3. 過時的工具推薦（例如已停止維護的工具）

輸出清單到 list-to-be-repaired.md
```

## 任務 2：補充缺失資訊

```
讀取 list-to-be-repaired.md，
對其中「資訊不完整」的條目：
1. 找出 wiki-pages/ 中最相關的 wiki 頁面
2. 補充該條目缺少的資訊
3. 更新相關 wiki 頁面
```

## 任務 3：尋找新連結

```
讀取所有 wiki-pages/ 下的 wiki 頁面，
找出目前 `## Cross References` 區塊沒有連結但實際相關的頁面對，
列出建議新增的連結：
格式：[文章A] → [文章B]：[關聯說明]
```

## 任務 4：建議新文章

```
分析 wiki-pages/index/總索引.md 與各分類索引中的所有條目，
找出被多個原始文件提到但尚未有對應 wiki 頁面的主題，
建議前 3 個最值得建立的新 wiki 頁面
```

## 任務 5：更新總索引

```
檢查 raw/ 目錄中是否有新文件尚未反映在 wiki-pages/index/ 下的對應索引，
將缺漏條目加入適當的 `*-索引.md`，
並同步更新 wiki-pages/index/總索引.md 中的統計摘要（例如原始文件數、Wiki 文章數、Stub 數、各主題文章數）
```

## 任務 6：記錄 lint 結果

```
完成 lint 後：
1. 將問題摘要輸出到 list-to-be-repaired.md
2. 在 wiki-pages/日誌.md 追加一筆紀錄
格式：## [YYYY-MM-DD] lint | <issue count>
```

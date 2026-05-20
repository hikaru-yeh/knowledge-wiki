---
網址: https://github.com/cablate/llm-atomic-wiki
作者: []
status: reference
---

建立在 **Andrej Karpathy 的 LLM Wiki 模式**之上的知識管理框架，規模：584 posts · 8,668 replies → 630 atoms → 83 wiki pages · 11 branches。

**Karpathy 原始模式：**
```
raw → wiki
```

**此 repo 的擴展：**
```
raw → atoms（按主題分 branch）→ wiki
```

**四個新增改進：**

1. **Atom 層**：Karpathy 一步到位（raw → wiki），此 repo 加入中間層 atom。一個 atom = 一個聲明 + frontmatter（來源、類型、深度、標籤、日期）。Atom 是真相來源；wiki 是衍生快取。

2. **Topic-branches**：Atom 層按主題組織到 branch 資料夾（每個 branch 一個資料夾），再編譯成平面 wiki 頁面（`wiki/<branch>-<subtopic>.md`）。

3. **兩層 Lint**：
   - 程式層（`scripts/lint.sh`）：處理確定性檢查（ghost links、孤兒頁、格式違規）
   - LLM 層：處理語義檢查（矛盾、過期聲明）
   - 程式層先跑，避免 LLM 浪費 attention 在格式問題上

4. **並行編譯命名鎖定（Parallel-compile naming lock）**：N 個 agent 並行編譯時，預先鎖定 slug 命名空間，agent 填入內容到預命名的槽位，不自行命名檔案。

**數字：**
| 階段 | 數字 |
|------|------|
| Raw 輸入 | 584 posts + 8,668 replies |
| Atom 提取 | 630 個（不可變，真相來源）|
| Branches | 11 個 |
| Wiki 頁面 | 83 個（每頁 3-8 atoms）|

## Cross References

- [[CLAUDE.md 與記憶設定]]: LLM wiki 知識庫架構


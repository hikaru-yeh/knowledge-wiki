---
網址: https://www.threads.com/@fatelvx/post/DYVnpWeH8Z-
作者: ["@fatelvx"]
tags: [AI, 架構, TypeScript, 工具]
status: reference
---

**GitHub**: [fatelvx/axiom](https://github.com/fatelvx/axiom) ⭐ 11 (alpha)

AI 時代 TypeScript/JavaScript 專案的靜態架構合約工具。在 `.axi` 檔案中宣告架構規則（哪個模組可依賴哪個），Axiom 比對實際 import 圖，CI 直接攔截架構漂移。

## 設計動機

AI 輔助開發讓程式碼更快，但架構往往在無人察覺下悄悄變形。Axiom 讓架構規則像型別一樣可驗證——人類與 CI 看到同一份架構證據。

## 四個指令

| 指令 | 用途 |
|------|------|
| `axi check` | CI gate：違反合約即失敗 |
| `axi observe` | 審查漂移、advisory 壓力、技術債 |
| `axi infer` | 從現有 import 推導起始合約（參考用，非架構意圖） |
| `axi diff` | 與基準線的 advisory 漂移對比 |

## 安裝（避免 npm 供應鏈攻擊）

```bash
npm install --ignore-scripts -D @fatelvx/axiom@0.6.0-alpha.5 --save-exact
npx --no-install axi infer --root . --include "src/**"
```

## 限制

- 目前只支援 TypeScript / JavaScript 靜態分析
- Python 與 runtime 動態依賴尚未支援

## Cross References

- [[Vibe-Coding]]：AI 輔助開發的工程化哲學
- [[AI Agent工程化工具趨勢]]：相關工程化工具

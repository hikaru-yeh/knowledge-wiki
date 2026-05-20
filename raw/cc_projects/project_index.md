# cc_projects 來源稿索引

`knowledge-wiki/raw/cc_projects/` 的來源稿目錄。由 project-wrap skill 寫入。

> ingest 後的 canonical 結構化頁面見 `wiki-pages/專案管理/projects/`。
> personal-wiki 的 `cc_projects` bridge pages 不由 project-wrap 直接寫入；來源稿中的 `Bridge Candidate` 區塊只供後續 update 模式判斷。

## 已有來源稿

| 檔案 | 最後更新 | 說明 |
|------|---------|------|
| _(尚無)_ | — | project-wrap 執行後會在此列出 |

## 格式模板

`_project_template.md` — project-wrap source draft 模板，包含 canonical frontmatter draft 與 bridge candidate 判斷材料

## 流程說明

```
project-wrap skill 執行
    ↓
raw/cc_projects/project_<name>.md（來源稿）
    ↓ knowledge-wiki ingest
wiki-pages/專案管理/projects/<name>.md（canonical 技術專案頁）
    ↓ 視職涯價值，由 personal-wiki update 模式建立
personal-wiki/Wiki_Pages/cc_projects/project_<name>.md（career portfolio bridge，可選）
```

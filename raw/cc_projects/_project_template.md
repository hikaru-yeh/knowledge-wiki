# [project_name]

> project-wrap source draft. This file is raw material for later ingest into
> `wiki-pages/專案管理/projects/[project_name].md`.

---

## Canonical Frontmatter Draft

```yaml
type: project
status: active | legacy | archived | paused
last_updated: YYYY-MM-DD
time: YYYY-MM
tech_stack:
  - [Technology]
depends_on:
  - [upstream_project_or_system]
feeds_into:
  - [downstream_project_or_output]
location: "D:\\shane_yeh\\Documents\\_Claude_Code\\[project_folder]"
```

## 專案任務

[為什麼要做這個工具？要解決什麼問題？背景脈絡是什麼？]

## Briefing（原始需求）

[最初的需求描述，從 session 對話、README、HANDOFF、MEMORY 或文件中提取。]

### 後續調整

[需求在過程中怎麼演變？若無則寫「尚無」。]

## 成品描述

[目前做出來的東西長什麼樣？完成度？主要功能？哪些已驗證、哪些尚未驗證？]

## 技術與架構

使用技術：[Python / JavaScript / Playwright / Claude API / Gemini CLI / ...]

架構說明：

```text
[text diagram 或流程步驟]
```

## 可複用的元件

- `ComponentName`（`path/to/file.py`）：[用途與複用方式]

## 學到什麼 / 踩過的坑

- [問題描述] → [解法或結論]

## 遺留問題 / 未完成

- [功能或問題]：[現況說明]

## Bridge Candidate（給 personal-wiki）

recommended: yes | no | maybe
sensitivity: public | private | sensitive
career_value_draft: [若建立 `personal-wiki/Wiki_Pages/cc_projects/project_[project_name].md`，此專案能展示什麼職涯能力？]
reason: [為什麼建議或不建議建立 bridge page？]

注意：此區塊只是給 personal-wiki update 模式使用的判斷材料，不代表 bridge page 已建立。

## Cross References

- [[專案管理/_overview]]

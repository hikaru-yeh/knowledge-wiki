---
source: session | 2026-05-20
status: reference
tags:
  - shane-wiki
  - person-disambiguation
  - wiki-governance
last_updated: 2026-05-20
---

# Shane Wiki 人物消歧

> 用 queue + frontmatter + AGENTS 規則，把跨平台同一人物的辨識與合併流程制度化。

## 定位與用途

這份筆記整理 Shane Wiki 在「人物消歧」上的實作方式，目標是避免 agent 在 ingest 社交資料時，因名稱相似、共同好友、同城市或平台重疊，就把不同人物錯誤合併。

這套做法適用於：
- LINE / Instagram / Facebook / Threads 等跨平台人物對照
- 暱稱、縮寫、全名、handle 混用的場景
- 已確認同人、待確認候選、明確非同人的混合情況

核心原則：
- 未確認時，寧可分開保留，也不要過早 merge。
- 人物消歧和 privacy governance 必須一起設計。
- queue 先行，canonical merge 後做。

## Metadata 欄位設計

建議加在 `Wiki_Pages/people/person_*.md` frontmatter：

| 欄位 | 用途 |
|------|------|
| `canonical_name` | wiki 內的正式主名稱 |
| `aliases` | 已知別名、暱稱、縮寫、不同拼法 |
| `platform_identities` | 各平台身份表現，例如 LINE 顯示名、IG handle |
| `disambiguation_status` | 目前消歧狀態 |
| `possible_duplicate_of` | 懷疑可能同人，但尚未確認 |
| `same_as` | 已確認同一人的其他頁面或身份 |
| `not_same_as` | 已確認不是同一人的頁面或身份 |

推薦的 `disambiguation_status`：
- `single_source_only`
- `possible_duplicate`
- `confirmed_same_person`
- `distinct_person`

## 人物消歧流程

### 1. 先做 metadata，不急著 merge

先把整套欄位補到人物頁，再開始處理跨平台同人。這樣 query、lint、graph、後續 ingest 才有穩定基礎。

### 2. 建立 queue 作為工作台

工作台頁面：
- `Wiki_Pages/people/disambiguation_queue.md`

用途：
- 記錄候選 A / 候選 B
- 摘要證據
- 給出 `unreviewed` / `possible_duplicate` / `probable_same_person` / `confirmed_same_person` / `distinct_person`
- 在真正 merge 前，先留審核軌跡

推薦欄位：
- `candidate_a`
- `candidate_b`
- `platform_overlap`
- `evidence_summary`
- `status`
- `reviewer_note`

### 3. 證據門檻採保守策略

可當強證據：
- 正文已明說「A = B」
- 同一 handle / 顯示名 / 對話脈絡明確對上
- 共同事件、時間線與人物背景高度重合

不能單獨當合併依據：
- 名字像
- 在同一城市
- 有共同好友
- 都出現在同一社群或政治活動裡

### 4. 確認後才回寫主頁

一旦確認同人：
- 把 canonical page 定下來
- 更新 canonical page 的 `aliases` / `platform_identities`
- 視情況將 duplicate page 刪除、保留 alias page，或標成 superseded
- 更新所有 wikilink、索引、queue、log

## 合併 canonical page 的做法

本 session 的實作案例：
- `person_j.md`
- `person_jenny.md`

決策：
- `person_jenny.md` 作為唯一 canonical page
- `person_j.md` 的 IG 視角內容併入 `person_jenny.md`
- 最後刪除 `person_j.md`

### 合併時要做的事

1. 整合正文，去重但保留不同平台視角
2. 更新 canonical page 的 frontmatter
3. 更新所有 `[[people/person_j]]` 到 `[[people/person_jenny]]`
4. 更新 `people/README.md`、`index.md`、`disambiguation_queue.md`
5. 在 `Wiki_Pages/log.md` 追加 reorganization / correction 紀錄

### canonical 指令模板

```text
請用 reorganization + correction 模式處理人物合併：

把 `Wiki_Pages/people/person_a.md` 和 `Wiki_Pages/people/person_b.md` 合併為同一人物。
請以 `Wiki_Pages/people/person_b.md` 作為 canonical page。

要求：
1. 先提出 merge plan，等我確認後再改。
2. 整合兩頁正文，去重但保留跨平台資訊。
3. 更新 frontmatter 的 disambiguation 欄位。
4. 更新所有受影響的 wikilink、索引與 queue。
5. 在 `Wiki_Pages/log.md` 追加紀錄。
6. 不要修改 Raw_Sources。
```

## 常見問題 / 踩坑

- **不要太早 merge**：跨平台名字很像，不代表是同一人。
- **queue 不是 optional**：沒有 queue，後面很難追蹤當時為什麼判定同人。
- **AGENTS.md 需要最小規則**：主流程要明寫「先查 queue、不得自動 merge、確認後才更新 `same_as`」。
- **frontmatter 更新後，正文也要收斂**：不然 metadata 說已確認同人，但正文還保留雙頁互指，長期會混亂。
- **刪頁前先改 links**：像 `person_j` 這種直接刪檔，必須先掃一輪 `[[people/person_j]]`。
- **log 的歷史紀錄不要回改**：舊檔名可以保留在歷史 log，新的操作另外追加。

## 相關頁面與規則

Shane Wiki 內相關頁面：
- `AGENTS.md`
- `privacy_sanitize_rules.md`
- `lifecycle_rules.md`
- `Wiki_Pages/people/disambiguation_queue.md`
- `Wiki_Pages/people/person_jenny.md`
- `Wiki_Pages/log.md`

這套流程的價值在於：
- 把人物消歧從一次性的人工判斷，變成可審核、可重做、可延續的 wiki workflow。

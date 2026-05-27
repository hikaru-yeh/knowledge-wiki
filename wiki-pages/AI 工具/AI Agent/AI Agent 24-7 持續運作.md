---
網址: https://www.threads.com/@henrywthung/post/DYfiMJoE_wk
作者: ["@henrywthung"]
tags: [AI]
status: wiki
---

## Main Content

還是上來問一下，以免重複發明輪子。
是否有既有的framework或者github project可以做到，讓AI Agent 24小時持續工作。目前codex / Claude code都有使用。
例如： 自動提案，人類一次同意10個提案。剩下時間就逐步完成，同時產出下一批提案。

昨天晚上寫到一半才發現可以先調查。
第一版是有watchdog, 監測執行狀況，一旦結束就叫起來執行下一次。
每次都會先檢查上次執行記錄，backlog/todo list, 從優先權高的抓來逐一完成，記錄進度，update memory, end. 進入下一輪。
目前先採single worktree,避免互相影響。

講完今天Google就出招了

現在是用heartbeat監測沒錯，如果停下來就用watchdog叫起來做事

另外一隻程式監測，持續叫起來做事。 沒有額度起來就會停掉，進入迴圈。直到額度回來就會繼續跑。 不過還沒遇到這個問題，能拉高額度就拉高。
與其去等五小時，我希望五分鐘都不要停

## 圖片文字

### 圖片 1

Sam's Sweat Shop
S
New Issue
Dashboard
Inbox

WORK
Issues
Routines
Workflows
Goals

PROJECTS
Cosmos mobile v2
Paperclip
Company enhancement

AGENTS
JARVIS (CEO)
AEGIS (Policy Drafting)
CASE (Program Delivery)
ED-E (Jira)
GLADOS (CTO)

Workflows > Agent Hiring SOP

Agent Hiring SOP
Standard end-to-end workflow for hiring a new agent:
research, design, review, approval, and provisioning.

Gather agent
requirements

Research agent design
leads

Draft agent config and
instruction bundle

Design review

Board approval for hire

Provision and onboard
agent

Root
No deps
Has deps
Dependency

NODES (6)

1 Gather agent requirements
Run agent-input-gathering checklist. Confirm: job to be done, stakeholders, reporting line,
required tools/skills/permissions, memory expectations, heartbeat needs, approval boundaries,
and success criteria. If any critical input is missing, stop and escalate.

Edit
Invoke

1 live
4

## Sources

- [AI Agent 24-7 持續運作](https://www.threads.com/@henrywthung/post/DYfiMJoE_wk) | 作者: henrywthung

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

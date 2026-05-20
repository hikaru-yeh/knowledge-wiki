---
base: "[[收藏清單_DB.base]]"
url: "https://www.threads.com/@levelup.daily_lab/post/DXHZVSnE4fa"
author: "levelup.daily_lab"
clip_type: "Claude Code"
date_added: 2026-04-21T12:58:00
---

[https://www.threads.com/@levelup.daily_lab/post/DXHZVSnE4fa](https://www.threads.com/@levelup.daily_lab/post/DXHZVSnE4fa)

## 主文

claude code
6d
Claude Code 的 Skills 越裝越多，能不能讓它們自己進化？
darwin-skill 試了一個想法，把特斯拉前AI總監 Karpathy autoresearch 的核心邏輯套到 Skill 優化上，簡單說就是一個打分迴圈。
先對目前的 Skill 打分數，8 個維度，結構佔 60 分，實際跑出來的效果佔 40
分。找到最弱的維度，然後丟給子 agent 重新評分。新分數比舊的高就保留，不然就退回去
我覺得有幾個地方設計得不錯：skill格式寫得再漂亮，跑出來的結果是爛的也沒用。評分交給子agent 做，不會選手兼裁判。每跑完一輪會停下來等妳確認，可以把skill越做越進化，分享給大家🤲

## 作者留言

claude code
6d
·
Author
github.com/alcha…
github.com
GitHub - alchaincyf/darwin-skill: 达尔文.skill —— 一个让你的Skill无限进化的系统：评估→改进→测试→保留或回滚 | Autoresearch-inspired autonomous skill optimization for Claude Code. Evaluate, improve, test, keep or re
---
網址: https://www.threads.com/@warmwarter.ai/post/DYN9RYoD-lf
作者: ["@warmwarter.ai"]
tags: []
status: wiki
---

## Main Content

AI Threads
17h
Agent 跑完一個任務之後，hermes-agent 會在背景默默問自己一個問題：「這次有沒有踩過坑、走過彎路？有的話，存下來。」
這不是 fine-tuning，不是 RLHF，是純粹在執行框架裡設計的一個迴路。主任務回應完畢，背景 fork 出一個 review agent，拿到整個對話的快照，判斷有沒有東西值得存成 playbook。有的話幾秒後終端顯示一條通知，沒有的話什麼都不發生。
最有意思的部分是 filter 的設計：直接成功不存，只存試錯的經驗。背後的邏輯是：直接成功代表現有能力夠用了，不需要多一份 playbook。只有被迫試錯的路徑，才包含值得記錄的知識。這個 filter 同時也防止 skill base 無限膨脹——一個沒有 filter 的 self-improve 系統，幾個月後會充滿各種邊緣情況的 playbook，反而讓 agent 一般任務也開始選錯。
warmwater.dev/blog…
warmwater.dev
Agent 怎麼學會新技能：Skill 系統設計與自我強化迴路

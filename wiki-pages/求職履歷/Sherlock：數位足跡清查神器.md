---
網址: https://www.threads.com/@sam_lung2077/post/DXWsJmNk_1e
作者: ["@sam_lung2077"]
tags: []
status: wiki
---

## Main Content

你的 username 能被一行指令在 479 個社群平台上掃光 👁️
Sherlock：81.5k stars、MIT、Python
`sherlock your_handle` → 列出目前還活著的社群帳號
工程師自查 + OSINT 紅隊常備工具

它的邏輯超簡單：
把你的 username 塞進 479 個網站的 user page URL template，並行 HTTP 請求，看 response 有沒有「使用者不存在」的 signature
幾秒內列出命中（跑太快可能被 Cloudflare 擋，偶有誤判）
GitHub / Reddit / Snapchat / Gravatar / Docker Hub / 連 Zhihu 都有

大部分人從 18 歲開始用一個 handle 到現在
那條 digital breadcrumb 比你想像中長：
- Codecademy 的練習帳號
- Fiverr 的試水溫
- Typeracer 的跑分
- Spotify 的 public playlist
只要帳號還沒刪，Sherlock 就能幫你把那些「忘記關掉的門」指出來

攻防兩用：
防：自己跑一次，看什麼帳號露在外面、有沒有被仿冒
攻：紅隊 / 社交工程 / 背景調查，畫出目標的 digital footprint
MIT license 意味著任何人都能拿、也都能衍生工具。已經有一堆 wrapper、web UI、API 版本在外面跑

Sherlock 2018 年就有，7 年老專案
- 81.5k stars
- 9.5k forks
- MIT license
- Python 3.14 跑得動、CI 綠
工具一直在那，看你想不想自查

3 件今天就能做的事：
1. 跑 `sherlock YOUR_HANDLE`
2. 陌生或仿冒帳號 → 去對應平台申訴刪除
3. 重要帳號（銀行、工作、主 email）換成不同 handle，跟日常 username 切乾淨
能看見的 exposure，才有機會整理掉

裝法：
`pipx install sherlock-project`
`sherlock your_username`
Repo：github.com/sherl…

查都差不到😂

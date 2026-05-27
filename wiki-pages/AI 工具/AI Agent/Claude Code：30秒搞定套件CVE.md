---
網址: https://www.threads.com/@kai_ch_chen/post/DYVtovNkt74
作者: ["@kai_ch_chen"]
tags: [Claude Code]
status: wiki
---

## Main Content

CERT 5/13 公告 6 個高風險 CVE。
你公司用的 npm、pip 套件有沒有中？
以前要工程師早上開 dashboard 一個個比對。現在 30 秒搞定。
做法：把 NVD MCP server 接進 Claude Code。
claude mcp add nvd-cve npx -@modelcontextprotocol/server-nvd

## 圖片文字

### 圖片 1

AI應用 × ⚡ MCP/CLI
6個高風險漏洞

1 掃描依賴
    用 MCP 串接 CLI, 快速找出風險套件

2 比對 CVE
    整理版本、嚴重度與可利用資訊

3 產出修補清單
    把漏洞轉成可執行的更新任務

@kai_ch_chen
更少重複, 更多創造。

### 圖片 2

5/13 CERT 公告
你公司用的 npm、pip
有沒有中？

1 抓公告
MCP 讀取 CERT 與 NVD 資料

2 比對套件
掃描 package-lock、
requirements

3 標記風險
列出受影響版本與修補建議

@kai_ch_chen
更少重複，更多創造。

### 圖片 3

一個個比對
工程師早上開 dashboard / 手動對清單，半天沒了

1 開 dashboard
   先看警告, 再翻 CVE 清單

2 手動比對
   套件、版本、環境逐項確認

3 半天消失
   重複查核拖慢真正修補

@kai_ch_chen
更少重複，更多創造。

### 圖片 4

現在 30 秒
接一個 MCP server / 讓 Claude 自己查

1 接 MCP server
把 CVE 資料源接進 Claude

2 丟套件清單
Claude 自動比對版本與風險

3 產出修補優先序
先處理高風險，少做重複查詢
高
中
低

@kai_ch_chen
更少重複，更多創造

### 圖片 5

一行指令搞定

claude mcp add nvd-cve / npx @modelcontextprotocol/server-nvd

1 加入 NVD CVE 工具
讓 Claude 直接查最新漏洞資料庫。

2 貼上一行指令
claude mcp add nvd-cve
npx @modelcontextprotocol/server-nvd

3 開始自動掃描
把套件、服務或 CVE 編號丟給它，
快速整理風險。

@kai_ch_chen
更少重複，更多創造。

### 圖片 6

問一句就出報告
「我們的 package.json /
有沒有中今天的 CVE？」

01 掃描依賴
讀取 package.json 與 lockfile，
列出實際安裝版本

02 對照 CVE
MCP 連到漏洞資料庫，
比對今天新增風險

03 產出報告
影響範圍、修補版本、
優先順序一次整理

@kai_ch_chen
更少重複，更多創造

### 圖片 7

7/7 完結篇

你還在手動查嗎？

📌 存起來，週一接上
先抓一個重點就好。
你最想先試哪一步？

追蹤 @kai_ch_chen 看更多實戰案例

@kai_ch_chen
更少重複，更多創造。

## Sources

- [Claude Code：30秒搞定套件CVE](https://www.threads.com/@kai_ch_chen/post/DYVtovNkt74) | 作者: kai_ch_chen

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

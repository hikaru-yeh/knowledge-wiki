---
網址: https://www.threads.com/@krumjahn/post/DXmIT_QGj0U
作者: ["@krumjahn"]
tags: []
status: wiki
---

## Main Content

你的 AI agent 為什麼爬不了大部分網站？
因為大部分網站會偵測你是不是真人。
用 curl 或 fetch 直接抓？直接被擋。原因是現代網站需要 JavaScript 執行才能載入內容——而且很多都有反爬蟲機制，一看到沒有瀏覽器環境就拒絕。
解法是 headless browser——一個沒有畫面的瀏覽器。它假裝是真人在用 Chrome，但全程在背景自動執行。
問題是 Playwright、Puppeteer 這些工具很重、很慢、而且容易被識破。
上週發現一個新的：Obscura。
Rust 寫的，內建 stealth 模式，直接接 CDP——現有的 Playwright 程式碼不用改。
13 天，4,800 個 GitHub star。
我還沒全面換，但已經在測了。
GitHub 放留言。

github.com/h4ckf…
github.com
GitHub - h4ckf0r0day/obscura: The headless browser for AI agents and web scraping

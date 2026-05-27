---
網址: https://www.threads.com/@yi.startup.dev/post/DYgEFW5Gj6F
作者: ["@yi.startup.dev"]
tags: [Claude Code]
status: wiki
---

## Main Content

你最近有把 API Key 直接送出給 AI 嗎?
最近嘗試像個普通人用 AI，發現 AI 很喜歡叫我「把 API Key 貼上」我幫你做⋯⋯，很省事，但是我頭皮發麻，API Key 一般來說不建議放在 Github, 也不建議使用任何的通訊軟體傳輸，雖然你把 API key 貼上的後果，只是把 API Key 送到 AI 公司的主機上，也有可能也會在AI 公司主機的歷史紀錄裡。
那你要怎麼樣 vibe coding ，又不直接貼 API key 給 AI？
把 Key 存在跟目錄裡面的 .env ，叫 AI 不要打開，由你的 script 透過 dotenv 自己讀
不會設的話，請 AI 帶你設定：
「請教我怎麼用 .env 存 API key，但你不要打開它」
如果你已經在用 Claude Code 這類 agent，在 Claude MD 檔加上這條格言
「永遠不讀 .env、~/.zshrc 等敏感檔案，永遠不要問我 API Key，而是由 script 載入」

它很棒！好好稱讚它！

喔拜託不要吧 🤣 怎麼那麼聰明

實際上會發生的事，就是 api key 送到 ai 公司的主機，如果你信任 ai 公司有把這些對話都當作最高機密，或是你傳送的過程沒有因為其他因素被看到 key，那⋯也許沒什麼大不了。
但是，這不是一個好的習慣，這就像是大家都知道密碼不要設 12345678 或是自己的生日，但是還是有人會這樣設的道理一樣。
記憶是存在你本機這沒有錯，但對話還是送給 ai 公司，這樣 ai 才知道你要他做什麼 💪

## Sources

- [別把 API Key 直接給 AI！](https://www.threads.com/@yi.startup.dev/post/DYgEFW5Gj6F) | 作者: yi.startup.dev

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

---
url: "https://www.threads.com/@crazyaitools_/post/DYHwiQHkpV8"
author: "@crazyaitools_"
clip_type: "Claude Code"
---

【我以前用 Claude Code 寫 PHP 專案，最頭痛的就是它常常不懂我引入的那些套件規則】 AI 寫 code，最怕它瞎猜，尤其是複雜的 Composer 依賴。
你得花大把時間解釋，它才懂這些套件有什麼 API、什麼設計模式。

最近挖到一個 GitHub repo，專門解決這個痛點。 這個 repo 叫 jardisTools/dev-skills。
它核心做的事，就是讓你的 AI 助手自動「懂」你專案裡 Composer 套件的規則跟 API。
它主要做到這幾點：
→ AI 代理程式技能自動化配置：透過 Composer plugin，在 composer install/update 後，自動掃描專案裡的 Jardis 套件，將 AI 技能定義和 API 規則複製到專案。
這樣 AI 就能即時掌握最新的開發規範，不用你手動餵。
→ AI 輔助開發環境客製化：你可以在 composer.json 裡精確設定要啟用或排除哪些內建 AI 技能。
像是架構規則、測試規則等，讓你的 AI 輔助開發環境符合專案需求。
→ 內建 7 項跨套件 AI 技能：涵蓋架構、模式、測試等，大幅提升 AI 輔助開發的廣度與深度。
→ 要求 PHP >= 8.3, Composer >= 2：這是使用這個工具的最低環境要求。

這工具適合 PHP 開發者，特別是那些專案大量使用 Composer 套件，又想用 Claude Code 這種 AI 助手來提升效率的人。 我裝來試了一下，最直接的感受是，以前 Claude Code 對於一些特定套件的用法，會一直問東問西，甚至亂寫。
現在它讀到這些規則後，給的建議就精準很多，減少了很多來回溝通的時間。
小工提醒：這東西雖然方便，但它只針對你 Composer 引入的套件進行技能整合。
如果你的專案有大量手寫的內部函式庫，還是得靠 CLAUDE.md 這種文件去定義，兩者可以搭配用。
這有點像 AI 拿到了一份自動更新的「外部套件使用手冊」，但「專案內部規範」還是得靠人寫。 我覺得這方向對了，AI 寫 code 不該只靠模型，而是要給它正確的「知識脈絡」。
專案連結：github.com/jardi…
⭐ 0 stars
週末來研究一下這套件怎麼幫我加速新專案的。
code.claude.com
Claude Code overview - Claude Code Docs

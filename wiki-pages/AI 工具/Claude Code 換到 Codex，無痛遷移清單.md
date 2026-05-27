---
網址: https://www.threads.com/@andrew54068/post/DXpAKInmp77
作者: ["@andrew54068"]
tags: []
status: wiki
---

## Main Content

你用 Claude Code 用順了，有一天想試試 Codex？ 大概會有這種感覺：該有的功能都在，但開發者體驗差了一截。

我這幾天實際換過去。 基礎功能都在——skill、tool、hook、subagent 全都有。 如果你只用基礎功能，幾乎是無痛轉移。

問題是，一旦你用慣了進階功能，差異就很明顯。

這篇整理給已經在用 Claude Code、正在考慮或剛開始試 Codex 的人。

【設定檔對應關係】

先從最基本的換名字開始：

[CLAUDE.md](http://claude.md/) → [AGENTS.md](https://l.threads.com/?u=http%3A%2F%2FAGENTS.md%2F&e=AUDbaVu5MymJR7vtmfjKLDEF2bco62mbGEuDFUvSx0Sjmv26xuAhAaxgfLn7Y-tsUCIa5_DHjT2Zy-XKvX-z83YB40XfA5ft4dBQ8dpBvvGUo68lCOO3u5O69VhBXV1lDLkIxEmorUbzyZGR3ObwvAQ) ~/.claude/ → ~/.codex/（但 Codex 也會去讀 ~/.agents/skills） ~/.claude/settings.json → ~/.codex/config.toml

換個名字，概念一樣。 skill、tool、hook、subagent——這些 Claude Code 有的，Codex 也有。

【主要差異速查】

| 項目 | Claude Code | Codex | | 快捷鍵 | 豐富 | 極少 | | Agent Teams | 有 | 沒有 | | Hook 支援 | 完整（20+ 事件）| 基本（6 事件）| | rules 格式 | Markdown | rules/ 有，但不支援 Markdown |

快捷鍵的部分讓我最有感。 幾個我每天在用的快捷鍵，Codex 全都沒有對應：

暫存打到一半的 prompt：Ctrl + S 切換 model：Option + P

這些要自己找替代方案，或放棄習慣。

【Codex 的定位：工具型指令集】

Codex 少了很多進階功能，這是設計決策。

Codex 把自己定位成工具型的指令集，不像 Claude Code 包山包海。 所以快捷鍵少、Agent Teams 沒有、Hook 也只有 6 個事件。

【Agent Teams vs Subagent】

Codex 只有 Subagent，沒有 Agent Teams。 兩者的核心差別是——Subagent 之間能不能互相溝通討論。

Agent Teams 可以，Subagent 不行。

官方目前沒有計畫實作 Agent Teams。 如果你需要這個功能，可以用社群開發的 vida-stack 來補。

【Hook 支援不完整】

Codex 的 plugin hook 支援只有基本 6 個事件。 Claude Code 有 20+ 個。

跟 hook 相關的 plugin，基本上不能直接從 Claude Code 搬過來用，需要額外改造。

例如 ralph-loop（Day 116 有介紹）。 在 Codex 上可以用 CodexPotter 或自製 Stop hook 來替代。 Day 116 有比較這兩條路線的差異。

【我的混用策略：skills-bullpen + symlink】

我目前是 Codex + Claude Code 混用，所以需要讓兩邊都能讀到同一套 skill。

做法：把所有 skill 都搬到 ~/.agents/skills-bullpen/ 資料夾下。 Claude Code 和 Codex 都能讀到這個路徑。

搭配自製的 /skills-manager 來管理。 要變成 global 還是專案專屬的，建立一個 symbolic link 到指定資料夾就搞定。

好處是：可以無腦把 skill 都丟進 bullpen，用到才連結出去。 不會擔心佔用 context window（AI 每次能記住的工作記憶上限）。

【一個小坑：rules 格式】

如果你在 Claude Code 裡有用到 ~/.claude/rules/，注意這件事： Codex 有 rules/ 資料夾，但不支援 Markdown 格式——內容要轉換才能用。 這部分要轉換，或直接寫進 AGENTS.md 裡。

這是 Codex 遷移系列三篇，補一下前兩篇的連結：

→ Day 115（Claude Code Hook 機制）: [threads.net/@andr…](https://www.threads.net/@andrew54068/post/DXjxPlaGnM1)

---
base: "[[收藏清單_DB.base]]"
url: "https://www.threads.com/@jasonj.lai/post/DXBHAVCERlR"
author: "jasonj.lai"
clip_type: "Claude Code"
date_added: 2026-04-21T12:58:00
---

[https://www.threads.com/@jasonj.lai/post/DXBHAVCERlR](https://www.threads.com/@jasonj.lai/post/DXBHAVCERlR)

## 主文

給小白的Claude code 風險管理
第一，看最前面的「動詞」是不是你認識的危險動詞。rm、sudo、dd、kill、chmod——這些你已經知道了。如果最前面的指令你不認識（像 gh、npx、wrangler），進入第二步。
第二，看 Claude Code 給的那行英文描述。它每次問你授權都會寫一句，像剛才寫的是 "List files in GitHub PIF12 repo"——list = 讀取，安全。如果描述裡出現 delete、remove、push、deploy、modify、overwrite 這類字眼就要多看一眼。
第三，看指令裡有沒有你認識的「安全信號」或「危險信號」。安全信號：cat、list、--dry-run、head、2>/dev/null（只是隱藏錯誤訊息）。危險信號：--force、--remote、-rf、| bash、> file（覆寫）、DELETE、DROP。
三個都看不懂的話，直接問 Claude Code/chat：「這個指令會不會改任何檔案或線上資源？」一句話就夠了，不丟臉。

## 作者留言

·
Author
但是作為被害妄想症患者（誤）、法律人職業病患者（✅）
一定會追問：
Claude Code 的描述可不可信？
不能完全信。它不是故意騙你，但它可能搞錯或描述得太輕描淡寫。比如一個 DELETE FROM messages 它可能描述成 "Clean up old messages"——聽起來很無害，但如果沒有 WHERE 條件就是清空整張表。所以描述只是「第一層篩選」，有疑慮時要看指令本身。
真正的信任鏈是：指令本身 > 你的判斷 > Claude 的描述。
完整的危險信號清單如下，先分類列，這樣比較好記：
第一類：
「會刪東西」的信號：rm（尤其搭配 -rf、-r、*）、DROP、DELETE、truncate、--prune、clean、purge、reset --hard。
「會覆寫東西」的信號：> 單箭頭（覆寫檔案，>> 雙箭頭是追加、相對安全）、--force 或 -f（強制覆蓋，不問你）、mv（目標同名會靜默覆寫）、cp（同上）、sed -i（直接改檔案內容）。

·
Author
第二類：
「會推到線上」的信號：deploy（不管是 wrangler deploy 還是別的）、push（尤其 --force）、publish、--remote（像你用過的 d1 execute --remote）。
第三類：
「會執行外來程式碼」的信號：| bash 或 | sh（把下載的東西直接當程式跑）、eval、exec、source（載入並執行腳本）。注意：單獨的 bash 不危險，危險的是管道接 bash，就是 curl ... | bash 這個模式。
「會提升權限」的信號：sudo、su、chmod 777、chmod -R、chown。
「會動資料庫結構」的信號：ALTER、DROP、TRUNCATE、DELETE（沒 WHERE）、UPDATE（沒 WHERE）。
所以怎麼記？
不知道，跟背英文單字一樣，多看多問多查，多看就會了（？）

·
Author
除了這些「咒語」，語法也蠻重要的，學會拆就不怕了
**一行指令的閱讀順序**
拿你的例子：`brew install gh 2>&1 | tail -5`
這行其實有三層：

·
Author
主指令是 `brew install gh`——這是真正在做事的部分。`brew` 是 macOS 的套件管理器，`install` 是動作，`gh` 是裝什麼。這是唯一需要判斷的部分。
`2>&1` 是把錯誤訊息合併到正常輸出——純粹是「怎麼顯示」，完全無害，看到直接跳過。
`| tail -5` 管道接 `tail`，只取最後 5 行顯示——也是純顯示，無害。
所以這行的風險判斷完全取決於 `brew install gh`：裝軟體，低風險但不是零風險（裝錯套件可能有問題），你知道 `gh` 是 GitHub CLI 就沒事。

·
Author
**常見的「無害裝飾」語法，看到直接跳過**
`2>&1` 和 `2>/dev/null` 控制錯誤訊息怎麼顯示。
`| head -N` 和 `| tail -N` 只取前幾行或後幾行。
`| grep "keyword"` 從輸出裡過濾特定文字。
`| wc -l` 數行數。
`| sort` 和 `| uniq` 排序和去重。
`| jq '.field'` 解析 JSON 格式。
`|| echo "fallback"` 前面失敗就印一段文字。
`&& echo "done"` 前面成功就印一段文字。
`$(command)` 把括號裡的結果當文字塞進去。
這些都不會改任何東西，是用來「整理顯示」的工具。

·
Author
**真正需要看的永遠是最前面的主指令**
`brew install gh 2>&1 | tail -5` → 重點是 `brew install gh`。
`cat file.txt | grep error | wc -l` → 重點是 `cat file.txt`（讀取，安全）。
`curl xxx.sh | bash` → 重點是 `curl ... | bash`（下載並執行，危險）。
`npx wrangler deploy 2>&1 | head -20` → 重點是 `wrangler deploy`（部署上線，要確認）。
但凡原則必有例外！！！！

·
Author
*例外：管道接「危險動詞」**
一般管道 `|` 後面接的都是顯示工具，但如果管道後面接的是 `bash`、`sh`、`xargs rm`、`tee` 加檔案路徑，那就要注意了。
`| bash` 和 `| sh` 把前面的輸出當程式執行，這是最危險的管道。
`| xargs rm` 把前面列出的每個檔名都刪掉。
`| tee secret.txt` 把內容寫進檔案（可能覆寫）。
**總結：閱讀一行指令的 SOP**
先找第一個詞（主指令），判斷它是讀還是寫。然後掃一眼管道 `|` 後面有沒有 `bash`、`sh`、`rm`、`tee`。其餘裝飾語法全部忽略。
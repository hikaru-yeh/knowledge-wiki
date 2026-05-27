---
網址: https://www.threads.com/@llamatechtrend_zh/post/DXwfJo3kX64
作者: ["@llamatechtrend_zh"]
tags: []
status: wiki
---

## Main Content

《連續三周24小時工作的agent開發團隊配置》
是連續24小時工作，不是待命。
這個架構真的很強，分享給大家。
TL: 一個Team Lead由codex擔任
PM: 一個PM由claude擔任
Worker: 三個Engineer由codex擔任
1. Claude做PM邏輯最簡單。
一、在大型複雜專案中，被我歸類為極度初階工程師，幾乎無法信任，超過十個文件互動的專案就會開始鬼打牆，用到第二天就會發現所有的bug都在rotate出現。
二、他有loop功能，這就像CPU的clock一樣，每一輪就會看任務工作結束沒，並跟TL拿新的任務。
三、超省token，因為loop優化過，可能是cache的原因，幾乎燒不到token，貴森森又笨的模型真的好好當clock跟傳聲筒就好。
2. 為什麼是三個Worker？
因為有很多任務是可以平行化去做的，還有很多測試要花很多時間用CV檢視、一步步操作畫面。所以讓TL自動分配給三個Worker，自動parallel增加了不少效率。
3. 已經有PM可以執行任務並確保需求交付了，為什麼還需要Team Lead？

一、PM的context會被loop污染，parse tmux其實還是滿髒的工作，每個clock都會污染一次，會讓PM本身失去工作焦點。
二、claude對大型專案的能力，無法檢視交付品質。我現在因為追求高度自動化，整個開發流程步驟非常多，以驗證來說，我設定了三個gate
- forward path verification: 就是從新trace一次code的邏輯對不對
- human path verification: 用介面操作一次，接結果是否符合預期
- requirement alignment verification：用claude -p跟codex exec去呼叫外部專家檢視，目前的實作有沒有符合需求文件跟專案標準。
不要說還有plan或是merge條件等，這個遵循成本非常高，下一步怎麼走需要非常多思考，我還是比較信任codex。
歷史進程
這個架構並不是拍腦袋的設計，或是參考別人的設計，他是一個公司擴張跟演進的過程。
1. 階段一：起初我自己控制三個codex session，每個要追進度，要安排工作，要處理blockers。

這個階段每次工作很難超過30分鐘。
2. 階段二：我發現codex交互或是harness真的做的不好，所以每一個worker我都配給他們一個pm，這樣一方面可以讓交互變得更好。另一方面，一個也可以透過telegram跟claude互動。此時工作時間已經可以到兩小時以上。
3. 階段三：三個PM還是要獨立跟三個claude session互動跟追進度，PM也大多在做空loop，因為Worker還沒工作完，理所當然的，我就把他們放到同一個PM下。比較剛好的是，此時剛好claude推出loop功能，所以我也開始嘗試用loop去監督worker工作，沒想到效果出奇的好，有loop根本就不需要優化harness了。
4. 階段四：新增TL，我慢慢發現claude無法遵照我定義的流程去給worker指令，遇到問題也只會跟著worker走，就是那種會被Engineer唬爛掉的PM。於是我又嘗試創了TL，沒想到效果出奇的好，整個架構已經24小時不間斷工作三周。
當然這還有很多變化空間，也還有很多切入點可以優化，如果現在就在思考，
怎麼開第二隻團隊，讓環境依舊乾淨。

怎麼讓每一個角色分工時有自己的agent file，不是拿專案共用的agent file。
怎麼讓不同角色的分工，可以透過更漂亮的介面，讓agent之間傳訊息，人類還是可以監視他們的互動。
這真的是一個agent蠻荒的時代，第一次我們有機會定義新世界的時代。
p.s. 附圖是TL指派工作給三個worker的指令

我現在是讓跨agent溝通時，每一個訊息都先放目標agent的agent file path讓他看一遍再開始工作😂😂😂

只跑loop真的燒很慢。
我上週就是這要用一整週的。
就真的不會滿。

codex 200 claude 100
codex 有時會爆週限制，多加100訂閱。

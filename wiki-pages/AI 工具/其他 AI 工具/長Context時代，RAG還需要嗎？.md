---
網址: https://www.threads.com/@ai.tech.share/post/DYfEfPGEww2
作者: ["@ai.tech.share"]
tags: [AI]
status: wiki
---

## Main Content

上週我把一個小專案的 RAG 砍掉，整個改成 1M context 直接丟整個知識庫。三天後我又把 RAG 加回來。
不是因為 RAG「比較強」。是因為兩個一起用最便宜。
全塞策略每次回應的 token 帳是 RAG 的 80 倍以上，使用者多了之後燒不起；但全用 RAG 又會在「需要看整份文件脈絡」的問題上漏掉關鍵。最後的結構：固定文件 prefill、動態 FAQ 走 RAG、對話歷史走 memory layer。
完整對照（成本帳、四種補位技術 CAG / GraphRAG / Agentic Retrieval / Memory Layer 的場景判斷）放文字附件。
「1M context 是不是讓 RAG 過時了」這個問題，要拆成幾件事看。
一、Context Window 跟 RAG 不是同一層東西
Context Window 是「模型一次能讀多少字」的容量上限。RAG 是「從大資料庫挑相關片段送進去」的工程模式。兩者解的問題不一樣：
・Context Window 解的是「給模型的 input 太短，塞不下」
・RAG 解的是「我手上的資料太多，不可能全塞」
1M token 讓「塞不下」的問題變鬆，但沒消除「資料太多 + 動態 + 多人 + 要追溯」這些工程問題。
二、1M context 的真實限制（不是規格表上的）
成本與延遲：丟 800K context vs 丟 8K 精挑片段，token 帳差 100 倍以上。回應時間從 0.5 秒拉到 5–10 秒，使用體驗直接破。
Lost in the Middle：Liu et al. 2023 的論文發現，模型對 context 中段的內容注意力會掉；放在開頭與結尾的內容被使用率高很多。1M 雖然能裝，但裝越多中段越被「淹沒」。
動態知識：FAQ、產品文件、客服訊息每天都在改。全塞策略每次都要重灌整個 context；RAG 只要重建 index（向量化新文件），成本差兩個數量級。
權限與多租戶：同一份資料給不同使用者，要靠檢索層在外面擋。長 context 本身沒有「只給看 A 不能看 B」的機制。
可追溯性：RAG 回應時可以回傳「這段答案來自哪份文件、哪一段」。長 context 是「整本書都塞了」，要追溯哪一句出處反而難。
三、RAG 自己的痛點（不能假裝不存在）
・Chunking 切不好：切太細語意斷掉、切太粗檢索精度低
・檢索質量不穩：vector similarity 是粗略的，純語意相似不等於「真的能回答這個問題」
・架構複雜：embedding model、向量庫、reranker、chunking pipeline、index 更新流程，任何一段壞掉整套就壞
・Cold start 痛：新領域沒有 ground truth 標註，檢索精度要靠人工調
四、RAG 以外的補位技術（2025–2026 比較常被討論的）
CAG（Cache-Augmented Generation）：把固定不變的知識（產品手冊、API 文件、SOP）直接 prefill 進模型的 KV cache，省掉檢索這一層。優點：低延遲、實作簡單。缺點：知識一改就要重 prefill，所以只適合「固定」內容。
GraphRAG：把文件先轉成知識圖譜（entity + relation），檢索時走圖結構而不是純向量相似度。能回答「A 跟 B 的關係是什麼」這種跨文件、關係型問題，純 RAG 很容易在這類問題上漏掉。缺點：建圖的前處理成本高。
Agentic Retrieval（Agentic RAG）：讓 agent 自己決定要不要再查、查什麼。例如第一次檢索結果不足，agent 會 reformulate query 再查一次，或主動分解成子問題。適合「複雜、多跳推理」的問題。缺點：每次回應的 LLM 呼叫次數變多，成本與延遲上升。
Long-term Memory Layer：mem0、Letta（前 MemGPT）這類，提供跨 session 的個人化記憶：使用者的偏好、過去對話、長期目標。這層在「使用者個人脈絡」上補了 RAG 抓不到的東西（RAG 通常處理的是「組織知識」，不是「個人歷史」）。
Fine-tuning / LoRA：嚴格說不是 RAG 的替代，是「把固定知識壓進模型參數」的另一條路。適合「風格、術語、領域語言」這種要內化的東西，不適合「會變動的事實」（事實變了就要重訓）。
五、實務上該怎麼選（場景判斷）
・一次性、整份文件分析：長 context 直丟最划算（不用建 RAG 基建）
・動態、大規模、多用戶：必走 RAG
・固定知識 + 高頻使用：CAG 比 RAG 簡單
・關係型、跨文件問題：GraphRAG 比純 vector RAG 強
・複雜多跳推理：Agentic Retrieval
・個人化、跨 session：Memory Layer
・風格、術語內化：Fine-tune
・真實世界：通常是上面幾個的組合，不是擇一
六、為什麼說「RAG 變強而不是被取代」
1M context 出現後，RAG 的角色其實變更舒服：
・檢索回來的 top-k 可以從 5–10 段拉到 50–100 段，召回率提高
・不用瘋狂壓縮 chunk，每個 chunk 可以更完整
・rerank 後的結果可以給模型更多上下文判斷
・少了「context 不夠用」的束縛，pipeline 設計變鬆
所以結論是：長 context 是 RAG 的好朋友，不是對手。
Read more

寫到這裡發現一個有趣的事：我們在問「RAG 還需要嗎」這個問題本身，其實假設了「context 變大就是萬能解」。但 AI 系統的工程問題從來不只是「能塞多少」，更多是成本、延遲、動態、權限、可追溯——這些東西模型參數量再大也不會自動解掉。
你最近在做的 AI 專案，是純 RAG、純長 context、還是混合架構？踩過最深的坑是哪一塊？留言聊聊，下篇可能挑一個常見組合做完整踩坑筆記。
💡 ai.tech.share｜不會讓你看不懂的 AI 技術頻道
#RAG #LLM #AI技術 #ContextWindow #AI開發

## Sources

- [長Context時代，RAG還需要嗎？](https://www.threads.com/@ai.tech.share/post/DYfEfPGEww2) | 作者: ai.tech.share

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

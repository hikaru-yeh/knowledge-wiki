---
url: "https://www.threads.com/@buildthink.ai/post/DYPKGdZjzKK"
author: "@buildthink.ai"
clip_type: "AI"
---

如何架構一個 AI Agent 的記憶：Hermes Agent 給我的五個關鍵教訓
大部分人建 AI agent，把所有精力放在選模型和寫 prompt 上。但用過一段時間就會發現：不管模型多強，你的 agent 每天把Token 全燒在重複推理上
Hermes Agent 使用量剛超越龍蝦，不是因為它用了更強的模型，而是因為它在架構層做了一件龍蝦沒做的事
它的記憶是四層各司其職的架構——把做過的流程自動寫成 Skill 文件下次直接調用，錯誤修復記錄確保同一個坑永遠不踩第二次
這四層加在一起，產生了一個反直覺的效果：Hermes 單次思考用的 token 比龍蝦更多，但開發者的總成本反而更低—
因為重試更少、重複推理更少
這篇整理了完整拆解：
→ 四層記憶架構：各自解決什麼問題
→ 每一層怎麼實現，附具體代碼邏輯
→ Skill 自動生成的觸發條件和存儲格式
→ 自我修復迴圈怎麼設計
→ 可寫運行時 vs 只讀運行時的本質差異
→ 為什麼有記憶的 agent 用越久越便宜
—
儲存 💾
追蹤
@buildthink.ai
獲取更多 AI 工具實戰教學

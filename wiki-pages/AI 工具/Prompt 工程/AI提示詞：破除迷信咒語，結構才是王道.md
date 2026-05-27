---
網址: https://www.threads.com/@buildthink.ai/post/DYSIIZeD1vh
作者: ["@buildthink.ai"]
tags: [AI]
status: wiki
---

## Main Content

90% 的「提示詞技巧」都是迷信——多屆提示詞比賽冠軍的重要一課
平時在 AI 圈廣泛流傳的「神咒」，在 GPT、Claude Opus、Gemini上全部沒有顯著效果。
真正有效的少數幾個技巧。差別不在措辭，而在結構。
2025 年新加坡 Prompt Royale 第三屆，2,500 名公務員，冠軍用的是 CO-STAR 框架。同年杜拜全球提示詞賽，125 個國家——四位冠軍的共同點不是某句神奇咒語，而是結構化的分步拆解。
2026 年的共識：結構優於措辭、肯定優於否定、少示例優於多示例。
隨著模型越來越強，prompt 工程正從「找咒語」轉向「寫規格說明」。
這篇整理了完整拆解：
￼ → 被數據證偽的五個「流行咒語」
→ 真正有效的技巧和準確率提升數字
→ 2025 年三大比賽冠軍的獲勝框架
→ 一個可以直接複製的萬能 Mega-Prompt 模板
→ 五種日常場景的實戰模板
→ 為什麼「寫好需求文檔」比「背 100 條咒語」強 10 倍
—
儲存 💾
追蹤
@buildthink.ai
獲取更多 AI 工具實戰教學

## 圖片文字

### 圖片 1

AI 工具速報

90% 的提示詞
技巧都是迷信

4,950 次測試 + 三大比賽冠軍告訴你什麼真正有效

結構優於措辭，真正有效的是規格化提示，而不是神奇句子。

數據驗證
大量測試 x 系統分析
找出真正有效的模式

比賽實證
三大頂尖賽事冠軍
共同驗證結構優勢

真實落地
真實任務表現更穩定
可複製、可擴展、可落地

4,950
次測試
沃頓提示詞科學報告

3 大比賽
冠軍共同結論：
靠結構，不靠咒語

US$272K
獎金池
比賽結果證明結構化
prompt 更重要

@buildthink.ai

### 圖片 2

AI 工具速報
這五句話
在 2026 年的模型上完全沒用
Wharton Prompting Science Report 3

X 「我給你 1000 美元小費」 → 4,950 次測試：
                                    無統計顯著效果

X 「深呼吸再回答」 → 只在 PaLM 2 曾有亮眼結果，
                                    當前模型不是最優

X 「你是世界頂級專家」 → 162 種角色 × 2,410 題：
                                    對客觀任務無提升

X 「答錯就開除你」 → 個別題目劇烈波動，
                                    方向不可預測 = 噪音

X 「這對我的職業生涯很重要」 → 情緒勒索在前沿模型上無效

來源：Wharton Prompting Science Report 3

• @buildthink.ai •

### 圖片 3

AI 工具速報

『你是專家』
到底有沒有用？

客觀任務                                主觀任務

162 種角色 × 4 模型 × 2,410 題             有效
                                        能穩定輸出風格和語氣

結果：無提升                              例如：
                                        『用 Dyson 文案風格寫』
甚至在偏見檢測任務中                        『像資深工程師 review』
準確率從 57% 掉到 28%

Role-play 控制風格 ✓ / Role-play 提升準確度 ✕

• @buildthink.ai •

### 圖片 4

AI 工具速報
『Let's think step by step』
什麼時候管用？

數學任務
*   MultiArith 17.7% → 78.7% (+61pp)
*   GSM8K 10.4% → 40.7%

非數學任務
*   MMLU 的 95% 增益來自含「=」的數學題
*   其他題型幾乎為零

推理模型
*   加 CoT 幾乎沒收益
*   回應時間增加 35%-600%
*   Gemini Flash 2.0 上正確率降低 13.1pp

非推理模型 + 數學
→ 加
推理模型
→ 不要加

@buildthink.ai

### 圖片 5

AI 工具速報

示例不是越多越好
2-5 個是甜蜜點

Few-shot 示例
最佳區間 2-5

準確率
示例數量

TriviaQA 64.3% → 71.2% (少樣本)
LAMBADA +18pp
超過 5-20 個後準確率開始下降

實用做法：
給 2-3 個高品質示例 / 包在 <examples> 標籤裡 / 放在用戶輸入之前

@buildthink.ai

### 圖片 6

| AI 工具速報

「不要做 X」
會讓 X 更容易出現

ⓧ 不要寫代碼解釋                                 ✔ 只輸出代碼塊
    模型容易補充過多說明，                               限制輸出格式，減少多餘文字，
    增加噪音與誤差                                   結果更精準可用

ⓧ 不要用專業術語                                 ✔ 用小學生能聽懂的語言
    模型傾向使用更複雜的詞彙，                           明確的簡單語言指令，
    增加理解門檻                                   更容易得到清楚答案

ⓧ 不要超過 500 字                                ✔ 控制在 300-500 字之間
    模型容易填滿篇幅，                               設定合理範圍，引導模型
    加入不必要的內容                               聚焦重點、避免冗長

來源：Don't Think of the White Bear (2025)
—— 反諷反彈效應在 LLM 中同樣存在

• @buildthink.ai •

### 圖片 7

AI 工具速報

三大比賽，三個冠軍
同一個結論

新加坡                 杜拜全球提示詞                 Kaggle
Prompt Royale 2025       錦標賽 2025                   Konwinski Prize

[Marina Bay Sands image]      [Burj Khalifa image]           [Growth chart image]

冠軍：Matthew Lee             3,800 人 / 125 國 /          冠軍：Eduardo
(HDB 高級建築師)              US$272K 獎金                 Rocha de Andrade

2,500 人 / 114 個                                      US$50K / 純提示詞工程
政府部門                                               不訓練任何模型

獲勝框架：                  四位冠軍共同點：               證明：
CO-STAR                   結構化分步拆解                 結構化 prompt
                                                     價值不降反升

共同結論：沒有人靠「神奇句子」贏，全部靠結構

• @buildthink.ai •

### 圖片 8

AI 工具速報

CO-STAR
從 2023 到 2025 持續獲勝的框架

C · Context (背景) ----> 給模型情境錨點
O · Objective (目標) ----> 單一、具體、可衡量
S · Style (風格) ----> 錨定到參考對象
T · Tone (語氣) ----> 情緒基調
A · Audience (受眾) ----> 決定詞彙深度和切入點
R · Response (格式) ----> 長度、結構、Markdown / JSON

2023 年 ----> 2024 年 ----> 2025 年
Sheila Teo 首創 消防員 Naim Zahari 延伸 Matthew Lee 再次驗證

@buildthink.ai

### 圖片 9

| AI 工具速報

可以直接複製的
萬能 Mega-Prompt 模板

<role> 具體專家角色 + 資歷
<context> 背景、受眾、品牌聲音
<objective> 單一目標 + 成功標準
<rules> 硬規則 (用肯定式)
<methodology> 分步方法論
<examples> 2-3 個高質量示例
<input_data> 實際內容
<output_format> 精確格式要求
<self_check> 完成前自我驗證

</> 跨 Claude / GPT / Gemini 都有效。本質 = 把 prompt 當軟體需求文檔寫

@buildthink.ai

### 圖片 10

AI 工具速報

五種日常場景
直接套用

---

  📄  1 寫作
先讓模型逐字引用文檔段落並編號 →
再寫答案用 [1] 引用 → 顯著降低幻覺率

---

  </>  2 編程
用 <review_criteria> 嵌套 <security>
<performance> <maintainability> →
每個發現給嚴重等級 + 修復代碼

---

  📊  3 分析
用變量鏈式技巧 → 每步大寫命名輸出
(CLUSTERS) → 後續步驟用 [CLUSTERS] 引用

---

  💡  4 頭腦風暴
結尾加『Give me 2 different
prioritizations』→ 強制多變體輸出

---

  📚  5 學習
蘇格拉底模式 → 『Your goal is to ask
probing questions』→ 防止模型直接講課

---

  ⭐ 一個好 prompt, 不只是問問題, 而是設計模型的工作流程。

---

• @buildthink.ai •

## Sources

- [AI提示詞：破除迷信咒語，結構才是王道](https://www.threads.com/@buildthink.ai/post/DYSIIZeD1vh) | 作者: buildthink.ai

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

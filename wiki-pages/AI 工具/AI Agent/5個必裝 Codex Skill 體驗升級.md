---
網址: https://www.threads.com/@kikitataysi/post/DYTF2nGksoT
作者: ["@kikitataysi"]
tags: [Codex, Skill, 工具]
status: reference
---

五個讓 OpenAI Codex 體驗升級的必裝 Skill，各有不同專注領域：

---

## 1. awesome-codex-skills

**GitHub**: [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) ⭐ 11,247

Codex Skill 精選大集合。開發 / 生產力 / 寫作 / 數據分析 / 實用工具五大類。

```bash
python skill-installer/scripts/install-skill-from-github.py \
  --repo ComposioHQ/awesome-codex-skills --path <skill-name>
```

## 2. repomix

**GitHub**: [yamadashy/repomix](https://github.com/yamadashy/repomix) ⭐ 25,448

把整個程式碼庫打包成 AI 友善的單一檔案。JSNation 開源獎入圍，Vibe coding 神器。

```bash
npx repomix
```

## 3. follow-builders

**GitHub**: [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) ⭐ 4,699

監控 X/Twitter 上 25 位頂尖 AI builder + 主流 AI podcast，每日/週摘要送到 Telegram/Email。

觸發：說 `/follow-builders` 或「set up follow builders」，Agent 互動式引導設定。

## 4. codex-plusplus

**GitHub**: [b-nnett/codex-plusplus](https://github.com/b-nnett/codex-plusplus) ⭐ 2,172

Codex 桌面應用的 tweak 注入系統。讓程式碼修改即時視覺化，並在 Settings UI 內管理 tweak 的啟停。

```bash
# Codex 內安裝
Inspect & install this for me: https://github.com/b-nnett/codex-plusplus
```

## 5. keep-codex-fast

**GitHub**: [vibeforge1111/keep-codex-fast](https://github.com/vibeforge1111/keep-codex-fast) ⭐ 1,144

重度使用後 Codex 變慢的維護技能。三種模式：Inspect（只報告）/ Maintain（歸檔舊 session、旋轉 log）/ Repair（修復 SQLite 元資料膨脹）。

```text
Use $keep-codex-fast to inspect my Codex local state and recommend a safe maintenance plan.
```

---

## Cross References

- [[Claude 蒸餾 Skill-Set 大禮包]]：Skill 蒸餾與管理方法
- [[技能包大總管]]：Skill 庫治理

---
網址: https://www.threads.com/@jimmyliao/post/DYcnLdrmiGe
作者: ["@jimmyliao"]
tags: [AI, tmux, CLI, Agent, 多 Agent, 工作流程]
status: wiki
source_blog: https://imitation-alpha.github.io/zh-Hant/blog/orchestrating-coding-agents.html
---

## Main Content

這篇很接近我的日常，本來很想將這段設計在教學內，後來發現這真的很看人。
imitation-alpha.github.io/zh-Ha…

> **同時駕馭 10+ 個 CLI 程式設計 agent 的設定方式**
> 作者：Arthur Yau | 2026-04-28 | 閱讀約 8 分鐘

---

## 核心概念

用 tmux + Tailscale + 自訂 PWA 面板，同時管理 Claude Code、Codex、Gemini CLI 等多個 AI Coding Agent，不混亂地處理長任務與快速操作。

**核心哲學：** 「壓縮你和 agent 之間的每個步驟」——降低摩擦才能無壓力地管理十個 agent。

---

## 技術棧

| 工具 | 用途 |
|------|------|
| **tmux** | Terminal 多工，session/window/pane 管理 |
| **Tailscale** | 私有 mesh 網路，不暴露公網 |
| **Termius** | iOS SSH client，行動作業 |
| **自訂 PWA Panel（vmux）** | 集中式 agent 狀態儀表板 |
| Mac: iTerm / Ghostty | 桌面 terminal |

---

## 架構設計

### tmux 結構

- **一個 session = 一個專案**
- Windows 按功能切分：Claude Code / 測試日誌 / 長任務 pipeline / git 操作
- Sessions 在斷線、切換裝置後持續存在

### 網路架構

Mac / iPhone → Tailscale private mesh → 家用伺服器（執行 tmux）

不需 port forwarding，無公網暴露風險。

---

## 關鍵設定細節

### SSH 自動 attach tmux

加到 `~/.bashrc` 或 `~/.zshrc`：

```bash
if [[ -z "$TMUX" && -n "$SSH_CONNECTION" && $- == *i* ]]; then
  tmux attach -t main 2>/dev/null || tmux new -s main
fi
```

Guards 防止 `scp`/`rsync` 時誤觸發。

### Termius 行動操作

重點：底部快捷列（Esc, Ctrl, Tab, 方向鍵, Shift+Tab）讓單手在捷運上也能操作 tmux。

### Session 重開機後持久化

三插件方案（TPM 管理）：

- **tmux-resurrect** — save/restore 快照
- **tmux-continuum** — 每 15 分鐘自動快照，開機自動還原

`~/.tmux.conf.local` 設定：

```
set -g @continuum-save-interval '15'
set -g @continuum-restore 'on'
set -g @resurrect-capture-pane-contents 'on'
```

### 常用 tmux 指令

| 指令 | 功能 |
|------|------|
| `tmux a` | attach 前一個 session |
| `tmux new -s <name>` | 建立新 session |
| `<C-b> z` | 最大化目前 pane |
| `<C-b> s` | session 選擇器 |
| `<C-b> q` | 顯示/跳到 pane 編號 |

---

## 自訂 PWA 控制面板（vmux）

**問題：** 10 個 session 中找哪個 agent 需要注意 → 每次 20 秒 overhead × 一整天 = 巨大損耗。

**功能：**

- 每個 CLI agent session 對應一張卡片
- 依最後互動時間排序
- 狀態指示：working / idle / waiting for input
- 每張卡片顯示專案 tag
- 完成或需要輸入時推播通知
- 直接輸入指令，不需繞路 SSH/tmux
- 廣播模式（多 session 同時下指令，未來功能）

**狀態：** GitHub repo 達 100 stars 後完整開源。

---

## Tailscale 優勢

- 100 台裝置免費
- MagicDNS：`ssh arthur-laptop` 取代 IP 地址
- 家用 Streamlit dashboard 直接用 `http://homebox:8501` 存取，無需 auth 基礎設施

---

## GUI 備援

少數不相容 headless 的工具：Chrome Remote Desktop 或 VNC 綁定到 Tailscale interface（比 SSH 慢，處理約 5% 的任務）。

---

## 安裝步驟概覽（約 20 分鐘）

**tmux：**

```bash
brew install tmux
git clone https://github.com/gpakosz/.tmux.git ~/.tmux
```

**Tailscale：** 官網下載，admin console 啟用 MagicDNS

**Termius：** App Store 安裝 → 加 SSH host → 設定底部快捷列 → 啟用自動重連

**驗證：** Tailscale SSH 連通 → `tmux new -s test` 出現綠色 status bar → detach/reattach 確認持久化

---

## 未來規劃

- 跨 agent 輸出共享（不需 copy-paste）
- 廣播模式（同時對多 session 下 prompt）
- 語音輸入（大眾交通工具場景）

---

## 延伸學習

MIT Missing Semester（2020 & 2026 版）：terminal、shell、tmux 基礎。

---

## Sources

- [我的 AI 日常：多 Agent CLI 設定](https://www.threads.com/@jimmyliao/post/DYcnLdrmiGe) | 作者: jimmyliao
- [同時駕馭 10+ 個 CLI 程式設計 agent 的設定方式](https://imitation-alpha.github.io/zh-Hant/blog/orchestrating-coding-agents.html) | 作者: Arthur Yau

## Cross References

- [[AI 工具-索引]]：AI 工具分類總覽

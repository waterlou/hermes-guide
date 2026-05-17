# Quickstart

Once Hermes Agent is installed and configured, you can start your first conversation immediately.

---

## Start a Conversation

### Classic CLI Mode

```bash
hermes
```

This launches the classic command-line interface. Type your message and press Enter to chat.

### TUI Mode (Recommended)

```bash
hermes --tui
```

The Terminal User Interface provides a richer experience with syntax highlighting, message history navigation, and split-pane views.

---

## Your First Commands

Try these to get familiar with Hermes:

```text
# Ask a question
> What can you do?

# Request a task
> Write a Python script to sort a list of files by modification date

# Use a tool
> Search the web for the latest AI news

# Save the conversation
> /save
```

---

## Resume a Session

If you close Hermes and want to continue where you left off:

```bash
hermes --continue
# or shorthand
hermes -c
```

This loads the last conversation session so you can pick up right where you stopped.

---

## Check System Status

```bash
hermes doctor
```

Use this anytime to verify your configuration, check for updates, or diagnose issues.

---

## Next Steps

- Learn about [Basic Usage](../usage/basic-usage.md) — more commands and workflow tips
- Explore [Slash Commands](../usage/slash-commands.md) — in-chat commands
- Set up [Skills](../advanced/skills.md) — reusable workflows
- Configure [MCP Servers](../advanced/mcp-servers.md) — custom tool integration

---

# 快速入門

安裝並設定 Hermes Agent 後，您就可以立即開始第一次對話。

---

## 開始對話

### 經典 CLI 模式

```bash
hermes
```

啟動經典命令列介面。輸入訊息後按 Enter 即可對話。

### TUI 模式（推薦）

```bash
hermes --tui
```

終端機使用者介面提供更豐富的體驗，包含語法高亮、訊息歷史導覽與分割畫面檢視。

---

## 您的第一個指令

嘗試以下指令來熟悉 Hermes：

```text
# 提問
> 你能做什麼？

# 請求任務
> 寫一個 Python 腳本，依修改日期排序檔案列表

# 使用工具
> 搜尋最新的 AI 新聞

# 儲存對話
> /save
```

---

## 恢復對話

若您關閉 Hermes 後想繼續先前的對話：

```bash
hermes --continue
# 或簡寫
hermes -c
```

此指令會載入上一次的對話記錄，讓您從中斷處繼續。

---

## 檢查系統狀態

```bash
hermes doctor
```

隨時使用此指令來驗證設定、檢查更新或診斷問題。

---

## 下一步

- 了解[基本使用](../usage/basic-usage.md) — 更多指令與工作流程技巧
- 探索[斜線指令](../usage/slash-commands.md) — 對話中的指令
- 設定[技能](../advanced/skills.md) — 可重複使用的工作流程
- 配置 [MCP 伺服器](../advanced/mcp-servers.md) — 自訂工具整合

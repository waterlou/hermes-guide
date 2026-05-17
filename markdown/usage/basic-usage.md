# Basic Usage

This page covers the everyday commands and workflows for using Hermes Agent.

---

## Starting Hermes

```bash
# Standard CLI mode
hermes

# TUI mode (recommended for daily use)
hermes --tui

# Resume last session
hermes --continue
hermes -c
```

---

## Session Management

### Start Fresh

```bash
hermes
```

Each invocation starts a new session unless `--continue` is used.

### Resume a Session

```bash
hermes -c
```

Your last conversation is automatically saved when you exit. Use `-c` to pick up where you left off.

### Save Manually

While in a conversation, type:

```text
/save
```

This saves the current session explicitly.

---

## Configuration Commands

```bash
# Switch provider or model
hermes model

# Run setup wizard
hermes setup

# Set individual config values
hermes config set <key> <value>

# View current configuration
hermes config show
```

---

## Tool Management

```bash
# List available tools
hermes tools

# Enable/disable specific tools
hermes tools enable <tool-name>
hermes tools disable <tool-name>
```

---

## Skills

```bash
# Search for skills
hermes skills search <query>

# Install a skill
hermes skills install <skill-name>

# List installed skills
hermes skills list
```

---

## Updates & Maintenance

```bash
# Update Hermes Agent
hermes update

# Run diagnostics
hermes doctor

# Launch web dashboard (v0.9+)
hermes dashboard
```

---

## Tips for Better Results

1. **Be specific** — Detailed instructions produce better results
2. **Use `/save` regularly** — Don't lose important conversations
3. **Try different models** — Some tasks benefit from specific models
4. **Leverage tools** — Use `/tools` to see what's available
5. **Use `/voice on`** — Enable voice input for hands-free interaction

---

# 基本使用

本頁涵蓋使用 Hermes Agent 的日常指令與工作流程。

---

## 啟動 Hermes

```bash
# 標準 CLI 模式
hermes

# TUI 模式（推薦日常使用）
hermes --tui

# 恢復上次對話
hermes --continue
hermes -c
```

---

## 對話管理

### 開始新對話

```bash
hermes
```

每次執行都會開始新對話，除非使用 `--continue`。

### 恢復對話

```bash
hermes -c
```

上次的對話會在您結束時自動儲存。使用 `-c` 從中斷處繼續。

### 手動儲存

在對話中輸入：

```text
/save
```

明確儲存當前對話。

---

## 設定指令

```bash
# 切換提供者或模型
hermes model

# 執行設定精靈
hermes setup

# 個別設定參數
hermes config set <key> <value>

# 檢視當前設定
hermes config show
```

---

## 工具管理

```bash
# 列出可用工具
hermes tools

# 啟用/停用特定工具
hermes tools enable <tool-name>
hermes tools disable <tool-name>
```

---

## 技能

```bash
# 搜尋技能
hermes skills search <query>

# 安裝技能
hermes skills install <skill-name>

# 列出已安裝技能
hermes skills list
```

---

## 更新與維護

```bash
# 更新 Hermes Agent
hermes update

# 執行診斷
hermes doctor

# 啟動網頁儀表板（v0.9+）
hermes dashboard
```

---

## 使用技巧

1. **具體明確** — 詳細的指令能產生更好的結果
2. **定期使用 `/save`** — 避免遺失重要的對話
3. **嘗試不同模型** — 某些任務適合特定模型
4. **善用工具** — 使用 `/tools` 查看可用工具
5. **使用 `/voice on`** — 啟用語音輸入以實現免持操作

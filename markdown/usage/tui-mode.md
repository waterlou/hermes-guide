# TUI Mode

The Terminal User Interface (TUI) mode provides a modern, rich interface for Hermes Agent with syntax highlighting, split-pane views, and keyboard navigation.

---

## Launching TUI

```bash
hermes --tui
```

You can also set TUI as the default mode by adding it to your configuration:

```bash
hermes config set default_mode tui
```

---

## Interface Layout

The TUI is divided into several panes:

```
┌─────────────────────────────────────────────┐
│  Header           Model: claude-sonnet-4-6   │
├─────────────────────────────────────────────┤
│                                             │
│  Chat Area                                   │
│  • Messages appear here                      │
│  • Syntax-highlighted code blocks            │
│  • Markdown-rendered content                 │
│                                             │
├─────────────────────────────────────────────┤
│  Input Area  > Type your message here...     │
└─────────────────────────────────────────────┘
```

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+N` | New conversation |
| `Ctrl+S` | Save conversation |
| `Ctrl+W` | Close pane |
| `Ctrl+C` | Cancel current response |
| `Tab` | Switch focus between panes |
| `Up/Down` | Navigate message history |
| `PageUp/PageDown` | Scroll through responses |
| `Esc` | Close menu / cancel |
| `/?` | Show help overlay |

---

## Features

### Message History

Scroll through your conversation history with `Up`/`Down` arrow keys. Previous messages are editable — press `Up` on an empty input to recall the last message.

### Syntax Highlighting

Code blocks in responses are highlighted for readability. Supported languages include Python, JavaScript, Bash, YAML, JSON, and many more.

### Split Panes

The TUI can display multiple panes simultaneously — for example, showing a code diff alongside the conversation, or viewing tool output separately.

### Auto-Completion

The input area supports tab-completion for slash commands and file paths.

---

## Tips

1. Use `Ctrl+S` frequently to save your session
2. Use `/?` to view all available keyboard shortcuts
3. Resize the terminal window to adjust pane sizes
4. Combine with `tmux` for persistent sessions

---

# TUI 模式

終端機使用者介面（TUI）模式為 Hermes Agent 提供現代化的豐富介面，具備語法高亮、分割畫面檢視與鍵盤導覽功能。

---

## 啟動 TUI

```bash
hermes --tui
```

您也可以將 TUI 設為預設模式：

```bash
hermes config set default_mode tui
```

---

## 介面配置

TUI 分為數個面板：

```
┌─────────────────────────────────────────────┐
│  標題列         Model: claude-sonnet-4-6     │
├─────────────────────────────────────────────┤
│                                             │
│  對話區域                                    │
│  • 訊息顯示於此                               │
│  • 語法高亮的程式碼區塊                        │
│  • Markdown 渲染內容                         │
│                                             │
├─────────────────────────────────────────────┤
│  輸入區域  > 在此輸入訊息...                   │
└─────────────────────────────────────────────┘
```

---

## 鍵盤快捷鍵

| 按鍵 | 功能 |
|------|------|
| `Ctrl+N` | 新對話 |
| `Ctrl+S` | 儲存對話 |
| `Ctrl+W` | 關閉面板 |
| `Ctrl+C` | 取消當前回應 |
| `Tab` | 切換面板焦點 |
| `上/下` | 瀏覽訊息歷史 |
| `PageUp/PageDown` | 捲動回應內容 |
| `Esc` | 關閉選單 / 取消 |
| `/?` | 顯示輔助說明 |

---

## 功能

### 訊息歷史

使用上/下方向鍵瀏覽對話歷史。可編輯先前的訊息 — 在空白輸入框按下「上」鍵可回叫上一則訊息。

### 語法高亮

回應中的程式碼區塊會進行語法高亮以提升可讀性。支援的語言包含 Python、JavaScript、Bash、YAML、JSON 等。

### 分割面板

TUI 可同時顯示多個面板 — 例如在對話旁顯示程式碼差異，或分別檢視工具輸出。

### 自動補全

輸入區域支援斜線指令與檔案路徑的 Tab 自動補全。

---

## 使用技巧

1. 經常使用 `Ctrl+S` 儲存對話
2. 使用 `/?` 檢視所有鍵盤快捷鍵
3. 調整終端機視窗大小以改變面板配置
4. 搭配 `tmux` 使用以實現持久連線

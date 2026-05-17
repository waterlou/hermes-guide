# Memory System

Hermes Agent features a sophisticated three-tier memory system that enables long-term learning and context retention.

---

## Three-Tier Architecture

### 1. Persistent Facts (Long-Term)

Facts are explicit pieces of information you teach Hermes that persist across sessions.

```text
/help
> Remember that my name is Alice and I prefer concise answers
```

These facts are stored permanently and loaded at the start of every conversation.

### 2. Conversation Recall (Medium-Term)

Hermes automatically indexes past conversations and can recall relevant context when needed.

- Automatic summarization of past sessions
- Semantic search across conversation history
- Configurable retention window

```text
/memory recall what was the project name we discussed last week
```

### 3. Procedural Memory (Short-Term)

Procedural memory tracks the current conversation's context, including:

- Active tools and their states
- Current workflow progress
- Recent messages and decisions
- Temporary variables and state

This is session-specific and cleared when the conversation ends (unless saved).

---

## Memory Commands

```bash
# View memory status
/memory

# Search past conversations
/memory recall <query>

# Add a persistent fact
> Remember that ...

# Clear session memory
/memory forget

# Show memory statistics
/memory stats
```

---

## Configuration

Memory behavior can be configured in `~/.hermes/config.yaml`:

```yaml
memory:
  # Maximum number of past conversations to index
  recall_limit: 100

  # Enable automatic summarization
  auto_summarize: true

  # Retention period in days (0 = forever)
  retention_days: 90

  # Maximum facts stored
  max_facts: 1000
```

---

## Privacy & Control

You have full control over your memory:

- View what Hermes remembers with `/memory`
- Delete specific memories with `/memory forget`
- Disable memory entirely in config
- All memory is stored locally — nothing is sent to external servers

---

# 記憶系統

Hermes Agent 具備精密的四層記憶系統，可實現長期學習與上下文保留。

---

## 三層架構

### 1. 持久事實（長期）

事實是您教導 Hermes 的明確資訊，會在對話之間持續保留。

```text
/help
> 記住我的名字是 Alice，我偏好簡潔的回答
```

這些事實會永久儲存，並在每次對話開始時載入。

### 2. 對話回憶（中期）

Hermes 會自動索引過去的對話，並在需要時回憶相關上下文。

- 自動摘要過去的對話
- 跨對話歷史的語意搜尋
- 可設定的保留期限

```text
/memory recall 我們上週討論的專案名稱是什麼
```

### 3. 程序記憶（短期）

程序記憶追蹤當前對話的上下文，包括：

- 啟用中的工具及其狀態
- 當前工作流程進度
- 最近的訊息與決策
- 暫時變數與狀態

此為對話特定，對話結束時會清除（除非已儲存）。

---

## 記憶指令

```bash
# 檢視記憶狀態
/memory

# 搜尋過去的對話
/memory recall <查詢>

# 新增持久事實
> 記住 ...

# 清除對話記憶
/memory forget

# 顯示記憶統計
/memory stats
```

---

## 設定

記憶行為可在 `~/.hermes/config.yaml` 中設定：

```yaml
memory:
  # 要索引的最大過去對話數
  recall_limit: 100

  # 啟用自動摘要
  auto_summarize: true

  # 保留天數（0 = 永久）
  retention_days: 90

  # 最大事實儲存數
  max_facts: 1000
```

---

## 隱私與控制

您對記憶擁有完全控制權：

- 使用 `/memory` 檢視 Hermes 記住了什麼
- 使用 `/memory forget` 刪除特定記憶
- 在設定中完全停用記憶功能
- 所有記憶都儲存在本機 — 不會傳送至外部伺服器

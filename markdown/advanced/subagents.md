# Subagents

Hermes Agent supports parallel task execution through an orchestrator/worker pattern using sub-agents. This allows complex tasks to be broken down and executed concurrently.

---

## How Subagents Work

```
┌─────────────────────────────────────┐
│          Orchestrator Agent          │
│  • Receives the high-level task      │
│  • Breaks it into subtasks           │
│  • Assigns subtasks to workers       │
│  • Merges results                    │
├────────────┬────────────┬────────────┤
│  Worker 1  │  Worker 2  │  Worker N  │
│  Subtask A │  Subtask B │  Subtask C │
└────────────┴────────────┴────────────┘
```

The orchestrator:
1. Analyzes the main task
2. Identifies independent subtasks
3. Spawns worker agents for each subtask
4. Collects and merges results into a coherent response

---

## When to Use Subagents

Subagents are particularly useful for:

- **Research** — Searching multiple sources simultaneously
- **Code generation** — Writing different modules in parallel
- **Data analysis** — Processing multiple datasets concurrently
- **Document creation** — Writing different sections independently
- **Testing** — Running multiple test suites at once

---

## Enabling Subagents

Subagents can be enabled in the configuration:

```yaml
# ~/.hermes/config.yaml
subagents:
  enabled: true
  max_workers: 5
  timeout: 120  # seconds per worker
```

Or via the CLI:

```bash
hermes config set subagents.enabled true
hermes config set subagents.max_workers 5
```

---

## Controlling Worker Count

```bash
hermes config set subagents.max_workers 3
```

Adjust this based on your system's capabilities and the complexity of your tasks. More workers means faster parallel execution but higher resource usage.

---

## Subagent Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| `enabled` | `true` | Enable subagent orchestration |
| `max_workers` | `5` | Maximum parallel workers |
| `timeout` | `120` | Worker timeout in seconds |
| `model` | *same as main* | Model used for subagents |
| `retry_attempts` | `2` | Number of retries on worker failure |

---

## Tips

1. **Start small** — Begin with 2-3 workers to gauge performance
2. **Set timeouts** — Prevent stuck workers from blocking the entire task
3. **Monitor workers** — Use `/stats` to see worker status
4. **Match models to tasks** — Simple subtasks can use faster, cheaper models
5. **Combine with skills** — Load relevant skills for specialized subtasks

---

# 子代理

Hermes Agent 透過協調者/工作者模式支援子代理並行任務執行。這使得複雜任務可以被分解並同時執行。

---

## 子代理運作方式

```
┌─────────────────────────────────────┐
│           協調者代理                    │
│  • 接收高層級任務                      │
│  • 將任務分解為子任務                   │
│  • 將子任務分配給工作者                 │
│  • 合併結果                           │
├────────────┬────────────┬────────────┤
│  工作者 1   │  工作者 2   │  工作者 N   │
│  子任務 A   │  子任務 B   │  子任務 C   │
└────────────┴────────────┴────────────┘
```

協調者的工作流程：
1. 分析主要任務
2. 識別可獨立執行的子任務
3. 為每個子任務產生工作者代理
4. 收集並合併結果為連貫的回應

---

## 何時使用子代理

子代理特別適用於以下情況：

- **研究** — 同時搜尋多個來源
- **程式碼生成** — 並行編寫不同模組
- **資料分析** — 同時處理多個資料集
- **文件建立** — 獨立編寫不同章節
- **測試** — 同時執行多個測試套件

---

## 啟用子代理

可在設定中啟用子代理：

```yaml
# ~/.hermes/config.yaml
subagents:
  enabled: true
  max_workers: 5
  timeout: 120  # 每個工作者的秒數
```

或透過 CLI：

```bash
hermes config set subagents.enabled true
hermes config set subagents.max_workers 5
```

---

## 控制工作者數量

```bash
hermes config set subagents.max_workers 3
```

根據您的系統能力和任務複雜度調整此數值。更多工作者意味著更快的並行執行速度，但資源消耗也更高。

---

## 子代理設定選項

| 選項 | 預設值 | 說明 |
|------|--------|------|
| `enabled` | `true` | 啟用子代理協調 |
| `max_workers` | `5` | 最大並行工作者數 |
| `timeout` | `120` | 工作者逾時秒數 |
| `model` | *同主模型* | 子代理使用的模型 |
| `retry_attempts` | `2` | 工作者失敗時的重試次數 |

---

## 使用技巧

1. **從小開始** — 先從 2-3 個工作者開始評估效能
2. **設定逾時** — 防止卡住的工作者阻塞整個任務
3. **監控工作者** — 使用 `/stats` 檢視工作者狀態
4. **為任務選擇合適模型** — 簡單的子任務可使用更快、更便宜的模型
5. **結合技能使用** — 為專業子任務載入相關技能

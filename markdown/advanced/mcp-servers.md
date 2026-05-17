# MCP Servers

The Model Context Protocol (MCP) allows Hermes Agent to connect to custom tool servers, extending its capabilities with specialized tools.

---

## What is MCP?

MCP (Model Context Protocol) is an open standard that enables AI agents to connect to external tool servers. With MCP, you can add custom capabilities to Hermes Agent such as:

- Database access
- API integrations
- File system operations
- Custom data processing
- External service connections

---

## Adding an MCP Server

MCP servers are configured in `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  my-database:
    command: python
    args:
      - /path/to/mcp-database-server.py
    env:
      DB_HOST: localhost
      DB_PORT: "5432"

  web-api:
    command: node
    args:
      - /path/to/mcp-api-server.js
    env:
      API_KEY: your-api-key-here
```

---

## MCP Server Configuration Fields

| Field | Required | Description |
|-------|----------|-------------|
| `command` | Yes | Executable to run the server |
| `args` | No | Command-line arguments |
| `env` | No | Environment variables |
| `disabled` | No | Set to `true` to disable without removing |
| `transport` | No | Transport type: `stdio` (default) or `sse` |

---

## Example: Filesystem MCP Server

```yaml
mcp_servers:
  filesystem:
    command: npx
    args:
      - -y
      - @modelcontextprotocol/server-filesystem
      - /path/to/allowed/directory
```

---

## Finding MCP Servers

You can find community MCP servers from:

- **Official MCP repository**: [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- **Community registries**: Various open-source directories
- **Custom servers**: Write your own using any language that supports stdio or SSE

---

## Writing a Custom MCP Server

Minimal Python example:

```python
import sys
import json

def handle_request(request):
    if request["method"] == "tools/list":
        return {
            "tools": [
                {
                    "name": "greet",
                    "description": "Greet a user",
                    "input_schema": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"}
                        }
                    }
                }
            ]
        }
    elif request["method"] == "tools/call":
        if request["params"]["name"] == "greet":
            name = request["params"]["arguments"]["name"]
            return {"content": f"Hello, {name}!"}

    return {"error": "unknown method"}

for line in sys.stdin:
    request = json.loads(line)
    response = handle_request(request)
    sys.stdout.write(json.dumps(response) + "\n")
    sys.stdout.flush()
```

---

## Managing MCP Servers via CLI

```bash
# List configured MCP servers
hermes tools

# The MCP tools will appear in the tool list when the server is running
```

---

# MCP 伺服器

模型上下文協定（MCP）允許 Hermes Agent 連線至自訂工具伺服器，透過專用工具擴展其功能。

---

## 什麼是 MCP？

MCP（Model Context Protocol）是一種開放標準，讓 AI 代理能夠連線至外部工具伺服器。透過 MCP，您可以為 Hermes Agent 新增自訂功能，例如：

- 資料庫存取
- API 整合
- 檔案系統操作
- 自訂資料處理
- 外部服務連線

---

## 新增 MCP 伺服器

MCP 伺服器在 `~/.hermes/config.yaml` 中設定：

```yaml
mcp_servers:
  my-database:
    command: python
    args:
      - /path/to/mcp-database-server.py
    env:
      DB_HOST: localhost
      DB_PORT: "5432"

  web-api:
    command: node
    args:
      - /path/to/mcp-api-server.js
    env:
      API_KEY: your-api-key-here
```

---

## MCP 伺服器設定欄位

| 欄位 | 必填 | 說明 |
|------|------|------|
| `command` | 是 | 執行伺服器的可執行檔 |
| `args` | 否 | 命令列參數 |
| `env` | 否 | 環境變數 |
| `disabled` | 否 | 設為 `true` 可停用而不移除 |
| `transport` | 否 | 傳輸類型：`stdio`（預設）或 `sse` |

---

## 範例：檔案系統 MCP 伺服器

```yaml
mcp_servers:
  filesystem:
    command: npx
    args:
      - -y
      - @modelcontextprotocol/server-filesystem
      - /path/to/allowed/directory
```

---

## 尋找 MCP 伺服器

您可以從以下來源找到社群 MCP 伺服器：

- **官方 MCP 儲存庫**：[github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- **社群註冊表**：各種開源目錄
- **自訂伺服器**：使用任何支援 stdio 或 SSE 的語言自行編寫

---

## 編寫自訂 MCP 伺服器

最小 Python 範例：

```python
import sys
import json

def handle_request(request):
    if request["method"] == "tools/list":
        return {
            "tools": [
                {
                    "name": "greet",
                    "description": "向使用者打招呼",
                    "input_schema": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"}
                        }
                    }
                }
            ]
        }
    elif request["method"] == "tools/call":
        if request["params"]["name"] == "greet":
            name = request["params"]["arguments"]["name"]
            return {"content": f"你好, {name}!"}

    return {"error": "unknown method"}

for line in sys.stdin:
    request = json.loads(line)
    response = handle_request(request)
    sys.stdout.write(json.dumps(response) + "\n")
    sys.stdout.flush()
```

---

## 透過 CLI 管理 MCP 伺服器

```bash
# 列出已設定的 MCP 伺服器
hermes tools

# MCP 工具會在伺服器執行時顯示在工具列表中
```

# Configuration

After installing Hermes Agent, you need to configure your LLM provider and API keys before you can start using it.

---

## Choose Your Provider

Run the provider/model selection command:

```bash
hermes model
```

This opens an interactive prompt where you can choose from supported providers.

### Supported Providers

| Provider | Command | Notes |
|----------|---------|-------|
| **Nous Portal** | Built-in | Comes with free credits, tool gateway included |
| **Anthropic** | `hermes model` | Claude models — requires API key |
| **OpenAI** | `hermes model` | GPT-4o, GPT-4, o-series — requires API key |
| **Google Gemini** | `hermes model` | Gemini models — requires API key |
| **xAI (Grok)** | `hermes model` | Grok models — requires API key |
| **DeepSeek** | `hermes model` | DeepSeek-V3, R1 — requires API key |
| **Alibaba Cloud** | `hermes model` | Qwen models — requires API key |
| **OpenRouter** | `hermes model` | 200+ models, one API key |
| **Groq** | `hermes model` | Fast inference models |
| **Cerebras** | `hermes model` | Fast inference models |

> **Minimum requirement**: All providers must support at least **64K token** context windows.

---

## Setup Wizard

The setup wizard guides you through the full configuration process:

```bash
hermes setup
```

This walks through:
1. **Provider selection** — Choose your primary LLM provider
2. **API key entry** — Enter your API key(s)
3. **Optional integrations** — Configure gateway platforms (Telegram, Discord)
4. **Tool settings** — Enable/disable built-in tools
5. **Memory configuration** — Set up memory persistence

---

## Manual Configuration

You can also configure settings individually:

```bash
hermes config set <key> <value>
```

### Common Configuration Keys

| Key | Description | Example Value |
|-----|-------------|---------------|
| `provider` | LLM provider | `anthropic` |
| `model` | Model name | `claude-sonnet-4-6` |
| `api_key` | API key for the provider | `sk-ant-...` |
| `temperature` | Response creativity (0-1) | `0.7` |
| `max_tokens` | Maximum response tokens | `4096` |

---

## Configuration File Location

Hermes Agent stores its configuration in `~/.hermes/config.yaml`. You can edit this file directly if you prefer:

```yaml
# ~/.hermes/config.yaml example
provider: anthropic
model: claude-sonnet-4-6
api_key: sk-ant-...
temperature: 0.7
max_tokens: 4096
tools:
  - web_search
  - file_system
  - code_interpreter
```

---

## Gateway Setup

To connect Hermes Agent to messaging platforms:

```bash
hermes gateway setup
```

Available gateways:
- **Telegram** — Chat with Hermes via Telegram bot
- **Discord** — Invite Hermes to your Discord server
- **Custom** — Webhook-based integration

Each gateway requires platform-specific tokens/bot credentials which you obtain from the platform's developer console.

---

## Verifying Configuration

Check if your configuration is valid:

```bash
hermes doctor
```

This runs a full diagnostic and reports any issues with your setup.

---

# 設定與配置

安裝 Hermes Agent 後，您需要設定 LLM 提供者與 API 金鑰才能開始使用。

---

## 選擇提供者

執行提供者/模型選擇指令：

```bash
hermes model
```

此指令會開啟互動式提示，讓您從支援的提供者中選擇。

### 支援的提供者

| 提供者 | 指令 | 備註 |
|--------|------|------|
| **Nous Portal** | 內建 | 附贈免費額度，包含工具閘道 |
| **Anthropic** | `hermes model` | Claude 模型 — 需要 API 金鑰 |
| **OpenAI** | `hermes model` | GPT-4o、GPT-4、o 系列 — 需要 API 金鑰 |
| **Google Gemini** | `hermes model` | Gemini 模型 — 需要 API 金鑰 |
| **xAI（Grok）** | `hermes model` | Grok 模型 — 需要 API 金鑰 |
| **DeepSeek** | `hermes model` | DeepSeek-V3、R1 — 需要 API 金鑰 |
| **阿里雲** | `hermes model` | Qwen 模型 — 需要 API 金鑰 |
| **OpenRouter** | `hermes model` | 200+ 模型，單一 API 金鑰 |
| **Groq** | `hermes model` | 快速推論模型 |
| **Cerebras** | `hermes model` | 快速推論模型 |

> **最低需求**：所有提供者須支援至少 **64K token** 的上下文視窗。

---

## 設定精靈

設定精靈會引導您完成完整的設定流程：

```bash
hermes setup
```

此精靈會引導：
1. **提供者選擇** — 選擇您的主要 LLM 提供者
2. **API 金鑰輸入** — 輸入您的 API 金鑰
3. **選擇性整合** — 設定閘道平台（Telegram、Discord）
4. **工具設定** — 啟用/停用內建工具
5. **記憶體設定** — 設定持久記憶

---

## 手動設定

您也可以個別設定參數：

```bash
hermes config set <key> <value>
```

### 常用設定參數

| 參數 | 說明 | 範例值 |
|------|------|--------|
| `provider` | LLM 提供者 | `anthropic` |
| `model` | 模型名稱 | `claude-sonnet-4-6` |
| `api_key` | API 金鑰 | `sk-ant-...` |
| `temperature` | 回應創意度 (0-1) | `0.7` |
| `max_tokens` | 最大回應 token 數 | `4096` |

---

## 設定檔位置

Hermes Agent 將設定儲存在 `~/.hermes/config.yaml`。您也可以直接編輯此檔案：

```yaml
# ~/.hermes/config.yaml 範例
provider: anthropic
model: claude-sonnet-4-6
api_key: sk-ant-...
temperature: 0.7
max_tokens: 4096
tools:
  - web_search
  - file_system
  - code_interpreter
```

---

## 閘道設定

將 Hermes Agent 連線至訊息平台：

```bash
hermes gateway setup
```

可用的閘道：
- **Telegram** — 透過 Telegram 機器人與 Hermes 對話
- **Discord** — 邀請 Hermes 至您的 Discord 伺服器
- **自訂** — 基於 Webhook 的整合

每個閘道需要平台特定的權杖/機器人憑證，請從平台的開發者控制台取得。

---

## 驗證設定

檢查設定是否有效：

```bash
hermes doctor
```

此指令會執行完整診斷並回報任何設定問題。

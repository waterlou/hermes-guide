# Hermes Agent Guide

Hermes Agent is an **open-source, self-evolving AI agent** by Nous Research. It features autonomous learning loops, persistent memory, multi-tool integration, and cross-platform support — all under the MIT license.

Built with Python, Hermes Agent goes beyond simple chat: it remembers past conversations, learns from its interactions, and can orchestrate sub-agents to tackle complex tasks in parallel.

---

## Key Features

- **Self-Evolving** — Improves through autonomous learning loops
- **Persistent Memory** — Three-tier memory system (facts, recall, procedural)
- **Multi-Platform** — CLI, TUI, Telegram, Discord, and web dashboard
- **Tool Ecosystem** — MCP server integration, custom skills, gateway messaging
- **Sub-Agent Orchestration** — Parallel task execution with worker agents
- **Broad LLM Support** — Claude, GPT, Gemini, Grok, DeepSeek, OpenRouter, and more

---

## Quick Links

- [Installation Guide](getting-started/installation.md)
- [Configuration & Setup](getting-started/configuration.md)
- [Quickstart](getting-started/quickstart.md)
- [Basic Usage](usage/basic-usage.md)
- [Troubleshooting](troubleshooting.md)
- [FAQ](faq.md)

---

## Supported Providers

| Provider | Models |
|----------|--------|
| **Nous Portal** | Built-in tool gateway |
| **Anthropic** | Claude 4 Opus, Sonnet, Haiku |
| **OpenAI** | GPT-4o, GPT-4, o-series |
| **Google** | Gemini 2.0 Pro, Flash |
| **xAI** | Grok-2, Grok-3 |
| **DeepSeek** | DeepSeek-V3, R1 |
| **Alibaba Cloud** | Qwen-Max, Qwen-Turbo |
| **OpenRouter** | 200+ models across providers |
| **Groq** | Llama, Mixtral (fast inference) |
| **Cerebras** | Fast inference models |

Minimum context window requirement: **64K tokens**

---

## License

Hermes Agent is released under the **MIT License**.

---

# Hermes Agent 指南

Hermes Agent 是由 Nous Research 開發的**開源自進化 AI 代理**。具備自主學習循環、持久記憶、多工具整合與跨平台支援，採用 MIT 授權。

Hermes Agent 以 Python 建構，不僅能進行對話，還能記住過往對話、從互動中學習，並可編排子代理並行處理複雜任務。

---

## 主要功能

- **自我進化** — 透過自主學習循環持續改進
- **持久記憶** — 三層記憶系統（事實、回憶、程序）
- **多平台支援** — CLI、TUI、Telegram、Discord、網頁儀表板
- **工具生態系** — MCP 伺服器整合、自訂技能、閘道訊息
- **子代理編排** — 並行任務執行與工作代理
- **廣泛 LLM 支援** — Claude、GPT、Gemini、Grok、DeepSeek、OpenRouter 等

---

## 快速連結

- [安裝指南](getting-started/installation.md)
- [設定與配置](getting-started/configuration.md)
- [快速入門](getting-started/quickstart.md)
- [基本使用](usage/basic-usage.md)
- [疑難排解](troubleshooting.md)
- [常見問題](faq.md)

---

## 支援的提供者

| 提供者 | 模型 |
|--------|------|
| **Nous Portal** | 內建工具閘道 |
| **Anthropic** | Claude 4 Opus、Sonnet、Haiku |
| **OpenAI** | GPT-4o、GPT-4、o 系列 |
| **Google** | Gemini 2.0 Pro、Flash |
| **xAI** | Grok-2、Grok-3 |
| **DeepSeek** | DeepSeek-V3、R1 |
| **阿里雲** | Qwen-Max、Qwen-Turbo |
| **OpenRouter** | 跨 200+ 模型 |
| **Groq** | Llama、Mixtral（快速推論） |
| **Cerebras** | 快速推論模型 |

最低上下文視窗需求：**64K tokens**

---

## 授權

Hermes Agent 採用 **MIT 授權**釋出。

# FAQ

## General

### What is Hermes Agent?

Hermes Agent is an open-source, self-evolving AI agent by Nous Research. It features autonomous learning loops, persistent memory, multi-tool integration, and cross-platform support.

### Is Hermes Agent free?

Yes, Hermes Agent is open-source under the MIT License and free to use. You only pay for the LLM API usage based on your chosen provider's pricing.

### Do I need powerful hardware?

No. Hermes Agent runs on standard hardware — the heavy computation happens on the LLM provider's servers. Any modern laptop or desktop can run it.

---

## Installation

### Does Hermes Agent work on Windows?

Not natively, but it works on **WSL2** (Windows Subsystem for Linux). Install WSL2 on Windows, then run the one-line install command inside the WSL2 terminal.

### Can I install Hermes Agent on a server?

Yes. The installation works on Linux servers. You can run it in a `tmux` or `screen` session for persistent access, or set up the gateway for remote interaction.

### Do I need Docker?

No. The installer sets up everything directly on your system. Docker is not required.

---

## Configuration

### Can I use multiple providers at the same time?

You can switch between providers but only one is active at a time. Use `hermes model` to switch. However, sub-agents can be configured to use a different model than the orchestrator.

### What is the minimum context window required?

**64K tokens**. Providers with smaller context windows are not supported.

### How do I switch models mid-conversation?

Use the `/model` slash command during a conversation to switch models interactively.

---

## Usage

### Is my conversation data private?

Yes. Conversations are stored locally on your machine. Hermes Agent does not send your conversation data to any server other than the LLM provider you configured for inference.

### How do I save a conversation?

Type `/save` during a conversation, or exit normally (sessions are auto-saved). Use `hermes -c` to resume.

### Can I use Hermes Agent offline?

No. Hermes Agent requires an internet connection to communicate with LLM provider APIs.

### How many conversations can I have?

There is no hard limit. Memory and storage on your machine are the only constraints.

---

## Technical

### What programming languages does Hermes Agent support?

Hermes Agent can write and understand code in any programming language through its LLM capabilities. The tool system supports Python, JavaScript, Bash, and more for code execution.

### Can I write my own tools?

Yes. Through the MCP (Model Context Protocol), you can create custom tool servers in any language.

### Does Hermes Agent support streaming responses?

Yes. Both CLI and TUI modes support streaming, showing responses as they are generated.

---

## Updates

### How often is Hermes Agent updated?

The project is actively maintained. Check for updates with `hermes update`.

### Will updating break my configuration?

No. Updates preserve your configuration file. However, you should check release notes for any breaking changes before updating.

---

# 常見問題

## 一般問題

### Hermes Agent 是什麼？

Hermes Agent 是由 Nous Research 開發的開源自進化 AI 代理。具備自主學習循環、持久記憶、多工具整合與跨平台支援。

### Hermes Agent 是免費的嗎？

是的，Hermes Agent 採用 MIT 授權開源且免費使用。您只需根據所選提供者的定價支付 LLM API 使用費用。

### 我需要強大的硬體嗎？

不需要。Hermes Agent 可在標準硬體上執行 — 大量計算發生在 LLM 提供者的伺服器上。任何現代筆記型電腦或桌上型電腦都可執行。

---

## 安裝

### Hermes Agent 可以在 Windows 上執行嗎？

不支援原生 Windows，但可在 **WSL2**（Windows Subsystem for Linux）上執行。在 Windows 上安裝 WSL2，然後在 WSL2 終端機中執行一鍵安裝指令。

### 我可以在伺服器上安裝 Hermes Agent 嗎？

可以。安裝程式適用於 Linux 伺服器。您可以在 `tmux` 或 `screen` 會話中執行以實現持久存取，或設定閘道進行遠端互動。

### 我需要 Docker 嗎？

不需要。安裝程式會直接在您的系統上設定一切，無需 Docker。

---

## 設定

### 我可以同時使用多個提供者嗎？

您可以切換提供者，但一次只能啟用一個。使用 `hermes model` 進行切換。不過，子代理可以設定使用與協調者不同的模型。

### 最低上下文視窗需求是多少？

**64K tokens**。不支援上下文視窗較小的提供者。

### 如何在對話中切換模型？

在對話中使用 `/model` 斜線指令即可互動式切換模型。

---

## 使用

### 我的對話資料隱私嗎？

是的。對話儲存在您的本機機器上。Hermes Agent 不會將您的對話資料傳送至除您設定的 LLM 提供者以外的任何伺服器。

### 如何儲存對話？

在對話中輸入 `/save`，或正常結束（對話會自動儲存）。使用 `hermes -c` 恢復。

### 我可以離線使用 Hermes Agent 嗎？

不可以。Hermes Agent 需要網路連線才能與 LLM 提供者的 API 通訊。

### 可以有多少個對話？

沒有嚴格限制。唯一限制是您機器上的記憶體和儲存空間。

---

## 技術問題

### Hermes Agent 支援哪些程式語言？

Hermes Agent 可透過其 LLM 能力以任何程式語言編寫和理解程式碼。工具系統支援 Python、JavaScript、Bash 等語言的程式碼執行。

### 我可以編寫自己的工具嗎？

可以。透過 MCP（模型上下文協定），您可以使用任何語言建立自訂工具伺服器。

### Hermes Agent 支援串流回應嗎？

支援。CLI 和 TUI 模式都支援串流，在產生回應時即時顯示。

---

## 更新

### Hermes Agent 多長時間更新一次？

該專案正在積極維護中。使用 `hermes update` 檢查更新。

### 更新會破壞我的設定嗎？

不會。更新會保留您的設定檔。不過，您應在更新前查看發行說明以了解任何重大變更。

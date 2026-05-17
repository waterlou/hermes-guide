# Gateway Integration

Hermes Agent can connect to messaging platforms through its gateway system, allowing you to interact from Telegram, Discord, and other platforms.

---

## Available Gateways

| Platform | Status | Features |
|----------|--------|----------|
| **Telegram** | ✅ Stable | Bot integration, voice messages |
| **Discord** | ✅ Stable | Server invite, channel integration |
| **Web Dashboard** | 🚧 v0.9+ | Browser-based interface |

---

## Gateway Setup

```bash
hermes gateway setup
```

This interactive wizard guides you through configuring each gateway.

---

## Telegram Setup

### 1. Create a Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` and follow the instructions
3. Copy the bot token you receive

### 2. Configure Hermes

```bash
hermes gateway setup
```

Select **Telegram** and paste your bot token when prompted.

### 3. Start Chatting

Search for your bot on Telegram and send `/start`. You can now interact with Hermes Agent through Telegram.

---

## Discord Setup

### 1. Create a Discord Application

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application** and give it a name
3. Go to the **Bot** section and click **Add Bot**
4. Copy the bot token

### 2. Configure Hermes

```bash
hermes gateway setup
```

Select **Discord** and paste your bot token when prompted.

### 3. Invite to Server

Use the OAuth2 URL generator in the Discord Developer Portal to create an invite link with the necessary bot permissions. Use this link to invite your bot to your server.

---

## Gateway Commands

```bash
# Check gateway status
/gateway status

# Reconnect gateways
/gateway reconnect
```

---

## Gateway Configuration

Gateways are configured in `~/.hermes/config.yaml`:

```yaml
gateway:
  telegram:
    enabled: true
    bot_token: "your-telegram-bot-token"

  discord:
    enabled: true
    bot_token: "your-discord-bot-token"
    server_id: "your-server-id"
```

---

## Security Considerations

- **Bot tokens are sensitive** — treat them like passwords
- **Never commit tokens** to version control
- **Use environment variables** for production deployments
- **Set permissions** on your messaging platforms appropriately
- **Monitor bot activity** for unexpected usage

---

# 閘道整合

Hermes Agent 可透過其閘道系統連線至訊息平台，讓您從 Telegram、Discord 及其他平台進行互動。

---

## 可用閘道

| 平台 | 狀態 | 功能 |
|------|------|------|
| **Telegram** | ✅ 穩定 | 機器人整合、語音訊息 |
| **Discord** | ✅ 穩定 | 伺服器邀請、頻道整合 |
| **網頁儀表板** | 🚧 v0.9+ | 瀏覽器介面 |

---

## 閘道設定

```bash
hermes gateway setup
```

此互動式精靈會引導您完成每個閘道的設定。

---

## Telegram 設定

### 1. 建立 Telegram 機器人

1. 開啟 Telegram 並搜尋 **@BotFather**
2. 傳送 `/newbot` 並依照指示操作
3. 複製您收到的機器人權杖

### 2. 設定 Hermes

```bash
hermes gateway setup
```

選擇 **Telegram** 並在提示時貼上您的機器人權杖。

### 3. 開始對話

在 Telegram 上搜尋您的機器人並傳送 `/start`。您現在可以透過 Telegram 與 Hermes Agent 互動。

---

## Discord 設定

### 1. 建立 Discord 應用程式

1. 前往 [Discord Developer Portal](https://discord.com/developers/applications)
2. 點擊 **New Application** 並命名
3. 前往 **Bot** 區塊並點擊 **Add Bot**
4. 複製機器人權杖

### 2. 設定 Hermes

```bash
hermes gateway setup
```

選擇 **Discord** 並在提示時貼上您的機器人權杖。

### 3. 邀請至伺服器

使用 Discord Developer Portal 中的 OAuth2 URL 產生器，建立具備必要機器人權限的邀請連結。使用此連結將您的機器人邀請至伺服器。

---

## 閘道指令

```bash
# 檢查閘道狀態
/gateway status

# 重新連線閘道
/gateway reconnect
```

---

## 閘道設定

閘道在 `~/.hermes/config.yaml` 中設定：

```yaml
gateway:
  telegram:
    enabled: true
    bot_token: "your-telegram-bot-token"

  discord:
    enabled: true
    bot_token: "your-discord-bot-token"
    server_id: "your-server-id"
```

---

## 安全考量

- **機器人權杖是敏感的** — 請像密碼一樣妥善保管
- **切勿將權杖提交** 至版本控制系統
- **使用環境變數** 進行生產環境部署
- **適當設定權限** 在您的訊息平台上
- **監控機器人活動** 以發現異常使用情況

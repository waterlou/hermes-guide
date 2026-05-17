# Troubleshooting

Common issues you might encounter with Hermes Agent and how to resolve them.

---

## Installation Issues

### `hermes: command not found`

**Solution**: Reload your shell configuration:

```bash
source ~/.bashrc   # bash
source ~/.zshrc    # zsh
```

If the command is still not found, check if the installer completed successfully. The `hermes` command should be in `~/.local/bin/`. Add it to your PATH if needed:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Permission Denied During Installation

**Solution**: Do NOT run the installer with `sudo`. The installer handles permissions automatically. If you're seeing permission errors, ensure your user has write access to the home directory.

### Network Timeout During Installation

**Solution**: Check your internet connection. If you're behind a corporate firewall or proxy:

```bash
# Set proxy environment variables
export HTTP_PROXY=http://proxy:port
export HTTPS_PROXY=http://proxy:port

# Then run the installer
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

---

## Configuration Issues

### "API key not set" Error

**Solution**: Configure your API key using the model selection command:

```bash
hermes model
```

Or set it directly:

```bash
hermes config set api_key <your-api-key>
```

### Empty or Broken Responses

**Solution**: The provider or model configuration may be incorrect. Re-run the model setup:

```bash
hermes model
```

Select your provider again and ensure the API key is correct.

### Provider Not Listed

**Solution**: Run `hermes update` to ensure you have the latest version, which may include new providers.

---

## Runtime Issues

### Gateway Won't Start

**Solution**: Re-run the gateway setup:

```bash
hermes gateway setup
```

Ensure your bot tokens are correct and that your messaging platform's API is accessible.

### Slow Responses

Possible causes and solutions:

| Cause | Solution |
|-------|----------|
| Large context window | Start a new session with `hermes` (without `-c`) |
| Complex tool calls | Check active tools with `/tools` and disable unused ones |
| Network latency | Check your internet connection |
| Model overload | Switch to a faster model with `/model` |

### Memory Issues

If Hermes seems to forget context:

1. Check memory status with `/memory`
2. Verify `auto_summarize` is enabled in config
3. Ensure `recall_limit` is set appropriately
4. Use `/save` to persist important conversations

---

## Diagnostic Tool

Always start with the built-in diagnostic tool:

```bash
hermes doctor
```

This checks:
- Installation integrity
- Configuration validity
- Provider connectivity
- Tool availability
- Memory system status
- Gateway connections

---

## Getting Help

If the above doesn't resolve your issue:

1. **GitHub Issues**: [github.com/NousResearch/hermes-agent/issues](https://github.com/NousResearch/hermes-agent/issues)
2. **Run `hermes doctor`** and include the output in your report
3. **Check for updates**: `hermes update`

---

# 疑難排解

您在使用 Hermes Agent 時可能遇到的常見問題及其解決方法。

---

## 安裝問題

### `hermes: command not found`

**解決方法**：重新載入 shell 設定：

```bash
source ~/.bashrc   # bash
source ~/.zshrc    # zsh
```

若指令仍未找到，請檢查安裝程式是否成功完成。`hermes` 指令應位於 `~/.local/bin/`。如有需要，請將其加入 PATH：

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### 安裝時權限不足

**解決方法**：請勿使用 `sudo` 執行安裝程式。安裝程式會自動處理權限。若看到權限錯誤，請確保您的使用者帳號對家目錄有寫入權限。

### 安裝時網路超時

**解決方法**：檢查您的網路連線。若您在公司防火牆或代理伺服器後方：

```bash
# 設定代理環境變數
export HTTP_PROXY=http://proxy:port
export HTTPS_PROXY=http://proxy:port

# 然後執行安裝程式
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

---

## 設定問題

### 「API key not set」錯誤

**解決方法**：使用模型選擇指令設定 API 金鑰：

```bash
hermes model
```

或直接設定：

```bash
hermes config set api_key <your-api-key>
```

### 空白或異常回應

**解決方法**：提供者或模型設定可能不正確。重新執行模型設定：

```bash
hermes model
```

重新選擇您的提供者並確認 API 金鑰正確。

### 提供者未列出

**解決方法**：執行 `hermes update` 以確保您使用的是最新版本，新版本可能包含新的提供者。

---

## 執行問題

### 閘道無法啟動

**解決方法**：重新執行閘道設定：

```bash
hermes gateway setup
```

確保您的機器人權杖正確，且訊息平台的 API 可存取。

### 回應緩慢

可能原因與解決方案：

| 原因 | 解決方案 |
|------|---------|
| 上下文視窗過大 | 使用 `hermes`（不加 `-c`）開始新對話 |
| 複雜的工具呼叫 | 使用 `/tools` 檢查啟用中的工具並停用不需要的 |
| 網路延遲 | 檢查您的網路連線 |
| 模型負載過高 | 使用 `/model` 切換至更快的模型 |

### 記憶問題

若 Hermes 似乎忘記了上下文：

1. 使用 `/memory` 檢查記憶狀態
2. 確認設定中已啟用 `auto_summarize`
3. 確保 `recall_limit` 設定適當
4. 使用 `/save` 保存重要的對話

---

## 診斷工具

請始終從內建的診斷工具開始：

```bash
hermes doctor
```

此工具會檢查：
- 安裝完整性
- 設定有效性
- 提供者連線能力
- 工具可用性
- 記憶系統狀態
- 閘道連線

---

## 取得協助

若上述方法無法解決您的問題：

1. **GitHub Issues**：[github.com/NousResearch/hermes-agent/issues](https://github.com/NousResearch/hermes-agent/issues)
2. **執行 `hermes doctor`** 並將輸出內容包含在您的報告中
3. **檢查更新**：`hermes update`

# Installation Guide

## Prerequisites

- **Linux, macOS, or WSL2** (native Windows is not supported)
- **Git** (the only required prerequisite)
- Internet connection

---

## One-Line Install

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### What the Installer Does

- Installs **uv** (fast Python package manager)
- Installs **Python 3.11** (via uv)
- Installs **Node.js v22**
- Installs **ripgrep** (fast file search)
- Installs **ffmpeg** (audio/video conversion)
- Clones the Hermes Agent repository
- Sets up a Python virtual environment
- Creates the global `hermes` command

---

## Post-Installation

Reload your shell to make the `hermes` command available:

```bash
source ~/.bashrc   # for bash
# or
source ~/.zshrc    # for zsh
```

Verify the installation:

```bash
hermes --version
```

---

## Updating

To update Hermes Agent to the latest version:

```bash
hermes update
```

This pulls the latest changes from the repository and rebuilds the environment.

---

## Platform-Specific Notes

### macOS

The installer works with both Intel and Apple Silicon (M1/M2/M3/M4) Macs. If you encounter permission issues, ensure you have Xcode Command Line Tools installed:

```bash
xcode-select --install
```

### Linux

Most Linux distributions work out of the box. Common dependencies (curl, git) should be installed via your package manager if missing:

```bash
# Debian / Ubuntu
sudo apt install curl git

# Fedora
sudo dnf install curl git

# Arch
sudo pacman -S curl git
```

### WSL2 (Windows)

1. Install WSL2 on Windows
2. Launch your WSL2 terminal
3. Run the one-line install command

### Termux (Android)

The installer supports Android via Termux. Ensure Termux is updated:

```bash
pkg update && pkg upgrade
```

Then run the one-line install.

---

## Troubleshooting Installation

| Issue | Solution |
|-------|----------|
| `hermes: command not found` | Run `source ~/.bashrc` or `source ~/.zshrc` |
| Permission denied | Avoid running with `sudo` — the installer handles permissions |
| Network timeout | Check your internet connection; use a proxy if needed |
| Python version conflict | The installer uses `uv` to manage Python versions independently |

For further help, run `hermes doctor` after installation or check the [Troubleshooting](../troubleshooting.md) page.

---

# 安裝指南

## 系統需求

- **Linux、macOS 或 WSL2**（不支援原生 Windows）
- **Git**（唯一必要的先決條件）
- 網路連線

---

## 一鍵安裝

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### 安裝程式會自動執行

- 安裝 **uv**（快速 Python 套件管理器）
- 安裝 **Python 3.11**（透過 uv）
- 安裝 **Node.js v22**
- 安裝 **ripgrep**（快速檔案搜尋）
- 安裝 **ffmpeg**（音訊/視訊轉換）
- 克隆 Hermes Agent 儲存庫
- 設定 Python 虛擬環境
- 建立全域 `hermes` 指令

---

## 安裝後設定

重新載入 shell 以使用 `hermes` 指令：

```bash
source ~/.bashrc   # 針對 bash
# 或
source ~/.zshrc    # 針對 zsh
```

驗證安裝是否成功：

```bash
hermes --version
```

---

## 更新

更新 Hermes Agent 至最新版本：

```bash
hermes update
```

此指令會從儲存庫拉取最新變更並重建環境。

---

## 平台特定說明

### macOS

安裝程式同時支援 Intel 與 Apple Silicon（M1/M2/M3/M4）Mac。若遇到權限問題，請先安裝 Xcode Command Line Tools：

```bash
xcode-select --install
```

### Linux

多數 Linux 發行版可直接使用。若缺少相依套件，請透過套件管理器安裝：

```bash
# Debian / Ubuntu
sudo apt install curl git

# Fedora
sudo dnf install curl git

# Arch
sudo pacman -S curl git
```

### WSL2（Windows）

1. 在 Windows 上安裝 WSL2
2. 啟動 WSL2 終端機
3. 執行一鍵安裝指令

### Termux（Android）

安裝程式支援 Android 的 Termux。請先更新 Termux：

```bash
pkg update && pkg upgrade
```

然後執行一鍵安裝。

---

## 安裝疑難排解

| 問題 | 解決方案 |
|------|---------|
| `hermes: command not found` | 執行 `source ~/.bashrc` 或 `source ~/.zshrc` |
| 權限不足 | 避免使用 `sudo` 執行 — 安裝程式會處理權限 |
| 網路超時 | 檢查網路連線；必要時使用代理 |
| Python 版本衝突 | 安裝程式使用 `uv` 獨立管理 Python 版本 |

若需進一步協助，請在安裝後執行 `hermes doctor` 或參閱[疑難排解](../troubleshooting.md)頁面。

# Skills

Skills are reusable workflows that extend Hermes Agent's capabilities. They package instructions, tools, and configurations into shareable modules.

---

## Skill Commands

```bash
# Search for community skills
hermes skills search <query>

# Install a skill
hermes skills install <skill-name>

# List installed skills
hermes skills list

# Remove a skill
hermes skills remove <skill-name>

# Show skill details
hermes skills info <skill-name>
```

---

## Installing Skills

### From the Community Repository

```bash
hermes skills search code review
hermes skills install code-reviewer
```

### From a Local File

```bash
hermes skills install ./my-skill.yaml
```

### From a URL

```bash
hermes skills install https://example.com/skills/my-skill.yaml
```

---

## Creating Custom Skills

Skills are defined in YAML files. Here's a minimal example:

```yaml
# ~/.hermes/skills/my-skill.yaml
name: my-skill
description: A custom skill for my workflow
version: "1.0"

instructions: |
  When asked to perform this task, follow these steps:
  1. Analyze the input
  2. Apply the workflow
  3. Return the result

tools:
  - file_system
  - code_interpreter
```

### Skill Structure

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier for the skill |
| `description` | Yes | Short description shown in listings |
| `version` | No | Semantic version string |
| `instructions` | Yes | System prompt or instructions for the agent |
| `tools` | No | List of tools the skill requires |
| `author` | No | Creator information |
| `tags` | No | Categorization tags |

---

## Managing Active Skills

During a conversation, use slash commands to manage skills:

```text
/skills             # List active skills
/skills load my-skill
/skills unload my-skill
```

Multiple skills can be active simultaneously.

---

## Skill Precedence

When multiple skills are active:

1. **Built-in skills** have the lowest priority
2. **Installed community skills** have medium priority
3. **Custom local skills** have the highest priority
4. **Explicitly loaded skills** override everything

---

# 技能

技能是可重複使用的工作流程，可擴展 Hermes Agent 的功能。它們將指令、工具和設定包裝成可分享的模組。

---

## 技能指令

```bash
# 搜尋社群技能
hermes skills search <查詢>

# 安裝技能
hermes skills install <技能名稱>

# 列出已安裝技能
hermes skills list

# 移除技能
hermes skills remove <技能名稱>

# 顯示技能詳細資訊
hermes skills info <技能名稱>
```

---

## 安裝技能

### 從社群儲存庫

```bash
hermes skills search code review
hermes skills install code-reviewer
```

### 從本機檔案

```bash
hermes skills install ./my-skill.yaml
```

### 從 URL

```bash
hermes skills install https://example.com/skills/my-skill.yaml
```

---

## 建立自訂技能

技能以 YAML 檔案定義。以下是一個最小範例：

```yaml
# ~/.hermes/skills/my-skill.yaml
name: my-skill
description: 用於我的工作流程的自訂技能
version: "1.0"

instructions: |
  當被要求執行此任務時，請遵循以下步驟：
  1. 分析輸入內容
  2. 套用工作流程
  3. 回傳結果

tools:
  - file_system
  - code_interpreter
```

### 技能結構

| 欄位 | 必填 | 說明 |
|------|------|------|
| `name` | 是 | 技能的唯一識別名稱 |
| `description` | 是 | 列表中顯示的簡短說明 |
| `version` | 否 | 語意化版本字串 |
| `instructions` | 是 | 代理的系統提示詞或指令 |
| `tools` | 否 | 技能所需的工具列表 |
| `author` | 否 | 建立者資訊 |
| `tags` | 否 | 分類標籤 |

---

## 管理啟用中的技能

在對話中，使用斜線指令管理技能：

```text
/skills             # 列出啟用中的技能
/skills load my-skill
/skills unload my-skill
```

多個技能可同時啟用。

---

## 技能優先順序

當多個技能同時啟用時：

1. **內建技能** 優先級最低
2. **已安裝的社群技能** 為中等優先級
3. **自訂的本機技能** 優先級最高
4. **明確載入的技能** 覆蓋所有其他技能

# Hermes Agent Guide — Sitemap

> A bilingual (English / Traditional Chinese) static website for installing, configuring, and using Hermes Agent.

## Site Structure

```
/
├── index.html                  # Home — overview & quick links
├── getting-started/
│   ├── installation.html       # Installation guide
│   ├── configuration.html      # Provider & model setup
│   └── quickstart.html         # First steps after install
├── usage/
│   ├── basic-usage.html        # CLI commands & daily use
│   ├── tui-mode.html           # Terminal UI mode
│   └── slash-commands.html     # In-chat slash commands
├── advanced/
│   ├── skills.html             # Custom skills / workflows
│   ├── memory-system.html      # Three-tier memory
│   ├── mcp-servers.html        # MCP tool integration
│   ├── subagents.html          # Parallel task execution
│   └── gateway.html            # Telegram / Discord / messaging
├── troubleshooting.html        # Common issues & fixes
└── faq.html                    # Frequently asked questions
```

## Source Files (markdown/)

| File | Content |
|------|---------|
| `index.md` | Landing page — what is Hermes Agent, key features, quick links |
| `getting-started/installation.md` | System requirements, one-line install, post-install verification |
| `getting-started/configuration.md` | Provider selection, API keys, `hermes model`, `hermes setup` |
| `getting-started/quickstart.md` | First conversation, basic commands, tips |
| `usage/basic-usage.md` | Daily commands (`hermes`, `hermes --continue`, session management) |
| `usage/tui-mode.md` | TUI interface, navigation, shortcuts |
| `usage/slash-commands.md` | All slash commands reference |
| `advanced/skills.md` | Skill search, install, create custom skills |
| `advanced/memory-system.md` | Persistent facts, conversation recall, procedural memory |
| `advanced/mcp-servers.md` | Adding custom MCP tool servers |
| `advanced/subagents.md` | Orchestrator/worker pattern, parallel execution |
| `advanced/gateway.md` | Telegram, Discord, and other messaging platforms |
| `troubleshooting.md` | Diagnostic steps, common errors, `hermes doctor` |
| `faq.md` | Frequently asked questions |

## Design

- **Bilingual layout**: Each page shows English on the left / Traditional Chinese on the right (two-column on desktop, stacked on mobile)
- **Theme**: Dark mode, minimal, clean, with a sidebar navigation
- **Tech stack**: Pure HTML + CSS + JavaScript (no external build tools or frameworks)
- **Navigation**: Collapsible sidebar with all sections, active page highlighted
- **Responsive**: Works on desktop and mobile
- **No external dependencies**: Self-contained, works offline

## Content Format

Each markdown source file contains both languages separated by an `---` divider:

```markdown
# Page Title (English)

English content...

---

# 頁面標題 (繁體中文)

繁體中文內容...
```

The build script parses this and generates a single HTML page with both languages.

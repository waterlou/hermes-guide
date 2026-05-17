#!/usr/bin/env python3
"""
Hermes Agent Guide — Static Site Generator
Converts bilingual markdown files into a static HTML website.
"""

import markdown
import re
import json
import os

SRC_DIR = "markdown"
OUT_DIR = "."
SITE_TITLE = "Hermes Agent Guide"

NAV_STRUCTURE = [
    {"title": "Home", "title_cn": "首页", "file": "index.md", "path": "index.html"},
    {
        "title": "Getting Started", "title_cn": "入门指南",
        "children": [
            {"title": "Installation", "title_cn": "安装", "file": "getting-started/installation.md", "path": "getting-started/installation.html"},
            {"title": "Configuration", "title_cn": "配置", "file": "getting-started/configuration.md", "path": "getting-started/configuration.html"},
            {"title": "Quickstart", "title_cn": "快速开始", "file": "getting-started/quickstart.md", "path": "getting-started/quickstart.html"},
        ],
    },
    {
        "title": "Usage", "title_cn": "使用指南",
        "children": [
            {"title": "Basic Usage", "title_cn": "基本使用", "file": "usage/basic-usage.md", "path": "usage/basic-usage.html"},
            {"title": "TUI Mode", "title_cn": "TUI 模式", "file": "usage/tui-mode.md", "path": "usage/tui-mode.html"},
            {"title": "Slash Commands", "title_cn": "斜杠命令", "file": "usage/slash-commands.md", "path": "usage/slash-commands.html"},
        ],
    },
    {
        "title": "Advanced", "title_cn": "高级功能",
        "children": [
            {"title": "Skills", "title_cn": "技能", "file": "advanced/skills.md", "path": "advanced/skills.html"},
            {"title": "Memory System", "title_cn": "记忆系统", "file": "advanced/memory-system.md", "path": "advanced/memory-system.html"},
            {"title": "MCP Servers", "title_cn": "MCP 服务器", "file": "advanced/mcp-servers.md", "path": "advanced/mcp-servers.html"},
            {"title": "Subagents", "title_cn": "子代理", "file": "advanced/subagents.md", "path": "advanced/subagents.html"},
            {"title": "Gateway", "title_cn": "网关", "file": "advanced/gateway.md", "path": "advanced/gateway.html"},
        ],
    },
    {"title": "Troubleshooting", "title_cn": "故障排除", "file": "troubleshooting.md", "path": "troubleshooting.html"},
    {"title": "FAQ", "title_cn": "常见问题", "file": "faq.md", "path": "faq.html"},
]


def flatten_nav():
    """Flatten nav tree into a list of (label, path) for template use."""
    items = []
    for section in NAV_STRUCTURE:
        if "children" in section:
            for child in section["children"]:
                items.append((child["title"], child["path"]))
        else:
            items.append((section["title"], section["path"]))
    return items


def split_bilingual(content):
    """Split markdown into (english, chinese) sections.

    The Chinese section is identified by the first h1/h2 header containing CJK characters.
    """
    lines = content.split("\n")
    split_idx = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r"^#{1,2}\s+.*[一-鿿]", stripped):
            split_idx = i
            break

    if split_idx is None:
        return content.strip(), ""

    english = "\n".join(lines[:split_idx]).strip()
    chinese = "\n".join(lines[split_idx:]).strip()
    return english, chinese


def render_markdown(text):
    """Convert markdown text to HTML and fix .md links to .html."""
    if not text:
        return ""
    extensions = [
        "markdown.extensions.fenced_code",
        "markdown.extensions.tables",
        "markdown.extensions.codehilite",
        "markdown.extensions.smarty",
    ]
    html = markdown.markdown(text, extensions=extensions)
    # Convert .md links to .html (but not external URLs or anchors)
    html = re.sub(r'href="([^"]+)\.md(#.*)?"', r'href="\1.html\2"', html)
    return html


def label_html(title, title_cn):
    """Generate bilingual label HTML."""
    if title_cn and title_cn != title:
        return (f'<span class="lang-label lang-en">{title}</span>'
                f'<span class="lang-label lang-cn">{title_cn}</span>')
    return title

def make_sidebar_html(current_path):
    """Generate sidebar navigation HTML, highlighting the current page."""
    depth = current_path.count("/")
    prefix = "../" * depth
    parts = []
    parts.append('<nav class="sidebar">')
    parts.append(f'<div class="sidebar-header"><a href="{prefix}index.html">{SITE_TITLE}</a></div>')
    parts.append('<ul class="nav-list">')

    for section in NAV_STRUCTURE:
        cn = section.get("title_cn", "")
        if "children" in section:
            is_active = any(
                child["path"] == current_path for child in section["children"]
            )
            active_class = " active-section" if is_active else ""
            parts.append(f'<li class="nav-section{active_class}">')
            parts.append(f'<span class="nav-section-title">{label_html(section["title"], cn)}</span>')
            parts.append('<ul class="nav-sublist">')
            for child in section["children"]:
                child_cn = child.get("title_cn", "")
                cls = ' class="active"' if child["path"] == current_path else ""
                parts.append(
                    f'<li><a href="{prefix}{child["path"]}"{cls}>{label_html(child["title"], child_cn)}</a></li>'
                )
            parts.append("</ul></li>")
        else:
            cls = ' class="active"' if section["path"] == current_path else ""
            parts.append(
                f'<li><a href="{prefix}{section["path"]}"{cls}>{label_html(section["title"], cn)}</a></li>'
            )

    parts.append("</ul></nav>")
    return "\n".join(parts)


def make_html(title_en, title_cn, html_en, html_cn, current_path):
    """Assemble the full HTML page."""
    depth = current_path.count("/")
    prefix = "../" * depth
    sidebar = make_sidebar_html(current_path)
    flat_nav = flatten_nav()

    # Build JSON for search index (use relative paths from current page)
    search_data = []
    for label, path in flat_nav:
        search_data.append({"title": label, "path": prefix + path})
    search_json = json.dumps(search_data, ensure_ascii=False)

    lang_toggle_html = ""
    if html_cn:
        lang_toggle_html = """
        <div class="lang-toggle">
            <button id="lang-en" class="lang-btn active" onclick="setLang('en')">English</button>
            <button id="lang-both" class="lang-btn" onclick="setLang('both')">Both</button>
            <button id="lang-cn" class="lang-btn" onclick="setLang('zh')">中文</button>
        </div>
        """

    en_col_class = "col col-en"
    cn_col_class = "col col-cn"
    if html_cn:
        en_col_class += ""
        cn_col_class += ""
    else:
        cn_col_class += " hidden"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_en if title_en != SITE_TITLE else SITE_TITLE}</title>
<style>
:root {{
    --bg: #ffffff;
    --bg-sidebar: #f7f8fa;
    --text: #1a1a2e;
    --text-dim: #6b7280;
    --accent: #3b82f6;
    --accent-hover: #2563eb;
    --border: #e5e7eb;
    --code-bg: #f1f5f9;
    --code-block-bg: #f8fafc;
    --table-border: #e5e7eb;
    --table-alt: #f8fafc;
    --sidebar-width: 280px;
}}

[data-theme="dark"] {{
    --bg: #0f172a;
    --bg-sidebar: #1e293b;
    --text: #e2e8f0;
    --text-dim: #94a3b8;
    --accent: #60a5fa;
    --accent-hover: #93c5fd;
    --border: #334155;
    --code-bg: #1e293b;
    --code-block-bg: #0f172a;
    --table-border: #334155;
    --table-alt: #1e293b;
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    background: var(--bg);
    color: var(--text);
    line-height: 1.7;
    display: flex;
    min-height: 100vh;
    transition: background 0.25s ease, color 0.2s ease;
}}

a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ color: var(--accent-hover); text-decoration: underline; }}

/* Sidebar */
.sidebar {{
    width: var(--sidebar-width);
    min-width: var(--sidebar-width);
    background: var(--bg-sidebar);
    border-right: 1px solid var(--border);
    height: 100vh;
    position: sticky;
    top: 0;
    overflow-y: auto;
    transition: background 0.25s ease, border-color 0.25s ease;
}}

.sidebar-header {{
    padding: 24px 24px 16px;
    font-size: 16px;
    font-weight: 700;
    border-bottom: 1px solid var(--border);
    letter-spacing: -0.01em;
    transition: border-color 0.25s ease;
}}

.sidebar-header a {{
    color: var(--text);
}}
.sidebar-header a:hover {{
    color: var(--accent);
    text-decoration: none;
}}

.nav-list {{ list-style: none; padding: 12px 0 24px; }}
.nav-list li {{ margin: 0; }}

.nav-section-title {{
    display: block;
    padding: 16px 24px 6px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-dim);
}}

.nav-sublist {{ list-style: none; padding: 0; }}
.nav-sublist li {{ margin: 0; }}

.nav-list > li > a,
.nav-sublist li a {{
    display: block;
    padding: 6px 24px 6px 24px;
    font-size: 14px;
    color: var(--text-dim);
    border-left: 2px solid transparent;
    transition: all 0.15s;
}}

.nav-sublist li a {{ padding-left: 24px; }}

.nav-list a:hover {{
    color: var(--text);
    text-decoration: none;
    background: rgba(0,0,0,0.03);
}}

[data-theme="dark"] .nav-list a:hover {{
    background: rgba(255,255,255,0.04);
}}

.nav-list a.active,
.nav-sublist li a.active {{
    color: var(--accent);
    border-left-color: var(--accent);
    font-weight: 500;
}}

/* Main content */
.main {{
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
}}

.top-bar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 32px;
    border-bottom: 1px solid var(--border);
    background: var(--bg);
    position: sticky;
    top: 0;
    z-index: 10;
    transition: background 0.25s ease, border-color 0.25s ease;
    gap: 12px;
}}

.top-bar-left {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.top-bar-right {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.mobile-menu-btn {{
    display: none;
    background: none;
    border: 1px solid var(--border);
    color: var(--text);
    font-size: 18px;
    padding: 4px 10px;
    cursor: pointer;
    border-radius: 6px;
    line-height: 1;
}}
.mobile-menu-btn:hover {{ background: rgba(0,0,0,0.04); }}

[data-theme="dark"] .mobile-menu-btn:hover {{ background: rgba(255,255,255,0.06); }}

.lang-toggle {{
    display: flex;
    gap: 0;
}}
.lang-btn {{
    background: transparent;
    border: 1px solid var(--border);
    color: var(--text-dim);
    padding: 4px 12px;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.15s;
}}
.lang-btn:first-child {{ border-radius: 6px 0 0 6px; }}
.lang-btn:last-child {{ border-radius: 0 6px 6px 0; }}
.lang-btn.active {{
    background: var(--accent);
    color: #fff;
    border-color: var(--accent);
}}
.lang-btn:not(.active):hover {{
    color: var(--text);
    background: rgba(0,0,0,0.04);
}}

[data-theme="dark"] .lang-btn:not(.active):hover {{
    background: rgba(255,255,255,0.06);
}}

/* Theme toggle */
.theme-toggle {{
    background: none;
    border: 1px solid var(--border);
    color: var(--text-dim);
    cursor: pointer;
    padding: 5px 9px;
    border-radius: 6px;
    font-size: 16px;
    line-height: 1;
    transition: all 0.15s;
    display: flex;
    align-items: center;
}}
.theme-toggle:hover {{
    color: var(--text);
    border-color: var(--text-dim);
}}

/* Search */
#search-input {{
    background: var(--code-bg);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 13px;
    width: 170px;
    outline: none;
    transition: border-color 0.2s;
}}
#search-input:focus {{
    border-color: var(--accent);
}}
#search-input::placeholder {{ color: var(--text-dim); }}

.content {{
    display: flex;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
    flex: 1;
}}

.col {{
    flex: 1;
    min-width: 0;
    padding: 40px 48px;
}}

.col-cn.hidden {{ display: none; }}

.divider-col {{
    width: 1px;
    min-width: 1px;
    background: var(--border);
    margin: 40px 0;
    transition: background 0.25s ease;
}}

/* Content styling */
.content h1 {{
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 24px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
    letter-spacing: -0.02em;
    transition: border-color 0.25s ease;
}}

.content h2 {{
    font-size: 22px;
    font-weight: 700;
    margin-top: 36px;
    margin-bottom: 12px;
    letter-spacing: -0.01em;
}}

.content h3 {{
    font-size: 18px;
    font-weight: 600;
    margin-top: 28px;
    margin-bottom: 8px;
}}

.content h4 {{
    font-size: 16px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 8px;
}}

.content p {{ margin-bottom: 18px; }}

.content ul, .content ol {{ margin-bottom: 18px; padding-left: 24px; }}
.content li {{ margin-bottom: 6px; }}

.content code {{
    font-family: "SF Mono", "Fira Code", "Fira Mono", "Cascadia Code", monospace;
    background: var(--code-bg);
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.875em;
    transition: background 0.2s ease;
}}

.content pre {{
    background: var(--code-block-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px;
    overflow-x: auto;
    margin-bottom: 18px;
    font-size: 13px;
    line-height: 1.6;
    transition: background 0.25s ease, border-color 0.25s ease;
}}

.content pre code {{
    background: none;
    padding: 0;
    border-radius: 0;
    font-size: inherit;
}}

.content blockquote {{
    border-left: 3px solid var(--accent);
    padding: 12px 20px;
    margin-bottom: 18px;
    color: var(--text-dim);
    background: rgba(59,130,246,0.04);
    border-radius: 0 6px 6px 0;
}}

[data-theme="dark"] .content blockquote {{
    background: rgba(96,165,250,0.05);
}}

.content table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 18px;
    font-size: 14px;
}}

.content th, .content td {{
    border: 1px solid var(--table-border);
    padding: 10px 14px;
    text-align: left;
    transition: border-color 0.25s ease;
}}

.content th {{
    background: var(--bg-sidebar);
    font-weight: 600;
}}

.content tr:nth-child(even) {{
    background: var(--table-alt);
}}

.content hr {{
    border: none;
    border-top: 1px solid var(--border);
    margin: 36px 0;
    transition: border-color 0.25s ease;
}}

.content img {{
    max-width: 100%;
    border-radius: 8px;
}}

/* Highlighted code blocks */
.codehilite {{ border-radius: 8px; }}
.codehilite pre {{ background: var(--code-block-bg); }}
.codehilite .hll {{ background-color: #f0f0f0; }}
.codehilite .c {{ color: #6b7280; font-style: italic; }}
.codehilite .k {{ color: #7c3aed; font-weight: 600; }}
.codehilite .kt {{ color: #7c3aed; }}
.codehilite .s {{ color: #059669; }}
.codehilite .na {{ color: #2563eb; }}
.codehilite .nb {{ color: #2563eb; }}
.codehilite .nc {{ color: #7c3aed; font-weight: 600; }}
.codehilite .no {{ color: #7c3aed; }}
.codehilite .nd {{ color: #7c3aed; font-weight: 600; }}
.codehilite .nf {{ color: #2563eb; font-weight: 600; }}
.codehilite .nv {{ color: #2563eb; }}
.codehilite .mi {{ color: #d97706; }}
.codehilite .mf {{ color: #d97706; }}
.codehilite .o {{ color: #6b7280; }}
.codehilite .p {{ color: #6b7280; }}

[data-theme="dark"] .codehilite .hll {{ background-color: #1e293b; }}
[data-theme="dark"] .codehilite .c {{ color: #64748b; }}
[data-theme="dark"] .codehilite .k {{ color: #a78bfa; }}
[data-theme="dark"] .codehilite .kt {{ color: #a78bfa; }}
[data-theme="dark"] .codehilite .s {{ color: #34d399; }}
[data-theme="dark"] .codehilite .na {{ color: #60a5fa; }}
[data-theme="dark"] .codehilite .nb {{ color: #60a5fa; }}
[data-theme="dark"] .codehilite .nc {{ color: #a78bfa; }}
[data-theme="dark"] .codehilite .no {{ color: #a78bfa; }}
[data-theme="dark"] .codehilite .nd {{ color: #a78bfa; }}
[data-theme="dark"] .codehilite .nf {{ color: #60a5fa; }}
[data-theme="dark"] .codehilite .nv {{ color: #60a5fa; }}
[data-theme="dark"] .codehilite .mi {{ color: #fbbf24; }}
[data-theme="dark"] .codehilite .mf {{ color: #fbbf24; }}
[data-theme="dark"] .codehilite .o {{ color: #94a3b8; }}
[data-theme="dark"] .codehilite .p {{ color: #94a3b8; }}

/* Language labels in nav */
.lang-label {{
    display: none;
}}
.lang-label.lang-en {{
    display: inline;
}}

/* Overlay for mobile sidebar */
.sidebar-overlay {{
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.4);
    z-index: 98;
}}

/* Responsive */
@media (max-width: 900px) {{
    .sidebar {{ display: none; }}
    .sidebar.open {{ display: block; position: fixed; z-index: 99; top: 0; left: 0; height: 100vh; box-shadow: 4px 0 20px rgba(0,0,0,0.15); }}
    .sidebar-overlay.open {{ display: block; }}
    .mobile-menu-btn {{ display: block; }}
    .content {{ flex-direction: column; }}
    .col {{ padding: 24px 20px; }}
    .divider-col {{ display: none; }}
    .top-bar {{ padding: 8px 16px; }}
    .lang-btn {{ padding: 3px 8px; font-size: 12px; }}
    #search-input {{ width: 120px; }}
}}

@media (min-width: 901px) {{
    .mobile-menu-btn {{ display: none; }}
    .sidebar-overlay {{ display: none !important; }}
}}
</style>
</head>
<body>

<div class="sidebar-overlay" id="sidebar-overlay" onclick="toggleSidebar()"></div>
{sidebar}

<div class="main">
    <div class="top-bar">
        <div class="top-bar-left">
            <button class="mobile-menu-btn" onclick="toggleSidebar()">☰</button>
            {lang_toggle_html}
        </div>
        <div class="top-bar-right">
            <input type="text" id="search-input" placeholder="Search...">
            <button class="theme-toggle" id="theme-toggle" onclick="toggleTheme()" title="Toggle theme">☀</button>
        </div>
    </div>
    <div class="content">
        <div class="{en_col_class}">
            <div class="content-body en-content">{html_en}</div>
        </div>
        {"<div class='divider-col'></div>" if html_cn else ""}
        <div class="{cn_col_class}">
            <div class="content-body cn-content">{html_cn}</div>
        </div>
    </div>
</div>

<script>
var searchIndex = {search_json};

var savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {{
    document.documentElement.setAttribute('data-theme', 'dark');
    document.getElementById('theme-toggle').textContent = '☾';
}}

var savedLang = localStorage.getItem('lang') || 'en';
setLang(savedLang);

function toggleTheme() {{
    var html = document.documentElement;
    var btn = document.getElementById('theme-toggle');
    if (html.getAttribute('data-theme') === 'dark') {{
        html.removeAttribute('data-theme');
        btn.textContent = '☀';
        localStorage.setItem('theme', 'light');
    }} else {{
        html.setAttribute('data-theme', 'dark');
        btn.textContent = '☾';
        localStorage.setItem('theme', 'dark');
    }}
}}

function toggleSidebar() {{
    document.querySelector('.sidebar').classList.toggle('open');
    document.getElementById('sidebar-overlay').classList.toggle('open');
}}

function setLang(lang) {{
    document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
    var enCol = document.querySelector('.col-en');
    var cnCol = document.querySelector('.col-cn');
    if (lang === 'en') {{
        document.getElementById('lang-en').classList.add('active');
        enCol.style.display = 'block';
        cnCol.style.display = 'none';
    }} else if (lang === 'zh') {{
        document.getElementById('lang-cn').classList.add('active');
        enCol.style.display = 'none';
        cnCol.style.display = 'block';
    }} else {{
        document.getElementById('lang-both').classList.add('active');
        enCol.style.display = 'block';
        cnCol.style.display = 'block';
    }}
    // Toggle nav labels
    document.querySelectorAll('.lang-label').forEach(function(el) {{
        el.style.display = 'none';
    }});
    if (lang === 'en') {{
        document.querySelectorAll('.lang-label.lang-en').forEach(function(el) {{
            el.style.display = 'inline';
        }});
    }} else if (lang === 'zh') {{
        document.querySelectorAll('.lang-label.lang-cn').forEach(function(el) {{
            el.style.display = 'inline';
        }});
    }} else {{
        document.querySelectorAll('.lang-label').forEach(function(el) {{
            el.style.display = 'inline';
        }});
    }}
    localStorage.setItem('lang', lang);
}}

document.getElementById('search-input').addEventListener('keydown', function(e) {{
    if (e.key === 'Enter') {{
        var q = this.value.toLowerCase();
        var match = searchIndex.find(function(item) {{
            return item.title.toLowerCase().includes(q);
        }});
        if (match) {{
            window.location.href = match.path;
        }}
    }}
}});
</script>
</body>
</html>"""


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def page_title(md_content):
    """Extract the first h1 title from markdown."""
    m = re.search(r"^#\s+(.+)$", md_content, re.MULTILINE)
    return m.group(1).strip() if m else "Untitled"


def generate_page(src_file, out_path):
    """Process one markdown file and write the HTML page."""
    with open(os.path.join(SRC_DIR, src_file), "r", encoding="utf-8") as f:
        content = f.read()

    en_md, cn_md = split_bilingual(content)

    title_en = page_title(en_md) or "Home"
    title_cn = page_title(cn_md) if cn_md else ""

    html_en = render_markdown(en_md)
    html_cn = render_markdown(cn_md) if cn_md else ""

    full_html = make_html(title_en, title_cn, html_en, html_cn, out_path)

    out_full = os.path.join(OUT_DIR, out_path)
    ensure_dir(os.path.dirname(out_full))
    with open(out_full, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"  ✓ {out_path}")


def main():
    pages = [
        ("index.md", "index.html"),
        ("getting-started/installation.md", "getting-started/installation.html"),
        ("getting-started/configuration.md", "getting-started/configuration.html"),
        ("getting-started/quickstart.md", "getting-started/quickstart.html"),
        ("usage/basic-usage.md", "usage/basic-usage.html"),
        ("usage/tui-mode.md", "usage/tui-mode.html"),
        ("usage/slash-commands.md", "usage/slash-commands.html"),
        ("advanced/skills.md", "advanced/skills.html"),
        ("advanced/memory-system.md", "advanced/memory-system.html"),
        ("advanced/mcp-servers.md", "advanced/mcp-servers.html"),
        ("advanced/subagents.md", "advanced/subagents.html"),
        ("advanced/gateway.md", "advanced/gateway.html"),
        ("troubleshooting.md", "troubleshooting.html"),
        ("faq.md", "faq.html"),
    ]

    print("Building Hermes Agent Guide...")
    for src, out in pages:
        generate_page(src, out)
    print(f"\nDone! {len(pages)} pages generated in '{OUT_DIR}/'.")


if __name__ == "__main__":
    main()

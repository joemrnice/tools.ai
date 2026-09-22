#!/usr/bin/env python3
"""
tools.ai Static Site Generator
Validates tool JSON schema and builds the static reference website.
"""

import os
import json
import shutil
import sys
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
TOOLS_DIR = DATA_DIR / "tools"
CATEGORIES_FILE = DATA_DIR / "categories.json"
DIST_DIR = BASE_DIR / "dist"
ASSETS_DIR = BASE_DIR / "assets"

REQUIRED_TOOL_FIELDS = [
    "id", "name", "maker", "tagline", "category", "subcategory",
    "definition", "why_it_matters", "workplace_use_cases", "who_uses_it",
    "how_to_use", "key_features", "pricing", "official_url",
    "logo_source_note", "related_tools", "launched", "platform"
]

REQUIRED_PRICING_FIELDS = [
    "model", "has_free_tier", "free_tier_details", "paid_plans", "pricing_last_verified"
]

def load_categories():
    if not CATEGORIES_FILE.exists():
        raise FileNotFoundError(f"Categories file not found at {CATEGORIES_FILE}")
    with open(CATEGORIES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_tool_schema(tool, file_path):
    missing_fields = [field for field in REQUIRED_TOOL_FIELDS if field not in tool]
    if missing_fields:
        raise ValueError(f"Schema Error in {file_path} for tool '{tool.get('id', 'UNKNOWN')}': Missing fields {missing_fields}")

    pricing = tool.get("pricing", {})
    missing_pricing = [field for field in REQUIRED_PRICING_FIELDS if field not in pricing]
    if missing_pricing:
        raise ValueError(f"Schema Error in {file_path} for tool '{tool.get('id', 'UNKNOWN')}': Missing pricing fields {missing_pricing}")

    if not isinstance(tool["workplace_use_cases"], list) or not tool["workplace_use_cases"]:
        raise ValueError(f"Schema Error in {file_path} for tool '{tool.get('id')}': 'workplace_use_cases' must be a non-empty list.")

    if not isinstance(tool["who_uses_it"], list) or not tool["who_uses_it"]:
        raise ValueError(f"Schema Error in {file_path} for tool '{tool.get('id')}': 'who_uses_it' must be a non-empty list.")

def load_all_tools():
    tools = []
    if not TOOLS_DIR.exists():
        print(f"Warning: Tools directory {TOOLS_DIR} does not exist yet.")
        return tools

    for tool_file in TOOLS_DIR.glob("*.json"):
        with open(tool_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        validate_tool_schema(item, tool_file)
                        tools.append(item)
                elif isinstance(data, dict):
                    validate_tool_schema(data, tool_file)
                    tools.append(data)
            except Exception as e:
                print(f"Error loading {tool_file}: {e}")
                sys.exit(1)

    # Sort tools alphabetically by name
    tools.sort(key=lambda x: x["name"].lower())
    return tools

def render_header(title, rel_prefix=""):
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — tools.ai</title>
  <meta name="description" content="The definitive reference directory for AI tools for working professionals.">
  <link rel="stylesheet" href="{rel_prefix}assets/css/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
  <nav class="navbar">
    <div class="nav-container">
      <a href="{rel_prefix}index.html" class="brand">
        <span class="brand-dot"></span> tools.ai
      </a>
      <ul class="nav-links">
        <li><a href="{rel_prefix}directory.html">Directory</a></li>
        <li><a href="{rel_prefix}categories/index.html">Categories</a></li>
        <li><a href="{rel_prefix}roles/index.html">By Role</a></li>
        <li><a href="{rel_prefix}about.html">About & Methodology</a></li>
      </ul>
      <button id="theme-toggle" class="theme-toggle-btn" aria-label="Toggle Theme">
        <span>☀️</span> Light
      </button>
    </div>
  </nav>
"""

def render_footer(rel_prefix=""):
    return f"""
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-brand">
        <a href="{rel_prefix}index.html" class="brand">
          <span class="brand-dot"></span> tools.ai
        </a>
        <p>The open-source reference website cataloging professional AI tools — explaining what they do, why they matter, and how much they cost.</p>
      </div>
      <div class="footer-column">
        <h4>Navigation</h4>
        <ul>
          <li><a href="{rel_prefix}directory.html">All Tools Directory</a></li>
          <li><a href="{rel_prefix}categories/index.html">Category Overview</a></li>
          <li><a href="{rel_prefix}roles/index.html">Tools by Role</a></li>
          <li><a href="{rel_prefix}about.html">About & Methodology</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h4>Open Source</h4>
        <ul>
          <li><a href="https://github.com/joemrnice/tools.ai" target="_blank" rel="noopener">GitHub Repository</a></li>
          <li><a href="https://github.com/joemrnice/tools.ai/issues" target="_blank" rel="noopener">Report Issue / Suggest Tool</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; tools.ai reference project. Open-source & community driven.</span>
      <span>Verified AI tooling references for working professionals.</span>
    </div>
  </footer>
  <script class="initial-js">
    // Global data injection for instant client-side filtering
  </script>
  <script src="{rel_prefix}assets/js/app.js"></script>
</body>
</html>
"""

def render_tool_card(tool, categories_map, rel_prefix=""):
    initial = tool["name"][0].upper()
    cat_info = categories_map.get(tool["category"], {"name": tool["category"], "icon": "⚡"})
    pricing_model = tool["pricing"]["model"]

    features_html = "".join([f"<li>{f}</li>" for f in tool["key_features"][:3]])
    roles_html = "".join([f'<span class="role-pill">{r}</span>' for r in tool["who_uses_it"][:3]])

    return f"""
    <article class="tool-card">
      <div class="tool-card-header">
        <div class="tool-identity">
          <div class="tool-icon-fallback">{initial}</div>
          <div class="tool-title-group">
            <h3><a href="{rel_prefix}tools/{tool['id']}.html">{tool['name']}</a></h3>
            <span class="tool-maker">by {tool['maker']}</span>
          </div>
        </div>
        <span class="pricing-badge {pricing_model}">{pricing_model}</span>
      </div>

      <a href="{rel_prefix}categories/{tool['category']}.html" class="category-tag">
        <span>{cat_info['icon']}</span> {cat_info['name']}
      </a>

      <p class="tool-tagline">{tool['tagline']}</p>

      <ul class="tool-features-preview">
        {features_html}
      </ul>

      <div class="tool-card-footer">
        <div class="tool-roles-list">
          {roles_html}
        </div>
        <a href="{tool['official_url']}" target="_blank" rel="noopener" class="btn-visit">
          Visit ↗
        </a>
      </div>
    </article>
"""

def build_site():
    print("Initializing site generator...")
    categories = load_categories()
    categories_map = {c["id"]: c for c in categories}
    tools = load_all_tools()

    print(f"Loaded {len(categories)} categories and {len(tools)} tools.")

    # Reset Dist Dir
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    (DIST_DIR / "categories").mkdir(exist_ok=True)
    (DIST_DIR / "tools").mkdir(exist_ok=True)
    (DIST_DIR / "roles").mkdir(exist_ok=True)

    # Copy Assets
    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, DIST_DIR / "assets")

    # Inject global window object for JS
    data_script = f"""
    <script>
      window.CATEGORIES_MAP = {json.dumps(categories_map)};
      window.TOOLS_DATA = {json.dumps(tools)};
    </script>
    """

    # 1. Homepage (index.html)
    print("Generating Homepage...")
    featured_tools = tools[:6]
    cat_grid_html = ""
    for cat in categories:
        cat_tools_count = len([t for t in tools if t["category"] == cat["id"]])
        cat_grid_html += f"""
        <a href="categories/{cat['id']}.html" class="category-card">
          <div class="category-header">
            <span class="category-icon">{cat['icon']}</span>
            <span class="category-title">{cat['name']}</span>
          </div>
          <p class="category-desc">{cat['description']}</p>
          <span class="category-count">{cat_tools_count} tool{'s' if cat_tools_count != 1 else ''} ➔</span>
        </a>
        """

    featured_grid_html = "".join([render_tool_card(t, categories_map) for t in featured_tools])

    home_html = render_header("tools.ai — The AI Tooling Reference Directory") + f"""
    <main class="container">
      <section class="hero">
        <span class="hero-tagline">Open-Source AI Reference</span>
        <h1>The AI Tooling Reference Directory</h1>
        <p>Curated, verified reference catalogs of AI tools for working professionals. Understand what tools do, why they matter, how to use them, and what they cost.</p>
      </section>

      <section class="search-container">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" id="home-search" class="search-input" placeholder="Search by tool name, role, category, or capability (e.g. 'code assistant', 'Claude', 'copywriter')..." onkeydown="if(event.key==='Enter') window.location.href='directory.html?q='+encodeURIComponent(this.value)">
        </div>
      </section>

      <section class="stats-bar">
        <div class="stat-item">
          <div class="stat-value">{len(tools)}+</div>
          <div class="stat-label">Verified Tools</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">{len(categories)}</div>
          <div class="stat-label">Categories</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">100%</div>
          <div class="stat-label">Verified Pricing</div>
        </div>
      </section>

      <section style="margin-bottom: 3rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; font-weight: 700;">Featured AI Tools</h2>
        <div class="tools-grid">
          {featured_grid_html if featured_grid_html else '<p style="color:var(--text-muted)">Tools coming soon.</p>'}
        </div>
        <div style="text-align: center;">
          <a href="directory.html" class="btn-primary">Browse All {len(tools)} Tools ➔</a>
        </div>
      </section>

      <section>
        <h2 style="font-size: 1.5rem; margin-bottom: 1.25rem; font-weight: 700;">Explore Categories</h2>
        <div class="category-grid">
          {cat_grid_html}
        </div>
      </section>
    </main>
    """ + render_footer().replace('<script class="initial-js">\n    // Global data injection for instant client-side filtering\n  </script>', data_script)

    with open(DIST_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write(home_html)

    # 2. Directory Page (directory.html)
    print("Generating Directory Page...")
    dir_html = render_header("All AI Tools Directory") + f"""
    <main class="container">
      <div style="margin-bottom: 2rem;">
        <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.5rem;">Global AI Tools Directory</h1>
        <p style="color: var(--text-secondary);">Search and filter across all {len(tools)} curated tools by category, pricing model, target role, or platform.</p>
      </div>

      <div class="filter-bar">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" id="search-input" class="search-input" placeholder="Type to search tools, features, makers, or roles...">
        </div>
        <div class="filter-group-row">
          <div class="filter-group">
            <span class="filter-label">Category:</span>
            <select id="filter-category" class="filter-select">
              <option value="all">All Categories</option>
              {"".join([f'<option value="{c["id"]}">{c["name"]}</option>' for c in categories])}
            </select>
          </div>
          <div class="filter-group">
            <span class="filter-label">Pricing:</span>
            <select id="filter-pricing" class="filter-select">
              <option value="all">All Models</option>
              <option value="free">Free</option>
              <option value="freemium">Freemium</option>
              <option value="paid">Paid</option>
              <option value="has_free_tier">Has Free Tier</option>
            </select>
          </div>
          <div class="filter-group">
            <span class="filter-label">Role:</span>
            <select id="filter-role" class="filter-select">
              <option value="all">All Roles</option>
              <option value="software_engineers">Software Engineers</option>
              <option value="marketers">Marketers</option>
              <option value="product_managers">Product Managers</option>
              <option value="writers">Writers</option>
              <option value="designers">Designers</option>
              <option value="data_analysts">Data Analysts</option>
              <option value="executives">Executives</option>
            </select>
          </div>
          <div class="filter-group">
            <span class="filter-label">Sort:</span>
            <select id="sort-select" class="sort-select">
              <option value="relevant">Default</option>
              <option value="alpha">Alphabetical (A-Z)</option>
              <option value="newest">Newest First</option>
            </select>
          </div>
          <button id="clear-filters" class="btn-clear-filters">Reset Filters</button>
        </div>
      </div>

      <div class="results-meta">
        <span id="results-count">Showing all {len(tools)} tools</span>
      </div>

      <div id="tools-grid-container" class="tools-grid">
        {"".join([render_tool_card(t, categories_map) for t in tools])}
      </div>
    </main>
    <script>
      // Auto-populate search from query param if present
      document.addEventListener('DOMContentLoaded', () => {{
        const params = new URLSearchParams(window.location.search);
        const query = params.get('q');
        if (query) {{
          const searchInput = document.getElementById('search-input');
          if (searchInput) {{
            searchInput.value = query;
            searchInput.dispatchEvent(new Event('input'));
          }}
        }}
      }});
    </script>
    """ + render_footer().replace('<script class="initial-js">\n    // Global data injection for instant client-side filtering\n  </script>', data_script)

    with open(DIST_DIR / "directory.html", "w", encoding="utf-8") as f:
        f.write(dir_html)

    # 3. Categories Index (categories/index.html)
    print("Generating Categories Index...")
    cat_index_cards = ""
    for cat in categories:
        cat_tools = [t for t in tools if t["category"] == cat["id"]]
        cat_index_cards += f"""
        <div class="detail-card" style="margin-bottom: 1.5rem;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="font-size: 1.75rem;">{cat['icon']}</span>
              <h2 style="margin: 0; border: None; padding: 0;">{cat['name']}</h2>
            </div>
            <a href="{cat['id']}.html" class="btn-primary" style="padding: 0.4rem 0.8rem; font-size: 0.85rem;">View Category ({len(cat_tools)}) ➔</a>
          </div>
          <p style="color: var(--text-secondary); margin-bottom: 1rem;">{cat['description']}</p>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            {"".join([f'<a href="../tools/{t["id"]}.html" class="tag-item" style="color: var(--text-primary);">{t["name"]}</a>' for t in cat_tools[:8]])}
            {f'<span class="tag-item">+{len(cat_tools)-8} more</span>' if len(cat_tools) > 8 else ''}
          </div>
        </div>
        """

    cat_index_html = render_header("Tool Categories", rel_prefix="../") + f"""
    <main class="container">
      <div style="margin-bottom: 2rem;">
        <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.5rem;">AI Tool Categories</h1>
        <p style="color: var(--text-secondary);">Browse AI tools organized into 20 specialized professional domains.</p>
      </div>

      <div style="max-width: 900px;">
        {cat_index_cards}
      </div>
    </main>
    """ + render_footer(rel_prefix="../").replace('<script class="initial-js">\n    // Global data injection for instant client-side filtering\n  </script>', data_script)

    with open(DIST_DIR / "categories" / "index.html", "w", encoding="utf-8") as f:
        f.write(cat_index_html)

    # 4. Individual Category Pages (categories/{cat_id}.html)
    print("Generating Category Pages...")
    for cat in categories:
        cat_tools = [t for t in tools if t["category"] == cat["id"]]
        cards_html = "".join([render_tool_card(t, categories_map, rel_prefix="../") for t in cat_tools])

        cat_page_html = render_header(f"{cat['name']} AI Tools", rel_prefix="../") + f"""
        <main class="container">
          <div style="margin-bottom: 2rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
              <span style="font-size: 2rem;">{cat['icon']}</span>
              <h1 style="font-size: 2.25rem; font-weight: 800; margin: 0;">{cat['name']}</h1>
            </div>
            <p style="color: var(--text-secondary); max-width: 800px; font-size: 1.1rem;">{cat['description']}</p>
          </div>

          <div class="results-meta">
            <span>{len(cat_tools)} tool{'s' if len(cat_tools) != 1 else ''} in this category</span>
            <a href="../directory.html?category={cat['id']}">Filter in global directory ➔</a>
          </div>

          <div class="tools-grid">
            {cards_html if cards_html else '<div class="empty-state"><h3>No tools currently added to this category</h3><p>Tools for this category are being verified.</p></div>'}
          </div>
        </main>
        """ + render_footer(rel_prefix="../").replace('<script class="initial-js">\n    // Global data injection for instant client-side filtering\n  </script>', data_script)

        with open(DIST_DIR / "categories" / f"{cat['id']}.html", "w", encoding="utf-8") as f:
            f.write(cat_page_html)

    # 5. Individual Tool Pages (tools/{tool_id}.html)
    print("Generating Individual Tool Detail Pages...")
    for tool in tools:
        cat_info = categories_map.get(tool["category"], {"name": tool["category"], "icon": "⚡"})
        initial = tool["name"][0].upper()
        pricing = tool["pricing"]

        use_cases_html = "".join([f"<li>{uc}</li>" for uc in tool["workplace_use_cases"]])
        features_html = "".join([f"<li>{f}</li>" for f in tool["key_features"]])
        who_uses_html = "".join([f'<span class="tag-item">{r}</span>' for r in tool["who_uses_it"]])
        platform_html = "".join([f'<span class="tag-item">{p}</span>' for p in tool["platform"]])

        paid_plans_rows = ""
        for plan in pricing.get("paid_plans", []):
            paid_plans_rows += f"""
            <tr>
              <td><strong>{plan['name']}</strong></td>
              <td><code>{plan['price']}</code></td>
              <td>{plan.get('notes', '-')}</td>
            </tr>
            """

        related_tools_html = ""
        for rel_id in tool.get("related_tools", []):
            rel_tool = next((t for t in tools if t["id"] == rel_id), None)
            if rel_tool:
                related_tools_html += f"""
                <a href="{rel_tool['id']}.html" style="display: block; padding: 0.75rem; background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: var(--radius-md); margin-bottom: 0.5rem; text-decoration: none;">
                  <div style="font-weight: 600; color: var(--text-primary);">{rel_tool['name']}</div>
                  <div style="font-size: 0.8rem; color: var(--text-secondary);">{rel_tool['tagline']}</div>
                </a>
                """

        tool_page_html = render_header(f"{tool['name']} — AI Tool Reference", rel_prefix="../") + f"""
        <main class="container">
          <div class="tool-detail-header">
            <div class="tool-detail-title-row">
              <div class="tool-detail-main-info">
                <div class="tool-detail-icon">{initial}</div>
                <div>
                  <h1 class="tool-detail-h1">{tool['name']}</h1>
                  <p class="tool-detail-tagline">by {tool['maker']}</p>
                </div>
              </div>
              <div class="tool-action-buttons">
                <a href="{tool['official_url']}" target="_blank" rel="noopener" class="btn-primary">
                  Visit Official Site ↗
                </a>
              </div>
            </div>

            <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
              <a href="../categories/{tool['category']}.html" class="category-tag" style="margin:0;">
                <span>{cat_info['icon']}</span> {cat_info['name']}
              </a>
              <span class="pricing-badge {pricing['model']}">{pricing['model']}</span>
              <span style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-muted);">Launched: {tool['launched']}</span>
            </div>
          </div>

          <div class="detail-grid">
            <div class="detail-main">
              <div class="detail-card">
                <h2><span>📖</span> What is {tool['name']}?</h2>
                <p>{tool['definition']}</p>
              </div>

              <div class="detail-card">
                <h2><span>💡</span> Why It Matters</h2>
                <p>{tool['why_it_matters']}</p>
              </div>

              <div class="detail-card">
                <h2><span>🎯</span> Workplace Use Cases</h2>
                <ul class="use-cases-list">
                  {use_cases_html}
                </ul>
              </div>

              <div class="detail-card">
                <h2><span>🚀</span> How to Use It</h2>
                <p>{tool['how_to_use']}</p>
              </div>

              <div class="detail-card">
                <h2><span>✨</span> Key Features</h2>
                <ul class="features-list">
                  {features_html}
                </ul>
              </div>

              <div class="detail-card">
                <h2><span>💳</span> Pricing & Plans</h2>
                <p><strong>Free Tier:</strong> {tool['pricing']['free_tier_details'] if tool['pricing']['has_free_tier'] else 'No free tier available.'}</p>

                {f'''
                <table class="pricing-table">
                  <thead>
                    <tr>
                      <th>Plan</th>
                      <th>Price</th>
                      <th>Notes</th>
                    </tr>
                  </thead>
                  <tbody>
                    {paid_plans_rows}
                  </tbody>
                </table>
                ''' if paid_plans_rows else ''}

                <div class="verified-badge">
                  <span>✓</span> Pricing verified as of {pricing['pricing_last_verified']}
                </div>
              </div>
            </div>

            <div class="detail-sidebar">
              <div class="meta-box">
                <div class="meta-item">
                  <div class="meta-label">Who Uses It</div>
                  <div class="tag-cloud">{who_uses_html}</div>
                </div>

                <div class="meta-item">
                  <div class="meta-label">Supported Platforms</div>
                  <div class="tag-cloud">{platform_html}</div>
                </div>

                <div class="meta-item">
                  <div class="meta-label">Subcategory</div>
                  <div class="meta-value" style="font-family: var(--font-mono); font-size: 0.85rem;">{tool['subcategory']}</div>
                </div>

                <div class="meta-item">
                  <div class="meta-label">Official URL</div>
                  <a href="{tool['official_url']}" target="_blank" rel="noopener" style="font-family: var(--font-mono); font-size: 0.85rem; word-break: break-all;">
                    {tool['official_url']}
                  </a>
                </div>

                <div class="meta-item">
                  <div class="meta-label">Asset Attribution</div>
                  <div style="font-size: 0.75rem; color: var(--text-muted);">{tool['logo_source_note']}</div>
                </div>
              </div>

              {f'''
              <div class="meta-box" style="margin-top: 1.5rem;">
                <div class="meta-label" style="margin-bottom: 0.75rem;">Related Tools</div>
                {related_tools_html}
              </div>
              ''' if related_tools_html else ''}
            </div>
          </div>
        </main>
        """ + render_footer(rel_prefix="../").replace('<script class="initial-js">\n    // Global data injection for instant client-side filtering\n  </script>', data_script)

        with open(DIST_DIR / "tools" / f"{tool['id']}.html", "w", encoding="utf-8") as f:
            f.write(tool_page_html)

    # 6. By Role Pages (roles/index.html & roles/{role_id}.html)
    print("Generating Roles Pages...")
    roles_map = {
        "software_engineers": "Software Engineers",
        "marketers": "Marketers",
        "product_managers": "Product Managers",
        "writers": "Writers",
        "designers": "Designers",
        "data_analysts": "Data Analysts",
        "executives": "Executives",
        "customer_support": "Customer Support"
    }

    role_index_items = ""
    for role_id, role_name in roles_map.items():
        role_tools = [
            t for t in tools if any(
                r.lower().replace(' ', '_') == role_id or role_name.lower() in r.lower()
                for r in t.get("who_uses_it", [])
            )
        ]

        role_index_items += f"""
        <div class="detail-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h2 style="border: none; padding: 0; margin: 0;">AI Tools for {role_name}</h2>
            <a href="{role_id}.html" class="btn-primary" style="padding: 0.3rem 0.7rem; font-size: 0.8rem;">View All ({len(role_tools)}) ➔</a>
          </div>
          <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;">Curated collection of tools used by {role_name} to automate workflows and enhance productivity.</p>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            {"".join([f'<a href="../tools/{t["id"]}.html" class="tag-item">{t["name"]}</a>' for t in role_tools[:6]])}
          </div>
        </div>
        """

        # Generate specific role page
        role_cards_html = "".join([render_tool_card(t, categories_map, rel_prefix="../") for t in role_tools])
        role_page_html = render_header(f"AI Tools for {role_name}", rel_prefix="../") + f"""
        <main class="container">
          <div style="margin-bottom: 2rem;">
            <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.5rem;">AI Tools for {role_name}</h1>
            <p style="color: var(--text-secondary);">Curated reference guide of top AI tools tailored for {role_name}.</p>
          </div>

          <div class="results-meta">
            <span>{len(role_tools)} tool{'s' if len(role_tools) != 1 else ''} found</span>
            <a href="../directory.html?role={role_id}">Filter in global directory ➔</a>
          </div>

          <div class="tools-grid">
            {role_cards_html if role_cards_html else '<div class="empty-state"><h3>No tools found for this role</h3></div>'}
          </div>
        </main>
        """ + render_footer(rel_prefix="../").replace('<script class="initial-js">\n    // Global data injection for instant client-side filtering\n  </script>', data_script)

        with open(DIST_DIR / "roles" / f"{role_id}.html", "w", encoding="utf-8") as f:
            f.write(role_page_html)

    role_index_html = render_header("AI Tools by Professional Role", rel_prefix="../") + f"""
    <main class="container">
      <div style="margin-bottom: 2rem;">
        <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.5rem;">AI Tools by Role</h1>
        <p style="color: var(--text-secondary);">Find the most effective AI tooling for your specific domain and role.</p>
      </div>

      <div style="max-width: 900px;">
        {role_index_items}
      </div>
    </main>
    """ + render_footer(rel_prefix="../").replace('<script class="initial-js">\n    // Global data injection for instant client-side filtering\n  </script>', data_script)

    with open(DIST_DIR / "roles" / "index.html", "w", encoding="utf-8") as f:
        f.write(role_index_html)

    # 7. About Page (about.html)
    print("Generating About Page...")
    about_html = render_header("About & Methodology") + f"""
    <main class="container" style="max-width: 900px;">
      <div style="margin-bottom: 2rem;">
        <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.5rem;">About tools.ai & Methodology</h1>
        <p style="color: var(--text-secondary); font-size: 1.1rem;">An open-source, static reference site cataloging AI tools for working professionals.</p>
      </div>

      <div class="detail-card">
        <h2><span>🎯</span> Our Purpose</h2>
        <p><strong>tools.ai</strong> is designed to cut through marketing noise and present structured, objective, and verified information about artificial intelligence tools. For every cataloged tool, we answer six essential questions:</p>
        <ul style="list-style: none; margin-left: 1rem; color: var(--text-secondary); display: flex; flex-direction: column; gap: 0.5rem;">
          <li>• <strong>What is it?</strong> A plain-language definition written without vendor fluff.</li>
          <li>• <strong>Why does it matter?</strong> Its market position, capability, and significance in its domain.</li>
          <li>• <strong>Who uses it?</strong> Target roles and professional domains.</li>
          <li>• <strong>Workplace Use Cases:</strong> Concrete, actionable scenarios where professionals apply the tool.</li>
          <li>• <strong>How to use it:</strong> Practical steps to get started.</li>
          <li>• <strong>Pricing & Free Tier:</strong> Exact costs, free tier limits, and last-verified dates.</li>
        </ul>
      </div>

      <div class="detail-card">
        <h2><span>🛡️</span> Content Quality & Verification Standards</h2>
        <p>To ensure high utility for professionals, tools.ai adheres to strict curation principles:</p>
        <ul style="list-style: none; margin-left: 1rem; color: var(--text-secondary); display: flex; flex-direction: column; gap: 0.5rem;">
          <li>• <strong>No Fabricated Pricing:</strong> All pricing models and tier details are manually checked against official sources. Every entry includes a <code>pricing_last_verified</code> timestamp.</li>
          <li>• <strong>Original Writing:</strong> Definitions and use cases are synthesized independently rather than copied from vendor marketing copy.</li>
          <li>• <strong>Zero Build-Step Dependencies:</strong> Built with standard Python static generation, raw HTML, CSS custom properties, and vanilla JavaScript.</li>
        </ul>
      </div>

      <div class="detail-card">
        <h2><span>🤝</span> How to Contribute</h2>
        <p>tools.ai is fully open-source and community-maintained. You can suggest a new tool, update stale pricing, or fix broken links by opening a pull request or issue on GitHub.</p>
        <div class="code-block-wrapper">
          <div class="code-block-header">
            <span>data/tools/example_tool.json</span>
            <button class="btn-copy">Copy Schema</button>
          </div>
          <pre><code>{{
  "id": "tool-id",
  "name": "Tool Name",
  "maker": "Company Name",
  "tagline": "One line summary",
  "category": "general_chat_assistants",
  "subcategory": "sub-category",
  "definition": "2-3 sentences plain language definition.",
  "why_it_matters": "2-4 sentences explaining market significance.",
  "workplace_use_cases": ["Concrete use case 1", "Concrete use case 2"],
  "who_uses_it": ["Software Engineers", "Marketers"],
  "how_to_use": "Short practical getting started steps.",
  "key_features": ["Feature 1", "Feature 2"],
  "pricing": {{
    "model": "freemium",
    "has_free_tier": true,
    "free_tier_details": "Free tier details...",
    "paid_plans": [{{"name": "Pro", "price": "$20/mo", "notes": "..."}}],
    "pricing_last_verified": "2026-09-22"
  }},
  "official_url": "https://example.com",
  "logo_source_note": "Official brand asset",
  "related_tools": [],
  "launched": "2024",
  "platform": ["Web", "API"]
}}</code></pre>
        </div>
      </div>
    </main>
    """ + render_footer().replace('<script class="initial-js">\n    // Global data injection for instant client-side filtering\n  </script>', data_script)

    with open(DIST_DIR / "about.html", "w", encoding="utf-8") as f:
        f.write(about_html)

    print("Site build complete! Output written to dist/")

if __name__ == "__main__":
    build_site()

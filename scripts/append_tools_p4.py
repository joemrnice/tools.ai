#!/usr/bin/env python3
"""
Populates remaining categories (9 to 20) with high quality tools so every category has ~9 tools.
Total tools will reach ~180 across all 20 categories.
"""

import json
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent.parent / "data" / "tools"

def load_cat(cat):
    file_path = TOOLS_DIR / f"{cat}.json"
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_cat(cat, tools):
    file_path = TOOLS_DIR / f"{cat}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2)

def t(id, name, maker, tagline, category, subcategory, definition, why_it_matters, workplace_use_cases, who_uses_it, how_to_use, key_features, pricing, official_url, logo_source_note, related_tools, launched, platform):
    return {
        "id": id,
        "name": name,
        "maker": maker,
        "tagline": tagline,
        "category": category,
        "subcategory": subcategory,
        "definition": definition,
        "why_it_matters": why_it_matters,
        "workplace_use_cases": workplace_use_cases,
        "who_uses_it": who_uses_it,
        "how_to_use": how_to_use,
        "key_features": key_features,
        "pricing": pricing,
        "official_url": official_url,
        "logo_source_note": logo_source_note,
        "related_tools": related_tools,
        "launched": str(launched),
        "platform": platform
    }

def free(desc="Free forever for all users."):
    return {"model": "free", "has_free_tier": True, "free_tier_details": desc, "paid_plans": [], "pricing_last_verified": "2026-03-01"}

def freemium(free_desc, paid_list):
    return {"model": "freemium", "has_free_tier": True, "free_tier_details": free_desc, "paid_plans": paid_list, "pricing_last_verified": "2026-03-01"}

def paid(trial_desc, paid_list):
    return {"model": "paid", "has_free_tier": False, "free_tier_details": trial_desc, "paid_plans": paid_list, "pricing_last_verified": "2026-03-01"}

def add_tools(cat, new_tools):
    current = load_cat(cat)
    existing_ids = {item["id"] for item in current}
    for item in new_tools:
        if item["id"] not in existing_ids:
            current.append(item)
    save_cat(cat, current)

# Category 9: Data BI
add_tools("data_bi", [
    t("thoughtspot_sage", "ThoughtSpot Sage", "ThoughtSpot", "AI-powered search analytics engine combining natural language processing with enterprise BI.",
      "data_bi", "conversational-bi",
      "ThoughtSpot Sage is an AI analytics interface that enables business users to search cloud data warehouses using natural language questions to generate instant charts.",
      "ThoughtSpot Sage replaced static SQL dashboard requests with conversational data exploration over enterprise data warehouses (Snowflake, Databricks).",
      ["Asking natural language sales questions across Snowflake cloud data warehouses", "Generating automated KPI trend charts for executive dashboards", "Creating interactive data visualizations without writing SQL"],
      ["Business Analysts", "Executives", "Data Engineers", "Sales Operations"],
      "Type a data question into ThoughtSpot Sage search bar and review generated visualizations.",
      ["Natural language search to SQL conversion over Snowflake and Databricks", "Automated anomaly and trend detection", "Interactive Liveboard sharing"],
      paid("30-day free trial available for cloud teams.", [
          {"name": "Team", "price": "$95/month", "notes": "Includes 5,000 query capacity units."},
          {"name": "Enterprise", "price": "Custom pricing", "notes": "Unlimited data warehouse connections, custom governance."}
      ]),
      "https://www.thoughtspot.com", "Official ThoughtSpot asset", ["julius_ai", "tableau_pulse"], 2023, ["Web", "Mobile"]),

    t("hex_magic", "Hex Magic", "Hex Technologies", "AI assistant integrated into collaborative Python/SQL data science notebooks.",
      "data_bi", "data-science-notebooks",
      "Hex Magic is an AI copilot embedded in Hex's collaborative data workspace, helping data scientists write SQL queries, debug Python code, and build interactive dashboards.",
      "Hex Magic streamlines data science workflows by bridging natural language text directly into SQL and Python notebook cells.",
      ["Converting natural language prompts into SQL joins and window functions", "Debugging Python pandas code errors in data notebook cells", "Generating interactive dashboard components from notebook analysis"],
      ["Data Scientists", "Data Analysts", "Analytics Engineers"],
      "In any Hex notebook, press Cmd+K, type your data prompt, and accept generated SQL/Python code.",
      ["Inline SQL and Python code generation", "Automatic error diagnosis in notebook code cells", "Context-aware database schema indexing"],
      freemium("Free Community plan includes 3 projects.", [
          {"name": "Team", "price": "$36/user/month", "notes": "Unlimited projects, version control, AI magic features."},
          {"name": "Enterprise", "price": "Custom pricing", "notes": "SOC2 Type II, SSO, dedicated VPC deployment."}
      ]),
      "https://hex.tech", "Official Hex asset", ["julius_ai"], 2023, ["Web"]),

    t("akkio", "Akkio", "Akkio Inc.", "No-code AI predictive analytics platform for forecasting business metrics and lead scoring.",
      "data_bi", "predictive-analytics",
      "Akkio is a no-code machine learning and predictive analytics platform that enables business teams to train forecasting models and score leads directly from spreadsheets.",
      "Akkio democratized predictive modeling, allowing non-technical marketers and sales operations leads to run ML forecasts without data science engineering.",
      ["Predicting customer churn probabilities from CRM lead records", "Scoring incoming sales leads based on historical deal closure patterns", "Forecasting monthly revenue and product inventory demand"],
      ["Sales Operations", "Growth Marketers", "Business Analysts"],
      "Connect your data source at akkio.com, select the column you want to predict, and generate a predictive model.",
      ["No-code machine learning model training in under 10 minutes", "Generative report summaries and data clean-up", "Native integrations with HubSpot, Salesforce, Google Sheets"],
      paid("14-day free trial available.", [
          {"name": "Starter", "price": "$49/month", "notes": "Includes 1 million rows/month and automated predictions."},
          {"name": "Professional", "price": "$499/month", "notes": "Includes 10 million rows, real-time API deployments."}
      ]),
      "https://www.akkio.com", "Official Akkio asset", ["julius_ai"], 2021, ["Web"]),

    t("rows_ai", "Rows AI", "Rows", "AI-native spreadsheet platform with built-in web scraping, LLM formulas, and chart design.",
      "data_bi", "ai-spreadsheets",
      "Rows AI is a modern spreadsheet application that integrates generative AI functions directly into standard spreadsheet formulas, enabling automated data enrichment and analysis.",
      "Rows re-imagined the humble spreadsheet by adding native AI formula capabilities (`=ASK_AI()`) and built-in integration connectors.",
      ["Enriching company domain lists with executive emails using `=ASK_AI()`", "Summarizing customer feedback survey rows automatically", "Creating interactive web-publishable data charts from raw spreadsheets"],
      ["Data Analysts", "Marketers", "Sales Ops", "Founders"],
      "Open rows.com, enter standard spreadsheet data, and type `=ASK_AI(A1, \"Summarize\")` or click AI Analyst.",
      ["Native `=ASK_AI()` spreadsheet formula functions", "AI Analyst tool for automatic chart and summary generation", "50+ pre-built API integrations (Google Analytics, Stripe, HubSpot)"],
      freemium("Free plan includes unlimited spreadsheets and 50 AI integration credits/month.", [
          {"name": "Plus", "price": "$15/user/month ($12/mo annually)", "notes": "10,000 integration credits, custom domain sharing."},
          {"name": "Pro", "price": "$30/user/month ($25/mo annually)", "notes": "100,000 integration credits, priority execution."}
      ]),
      "https://rows.com", "Official Rows asset", ["julius_ai"], 2021, ["Web"]),

    t("polymer_search", "Polymer", "Polymer Search", "AI tool that instantly converts raw spreadsheets into searchable, interactive data portals.",
      "data_bi", "data-visualization",
      "Polymer is an AI data visualization platform that converts static CSV, Excel, or Airtable files into interactive, searchable web dashboards without code.",
      "Polymer simplifies data presentation by automatically detecting spreadsheet data types and rendering interactive filter grids.",
      ["Building interactive, searchable customer showcase databases", "Transforming e-commerce inventory spreadsheets into visual catalog portals", "Presenting marketing campaign performance metrics to clients"],
      ["Marketers", "E-commerce Managers", "Data Analysts"],
      "Upload a CSV or Excel file to polymersearch.com, select suggested layout cards, and share the interactive dashboard link.",
      ["Automated spreadsheet data type detection and card rendering", "AI Insights for highlighting statistical outliers", "Embeddable interactive web dashboards"],
      freemium("Free 14-day trial with full access.", [
          {"name": "Starter", "price": "$20/month ($10/mo annually)", "notes": "Includes 1 user, 100k data cells."},
          {"name": "Pro", "price": "$50/month ($25/mo annually)", "notes": "Includes 300k data cells, custom branding."}
      ]),
      "https://www.polymersearch.com", "Official Polymer asset", ["julius_ai", "rows_ai"], 2021, ["Web"]),

    t("chartpixel", "ChartPixel", "ChartPixel", "AI tool that cleans raw data files and automatically generates presentation-grade charts with insights.",
      "data_bi", "chart-generation",
      "ChartPixel is an AI tool designed to convert unstructured raw data files into annotated presentation-ready charts and natural language key takeaway bullets.",
      "ChartPixel automates the tedious chart formatting and insight annotation process for business slide decks.",
      ["Converting raw survey data into formatted pie and bar charts for slide decks", "Generating key statistical insight bullets from sales spreadsheets", "Cleaning dirty CSV files before generating visual reports"],
      ["Consultants", "Marketers", "Researchers", "Executives"],
      "Upload a CSV/Excel file at chartpixel.com, select key variables, and export generated charts.",
      ["Automated data cleaning and variable type detection", "Generates presentation-ready charts with explanatory text annotations", "Export to PowerPoint and PDF"],
      freemium("Free credits upon signup.", [
          {"name": "Pro", "price": "$12/month", "notes": "Unlimited chart exports and higher row processing limits."}
      ]),
      "https://chartpixel.com", "Official ChartPixel asset", ["julius_ai", "gamma"], 2023, ["Web"])
])

# Category 10: Presentation & Docs
add_tools("presentation_docs", [
    t("pitch_ai", "Pitch AI", "Pitch Software GmbH", "Collaborative presentation platform with integrated AI slide generation and deck editing.",
      "presentation_docs", "presentation-software",
      "Pitch AI is a collaborative presentation workspace that generates slide decks from prompts or text documents while offering professional design team collaboration tools.",
      "Pitch combines generative AI slide building with real-time multi-user editing and presentation engagement analytics.",
      ["Drafting startup pitch decks and client proposals in branded design systems", "Collaborating live with team members on presentation slide decks", "Tracking presentation view analytics and slide drop-off rates"],
      ["Founders", "Sales Reps", "Designers", "Consultants"],
      "Sign in at pitch.com, click 'Draft with AI', enter a prompt or brief, and customize the generated slides.",
      ["AI deck generator adhering to custom brand templates", "Real-time team co-editing and presentation recordings", "Slide view engagement analytics dashboard"],
      freemium("Free plan includes unlimited presentation creation and basic AI credits.", [
          {"name": "Pro", "price": "$20/user/month ($17/mo annually)", "notes": "Unlimited AI usage, custom fonts, video uploads, analytics."},
          {"name": "Business", "price": "$80/month", "notes": "Includes 5 seats, advanced brand controls."}
      ]),
      "https://pitch.com", "Official Pitch asset", ["gamma", "tome", "beautiful_ai"], 2020, ["Web", "macOS", "Windows", "iOS", "Android"]),

    t("slidebean", "Slidebean", "Slidebean Inc.", "AI pitch deck builder tailored for startup founders seeking investor funding.",
      "presentation_docs", "startup-pitch-decks",
      "Slidebean is an AI presentation tool specifically designed for startup founders, combining automated slide design with investor pitch deck templates and financial modeling.",
      "Slidebean focuses on the startup fundraising ecosystem, pairing AI slide arrangement with proven investor deck structures.",
      ["Building investor pitch decks matching successful Y Combinator startup formats", "Formatting pitch deck typography and alignment automatically", "Tracking investor engagement and time spent per slide"],
      ["Startup Founders", "Entrepreneurs", "Fundraising Consultants"],
      "Go to slidebean.com, choose an investor deck template, type your content, and let AI format the layout.",
      ["Automated AI slide layout and alignment engine", "Proven startup pitch deck template library", "Investor viewer analytics tracking"],
      paid("14-day free trial available.", [
          {"name": "All Access", "price": "$199/year (~$16.50/month)", "notes": "Unlimited deck creation, investor tracking analytics, financial models."}
      ]),
      "https://slidebean.com", "Official Slidebean asset", ["gamma", "pitch_ai"], 2014, ["Web"]),

    t("canva_magic_design", "Canva Magic Design", "Canva", "AI design tool inside Canva for generating presentations, social media assets, and documents.",
      "presentation_docs", "visual-design-docs",
      "Canva Magic Design is the generative AI suite embedded inside Canva, allowing users to create slide decks, social graphics, and visual documents from text prompts.",
      "Canva brought generative AI presentations to over 150 million users, offering seamless access to Canva's vast stock media library.",
      ["Generating presentation decks from raw text outlines inside Canva", "Creating branded social media graphic sets instantly", "Converting presentation slides into visual documents"],
      ["Marketers", "Designers", "Educators", "Small Business Owners"],
      "Open Canva, click Magic Design, type your presentation topic, choose a brand style, and generate.",
      ["Generates custom presentations with matching typography and stock images", "Magic Write inline copy generator", "Brand Hub integration for automated brand style matching"],
      freemium("Free access with daily Magic Design generation limits.", [
          {"name": "Canva Pro", "price": "$15/month ($120/year)", "notes": "Unlimited Magic Design features, full brand hub, 100M+ stock assets."}
      ]),
      "https://www.canva.com/magic-design/", "Official Canva asset", ["gamma", "beautiful_ai"], 2023, ["Web", "iOS", "Android", "Desktop"]),

    t("decktopus", "Decktopus", "Decktopus", "AI presentation generator built for fast corporate deck creation with voiceover narration.",
      "presentation_docs", "ai-presentations",
      "Decktopus is an AI presentation deck builder that automatically structures slides, adds speaker notes, suggests interactive forms, and embeds voiceover narration.",
      "Decktopus focuses on fast corporate presentations with built-in audience lead generation forms inside slides.",
      ["Creating interactive sales proposal decks with embedded lead capture forms", "Generating training slide decks complete with automated speaker notes", "Adding AI voiceover narration to online presentation links"],
      ["Sales Reps", "Corporate Trainers", "Consultants", "Educators"],
      "Visit decktopus.com, enter your presentation topic and target audience, and select a theme.",
      ["Automated slide layout with speaker notes generation", "Embedded lead capture forms and live polling inside slides", "AI voiceover narration generator"],
      freemium("Free plan includes basic deck creation and credits.", [
          {"name": "Pro AI", "price": "$14.99/month ($9.99/mo annually)", "notes": "750 AI credits/month, custom domain, PDF export."},
          {"name": "Business AI", "price": "$48/month ($36/mo annually)", "notes": "1,000 AI credits/month, team management, lead generation analytics."}
      ]),
      "https://www.decktopus.com", "Official Decktopus asset", ["gamma", "tome"], 2021, ["Web"]),

    t("prezi_ai", "Prezi AI", "Prezi", "AI-powered zooming presentation tool that transforms structured text into dynamic mind-map decks.",
      "presentation_docs", "zooming-presentations",
      "Prezi AI is the generative extension of Prezi's famous non-linear zooming presentation canvas, turning prompts into interactive, mind-map style presentations.",
      "Prezi AI brings non-linear spatial storytelling to AI presentation tools, creating engaging visual narrative maps.",
      ["Creating spatial, interactive presentation decks for keynote speeches", "Mapping complex business strategies into visual zooming presentation trees", "Delivering engaging virtual presentations via Prezi Video"],
      ["Keynote Speakers", "Educators", "Executives", "Consultants"],
      "Sign in at prezi.com, prompt Prezi AI with your presentation topic, and customize the visual canvas.",
      ["Generates non-linear zooming presentation spatial structures", "Prezi Video integration for presenting alongside video screens", "AI text and layout styling tools"],
      freemium("Free tier includes up to 3 public presentations.", [
          {"name": "Plus", "price": "$15/month ($12/mo annually)", "notes": "Unlimited presentations, PDF export, offline desktop app."},
          {"name": "Premium", "price": "$25/month ($19/mo annually)", "notes": "Advanced analytics, Prezi Video powerful features."}
      ]),
      "https://prezi.com", "Official Prezi asset", ["gamma", "tome"], 2023, ["Web", "Desktop", "iOS", "Android"])
])

print("Category 9 & 10 appended.")

#!/usr/bin/env python3
"""
Adds final 13 tools across categories with 7-8 tools to reach 180 total tools (9 tools in each of 20 categories).
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

# audio_voice (needs 1 -> 9)
add_tools("audio_voice", [
    t("adobe_podcast", "Adobe Podcast", "Adobe", "AI audio recording and enhancement suite for crystal-clear spoken audio.",
      "audio_voice", "audio-enhancement",
      "Adobe Podcast (formerly Project Shasta) is an AI-powered audio platform that removes background noise, enhances speech clarity, and enables text-based audio editing.",
      "Adobe Podcast transformed remote audio recording by turning noisy laptop mic tracks into studio-quality vocal tracks with one click.",
      ["Enhancing remote podcast audio recordings to professional microphone quality", "Editing audio tracks by deleting transcript text in a web browser", "Removing room echo and background noise from video voiceovers"],
      ["Podcasters", "Video Editors", "Content Creators", "Educators"],
      "Upload audio files to podcast.adobe.com/enhance or record in browser, and download cleaned audio.",
      ["Enhance Speech one-click studio sound processing", "Mic Check AI mic setup wizard", "Text-based web audio editor"],
      freemium("Free access to basic speech enhancement (up to 30 mins/day).", [
          {"name": "Adobe Express Premium", "price": "$9.99/month", "notes": "Unlocks bulk audio enhancement, strength controls, 4 hours/day."}
      ]),
      "https://podcast.adobe.com", "Official Adobe asset", ["descript", "elevenlabs"], 2022, ["Web"])
])

# data_bi (needs 1 -> 9)
add_tools("data_bi", [
    t("power_bi_copilot", "Power BI Copilot", "Microsoft", "AI analytics assistant integrated into Microsoft Power BI for natural language reporting.",
      "data_bi", "enterprise-bi",
      "Power BI Copilot is the AI assistant built into Microsoft Power BI, generating DAX measures, narrative visual summaries, and interactive report pages from text prompts.",
      "Power BI Copilot accelerates enterprise business intelligence reporting across the Microsoft data stack.",
      ["Generating executive DAX formulas and data calculations in Power BI", "Creating interactive report pages from simple text descriptions", "Summarizing complex data dashboard trends into narrative bullet points"],
      ["Data Analysts", "BI Developers", "Business Executives"],
      "Open Power BI Desktop, click Copilot, type your report prompt or DAX question, and insert generated visuals.",
      ["Natural language to DAX calculation generation", "Automated report page layout builder", "Executive narrative summary card generation"],
      paid("Requires Power BI Premium or Fabric capacity.", [
          {"name": "Power BI Pro", "price": "$10/user/month", "notes": "Requires Fabric F64 or Power BI Premium capacity for Copilot access."}
      ]),
      "https://powerbi.microsoft.com", "Official Microsoft asset", ["tableau_pulse", "thoughtspot_sage"], 2023, ["Desktop", "Web"])
])

# governance_security (needs 1 -> 9)
add_tools("governance_security", [
    t("whylogs", "WhyLabs", "WhyLabs", "AI observability and data health platform monitoring model drift and data quality in production.",
      "governance_security", "ai-observability",
      "WhyLabs is an AI observability platform that monitors machine learning models and data pipelines for data drift, performance degradation, and data quality issues.",
      "WhyLabs enables enterprise MLOps teams to catch model performance degradation before it impacts business operations.",
      ["Monitoring production ML model feature drift over time", "Detecting schema changes and missing values in automated data pipelines", "Auditing LLM prompt toxicity and sentiment trends"],
      ["MLOps Engineers", "Data Engineers", "AI Governance Leads"],
      "Install `whylogs` in Python, generate data profiles, and send to WhyLabs dashboard.",
      ["Open-source `whylogs` profiling library with lightweight data privacy", "Automated model drift and data quality alerts", "Supports tabular, image, and text LLM data"],
      freemium("Free Developer tier for up to 2 model monitor projects.", [
          {"name": "Enterprise", "price": "Custom pricing", "notes": "Unlimited model monitoring, SOC 2 compliance, dedicated support."}
      ]),
      "https://whylabs.ai", "Official WhyLabs asset", ["robust_intelligence", "arize_phoenix"], 2020, ["Python Library", "Web"])
])

# hr_recruiting (needs 1 -> 9)
add_tools("hr_recruiting", [
    t("charthop_ai", "ChartHop", "ChartHop", "People analytics platform providing AI organization charts, headcount planning, and compensation analysis.",
      "hr_recruiting", "people-analytics",
      "ChartHop is an AI people analytics platform that consolidates HRIS data into interactive organization charts, headcount planning forecasts, and compensation benchmarks.",
      "ChartHop unifies HRIS data silos to give executives clear visibility into organization structure and headcount spend.",
      ["Visualizing interactive company org charts and reporting lines", "Modeling future headcount budgets and compensation equity scenarios", "Analyzing employee turnover and performance metrics"],
      ["HR Directors", "People Ops", "CFOs", "Executives"],
      "Connect ChartHop to your HRIS (BambooHR, Gusto, Workday) and view people analytics dashboards.",
      ["Interactive visual organization chart with custom field filters", "Headcount scenario planning and compensation modeling", "HRIS data integrations with major payroll tools"],
      paid("14-day free trial available.", [
          {"name": "Standard", "price": "$8/user/month", "notes": "Includes org charts, basic people analytics, HRIS sync."},
          {"name": "Premium", "price": "$12/user/month", "notes": "Advanced headcount planning, compensation reviews."}
      ]),
      "https://www.charthop.com", "Official ChartHop asset", ["textio", "paradox_ai"], 2019, ["Web"])
])

# legal_finance (needs 1 -> 9)
add_tools("legal_finance", [
    t("casetext_research", "Casetext", "Thomson Reuters / Casetext", "AI legal research database providing CARA AI document analysis and case law search.",
      "legal_finance", "legal-research",
      "Casetext is an AI-powered legal research platform that analyzes litigation briefs and retrieves relevant judicial case law precedents using CARA AI.",
      "Casetext pioneered AI litigation research, matching uploaded legal briefs directly to supporting judicial precedents.",
      ["Uploading opposing counsel litigation briefs to automatically find counter-precedents", "Searching judicial statutes and case law across federal and state jurisdictions", "Validating case law citation accuracy"],
      ["Litigators", "Law Firm Associates", "Legal Researchers"],
      "Sign in at casetext.com, upload a brief to CARA AI, and review suggested case law citations.",
      ["CARA AI document-based legal research engine", "Comprehensive US federal and state primary law database", "Judicial citation analysis and case law summaries"],
      paid("14-day free trial available.", [
          {"name": "Basic Research", "price": "$110/user/month", "notes": "Includes primary law search and appellate briefs."},
          {"name": "Advanced Research", "price": "$220/user/month", "notes": "Includes CARA AI brief analyzer and expert witness data."}
      ]),
      "https://casetext.com", "Official Casetext asset", ["cocounsel", "harvey_ai"], 2013, ["Web"])
])

# marketing_seo (needs 2 -> 9)
add_tools("marketing_seo", [
    t("buzzsumo_ai", "BuzzSumo", "Brand24 / BuzzSumo", "Content research and influencer discovery platform analyzing viral social media engagement.",
      "marketing_seo", "content-research",
      "BuzzSumo is a content research tool that analyzes social media shares and backlink trends to identify top-performing content ideas and key influencers.",
      "BuzzSumo provides content strategists with data-backed insights on which article topics generate viral social media shares.",
      ["Researching viral content headlines and topic ideas across social media", "Identifying key niche influencers for brand campaign outreach", "Monitoring competitor content performance"],
      ["Content Strategists", "PR Leads", "Social Media Managers"],
      "Enter a keyword or domain at buzzsumo.com, view top shared content, and export reports.",
      ["Content Analyzer indexing billions of social media posts", "Influencer discovery and outreach database", "Brand mention monitoring alerts"],
      paid("30-day free trial available.", [
          {"name": "Content Creation", "price": "$199/month ($159/mo annually)", "notes": "1 user, 80 searches/day, content research."},
          {"name": "PR & Comms", "price": "$299/month ($239/mo annually)", "notes": "5 users, media database, real-time alerts."}
      ]),
      "https://buzzsumo.com", "Official BuzzSumo asset", ["semrush_one2tree", "ahrefs_brand"], 2014, ["Web"]),

    t("marketmuse", "MarketMuse", "MarketMuse, Inc.", "AI content strategy and SEO platform providing domain content auditing and topic modeling.",
      "marketing_seo", "content-strategy",
      "MarketMuse is an AI content intelligence platform that analyzes domain content authority to build data-driven SEO content plans and content briefs.",
      "MarketMuse focuses on domain topic authority, telling content teams exactly where their site has content gaps compared to competitors.",
      ["Auditing website content authority and identifying high-value topic gaps", "Generating detailed SEO content briefs for staff writers", "Planning quarterly editorial content roadmaps"],
      ["SEO Directors", "Content Strategists", "Managing Editors"],
      "Enter domain URL at marketmuse.com, review topic authority scores, and build content briefs.",
      ["First-party AI topic modeling engine", "Content Inventory & Audit tool for domain authority mapping", "Automated Content Brief generator"],
      freemium("Free tier includes 10 queries/month and 1 user.", [
          {"name": "Standard", "price": "$149/month", "notes": "Includes 100 queries/month and full topic modeling."},
          {"name": "Team", "price": "$399/month", "notes": "3 seats, un-capped queries, custom domain tracking."}
      ]),
      "https://www.marketmuse.com", "Official MarketMuse asset", ["surfer_seo", "semrush_one2tree"], 2015, ["Web"])
])

# meeting_notes (needs 1 -> 9)
add_tools("meeting_notes", [
    t("krisp_ai", "Krisp", "Krisp Technologies", "AI noise-cancellation app that removes background noise, echo, and generates meeting notes.",
      "meeting_notes", "audio-noise-cancellation",
      "Krisp is an AI desktop application that removes background noise, room echo, and voices from microphone and speaker audio during live calls, while auto-generating meeting notes.",
      "Krisp is the gold standard for real-time background noise cancellation, allowing remote workers to take calls in noisy cafes or home environments.",
      ["Canceling barking dogs, construction, and cafe noise during live Zoom calls", "Removing room acoustic echo from microphone audio", "Generating automated meeting transcripts and summaries"],
      ["Remote Workers", "Customer Support Agents", "Executives", "Podcasters"],
      "Download Krisp on macOS/Windows, select Krisp Microphone/Speaker in Zoom/Teams, and toggle noise cancellation.",
      ["Real-time bi-directional AI noise and echo cancellation", "Automatic meeting recording and transcription", "Works with all video conferencing apps (Zoom, Teams, Meet)"],
      freemium("Free tier includes 60 minutes/day of noise cancellation.", [
          {"name": "Pro", "price": "$12/user/month ($8/mo annually)", "notes": "Unlimited noise cancellation, unlimited meeting notes, central billing."}
      ]),
      "https://krisp.ai", "Official Krisp asset", ["otter_ai", "fathom"], 2017, ["macOS", "Windows", "Desktop"])
])

# nocode_automation (needs 1 -> 9)
add_tools("nocode_automation", [
    t("make_nocode", "Make", "Celonis / Make", "Visual no-code automation platform for connecting APIs and AI modules visually.",
      "nocode_automation", "visual-automation",
      "Make (formerly Integromat) is a visual no-code automation workspace where users build complex data scenarios connecting web apps, databases, and AI models.",
      "Make offers unmatched visual control over multi-step conditional branching and data iteration.",
      ["Automating lead routing from web forms into CRMs and Slack", "Building complex multi-app data sync pipelines", "Processing incoming documents with OpenAI modules"],
      ["Operations Managers", "Automation Engineers", "No-Code Developers"],
      "Drag and drop app modules on the Make canvas, connect APIs, and turn on the scenario.",
      ["Visual drag-and-drop scenario builder with infinite branching", "1,500+ pre-built app connectors", "Native OpenAI and Claude processing modules"],
      freemium("1,000 free operations/month.", [
          {"name": "Core", "price": "$10.59/month ($9/mo annually)", "notes": "10,000 operations/month, unlimited active scenarios."}
      ]),
      "https://www.make.com", "Official Make asset", ["zapier_central", "n8n"], 2020, ["Web"])
])

# presentation_docs (needs 1 -> 9)
add_tools("presentation_docs", [
    t("simplified_ai", "Simplified", "Simplified", "All-in-one AI platform for graphic design, video editing, copywriting, and presentation generation.",
      "presentation_docs", "content-suite",
      "Simplified is an all-in-one content creation workspace offering AI presentation generation, graphic design tools, video editing, and copywriting.",
      "Simplified combines presentation design with social media post scheduling in a single workspace.",
      ["Generating presentation decks from text briefs", "Creating matching social media graphics for presentations", "Scheduling multi-channel social media posts"],
      ["Marketers", "Small Business Owners", "Content Creators"],
      "Go to simplified.com, select AI Presentation, type your prompt, and customize.",
      ["AI presentation, graphic design, and video editor tools", "Social media post scheduling dashboard", "Multi-brand asset kits"],
      freemium("Free tier includes basic design tools and AI credits.", [
          {"name": "Pro", "price": "$18/month ($12/mo annually)", "notes": "1 user, 100k AI words, advanced presentation tools."}
      ]),
      "https://simplified.com", "Official Simplified asset", ["gamma", "canva_magic_design"], 2021, ["Web", "iOS", "Android"])
])

# productivity_automation (needs 1 -> 9)
add_tools("productivity_automation", [
    t("shortcut_ai", "Shortcuts AI", "Apple", "Native iOS and macOS automation engine utilizing local device AI and app actions.",
      "productivity_automation", "native-automation",
      "Apple Shortcuts is the native automation system built into iOS and macOS, enabling users to combine app actions, Siri prompts, and system controls into custom automated workflows.",
      "Apple Shortcuts provides deep native system hardware integration across iPhones, iPads, and Mac computers.",
      ["Building custom one-tap Siri voice shortcuts for work tasks", "Automating image resizing and document PDF exports on Mac", "Creating custom location-based reminders"],
      ["Mac Power Users", "Mobile Professionals", "Developers"],
      "Open the Shortcuts app on Mac/iPhone, click '+', add action blocks, and trigger via Siri or hotkey.",
      ["Native deep iOS and macOS system integration", "Siri voice trigger support", "Syncs across Apple hardware ecosystem"],
      free("Built natively into iOS, iPadOS, and macOS."),
      "https://support.apple.com/guide/shortcuts/welcome/ios", "Official Apple asset", ["raycast_ai"], 2018, ["macOS", "iOS", "iPadOS"])
])

# research_search (needs 1 -> 9)
add_tools("research_search", [
    t("bing_search_ai", "Microsoft Copilot Search", "Microsoft", "AI-powered web search engine grounded in Bing search index and GPT-4o.",
      "research_search", "ai-search-engine",
      "Microsoft Copilot Search (formerly Bing Chat) is an AI search engine that combines real-time Bing web index data with GPT-4o reasoning to deliver cited answers.",
      "Copilot Search brought conversational AI search directly into the mainstream Microsoft Bing search engine.",
      ["Searching live news events and market pricing with web source links", "Comparing product features with side-by-side table summaries", "Generating images via DALL-E 3 directly inside search"],
      ["Researchers", "Executives", "Students", "General Users"],
      "Go to copilot.microsoft.com or bing.com, select Search/Chat, and enter your query.",
      ["Grounded in Bing web search index for real-time accuracy", "Inline source citation links", "Integrated DALL-E 3 image generator"],
      free("Free for all web users at copilot.microsoft.com."),
      "https://copilot.microsoft.com", "Official Microsoft asset", ["perplexity", "chatgpt"], 2023, ["Web", "Windows", "Edge Browser"])
])

# sales_crm (needs 1 -> 9)
add_tools("sales_crm", [
    t("lusha_ai", "Lusha", "Lusha", "B2B sales prospecting database and contact intelligence platform with AI lead recommendations.",
      "sales_crm", "b2b-contact-data",
      "Lusha is a B2B sales intelligence tool that provides verified phone numbers, direct email addresses, and company insights for sales prospecting.",
      "Lusha provides sales reps with reliable direct phone numbers and B2B emails via a convenient browser extension.",
      ["Finding direct cell phone numbers for B2B target decision-makers", "Enriching corporate CRM leads with company headcount and industry data", "Sourcing prospects directly while browsing LinkedIn"],
      ["Sales Development Reps", "Account Executives", "Recruiters"],
      "Install Lusha Chrome extension, visit LinkedIn prospect profiles, and reveal contact info.",
      ["85M+ direct phone numbers and B2B contact database", "Chrome extension for instant contact reveal on LinkedIn", "Salesforce and HubSpot CRM integration"],
      freemium("Free plan includes 5 contact credits/month.", [
          {"name": "Pro", "price": "$49/user/month ($36/mo annually)", "notes": "480 contact credits/year, export data."},
          {"name": "Premium", "price": "$79/user/month ($59/mo annually)", "notes": "960 contact credits/year, usage analytics."}
      ]),
      "https://www.lusha.com", "Official Lusha asset", ["apollo_ai", "clay_run"], 2016, ["Web", "Chrome Extension"])
])

print("Final tools added successfully.")

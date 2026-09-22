#!/usr/bin/env python3
"""
Populates categories 13 through 20 to finish the 180+ tool dataset.
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

# Category 13: Customer Support & Chatbots
add_tools("customer_support", [
    t("ada", "Ada", "Ada Support Inc.", "Enterprise AI customer service agent platform resolving complex multi-channel support tickets.",
      "customer_support", "ai-customer-service",
      "Ada is an enterprise AI customer service platform that resolves customer support inquiries across messaging, email, voice, and web chat.",
      "Ada provides enterprise organizations with no-code AI agent building that integrates directly into backend systems (Zendesk, Salesforce, Shopify).",
      ["Resolving automated order tracking, refund requests, and billing queries", "Deploying multi-channel AI support agents across web, mobile app, and WhatsApp", "Executing automated backend account actions via API webhooks"],
      ["Customer Support Directors", "VP of Customer Experience", "Support Operations"],
      "Build agent workflows in Ada's visual dashboard, sync help documentation, and deploy the messaging widget.",
      ["Multi-channel resolution engine (Web, Mobile, SMS, Voice, WhatsApp)", "No-code AI agent reasoning flow builder", "Native integrations with Zendesk, Salesforce, and Shopify"],
      paid("Custom enterprise quotes based on resolution volume.", [
          {"name": "Enterprise Resolution Plan", "price": "Custom annual contract", "notes": "Calculated per ticket resolution and channel support scope."}
      ]),
      "https://www.ada.cx", "Official Ada asset", ["fin_intercom", "zendesk_ai"], 2016, ["Web", "iOS", "Android", "API"]),

    t("tidio_lyro", "Lyro by Tidio", "Tidio", "Conversational AI support bot for SMBs and e-commerce stores that answers customer questions.",
      "customer_support", "smb-chatbots",
      "Lyro is a conversational AI customer support bot developed by Tidio, designed for small businesses and e-commerce stores to automate customer inquiries.",
      "Lyro offers small e-commerce businesses accessible AI support bot setup that syncs with Shopify in under 5 minutes.",
      ["Answering e-commerce product questions and shipping policy inquiries 24/7", "Reducing ticket volume for small support teams", "Handing off complex sales leads to live human chat agents"],
      ["E-commerce Store Owners", "SMB Customer Support Reps", "Shopify Merchants"],
      "Connect Tidio to your Shopify store or website, upload FAQ URLs, and activate Lyro.",
      ["5-minute setup trained directly on website FAQ pages", "Shopify and WordPress live chat integration", "Seamless human agent handoff"],
      freemium("Free tier includes 50 AI conversations.", [
          {"name": "Lyro AI Add-on", "price": "$39/month", "notes": "Includes 500 AI conversations/month."},
          {"name": "Tidio Plus", "price": "$394/month", "notes": "Custom AI conversations, dedicated support manager."}
      ]),
      "https://www.tidio.com/lyro/", "Official Tidio asset", ["fin_intercom", "chatling"], 2023, ["Web", "Shopify", "WordPress"]),

    t("chatling", "Chatling", "Chatling", "No-code AI chatbot builder trained on custom website content, PDFs, and knowledge bases.",
      "customer_support", "custom-chatbots",
      "Chatling is a no-code AI chatbot platform that allows businesses to build custom customer support chatbots trained on their website content and documents.",
      "Chatling simplifies custom support bot creation for non-technical teams with easy document uploading and web crawling.",
      ["Building custom website support chatbots trained on PDF documentation", "Answering visitor sales questions on SaaS marketing websites", "Capturing sales lead contact details directly inside chat windows"],
      ["Small Business Owners", "Marketers", "Support Leads"],
      "Sign in at chatling.ai, input your website URL or upload PDF manuals, customize the chat widget, and embed.",
      ["Train AI on website URLs, PDFs, DOCX, and Notion pages", "Custom branding and chat widget styling", "Lead capture forms and visitor analytics"],
      freemium("Free plan includes 1 chatbot and 350 response credits/month.", [
          {"name": "Basic", "price": "$15/month ($12/mo annually)", "notes": "2 chatbots, 2,000 response credits/month, no watermark."},
          {"name": "Pro", "price": "$35/month ($28/mo annually)", "notes": "5 chatbots, 5,000 response credits/month, auto-sync data sources."}
      ]),
      "https://chatling.ai", "Official Chatling asset", ["fin_intercom", "tidio_lyro"], 2023, ["Web"]),

    t("forethought", "Forethought", "Forethought Technologies", "Generative AI customer service platform automating triage, resolution, and agent coaching.",
      "customer_support", "enterprise-cx",
      "Forethought is an enterprise generative AI platform for customer service, featuring Solve (autonomous resolution), Triage (ticket routing), and Assist (agent copilot).",
      "Forethought brought deep learning intent resolution to enterprise support, reducing cost per ticket dramatically.",
      ["Automating immediate support ticket resolution across email and chat", "Routing incoming support tickets based on urgency and customer sentiment", "Assisting human support agents with inline answer suggestions"],
      ["Enterprise CX Executives", "Support Operations Directors"],
      "Integrate Forethought with your enterprise helpdesk (Zendesk, Salesforce Service Cloud), and configure resolution rules.",
      ["Solve autonomous AI ticket resolution engine", "Triage automated ticket routing and sentiment analysis", "Assist in-inbox agent copilot"],
      paid("Enterprise annual quotes based on ticket volume.", [
          {"name": "Enterprise Subscription", "price": "Custom annual contract", "notes": "Priced per ticket resolution and helpdesk integration scope."}
      ]),
      "https://forethought.ai", "Official Forethought asset", ["fin_intercom", "zendesk_ai", "ada"], 2018, ["Web", "Zendesk", "Salesforce Service Cloud"]),

    t("kustomer_iq", "Kustomer IQ", "Kustomer / Meta", "AI customer service automation platform optimizing omnichannel customer service conversations.",
      "customer_support", "omnichannel-cx",
      "Kustomer IQ is the artificial intelligence engine embedded in the Kustomer CRM, automating routing, sentiment analysis, and self-service chat workflows.",
      "Kustomer IQ unifies customer CRM data history with conversational AI chat across messaging apps.",
      ["Providing customer support agents with a 360-degree timeline of customer interactions", "Automating self-service chat workflows on WhatsApp and Instagram", "Predicting customer sentiment during support interactions"],
      ["Customer Service Directors", "E-commerce Support Leads"],
      "Enable Kustomer IQ inside Kustomer CRM dashboard and set up self-service workflows.",
      ["Omnichannel timeline CRM integration", "Self-service conversational bot builder", "Automated ticket sentiment scoring"],
      paid("Requires active Kustomer CRM platform subscription.", [
          {"name": "Enterprise", "price": "$89/user/month", "notes": "Includes core Kustomer IQ routing and self-service bots."},
          {"name": "Ultimate", "price": "$139/user/month", "notes": "Advanced AI capabilities, custom SLAs."}
      ]),
      "https://www.kustomer.com", "Official Kustomer asset", ["zendesk_ai", "fin_intercom"], 2017, ["Web", "iOS", "Android"]),

    t("chatbase", "Chatbase", "Chatbase", "Custom AI chatbot builder that creates ChatGPT-like bots trained on your data.",
      "customer_support", "custom-chatbots",
      "Chatbase is a popular no-code AI chatbot creation platform that lets users build a custom support bot trained on files, web links, and Notion pages in minutes.",
      "Chatbase popularized quick, custom knowledge-base chatbot creation for creators and startups.",
      ["Embedding a custom AI support chatbot on marketing websites", "Creating internal documentation Q&A bots for employees", "Answering customer product queries on e-commerce sites"],
      ["Founders", "Marketers", "Support Reps", "Web Developers"],
      "Upload documents or enter website links at chatbase.co, customize chatbot appearance, and paste embed script.",
      ["Trained on PDFs, text files, website URLs, and Notion", "Custom domain and chat widget branding options", "Lead generation collection forms"],
      freemium("Free plan includes 1 chatbot and 20 message credits/month.", [
          {"name": "Hobby", "price": "$19/month", "notes": "2 chatbots, 2,000 message credits/month."},
          {"name": "Standard", "price": "$99/month", "notes": "5 chatbots, 10,000 message credits/month, custom domain."}
      ]),
      "https://www.chatbase.co", "Official Chatbase asset", ["chatling", "fin_intercom"], 2023, ["Web"]),

    t("customgpt_ai", "CustomGPT.ai", "CustomGPT", "Privacy-first enterprise custom AI chatbot builder with zero hallucination protection.",
      "customer_support", "enterprise-chatbots",
      "CustomGPT.ai is an enterprise custom AI platform that builds chatbots trained on company data with strict anti-hallucination guardrails and citations.",
      "CustomGPT.ai focuses heavily on enterprise data privacy and accurate citation backings for every answer.",
      ["Building internal employee knowledge base Q&A bots with exact document citation links", "Deploying customer support chatbots with zero hallucination protection", "Searching across enterprise technical manuals"],
      ["Enterprise IT Directors", "Customer Support Leads", "Knowledge Managers"],
      "Upload data sources at customgpt.ai, configure persona guardrails, and deploy via widget or API.",
      ["Zero hallucination guardrails with document citation links", "Supports 1,400+ file formats and site crawling", "SOC 2 Type II certified data security"],
      paid("14-day free trial available.", [
          {"name": "Standard", "price": "$99/month", "notes": "10 chatbots, 5,000 query credits/month."},
          {"name": "Premium", "price": "$499/month", "notes": "100 chatbots, 50,000 query credits/month, API access."}
      ]),
      "https://customgpt.ai", "Official CustomGPT asset", ["chatbase", "fin_intercom"], 2023, ["Web", "API"])
])

# Category 14: Sales & CRM
add_tools("sales_crm", [
    t("apollo_ai", "Apollo.io AI", "Apollo.io", "All-in-one sales intelligence and engagement platform with AI lead recommendations.",
      "sales_crm", "sales-intelligence",
      "Apollo.io is a sales intelligence platform featuring a database of 275 million+ B2B contacts, integrated with AI lead scoring, email writing, and call intelligence.",
      "Apollo combined contact database lookup with automated AI outbound sales sequences in a single workspace.",
      ["Finding verified prospect phone numbers and emails for target accounts", "Generating personalized outbound email cadences using AI Assistant", "Automating multi-touch sales sequences across email and phone calls"],
      ["Sales Development Reps", "Account Executives", "Founders", "Growth Marketers"],
      "Search prospect leads at apollo.io, add to an AI sales sequence, and track email engagement.",
      ["275M+ B2B prospect database with email/phone verification", "AI Power Assistant for personalized email copy generation", "Dialer and automated sequence execution"],
      freemium("Free plan includes 60 mobile credits and 120 export credits/year.", [
          {"name": "Basic", "price": "$59/user/month ($49/mo annually)", "notes": "Unlimited email credits, 2,500 export credits/year."},
          {"name": "Professional", "price": "$99/user/month ($79/mo annually)", "notes": "Uncapped email send, AI assistant, call recording."}
      ]),
      "https://www.apollo.io", "Official Apollo asset", ["clay_run", "gong_io"], 2018, ["Web", "Chrome Extension"]),

    t("salesforce_einstein", "Salesforce Einstein AI", "Salesforce", "Enterprise CRM AI layer delivering lead scoring, automated deal insights, and predictive analytics.",
      "sales_crm", "enterprise-crm-ai",
      "Salesforce Einstein is the conversational and predictive AI layer built natively into Salesforce CRM, providing predictive lead scoring, opportunity insights, and automated email drafting.",
      "Einstein brings predictive AI directly into the world's most widely used enterprise CRM platform.",
      ["Predictively scoring incoming sales leads based on historical deal conversion data", "Drafting personalized sales emails directly inside Salesforce Sales Cloud", "Generating automated pipeline forecasting summaries for CROs"],
      ["Enterprise Account Executives", "VP of Sales", "Sales Operations Leads"],
      "Enable Einstein AI features in Salesforce Setup and view predictive scores on Opportunity records.",
      ["Einstein Lead & Opportunity Scoring predictive models", "Einstein GPT for automated email and response drafting", "Seamless integration with Sales Cloud and Service Cloud"],
      paid("Requires active Salesforce Sales Cloud license.", [
          {"name": "Sales Cloud Enterprise + Einstein", "price": "$165-$300/user/month", "notes": "Includes core Einstein predictive scoring and generative AI capabilities."}
      ]),
      "https://www.salesforce.com/products/einstein/overview/", "Official Salesforce asset", ["gong_io", "hubspot_breeze"], 2016, ["Web", "Mobile"]),

    t("hubspot_breeze", "HubSpot Breeze AI", "HubSpot", "AI intelligence copilot and autonomous agents embedded across HubSpot CRM.",
      "sales_crm", "crm-ai-copilot",
      "HubSpot Breeze is the AI intelligence suite integrated across HubSpot CRM, featuring Breeze Copilot (AI assistant), Breeze Agents (automated marketing/sales bots), and Breeze Intelligence (data enrichment).",
      "HubSpot Breeze provides accessible AI automation for inbound sales, content generation, and CRM data enrichment.",
      ["Enriching incoming CRM lead records with company headcount and revenue data", "Drafting blog posts, social graphics, and sales emails inside HubSpot", "Deploying automated customer service and prospecting agents"],
      ["Inbound Marketers", "Sales Reps", "Customer Success Leads", "SMB Owners"],
      "Access Breeze Copilot in your HubSpot portal toolbar or trigger Breeze Intelligence enrichment.",
      ["Breeze Intelligence automated CRM B2B data enrichment", "Breeze Copilot for inline content generation and data lookup", "Autonomous Social Media and Prospecting Agents"],
      freemium("Core AI features included in HubSpot Free tools.", [
          {"name": "Sales Hub Professional", "price": "$100/user/month ($90/mo annually)", "notes": "Includes full Breeze AI capabilities and sequence automation."}
      ]),
      "https://www.hubspot.com/products/breeze", "Official HubSpot asset", ["salesforce_einstein", "clay_run"], 2024, ["Web", "Mobile"]),

    t("instantly_ai", "Instantly.ai", "Instantly", "Cold email outreach platform featuring automated warmup, lead database, and AI copywriter.",
      "sales_crm", "cold-email",
      "Instantly.ai is a cold email outreach platform designed to scale outbound email deliverability with automated inbox warmup, multi-account rotation, and AI lead copy generation.",
      "Instantly solved cold email deliverability at scale by allowing users to connect unlimited sending accounts with automated warmup.",
      ["Scaling cold email outreach across dozens of dedicated domain accounts", "Warming up new sales sending domains automatically to prevent spam flags", "Generating personalized outbound email cadences using AI"],
      ["Sales Development Reps", "Outbound Agencies", "Founders"],
      "Connect sending domains at instantly.ai, upload prospect leads, enable warmup, and launch sequences.",
      ["Unlimited email sending account connections and automated warmup", "AI Copywriter for personalized outbound email generation", "CRM Unibox for managing prospect email replies"],
      paid("14-day free trial available.", [
          {"name": "Growth", "price": "$37/month ($30/mo annually)", "notes": "5,000 leads, 1,000 monthly emails, unlimited warmup."},
          {"name": "Hypergrowth", "price": "$97/month ($77/mo annually)", "notes": "25,000 leads, 125,000 monthly emails, premium support."}
      ]),
      "https://instantly.ai", "Official Instantly asset", ["clay_run", "smartlead"], 2021, ["Web"]),

    t("smartlead", "Smartlead.ai", "Smartlead", "Enterprise cold email outreach infrastructure platform built for agencies and SDR teams.",
      "smartlead", "cold-email-infrastructure",
      "Smartlead.ai is a cold email automation engine designed for sales agencies and growth teams, offering unlimited email account warmup, master inbox management, and webhooks.",
      "Smartlead provides enterprise-grade infrastructure for managing complex multi-domain outbound sales operations.",
      ["Managing outbound sales cold email infrastructure for multiple client accounts", "Automating multi-channel email sequences with webhook triggers", "Tracking centralized master inbox responses across 100+ domains"],
      ["Outbound Agencies", "Sales Operations Leads", "Growth Hackers"],
      "Connect domains at smartlead.ai, set up sequence schedules, and manage replies in Master Inbox.",
      ["Unlimited email account warmup and domain rotation", "Master Inbox for centralized response management", "API webhooks for integration with Clay and CRM platforms"],
      paid("14-day free trial available.", [
          {"name": "Basic", "price": "$39/month ($33/mo annually)", "notes": "2,000 active leads, 6,000 emails/month, unlimited warmup."},
          {"name": "Pro", "price": "$94/month ($78/mo annually)", "notes": "30,000 active leads, 150,000 emails/month, master inbox."}
      ]),
      "https://www.smartlead.ai", "Official Smartlead asset", ["instantly_ai", "clay_run"], 2022, ["Web"]),

    t("outreach_kaia", "Outreach Kaia", "Outreach", "Real-time sales execution and conversation intelligence assistant built into Outreach sales platform.",
      "sales_crm", "sales-execution",
      "Outreach Kaia (Knowledge AI Assistant) is a real-time sales conversation assistant that provides Account Executives with live content prompts, objection handling cards, and automated call summaries during video calls.",
      "Kaia delivers live, in-call assistance to sales reps, surfacing relevant competitive battlecards during live prospect meetings.",
      ["Surfacing real-time competitive battlecards during live prospect sales calls", "Generating automated post-call meeting summaries and action item lists", "Syncing call notes automatically into Outreach deal pipelines"],
      ["Account Executives", "Sales Managers", "Sales Enablement"],
      "Enable Kaia in your Outreach workspace, and Kaia will join Zoom/Teams calls to provide live prompts.",
      ["Real-time in-call competitive battlecard prompts", "Automated post-call summary and action item capture", "Direct integration with Outreach sales execution platform"],
      paid("Enterprise custom annual quotes.", [
          {"name": "Enterprise Subscription", "price": "Custom annual contract", "notes": "Priced per user seat on top of Outreach sales execution platform."}
      ]),
      "https://www.outreach.io", "Official Outreach asset", ["gong_io", "salesforce_einstein"], 2020, ["Web"])
])

# Category 15: Research & AI Search Engines
add_tools("research_search", [
    t("scite_ai", "Scite.ai", "Scite Inc.", "Smart citation research platform that analyzes whether academic papers support or contrast findings.",
      "research_search", "academic-citations",
      "Scite.ai is an academic research tool that uses AI to analyze research paper citations, showing contextual excerpts and categorizing whether citations support or contrast a study's claims.",
      "Scite introduced 'Smart Citations', allowing researchers to evaluate paper reliability by seeing how subsequent studies cited the research.",
      ["Verifying whether a scientific claim is supported or contested in peer-reviewed literature", "Evaluating the citation reliability of academic authors and journals", "Writing literature review summaries backed by Smart Citations"],
      ["Academic Researchers", "Medical Officers", "PhDs", "Science Writers"],
      "Search a topic or DOI at scite.ai, view Smart Citation breakdowns, and evaluate paper support.",
      ["Smart Citations showing citation context and supporting/contrasting classification", "Assistant for asking research questions grounded in scientific literature", "Indexes over 1.2 billion citation statements"],
      paid("7-day free trial available.", [
          {"name": "Individual", "price": "$20/month ($12/mo annually)", "notes": "Unlimited Smart Citation searches, AI Assistant access."},
          {"name": "Team", "price": "$24/user/month", "notes": "Shared research reference libraries and admin controls."}
      ]),
      "https://scite.ai", "Official Scite asset", ["consensus", "elicit", "perplexity"], 2018, ["Web", "Extension"]),

    t("semantic_scholar", "Semantic Scholar", "Allen Institute for AI", "Free AI-powered academic search engine indexing over 200M+ research papers.",
      "research_search", "academic-search",
      "Semantic Scholar is a free, non-profit AI research tool developed by the Allen Institute for AI that indexes over 200 million academic papers, extracting key citations, topics, and one-sentence TLDR summaries.",
      "Semantic Scholar serves as the foundational open database powering many commercial academic AI tools.",
      ["Searching across millions of computer science, biomedical, and physics research papers", "Reading one-sentence AI TLDR summaries of complex academic studies", "Exploring citation graphs to trace research lineage"],
      ["Researchers", "Students", "Data Scientists", "Academics"],
      "Visit semanticscholar.org, enter your research query or paper title, and read AI TLDR summaries.",
      ["Free access to 200M+ indexed research papers", "AI-generated TLDR paper summaries", "Citation velocity and influential citation tracking"],
      free("Free non-profit service funded by the Allen Institute for AI."),
      "https://www.semanticscholar.org", "Official Allen AI asset", ["consensus", "elicit"], 2015, ["Web"]),

    t("notebooklm", "NotebookLM", "Google", "Personal AI research notebook grounded strictly in your uploaded documents and notes.",
      "research_search", "research-notebook",
      "NotebookLM is an AI research notebook developed by Google Labs. Grounded strictly in your uploaded documents (PDFs, Google Docs, slides, web links), it synthesizes notes, generates study guides, and creates realistic Audio Overviews (AI podcasts).",
      "NotebookLM gained viral acclaim for its 'Audio Overview' feature, which converts boring PDF research documents into engaging, conversational two-host podcast audio discussions.",
      ["Generating an interactive AI audio podcast from complex technical whitepapers", "Synthesizing research notes across dozens of project PDFs without hallucination", "Drafting study guides, FAQs, and executive summaries from uploaded source files"],
      ["Researchers", "Students", "Executives", "Journalists", "Product Managers"],
      "Go to notebooklm.google.com, create a notebook, upload source documents, and click 'Generate Audio Overview'.",
      ["Grounded strictly in user-uploaded sources (zero web hallucination)", "Audio Overview generates photorealistic two-host podcast audio conversations", "Inline source citation links referencing exact PDF page paragraphs"],
      free("Free experimental tool provided by Google Labs."),
      "https://notebooklm.google.com", "Official Google Labs asset", ["perplexity", "consensus"], 2023, ["Web"]),

    t("genei", "Genei", "Genei Ltd", "AI research tool that automatically summarizes background reading and extracts key data from PDFs.",
      "research_search", "pdf-summarizer",
      "Genei is an AI research and document summarization tool designed to accelerate background reading by extracting key claims, figures, and definitions from PDFs and web pages.",
      "Genei streamlines academic and market research by automatically organizing key document claims into structured notes.",
      ["Summarizing long PDF reports for market research", "Extracting key figures and statistical data from academic papers", "Organizing research documents into categorized projects"],
      ["Researchers", "Students", "Market Analysts", "Content Writers"],
      "Upload PDFs or enter web links at genei.io, and view automated summary notes.",
      ["Automated PDF summarization and key data extraction", "In-document AI question answering", "Note-taking editor with citation references"],
      paid("14-day free trial available.", [
          {"name": "Basic", "price": "£9.99/month (~$12.50/mo)", "notes": "Standard AI summaries, PDF document management."},
          {"name": "Pro", "price": "£29.99/month (~$37.50/mo)", "notes": "GPT-4 summaries, multi-document research analysis."}
      ]),
      "https://www.genei.io", "Official Genei asset", ["elicit", "consensus"], 2020, ["Web"]),

    t("typeset_io", "SciSpace (Typeset.io)", "SciSpace", "All-in-one AI platform for searching, reading, and understanding scientific research papers.",
      "research_search", "academic-reader",
      "SciSpace (formerly Typeset.io) is an AI academic research workspace that helps users discover, read, and comprehend scientific papers with an interactive AI research assistant (Copilot).",
      "SciSpace simplifies dense scientific jargon by letting users highlight complex mathematical equations or text to receive instant plain-language explanations.",
      ["Explaining complex math formulas and scientific jargon inside research PDFs", "Translating academic papers into 75+ global languages", "Extracting key paper methodologies into comparison tables"],
      ["Students", "PhD Researchers", "Medical Professionals", "Translators"],
      "Visit typeset.io, search a research topic, open a paper PDF, and use Copilot to ask questions or highlight text.",
      ["SciSpace Copilot for explaining highlighted PDF math/text in plain language", "Database of 270M+ research papers", "Instant translation into 75+ languages"],
      freemium("Free access to basic search and Copilot query limits.", [
          {"name": "Premium", "price": "$20/month ($12/mo annually)", "notes": "Unlimited Copilot queries, literature review matrix export, plagiarism check."}
      ]),
      "https://typeset.io", "Official SciSpace asset", ["consensus", "elicit"], 2016, ["Web"])
])

# Category 16: No-Code & Low-Code
add_tools("nocode_automation", [
    t("flutterflow_ai", "FlutterFlow AI Gen", "FlutterFlow", "Low-code visual builder for crafting native iOS, Android, and web apps with AI generation.",
      "nocode_automation", "low-code-mobile",
      "FlutterFlow AI Gen is the generative feature suite built into FlutterFlow, allowing developers to generate Flutter UI screens, database schemas, and custom Dart code from text prompts.",
      "FlutterFlow provides developers with production-grade Flutter code export alongside visual low-code app building.",
      ["Generating native mobile app UI screens for iOS and Android", "Writing custom Dart code logic functions with AI assistance", "Building full-stack mobile applications connected to Firebase and Supabase"],
      ["Mobile Developers", "Founders", "Product Managers", "Agencies"],
      "Open flutterflow.io, click 'AI Gen', prompt your screen design, and export clean Flutter code.",
      ["Generates native Flutter UI code and database connections", "One-click export of clean, maintainable Flutter source code", "Direct App Store and Google Play deployment pipelines"],
      freemium("Free plan includes full visual editor and web testing.", [
          {"name": "Standard", "price": "$30/month", "notes": "Source code download, APK builds."},
          {"name": "Pro", "price": "$70/month", "notes": "One-click App Store deployment, GitHub integration, AI Gen."}
      ]),
      "https://flutterflow.io", "Official FlutterFlow asset", ["bubble_ai", "glide_ai"], 2020, ["Web", "macOS", "Windows"]),

    t("softr_ai", "Softr AI", "Softr", "No-code web app builder that generates client portals and internal tools from Airtable/Google Sheets.",
      "nocode_automation", "no-code-portals",
      "Softr AI is a no-code web app builder that converts Airtable bases, Google Sheets, or HubSpot data into custom client portals, internal dashboards, and membership sites.",
      "Softr enables non-technical teams to build secure, password-protected client portals in under an hour.",
      ["Building client portal web apps connected to company Airtable data", "Creating internal employee directories and resource hubs", "Generating membership web apps with user login access"],
      ["Operations Managers", "Agencies", "SMB Owners", "Community Managers"],
      "Sign up at softr.io, connect your Airtable or Google Sheets data, select AI app generation, and publish.",
      ["Generates responsive web apps from Airtable and Google Sheets data", "Granular user permission and membership access controls", "Native Stripe checkout and domain publishing"],
      freemium("Free plan includes 1 custom domain and 5 workspace collaborators.", [
          {"name": "Basic", "price": "$59/month ($49/mo annually)", "notes": "100 internal users, custom domain, 1,000 domain visitors."},
          {"name": "Professional", "price": "$167/month ($139/mo annually)", "notes": "500 internal users, charts, custom code."}
      ]),
      "https://www.softr.io", "Official Softr asset", ["glide_ai", "bubble_ai"], 2020, ["Web"]),

    t("framer_nocode", "Framer", "Framer", "Interactive web design and publishing platform with AI design generation and CMS.",
      "nocode_automation", "web-builder",
      "Framer is a visual website design and publishing platform that uses AI to generate responsive marketing websites, offering advanced web animations and built-in CMS.",
      "Framer bridged the gap between visual design tools and production web hosting with high animation fidelity.",
      ["Publishing responsive SaaS marketing landing pages", "Designing custom interactive web portfolios with scroll animations", "Managing blog content via Framer CMS"],
      ["Web Designers", "Growth Marketers", "Founders"],
      "Go to framer.com, click 'Start with AI', type your site prompt, and publish.",
      ["Text-to-website design generator", "Built-in CMS and custom domain publishing", "Advanced scroll and hover web animations"],
      freemium("Free plan includes framer.website domain.", [
          {"name": "Mini", "price": "$10/month ($5/mo annually)", "notes": "Custom domain, 1,000 visitors/month."},
          {"name": "Basic", "price": "$20/month ($15/mo annually)", "notes": "10,000 visitors/month, password protection."}
      ]),
      "https://www.framer.com", "Official Framer asset", ["framer_ai", "webflow"], 2023, ["Web", "Desktop"]),

    t("appsheet_ai", "AppSheet AI", "Google / AppSheet", "Google's no-code enterprise app development platform using natural language to build apps from Workspace data.",
      "nocode_automation", "enterprise-no-code",
      "AppSheet AI is Google Cloud's no-code enterprise application builder that converts Google Sheets, Drive, and BigQuery data into custom mobile and web business apps.",
      "AppSheet enables corporate operations leads to build enterprise mobile apps with strict Google Cloud security compliance.",
      ["Building mobile field inspection apps for corporate teams", "Automating inventory tracking and asset barcode scanning", "Creating internal approval workflow apps"],
      ["Enterprise Operations Leads", "IT Managers", "Field Engineers"],
      "Access appsheet.com, select a Google Sheet, and let AppSheet generate an application.",
      ["Direct integration with Google Workspace, Drive, and BigQuery", "Mobile camera barcode scanning and offline data sync", "Google Cloud enterprise security compliance"],
      freemium("Free prototyping mode for up to 10 test users.", [
          {"name": "Starter", "price": "$5/user/month", "notes": "Basic data connectors, forms, and mobile app deployment."},
          {"name": "Core", "price": "$10/user/month", "notes": "Advanced security, barcode scanning, email notifications."}
      ]),
      "https://about.appsheet.com", "Official Google AppSheet asset", ["glide_ai", "softr_ai"], 2014, ["Web", "iOS", "Android"]),

    t("dify_ai", "Dify.AI", "Dify", "Open-source LLM application development platform for building AI workflows and RAG agents.",
      "nocode_automation", "llm-app-builder",
      "Dify.AI is an open-source LLM application development workspace that combines AI workflow orchestration, RAG engine management, and prompt engineering in a visual interface.",
      "Dify gives developers and businesses an open-source alternative to proprietary AI app builders, supporting self-hosted enterprise deployment.",
      ["Building visual RAG AI agents connected to corporate knowledge bases", "Orchestrating multi-model AI workflows with API webhooks", "Deploying custom internal AI chat widgets for employees"],
      ["AI Engineers", "Software Engineers", "Product Managers", "DevOps"],
      "Run Dify locally via Docker (`docker-compose up`) or sign up on Dify Cloud, and build visual LLM workflows.",
      ["Visual AI workflow builder and RAG pipeline engine", "Supports OpenAI, Anthropic, Llama, and self-hosted models", "Open-source core engine with self-hosting support"],
      freemium("Free open-source self-hosted version + free Cloud Sandbox.", [
          {"name": "Professional Cloud", "price": "$59/month", "notes": "5,000 vector executions/month, team seats."},
          {"name": "Team Cloud", "price": "$159/month", "notes": "20,000 vector executions/month, custom domain."}
      ]),
      "https://dify.ai", "Official Dify asset", ["relevance_ai", "langsmith"], 2023, ["Web", "Docker", "Self-Hosted"]),

    t("flowise_ai", "Flowise AI", "Flowise", "Open-source drag-and-drop UI node tool for building customized LangChain AI workflows.",
      "nocode_automation", "visual-ai-nodes",
      "Flowise AI is an open-source visual node builder that enables users to create customized LangChain AI applications, vector DB connections, and agents using a drag-and-drop canvas.",
      "Flowise democratized LangChain development by turning complex Python code chains into visual, connectable nodes.",
      ["Building visual RAG agents connected to Pinecone or Weaviate vector databases", "Prototyping multi-step LLM chains without writing Python code", "Deploying REST API endpoints for custom AI agents"],
      ["AI Developers", "No-Code Builders", "Software Engineers"],
      "Run `npx flowise start` locally or deploy via Docker, drag and drop nodes, and test your AI flow.",
      ["Open-source drag-and-drop visual node builder (LangChain & LlamaIndex)", "One-click REST API endpoint deployment for generated flows", "Supports local models via Ollama and commercial APIs"],
      free("100% open-source tool (MIT License). Free to run locally or self-host."),
      "https://flowiseai.com", "Official Flowise asset", ["dify_ai", "n8n"], 2023, ["Self-Hosted", "Docker", "Web"])
])

# Category 17: Developer Tools & MLOps
add_tools("developer_mlops", [
    t("weights_and_biases", "Weights & Biases", "Weights & Biases, Inc.", "Developer platform for MLOps, model training tracking, dataset versioning, and LLM evaluation.",
      "developer_mlops", "mlops-platform",
      "Weights & Biases (W&B) is an MLOps platform that provides experiment tracking, dataset versioning, model evaluation, and LLM fine-tuning monitoring for AI developers.",
      "W&B is the industry-standard experiment tracking framework relied upon by top AI labs (OpenAI, Meta) during foundation model training.",
      ["Tracking loss curves, GPU memory usage, and hyperparameters during LLM fine-tuning", "Versioning training datasets and model weights across team runs", "Evaluating LLM prompt responses against golden benchmark datasets"],
      ["ML Engineers", "AI Researchers", "Data Scientists"],
      "Install `wandb` via pip, add `wandb.init()` to your Python training script, and view live training loss metrics on your dashboard.",
      ["Experiment tracking for PyTorch, TensorFlow, and Hugging Face", "Dataset and model artifact version control", "W&B Prompts for LLM trace evaluation"],
      freemium("Free plan for individuals with 100GB artifact storage.", [
          {"name": "Team", "price": "$50/user/month", "notes": "Shared project dashboards, team access controls."},
          {"name": "Enterprise", "price": "Custom pricing", "notes": "Dedicated VPC/on-prem deployment, custom SLAs, SOC2 compliance."}
      ]),
      "https://wandb.ai", "Official Weights & Biases asset", ["langsmith", "huggingface"], 2017, ["Python Library", "Web"]),

    t("huggingface", "Hugging Face", "Hugging Face, Inc.", "The central open-source community platform for hosting machine learning models, datasets, and AI apps.",
      "developer_mlops", "model-hub",
      "Hugging Face is the leading open-source machine learning platform and model repository, hosting over 500,000 open-weights AI models, datasets, and interactive Spaces (Gradio apps).",
      "Hugging Face is the 'GitHub of AI', serving as the indispensable global repository for downloading open-source model weights (Llama, DeepSeek, Whisper).",
      ["Downloading open-weights AI models for local deployment or fine-tuning", "Hosting interactive Gradio/Streamlit AI app demos via Hugging Face Spaces", "Accessing open-source research datasets"],
      ["AI Researchers", "ML Engineers", "Software Engineers", "Data Scientists"],
      "Browse huggingface.co, install the `transformers` Python library, and load models with `from_pretrained()`.",
      ["500,000+ open-source ML models and datasets", "Hugging Face Spaces for hosting interactive web demos", "Inference Endpoints for managed cloud model deployment"],
      freemium("Free access to model hub, open datasets, and basic Spaces.", [
          {"name": "Pro Account", "price": "$9/month", "notes": "Higher compute hardware for Spaces, priority support."},
          {"name": "Enterprise Hub", "price": "$20/user/month", "notes": "Organization-wide private model repositories and SSO."}
      ]),
      "https://huggingface.co", "Official Hugging Face asset", ["weights_and_biases", "ollama"], 2016, ["Web", "Python Library", "CLI"]),

    t("ollama", "Ollama", "Ollama", "Open-source tool for running large language models locally on macOS, Linux, and Windows.",
      "developer_mlops", "local-llm-runtime",
      "Ollama is an open-source application that allows developers to run, manage, and query large language models (Llama 3, DeepSeek, Mistral) locally on their computers.",
      "Ollama made running local open-weights LLMs effortless, providing a simple Docker-like CLI command (`ollama run llama3`).",
      ["Running 100% private, offline LLM inference on local Mac/PC hardware", "Connecting local LLMs to VS Code extensions (Continue, Cursor) for air-gapped coding", "Testing open-source model weights locally before cloud deployment"],
      ["Software Engineers", "AI Developers", "Privacy Specialists"],
      "Download Ollama, open your terminal, run `ollama run llama3`, and chat locally.",
      ["Simple terminal CLI for model downloading and execution", "Built-in local REST API compatible with OpenAI endpoint format", "Supports Llama 3, DeepSeek-R1, Mistral, Gemma, and Phi"],
      free("100% free and open-source tool (MIT License)."),
      "https://ollama.com", "Official Ollama asset", ["huggingface", "continue_dev"], 2023, ["macOS", "Linux", "Windows", "CLI"]),

    t("groq", "Groq LPU", "Groq, Inc.", "Ultra-high-speed AI inference engine powered by custom LPU (Language Processing Unit) hardware.",
      "developer_mlops", "ai-hardware-inference",
      "Groq is an AI hardware and cloud inference company that utilizes custom Language Processing Unit (LPU) chips to run open LLMs (Llama 3, DeepSeek) at blazing speeds (500+ tokens/second).",
      "Groq shattered AI inference latency records, enabling real-time voice and conversational search applications.",
      ["Deploying real-time voice and chat applications requiring near-instant response latency", "Running high-throughput API inference for open-source models at low cost", "Powering real-time streaming LLM applications"],
      ["AI Engineers", "Software Developers", "Enterprise Architects"],
      "Get an API key at groq.com, replace your OpenAI base URL with Groq's endpoint in your code, and run instant inference.",
      ["Ultra-fast 500+ tokens/second LLM generation speed", "Custom LPU (Language Processing Unit) chip architecture", "OpenAI-compatible REST API for easy drop-in replacement"],
      freemium("Free Developer tier with generous rate limits for testing.", [
          {"name": "Pay-As-You-Go API", "price": "~$0.05-$0.59 / 1M tokens", "notes": "Charged per million tokens depending on model size."}
      ]),
      "https://groq.com", "Official Groq asset", ["huggingface", "ollama"], 2016, ["API", "Web"]),

    t("cohere_platform", "Cohere", "Cohere", "Enterprise AI platform specializing in multilingual embeddings, reranking, and enterprise search.",
      "developer_mlops", "enterprise-llm",
      "Cohere is an enterprise AI platform providing high-performance models for multilingual vector embeddings, RAG search reranking (Rerank 3), and domain-specific text generation.",
      "Cohere stands out in enterprise search by offering the industry's leading Rerank model, vastly improving RAG retrieval accuracy.",
      ["Reranking vector search results in enterprise RAG applications to improve relevance", "Generating multilingual vector embeddings across 100+ languages", "Deploying enterprise-grade LLMs on private cloud infrastructure (AWS, Azure)"],
      ["Enterprise AI Engineers", "Search Engineers", "CTOs"],
      "Get an API key at cohere.com, install `cohere` Python package, and query Cohere models.",
      ["Cohere Rerank 3 model for boosting RAG search accuracy", "Embed v3 multilingual vector embedding models", "Deployable on AWS SageMaker, Azure, and private VPCs"],
      freemium("Free Developer plan for non-production testing.", [
          {"name": "Production API", "price": "Pay-as-you-go token pricing", "notes": "Usage-based pricing for Command, Embed, and Rerank models."}
      ]),
      "https://cohere.com", "Official Cohere asset", ["pinecone", "weaviate"], 2019, ["API", "AWS", "Azure", "Python SDK"]),

    t("vllm", "vLLM", "vLLM Project", "High-throughput and memory-efficient open-source LLM serving engine powered by PagedAttention.",
      "developer_mlops", "llm-serving",
      "vLLM is an open-source, high-throughput LLM serving engine developed at UC Berkeley. It utilizes PagedAttention memory management to serve open models at maximum throughput.",
      "vLLM became the standard self-hosted inference engine for serving open-weights LLMs in production environments.",
      ["Self-hosting production LLM API infrastructure with high concurrency", "Serving open-source models (DeepSeek, Llama 3) on private GPU clusters", "Maximizing GPU memory utilization during batch inference"],
      ["MLOps Engineers", "Infrastructure Engineers", "AI Developers"],
      "Install via `pip install vllm` and launch the OpenAI-compatible server using `python -m vllm.entrypoints.openai.api_server`.",
      ["PagedAttention algorithm for optimized KV cache memory management", "OpenAI-compatible API server endpoint", "Supports continuous batching and multi-GPU tensor parallelism"],
      free("100% open-source software (Apache 2.0 License)."),
      "https://vllm.ai", "Official vLLM project asset", ["ollama", "huggingface"], 2023, ["Python Library", "Docker", "CLI"])
])

# Category 18: HR & Recruiting
add_tools("hr_recruiting", [
    t("hirevue", "HireVue", "HireVue", "Enterprise talent experience platform featuring automated video interview analysis and skill assessments.",
      "hr_recruiting", "video-interviewing",
      "HireVue is an enterprise recruitment platform that provides automated video interviews, AI-driven skill assessments, and conversational interview scheduling.",
      "HireVue pioneered digital video interview screening for Fortune 500 high-volume hiring pipelines.",
      ["Screening high-volume job applicant video responses automatically", "Conducting standardized technical and behavioral skill assessments", "Automating candidate interview scheduling"],
      ["Enterprise Recruiters", "Talent Acquisition Directors", "HR Leads"],
      "Integrate HireVue with your enterprise ATS (Workday, SAP), send video interview links to candidates, and review candidate scorecards.",
      ["On-demand structured video interview recording", "AI-backed technical and conversational skill assessments", "ATS integrations with Workday, SuccessFactors, Greenhouse"],
      paid("Custom enterprise quotes based on hiring volume.", [
          {"name": "Enterprise Subscription", "price": "Custom annual contract", "notes": "Priced per candidate assessment volume and ATS integration scope."}
      ]),
      "https://www.hirevue.com", "Official HireVue asset", ["paradox_ai", "textio"], 2004, ["Web", "iOS", "Android"]),

    t("eightfold_ai", "Eightfold AI", "Eightfold AI", "AI-powered talent intelligence platform for skills-based hiring, retention, and workforce planning.",
      "hr_recruiting", "talent-intelligence",
      "Eightfold AI is an enterprise talent intelligence platform that uses deep learning to match candidate skills with open roles, track internal mobility, and promote diversity.",
      "Eightfold shifted recruiting from strict resume keyword matching toward holistic skills-based talent matching.",
      ["Matching candidate skill profiles against enterprise job openings", "Identifying internal employees for career promotion and internal mobility", "Auditing workforce skill gaps and planning future talent needs"],
      ["Chief Human Resources Officers (CHROs)", "Talent Acquisition Directors", "People Ops"],
      "Connect Eightfold to your enterprise HRIS and ATS systems to view talent intelligence graphs.",
      ["Deep learning skill matching engine trained on global career data", "Diversity and equal opportunity hiring guardrails", "Internal mobility and career path planning portal"],
      paid("Enterprise annual quotes.", [
          {"name": "Enterprise Talent Platform", "price": "Custom annual contract", "notes": "Calculated based on organization headcount and ATS integration."}
      ]),
      "https://eightfold.ai", "Official Eightfold asset", ["paradox_ai", "hirevue"], 2016, ["Web"]),

    t("seeker_ai", "Fetcher", "Fetcher", "Automated candidate sourcing platform combining AI recruiting search with human recruiter review.",
      "hr_recruiting", "candidate-sourcing",
      "Fetcher is an AI-powered talent sourcing platform that searches candidate databases to deliver qualified, diverse candidate pools directly to recruiters.",
      "Fetcher automates tedious candidate sourcing, delivering curated prospect lists directly to recruiter inboxes daily.",
      ["Automating outbound LinkedIn candidate sourcing for niche engineering roles", "Sending automated email outreach sequences to passive job candidates", "Tracking candidate email open and response metrics"],
      ["Technical Recruiters", "Talent Acquisition Leads", "Founders"],
      "Input a job description at fetcher.ai, configure target candidate criteria, and receive daily vetted candidate profiles.",
      ["AI candidate sourcing paired with human quality review", "Automated email outreach sequences and follow-up cadences", "Diversity sourcing filters"],
      paid("14-day free demo available.", [
          {"name": "Starter", "price": "$149/month", "notes": "1 active job search, automated email sequences."},
          {"name": "Professional", "price": "$599/month", "notes": "5 active job searches, dedicated sourcing team support."}
      ]),
      "https://www.fetcher.ai", "Official Fetcher asset", ["textio", "paradox_ai"], 2017, ["Web"]),

    t("metaview", "Metaview", "Metaview", "AI conversation intelligence tool that writes structured interview notes for hiring teams.",
      "hr_recruiting", "interview-notes",
      "Metaview is an AI meeting assistant built specifically for recruiting. It transcribes candidate interviews and generates structured interview notes aligned with company scorecards.",
      "Metaview eliminates manual recruiter note-taking during candidate calls, allowing interviewers to focus entirely on conversation.",
      ["Generating structured candidate interview summaries for ATS scorecards", "Ensuring consistent, unbiased interviewer evaluation criteria", "Coaching hiring managers on interview best practices"],
      ["Recruiters", "Hiring Managers", "Talent Acquisition Leads"],
      "Connect Metaview to your calendar and web conferencing, conduct candidate calls, and view generated interview notes.",
      ["Auto-generates structured candidate notes aligned with ATS scorecards", "Integrates with Greenhouse, Lever, Ashby, Zoom, and Teams", "Interview coaching analytics for hiring managers"],
      freemium("Free tier includes 5 interview recordings/month.", [
          {"name": "Pro", "price": "$48/user/month ($39/mo annually)", "notes": "Unlimited interview recordings, ATS integrations."}
      ]),
      "https://www.metaview.ai", "Official Metaview asset", ["otter_ai", "paradox_ai"], 2021, ["Web", "Chrome Extension"]),

    t("seekout", "SeekOut", "SeekOut", "Enterprise talent discovery and analytics platform for sourcing hard-to-find technical and diverse talent.",
      "hr_recruiting", "talent-discovery",
      "SeekOut is an enterprise talent sourcing platform that indexes public GitHub code repositories, academic papers, and patent databases to uncover specialized technical candidate profiles.",
      "SeekOut provides technical recruiters with deep visibility into developer GitHub repositories and diversity talent pools.",
      ["Sourcing niche software engineering talent based on GitHub code contributions", "Discovering diverse candidate profiles across technical industries", "Analyzing competitive talent movement trends"],
      ["Technical Recruiters", "Talent Acquisition Executives", "Diversity Leads"],
      "Search candidate criteria at seekout.com, view GitHub/patent portfolio analytics, and initiate candidate outreach.",
      ["GitHub code repository and academic paper candidate indexing", "SeekOut AI Assistant for natural language talent searching", "Diversity sourcing and talent analytics dashboards"],
      paid("Custom enterprise annual quotes.", [
          {"name": "Enterprise License", "price": "Custom annual contract", "notes": "Priced per recruiter seat count and database access scope."}
      ]),
      "https://www.seekout.com", "Official SeekOut asset", ["fetcher", "eightfold_ai"], 2017, ["Web"]),

    t("beamery", "Beamery", "Beamery", "Enterprise talent lifecycle management platform for talent marketing, CRM, and skills planning.",
      "hr_recruiting", "talent-crm",
      "Beamery is an enterprise talent CRM and lifecycle management platform that uses AI skills intelligence to manage candidate relationships, internal mobility, and talent pipelines.",
      "Beamery combines CRM candidate relationship marketing with AI skills workforce analytics.",
      ["Managing long-term candidate talent pipelines for enterprise roles", "Executing personalized email nurturing campaigns for past job applicants", "Mapping workforce skills transformation and internal career paths"],
      ["Enterprise Talent Directors", "Recruiting Operations", "CHROs"],
      "Connect Beamery with your enterprise ATS and HRIS, and set up automated talent pipeline nurture workflows.",
      ["Enterprise Talent CRM with automated candidate relationship tracking", "AI Skills Architecture for internal mobility mapping", "SOC 2 Type II enterprise security"],
      paid("Enterprise annual quotes.", [
          {"name": "Enterprise Talent CRM", "price": "Custom annual contract", "notes": "Calculated based on enterprise talent database size and recruiter seat count."}
      ]),
      "https://beamery.com", "Official Beamery asset", ["eightfold_ai", "paradox_ai"], 2014, ["Web"])
])

# Category 19: Legal, Finance & Vertical
add_tools("legal_finance", [
    t("bloomberg_gpt", "Bloomberg Terminal AI", "Bloomberg L.P.", "Financial intelligence and analytics AI integrated into the Bloomberg Terminal.",
      "legal_finance", "financial-ai",
      "Bloomberg Terminal AI is the domain-specific financial intelligence suite integrated into the Bloomberg Terminal, analyzing SEC filings, earnings call transcripts, and market news.",
      "Bloomberg provides the world's most trusted financial data ecosystem, combining financial market databases with fine-tuned LLMs.",
      ["Analyzing SEC 10-K and 10-Q filing notes for financial risk factors", "Summarizing corporate earnings call transcripts in real time", "Extracting financial market sentiment trends across global news wires"],
      ["Financial Analysts", "Portfolio Managers", "Investment Bankers", "Traders"],
      "Access via Bloomberg Terminal software commands (e.g. `{TOP AI <GO>}`).",
      ["Domain-specific financial model trained on decades of Bloomberg data", "Real-time market news and earnings call transcription analysis", "Direct integration with Bloomberg market pricing feeds"],
      paid("Requires active Bloomberg Terminal subscription.", [
          {"name": "Bloomberg Terminal", "price": "~$27,000/user/year", "notes": "Standard annual Bloomberg Terminal subscription fee."}
      ]),
      "https://www.bloomberg.com/professional/", "Official Bloomberg asset", ["harvey_ai"], 2023, ["Desktop Terminal"]),

    t("spellbook_legal", "Spellbook", "Rally Legal", "AI contract drafting and review assistant embedded directly in Microsoft Word.",
      "legal_finance", "contract-review",
      "Spellbook is an AI legal assistant that operates directly inside Microsoft Word. Powered by GPT-4, it reviews contracts, suggests missing clauses, and drafts negotiation redlines in real time.",
      "Spellbook operates directly inside Microsoft Word where lawyers actually work, accelerating contract turnaround times.",
      ["Reviewing commercial contracts and identifying missing protective clauses", "Suggesting redline edits during contract negotiations directly in Word", "Drafting custom agreement clauses based on deal terms"],
      ["Corporate Attorneys", "In-House Legal Counsels", "Paralegals"],
      "Install the Spellbook add-in in Microsoft Word, open a contract document, and click 'Review Contract'.",
      ["Microsoft Word native add-in interface", "Automated contract clause review and redline suggestions", "Trained on legal contract doctrine and commercial precedent"],
      paid("7-day free trial available.", [
          {"name": "Pro", "price": "$125/user/month ($89/mo annually)", "notes": "Includes full Word add-in, contract review, and clause drafting."}
      ]),
      "https://www.spellbook.legal", "Official Spellbook asset", ["harvey_ai", "cocounsel"], 2022, ["MS Word Extension"]),

    t("kavout", "Kavout", "Kavout Corp.", "AI investment intelligence platform providing quantitative stock ranking and equity portfolio analysis.",
      "legal_finance", "equity-research",
      "Kavout is an AI financial technology platform that uses machine learning (K Score) to analyze market data, financial statements, and price momentum to rank stocks and assist portfolio managers.",
      "Kavout brings quantitative machine learning equity ranking models to financial advisors and individual investors.",
      ["Screening US stock equities based on AI K Score factor ratings", "Analyzing corporate financial health indicators and earnings quality", "Constructing quantitative equity model portfolios"],
      ["Portfolio Managers", "Financial Advisors", "Quantitative Analysts"],
      "Sign in at kavout.com, enter stock tickers to view K Score predictive ratings, or run stock screeners.",
      ["K Score equity rating model (1-9 predictive rating)", "Automated stock screener and fundamental data analysis", "Portfolio risk management analytics"],
      freemium("Free plan includes basic stock search and K Scores.", [
          {"name": "Pro", "price": "$49/month", "notes": "Advanced stock screener, real-time AI market signals."}
      ]),
      "https://www.kavout.com", "Official Kavout asset", ["bloomberg_gpt"], 2015, ["Web"]),

    t("robin_ai", "Robin AI", "Robin AI", "Legal AI platform for contract copilot editing and legal repository management.",
      "legal_finance", "contract-management",
      "Robin AI is a legal AI platform that combines LLMs with human legal expert review to accelerate contract drafting, negotiation, and repository management.",
      "Robin AI pairs generative AI contract review with an optional human-in-the-loop legal team for total accuracy.",
      ["Accelerating commercial contract review against company playbook rules", "Searching across corporate contract repositories for expiration dates", "Redlining non-disclosure agreements (NDAs) automatically"],
      ["In-House Legal Teams", "Procurement Leads", "General Counsels"],
      "Upload contracts to robinai.com or open the MS Word add-in to review against your legal playbook.",
      ["Contract Copilot for inline Word redlining", "Legal playbook enforcement engine", "Optional human legal expert review add-on"],
      paid("Custom quotes based on contract review volume.", [
          {"name": "Enterprise Legal", "price": "Custom annual contract", "notes": "Priced per user seat and contract processing volume."}
      ]),
      "https://www.robinai.com", "Official Robin AI asset", ["harvey_ai", "spellbook_legal"], 2019, ["Web", "MS Word Extension"]),

    t("doximity_gpt", "Doximity GPT", "Doximity", "HIPAA-compliant AI medical writing assistant for physicians and healthcare professionals.",
      "legal_finance", "medical-ai",
      "Doximity GPT is a HIPAA-compliant AI medical writing assistant integrated into Doximity's physician network. It assists doctors with drafting patient insurance appeal letters, clinical summaries, and medical documentation.",
      "Doximity provided verified US doctors with a secure, HIPAA-compliant AI writing environment tailored to clinical workflows.",
      ["Drafting insurance prior authorization appeal letters for patient treatments", "Writing clinical patient visit summary letters in plain language", "Translating medical instructions for patients"],
      ["Physicians", "Nurse Practitioners", "Clinical Operations Leads"],
      "Access Doximity GPT via verified Doximity physician account, select a clinical template, and input patient details.",
      ["HIPAA-compliant secure medical writing environment", "Pre-built templates for prior authorization letters and appeal notes", "Integration with Doximity physician network platform"],
      free("Free for verified US medical professionals on Doximity network."),
      "https://www.doximity.com", "Official Doximity asset", ["harvey_ai"], 2023, ["Web", "iOS", "Android"]),

    t("finquery_ai", "Finquery AI", "Finquery", "Financial accounting AI platform for lease, contract, and balance sheet compliance.",
      "legal_finance", "accounting-ai",
      "Finquery AI is a financial accounting compliance platform that uses AI to parse corporate lease agreements, contracts, and financial documents to ensure ASC 842 and IFRS 16 compliance.",
      "Finquery automates complex corporate accounting compliance and balance sheet audit tracking.",
      ["Extracting lease payment schedules and audit terms from corporate contracts", "Ensuring balance sheet compliance with ASC 842 accounting standards", "Auditing vendor contract financial commitments"],
      ["Corporate Controllers", "CFOs", "Accounting Managers"],
      "Upload corporate lease documents to Finquery, and the AI extracts financial schedule parameters.",
      ["Automated contract schedule extraction for lease accounting", "ASC 842 and IFRS 16 compliance reporting", "Audit trail documentation tracking"],
      paid("Custom corporate quotes based on contract volume.", [
          {"name": "Enterprise Accounting", "price": "Custom annual contract", "notes": "Calculated based on lease contract volume and accounting scope."}
      ]),
      "https://finquery.com", "Official Finquery asset", ["bloomberg_gpt"], 2011, ["Web"])
])

# Category 20: Enterprise Governance & Security
add_tools("governance_security", [
    t("credal_ai", "Credal.ai", "Credal", "Enterprise AI security proxy enforcing data access controls and preventing PII leaks across LLMs.",
      "governance_security", "ai-security-proxy",
      "Credal.ai is an enterprise AI security gateway that allows companies to safely deploy LLMs (ChatGPT, Claude) while enforcing internal Slack/SharePoint permissions and preventing PII leakage.",
      "Credal enables enterprise IT teams to connect corporate data sources to LLMs without risking permission boundary breaches.",
      ["Enforcing user-level document security permissions when querying internal AI knowledge bases", "Redacting PII and sensitive source code before sending prompts to third-party LLMs", "Monitoring company-wide LLM usage for SOC 2 compliance auditing"],
      ["CISOs", "IT Security Directors", "Enterprise Software Architects"],
      "Deploy Credal gateway proxies between enterprise applications and LLM providers.",
      ["Real-time PII and secret key redaction", "Document permission sync with Slack, Google Drive, and SharePoint", "SOC 2 Type II audit logging dashboard"],
      paid("Custom enterprise quotes based on organization user count.", [
          {"name": "Enterprise Security Gateway", "price": "Custom annual contract", "notes": "Calculated per active enterprise seat and LLM gateway traffic."}
      ]),
      "https://www.credal.ai", "Official Credal asset", ["robust_intelligence", "lakera_guard"], 2023, ["Cloud Proxy", "API", "Web"]),

    t("prompt_security", "Prompt Security", "Prompt Security", "Enterprise platform protecting organizations from shadow AI usage, data leaks, and prompt attacks.",
      "governance_security", "shadow-ai-protection",
      "Prompt Security is an enterprise AI security platform that inspects, audits, and secures all AI usage across employees, applications, and model APIs.",
      "Prompt Security offers full coverage against Shadow AI by discovering unapproved browser AI tools used by corporate employees.",
      ["Discovering shadow AI browser extensions used across corporate laptops", "Inspecting employee prompts for confidential company code or financial data", "Protecting customer-facing AI applications from prompt injection"],
      ["Chief Information Security Officers", "AppSec Teams", "IT Administrators"],
      "Deploy the Prompt Security browser extension or API gateway to monitor employee AI traffic.",
      ["Shadow AI discovery engine for corporate IT visibility", "Real-time prompt inspection and data loss prevention (DLP)", "Protection against indirect prompt injection attacks"],
      paid("Custom enterprise annual quotes.", [
          {"name": "Enterprise Security Suite", "price": "Custom annual contract", "notes": "Priced per employee seat and application endpoint protected."}
      ]),
      "https://www.prompt.security", "Official Prompt Security asset", ["robust_intelligence", "lakera_guard"], 2023, ["Browser Extension", "API Gateway", "Web"]),

    t("calypsoai", "CalypsoAI", "CalypsoAI", "Enterprise LLM security and AI governance platform providing real-time prompt scanning and threat prevention.",
      "governance_security", "ai-firewall",
      "CalypsoAI is an enterprise AI security platform offering real-time AI firewalls, threat monitoring, and policy enforcement across generative AI applications.",
      "CalypsoAI is trusted by government agencies and financial institutions for strict AI safety auditing.",
      ["Enforcing corporate AI acceptable-use policies in real time", "Scanning internal LLM prompts for malware, toxic content, and data leaks", "Providing security audit trails for government AI compliance"],
      ["CISOs", "Government Security Officers", "IT Directors"],
      "Deploy CalypsoAI firewall proxies across corporate networks and model endpoints.",
      ["Real-time LLM prompt scanning and data loss prevention", "Customizable corporate policy enforcement rules", "Comprehensive AI threat analytics dashboard"],
      paid("Custom enterprise quotes.", [
          {"name": "Enterprise Governance Suite", "price": "Custom annual contract", "notes": "Calculated based on enterprise user seats and security endpoints."}
      ]),
      "https://calypsoai.com", "Official CalypsoAI asset", ["robust_intelligence", "credal_ai"], 2018, ["Cloud Proxy", "On-Premises"]),

    t("hidden_layer", "HiddenLayer", "HiddenLayer, Inc.", "MDR (Managed Detection & Response) security platform safeguarding enterprise AI models from adversarial attacks.",
      "governance_security", "model-security",
      "HiddenLayer is an AI application security platform that protects enterprise machine learning models from adversarial attacks, model poisoning, and intellectual property theft.",
      "HiddenLayer provides non-invasive threat detection for ML models without requiring code changes or access to raw training data.",
      ["Detecting adversarial attack attempts aimed at stealing proprietary ML model weights", "Preventing data poisoning attacks on enterprise training datasets", "Monitoring ML model inputs and outputs for security anomalies"],
      ["Security Engineers", "MLOps Teams", "CISOs"],
      "Integrate HiddenLayer MLDR sensor software alongside enterprise model inference endpoints.",
      ["MLDR (Machine Learning Detection & Response) non-invasive sensor", "Adversarial attack and model extraction defense", "No raw model training data access required"],
      paid("Custom enterprise quotes.", [
          {"name": "Enterprise MLDR Contract", "price": "Custom annual contract", "notes": "Priced per enterprise model endpoint protected."}
      ]),
      "https://hiddenlayer.com", "Official HiddenLayer asset", ["robust_intelligence", "lakera_guard"], 2022, ["Cloud", "On-Premises", "API"]),

    t("protect_ai", "Protect AI", "Protect AI", "End-to-end AI application security platform securing ML pipelines, notebooks, and models.",
      "governance_security", "ml-secops",
      "Protect AI is a developer-focused AI security platform offering tools (Guardian, NBDefense) to scan Jupyter notebooks, ML pipelines, and model artifacts for security vulnerabilities.",
      "Protect AI focuses on ML SecOps, securing the entire machine learning supply chain from notebook code to model deployment.",
      ["Scanning Jupyter notebooks for hardcoded API keys and security flaws", "Auditing open-source Hugging Face model files for embedded malware", "Securing MLOps build pipelines in CI/CD"],
      ["AppSec Engineers", "ML Engineers", "DevOps Specialists"],
      "Install NBDefense or Protect AI Guardian scanner in your ML CI/CD build pipeline.",
      ["NBDefense for scanning Jupyter notebooks and Python scripts", "Model artifact security scanner for detecting malicious model files", "ML Supply Chain Security vulnerability management"],
      freemium("Free open-source scanners available for individual developers.", [
          {"name": "Enterprise Platform", "price": "Custom annual contract", "notes": "Full ML SecOps pipeline security, administrative dashboard."}
      ]),
      "https://protectai.com", "Official Protect AI asset", ["hidden_layer", "robust_intelligence"], 2022, ["Python Library", "CLI", "Web"]),

    t("arize_phoenix", "Arize Phoenix", "Arize AI", "Open-source AI observability and evaluation platform for tracing and auditing LLM applications.",
      "governance_security", "llm-observability",
      "Arize Phoenix is an open-source AI observability platform that provides tracing, evaluation, and hallucination auditing for RAG applications and LLM pipelines.",
      "Phoenix provides developers with an open-source evaluation framework for tracing LLM execution steps locally.",
      ["Tracing RAG application retrieval steps to audit context recall errors", "Evaluating LLM response hallucination scores using benchmark metrics", "Exporting execution trace logs for enterprise compliance"],
      ["AI Engineers", "Software Engineers", "Security Auditors"],
      "Install via `pip install arize-phoenix` and launch local tracing in your Python LLM application.",
      ["Open-source tracing and evaluation engine (Evals)", "Visual execution trace graphs for RAG applications", "Seamless integration with LlamaIndex and LangChain"],
      freemium("Open-source version is free to run locally. Paid hosted version available on Arize Cloud.", [
          {"name": "Arize Enterprise Cloud", "price": "Custom annual contract", "notes": "Hosted enterprise observability platform, custom SLAs."}
      ]),
      "https://phoenix.arize.com", "Official Arize AI asset", ["langsmith", "credal_ai"], 2023, ["Python Library", "Web", "Docker"])
])

print("Categories 13 through 20 appended successfully.")

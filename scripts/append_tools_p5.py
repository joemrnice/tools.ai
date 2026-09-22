#!/usr/bin/env python3
"""
Populates categories 11 through 20 to complete the 180+ tool dataset.
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

# Category 11: Design & UI/UX
add_tools("design_ui_ux", [
    t("uizard", "Uizard", "Uizard Technologies", "AI-powered UI design and prototyping tool that converts hand-drawn sketches into editable wireframes.",
      "design_ui_ux", "prototyping",
      "Uizard is an AI design platform that converts text prompts, paper wireframe sketches, and web screenshots into editable, interactive digital prototypes.",
      "Uizard democratized app wireframing, allowing non-designers to convert whiteboard sketches into functional UI prototypes in minutes.",
      ["Converting paper wireframe sketches into digital mobile prototypes", "Generating full application UI wireframes from text prompts", "Creating interactive click-through prototypes for stakeholder demos"],
      ["Product Managers", "Founders", "UX Researchers", "Non-Designers"],
      "Sign in at uizard.io, upload a sketch or type a prompt, and edit generated UI wireframe screens.",
      ["Sketch-to-screen AI wireframe conversion", "Text-to-UI screen generator", "Autodesign 2.0 theme and component styling"],
      freemium("Free plan includes 2 projects and 10 free AI generations.", [
          {"name": "Pro", "price": "$19/month ($12/mo annually)", "notes": "Unlimited projects, 500 AI generations/month."},
          {"name": "Business", "price": "$49/month ($39/mo annually)", "notes": "Unlimited AI generations, custom design systems."}
      ]),
      "https://uizard.io", "Official Uizard asset", ["figma_ai", "framer_ai"], 2018, ["Web"]),

    t("visily", "Visily", "Visily", "AI wireframing and UI prototyping tool engineered for software teams and product managers.",
      "design_ui_ux", "wireframing",
      "Visily is an AI design tool that converts screenshots, templates, and text prompts into low and high-fidelity wireframes.",
      "Visily focuses specifically on product managers and developers needing fast, accessible wireframes without Figma's complexity.",
      ["Converting app screenshots into editable wireframe components", "Creating low-fidelity wireframes for user stories and PRDs", "Collaborating on product user flow diagrams"],
      ["Product Managers", "Software Engineers", "UX Designers"],
      "Open visily.ai, select Screenshot-to-Design or Text-to-Design, and generate wireframes.",
      ["Screenshot to editable UI wireframe converter", "Text to wireframe layout generator", "Rich library of pre-built UI components"],
      freemium("Free access during public platform launch.", [
          {"name": "Pro", "price": "$14/user/month", "notes": "Advanced AI credits, team design libraries, export to code."}
      ]),
      "https://www.visily.ai", "Official Visily asset", ["uizard", "figma_ai"], 2022, ["Web"]),

    t("galileo_ai", "Galileo AI", "Galileo AI", "Generative AI platform for creating editable UI designs from natural language prompts.",
      "design_ui_ux", "generative-ui",
      "Galileo AI is a generative UI tool that creates complex, multi-screen mobile and web interface designs from text prompts, exportable directly to Figma.",
      "Galileo AI generates high-fidelity UI screens complete with realistic microcopy and iconography.",
      ["Generating full mobile application user flows from text briefs", "Exporting generated UI screens into Figma component files", "Exploring visual UI theme options"],
      ["UI/UX Designers", "Product Designers", "Founders"],
      "Visit usegalileo.ai, type a prompt (e.g. 'Build a food delivery checkout screen'), and export to Figma.",
      ["Generates high-fidelity mobile and web UI screens", "Direct export to editable Figma layers and auto-layouts", "Contextually accurate microcopy generation"],
      freemium("Free trial credits upon signup.", [
          {"name": "Standard", "price": "$19/month ($16/mo annually)", "notes": "1,200 credits/month, Figma export."},
          {"name": "Pro", "price": "$39/month ($32/mo annually)", "notes": "3,000 credits/month, private generation mode."}
      ]),
      "https://www.usegalileo.ai", "Official Galileo AI asset", ["figma_ai", "v0"], 2023, ["Web"]),

    t("spline_ai", "Spline AI", "Spline", "3D design platform with generative AI for creating, animating, and embedding interactive 3D assets.",
      "design_ui_ux", "3d-design",
      "Spline AI is a 3D web design editor that uses generative prompts to create, texture, and animate 3D objects directly on a web canvas.",
      "Spline AI democratized 3D web design, enabling UI designers to embed interactive 3D elements into websites without complex Blender workflows.",
      ["Generating 3D web assets and background objects from text prompts", "Applying AI textures to 3D meshes on a web canvas", "Embedding interactive 3D models into Framer or Webflow sites"],
      ["3D Web Designers", "UI/UX Designers", "Brand Designers"],
      "Open spline.design, click Spline AI, enter a prompt (e.g. 'Create a glowing sci-fi cube'), and embed.",
      ["Text-to-3D object and texture generation", "Real-time physics and interactivity controls", "Direct export to WebGL, React, and HTML embed code"],
      freemium("Free plan includes unlimited personal 3D files and basic AI credits.", [
          {"name": "Super", "price": "$12/month ($9/mo annually)", "notes": "Full AI features, export without watermark."},
          {"name": "Team", "price": "$20/user/month", "notes": "Shared 3D asset libraries and team folders."}
      ]),
      "https://spline.design", "Official Spline asset", ["midjourney", "framer_ai"], 2023, ["Web", "macOS", "Windows"]),

    t("khroma", "Khroma", "Khroma", "AI color palette generator trained on professional human designer preferences.",
      "design_ui_ux", "color-design",
      "Khroma is an AI color tool for designers that learns your color preferences and generates endless, harmonious color palettes, typography pairs, and gradients.",
      "Khroma uses neural networks trained on thousands of professional color combinations to personalize palette generation.",
      ["Selecting personalized brand color palettes for UI design systems", "Testing accessible typography contrast combinations", "Generating custom dual-color gradients"],
      ["Brand Designers", "UI/UX Designers", "Graphic Artists"],
      "Select 50 favorite colors at khroma.co to train the neural network, then browse generated palettes.",
      ["Personalized neural network color matching engine", "Displays color pairs on typography, cards, and gradients", "WCAG accessibility contrast score checking"],
      free("Free forever for all web users."),
      "https://www.khroma.co", "Official Khroma asset", ["figma_ai"], 2018, ["Web"]),

    t("diagram_genius", "Genius by Diagram", "Diagram / Figma", "AI design companion embedded in Figma for automated component generation and layout iteration.",
      "design_ui_ux", "figma-plugins",
      "Genius (created by Diagram, acquired by Figma) is an AI design assistant plugin for Figma that suggests UI component iterations and autocompletes design frames.",
      "Genius brought predictive UI design autocompletion directly inside professional Figma design files.",
      ["Autocompleting UI design frame layouts based on adjacent design system tokens", "Generating custom UI icons and vector graphics in Figma", "Writing UI microcopy"],
      ["Figma Designers", "Design Systems Engineers", "UI/UX Specialists"],
      "Install Diagram plugins in Figma, invoke Genius on a frame, and accept design suggestions.",
      ["Predictive UI design autocompletion", "Direct integration with Figma design tokens and component libraries", "AI vector graphic generation"],
      freemium("Free tier included with Figma account.", [
          {"name": "Diagram Pro", "price": "$15/month", "notes": "Full access to Magician, Genius, and Automator Figma plugins."}
      ]),
      "https://diagram.com", "Official Diagram asset", ["figma_ai"], 2022, ["Figma Plugin"])
])

# Category 12: Marketing, SEO & Ads
add_tools("marketing_seo", [
    t("semrush_one2tree", "Semrush Copilot AI", "Semrush", "Enterprise SEO and digital marketing intelligence platform with AI content and keyword insights.",
      "marketing_seo", "seo-platform",
      "Semrush Copilot AI is the intelligent automation layer across the Semrush platform, providing personalized SEO recommendations, keyword gap analysis, and content ideas.",
      "Semrush is the enterprise backbone of SEO, combining massive search databases with AI-driven competitor analysis.",
      ["Auditing domain technical SEO health and identifying high-volume keyword gaps", "Generating automated SEO content briefs for content marketing teams", "Tracking global search engine ranking positions across competitors"],
      ["SEO Directors", "Content Strategists", "Digital Agencies", "Growth Marketers"],
      "Log in at semrush.com, view Semrush Copilot recommendations dashboard, and run site audits.",
      ["Semrush Copilot personalized AI SEO alert engine", "Database of 25 billion+ keywords across global search engines", "AI Writing Assistant for real-time SEO score checking"],
      paid("7-day free trial available.", [
          {"name": "Pro", "price": "$139.95/month ($117/mo annually)", "notes": "5 projects, 500 keywords to track."},
          {"name": "Guru", "price": "$249.95/month ($208/mo annually)", "notes": "15 projects, 1,500 keywords, historical data."},
          {"name": "Business", "price": "$499.95/month ($416/mo annually)", "notes": "40 projects, 5,000 keywords, API access."}
      ]),
      "https://www.semrush.com", "Official Semrush asset", ["surfer_seo", "ahrefs"], 2008, ["Web"]),

    t("ahrefs_brand", "Ahrefs AI Tools", "Ahrefs", "Industry-leading backlink and SEO research platform with AI content and keyword tools.",
      "marketing_seo", "seo-platform",
      "Ahrefs AI is a collection of free and premium AI tools built into Ahrefs for generating meta tags, content outlines, keyword ideas, and auditing backlink profiles.",
      "Ahrefs possesses the web's largest backlink crawler index, providing unmatched data accuracy for link building and SEO research.",
      ["Analyzing competitor backlink strategies and domain authority metrics", "Generating SEO meta titles and descriptions automatically", "Conducting keyword difficulty and search volume research"],
      ["SEO Specialists", "Digital Marketers", "Link Builders", "Content Leads"],
      "Visit ahrefs.com, enter a target domain or keyword, and utilize Site Explorer and AI writing tools.",
      ["Industry-leading web crawler backlink database", "AI Content Helper for SEO score optimization", "Site Audit tool for technical SEO issue detection"],
      freemium("Free Webmaster Tools for verified website owners.", [
          {"name": "Lite", "price": "$129/month ($99/mo annually)", "notes": "Essential data for small business SEO."},
          {"name": "Standard", "price": "$249/month ($199/mo annually)", "notes": "Full research historical data and SERP updates."}
      ]),
      "https://ahrefs.com", "Official Ahrefs asset", ["semrush_one2tree", "surfer_seo"], 2010, ["Web"]),

    t("anyword", "Anyword", "Anyword Inc.", "Performance copywriting AI that scores and predicts ad and email conversion rates.",
      "marketing_seo", "conversion-copywriting",
      "Anyword is an AI copywriting platform designed for performance marketers. It analyzes target audience demographics to score copy variations based on predicted conversion performance.",
      "Anyword stands out by assigning a predictive Performance Score to generated copy variations prior to launching ad campaigns.",
      ["Scoring ad copy variations before launching Meta and Google Ad campaigns", "Generating high-converting email subject lines and CTA buttons", "Personalizing web landing page copy by target audience demographic"],
      ["Performance Marketers", "Copywriters", "Growth Marketers", "Ad Agencies"],
      "Sign in at anyword.com, input your target audience persona, select a channel, and generate scored copy.",
      ["Predictive Performance Score evaluating conversion probability", "Custom AI trained on your brand's historical ad performance data", "Landing page copy optimization and A/B testing"],
      paid("7-day free trial available.", [
          {"name": "Starter", "price": "$49/month ($39/mo annually)", "notes": "1 user, predictive performance score, 100+ copy templates."},
          {"name": "Data-Driven", "price": "$99/month ($79/mo annually)", "notes": "Connect ad accounts for custom performance model training."}
      ]),
      "https://anyword.com", "Official Anyword asset", ["adcreative_ai", "jasper", "copy_ai"], 2013, ["Web"]),

    t("brand24", "Brand24", "Brand24", "AI social listening and brand reputation monitoring platform with automated sentiment analysis.",
      "marketing_seo", "brand-monitoring",
      "Brand24 is an AI brand monitoring tool that tracks brand mentions across social media, news, blogs, and podcasts in real time, analyzing brand sentiment.",
      "Brand24 provides automated crisis detection and sentiment scoring across social media channels.",
      ["Monitoring real-time social media brand mentions and executive discussions", "Detecting sudden negative sentiment spikes during PR crises", "Tracking competitor share of voice across industry news outlets"],
      ["PR Directors", "Brand Managers", "Social Media Leads", "Executives"],
      "Enter brand keywords at brand24.com, configure alert notifications, and view the AI sentiment dashboard.",
      ["AI Sentiment Analysis categorizing positive, neutral, and negative mentions", "Automated PR Crisis Alert notifications", "Share of Voice and Reach metric tracking"],
      paid("14-day free trial available.", [
          {"name": "Individual", "price": "$99/month ($79/mo annually)", "notes": "3 keywords, 2k mentions/month."},
          {"name": "Team", "price": "$179/month ($149/mo annually)", "notes": "7 keywords, 5k mentions/month, AI insights."},
          {"name": "Pro", "price": "$249/month ($199/mo annually)", "notes": "12 keywords, 25k mentions/month, real-time alerts."}
      ]),
      "https://brand24.com", "Official Brand24 asset", ["semrush_one2tree"], 2011, ["Web", "iOS", "Android"]),

    t("phrasee", "Phrasee", "Phrasee", "Enterprise AI marketing platform optimizing brand messaging across email, push, and SMS.",
      "marketing_seo", "enterprise-marketing",
      "Phrasee is an enterprise marketing AI platform that generates and optimizes commercial message copy across email marketing, push notifications, and SMS campaigns.",
      "Phrasee focuses on enterprise brand voice safety and automated multivariate copy testing.",
      ["Optimizing enterprise email newsletter subject lines for open rate uplift", "Generating compliant SMS ad copy for retail promotions", "Executing multivariate copy testing across millions of consumer push notifications"],
      ["Enterprise Marketers", "CRM Directors", "E-commerce Growth Leads"],
      "Integrate Phrasee with Salesforce Marketing Cloud or Braze, set brand guardrails, and run automated copy experiments.",
      ["Enterprise Brand Language fine-tuned model guardrails", "Automated multivariate copy optimization engine", "Integrations with Salesforce Marketing Cloud, Braze, and Klaviyo"],
      paid("Enterprise custom annual quotes.", [
          {"name": "Enterprise Subscription", "price": "Custom annual contract", "notes": "Calculated per consumer messaging volume and platform integrations."}
      ]),
      "https://phrasee.co", "Official Phrasee asset", ["anyword", "jasper"], 2015, ["Web"])
])

print("Category 11 & 12 appended.")

#!/usr/bin/env python3
"""
Populates remaining categories (6 to 20) with high quality tools so every category has 8-10 tools.
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

# Category 6: Writing & Content
add_tools("writing_editing", [
    t("rytr", "Rytr", "Rytr LLC", "Intuitive AI copywriting assistant for generating marketing content, emails, and social copy.",
      "writing_editing", "copywriting",
      "Rytr is an AI writing assistant that helps users generate high-converting copy for blogs, social media, emails, and product descriptions.",
      "Rytr offers an accessible, fast copywriting tool with built-in tone selection and inline document editing.",
      ["Drafting social media posts and ad copy", "Generating catchy email subject lines and sales outreach body copy", "Creating SEO meta descriptions and landing page headlines"],
      ["Marketers", "Copywriters", "Entrepreneurs", "Social Media Managers"],
      "Sign up at rytr.me, select a use case and tone, input key points, and click Ryte for me.",
      ["40+ use cases and 20+ tone variations", "Built-in plagiarism checker and text reformer", "Rich text editor with formatting options"],
      freemium("10,000 characters per month on the free plan.", [
          {"name": "Unlimited", "price": "$9/month ($7.50/mo annually)", "notes": "Unlimited characters, 20+ tones, custom use cases."},
          {"name": "Premium", "price": "$29/month ($24.16/mo annually)", "notes": "Plagiarism checks included, priority support."}
      ]),
      "https://rytr.me", "Official Rytr logo asset", ["copy_ai", "jasper"], 2021, ["Web", "Extension"]),

    t("sudowrite", "Sudowrite", "Sudowrite", "AI narrative writing partner engineered specifically for creative fiction authors and novelists.",
      "writing_editing", "fiction-writing",
      "Sudowrite is an AI story generator and writing assistant tailored for creative writers, novelists, and screenwriters.",
      "Unlike corporate copywriting tools, Sudowrite is built specifically for narrative pacing, sensory description, and character dialogue development.",
      ["Brainstorming plot twists and character arc developments", "Expanding sensory scene descriptions (sight, sound, smell)", "Drafting full chapter prose from outline beats"],
      ["Novelists", "Fiction Authors", "Screenwriters", "Creative Writers"],
      "Open sudowrite.com, paste your draft, highlight text, and use Write, Describe, or Rewrite tools.",
      ["Story Engine for turning detailed story bibles into full chapters", "Describe tool for rich sensory prose generation", "Brainstorm tool for dialogue and plot ideas"],
      paid("14-day free trial available.", [
          {"name": "Hobby & Student", "price": "$19/month ($10/mo annually)", "notes": "225,000 AI credits per month."},
          {"name": "Professional", "price": "$29/month ($22/mo annually)", "notes": "450,000 AI credits per month."},
          {"name": "Max", "price": "$59/month ($44/mo annually)", "notes": "2,000,000 AI credits per month."}
      ]),
      "https://www.sudowrite.com", "Official Sudowrite asset", ["claude", "chatgpt"], 2021, ["Web"]),

    t("quillbot", "QuillBot", "Course Hero / QuillBot", "AI paraphrasing, grammar checking, and summarizing tool for academic and professional writing.",
      "writing_editing", "paraphrasing",
      "QuillBot is an AI writing platform that specializes in paraphrasing, sentence restructuring, summarization, and grammar correction.",
      "QuillBot is widely used by students and researchers to rephrase complex sentences and improve writing clarity.",
      ["Paraphrasing academic excerpts for research summaries", "Shortening lengthy paragraphs for executive briefs", "Checking grammar and vocabulary fluency"],
      ["Students", "Researchers", "Academic Writers", "Non-native English Speakers"],
      "Paste text into quillbot.com, choose a paraphrasing mode (Standard, Fluency, Formal), and click Paraphrase.",
      ["Paraphraser with 8 customizable modes and synonym slider", "Summarizer tool for extracting key points from long articles", "Built-in Grammar Checker and Citation Generator"],
      freemium("125 words max on free paraphraser, basic modes.", [
          {"name": "Premium", "price": "$19.95/month ($8.33/mo annually)", "notes": "Unlimited words in Paraphraser, all modes, plagiarism checker."}
      ]),
      "https://quillbot.com", "Official QuillBot asset", ["grammarly", "writer_com"], 2017, ["Web", "Chrome Extension", "Word Add-in"]),

    t("wordtune", "Wordtune", "AI21 Labs", "AI reading and writing companion that offers contextual sentence rephrasing and summarization.",
      "writing_editing", "paraphrasing",
      "Wordtune is an AI writing tool built by AI21 Labs that suggests contextual rewrites to make written text more clear, compelling, and professional.",
      "Wordtune provides sentence-level rephrasing options, giving writers fine control over tone and length.",
      ["Rewriting informal draft emails into professional executive messages", "Shortening long sentences to improve readability", "Summarizing YouTube videos and long PDFs"],
      ["Executives", "Marketers", "Copywriters", "Customer Support Reps"],
      "Highlight text in Wordtune or via Chrome extension and select a rewrite suggestion.",
      ["Contextual Rewrite with Formal and Casual tone switches", "Spelling and grammar checking", "Summarize tool for web pages and documents"],
      freemium("10 free rewrites per day on free plan.", [
          {"name": "Plus", "price": "$24.99/month ($9.99/mo annually)", "notes": "30 rewrites/day, premium AI prompts."},
          {"name": "Unlimited", "price": "$37.50/month ($14.99/mo annually)", "notes": "Unlimited rewrites and summaries."}
      ]),
      "https://www.wordtune.com", "Official Wordtune asset", ["grammarly", "quillbot"], 2020, ["Web", "Chrome Extension"])
])

# Category 7: Meeting Notes & Transcription
add_tools("meeting_notes", [
    t("avoma", "Avoma", "Avoma, Inc.", "AI meeting assistant and conversation intelligence platform for sales and customer success.",
      "meeting_notes", "conversation-intelligence",
      "Avoma is an AI meeting assistant that automatically records, transcribes, and summarizes business meetings, analyzing conversation insights for sales and support.",
      "Avoma unifies pre-meeting scheduling, live note-taking, and post-meeting CRM updates in one platform.",
      ["Automatically logging structured call notes into Salesforce and HubSpot", "Analyzing sales team talk-to-listen ratios and key topic mentions", "Sharing timestamped meeting snippets with product teams"],
      ["Account Executives", "Customer Success Leads", "Sales Managers"],
      "Connect calendar and web conferencing to Avoma, and the AI bot will join scheduled meetings.",
      ["AI Meeting Assistant with automated speaker identification", "Revenue Intelligence and deal pipeline tracking", "CRM automatic note sync and keyword search"],
      freemium("Free tier includes basic manual note-taking and call recording.", [
          {"name": "Starter", "price": "$24/user/month ($19/mo annually)", "notes": "AI meeting summaries, automated CRM sync."},
          {"name": "Plus", "price": "$59/user/month ($49/mo annually)", "notes": "Advanced conversation intelligence, topic tracking."}
      ]),
      "https://www.avoma.com", "Official Avoma asset", ["gong_io", "fireflies_ai"], 2017, ["Web"]),

    t("supernormal", "Supernormal", "Supernormal", "AI note taker for Google Meet, Zoom, and Teams with customizable meeting templates.",
      "meeting_notes", "meeting-transcription",
      "Supernormal is an AI meeting assistant that automatically records, transcribes, and writes structured meeting notes tailored to specific meeting types.",
      "Supernormal stands out with custom meeting templates designed for 1-on-1s, executive syncs, and candidate interviews.",
      ["Capturing structured action items and decision points during executive meetings", "Generating standardized interview summaries for candidate hiring loops", "Syncing notes into Notion, Slack, and HubSpot"],
      ["Product Managers", "Hiring Managers", "Executives", "Consultants"],
      "Install the Chrome extension or invite Supernormal bot to your calendar events.",
      ["Customizable meeting templates for different meeting formats", "Multi-language transcription in 20+ languages", "Direct export to Notion, Slack, and Google Docs"],
      freemium("1,000 free meeting minutes upon signup.", [
          {"name": "Pro", "price": "$18/user/month ($10/mo annually)", "notes": "Unlimited meeting notes, custom templates, CRM integration."}
      ]),
      "https://supernormal.com", "Official Supernormal asset", ["fathom", "otter_ai"], 2022, ["Web", "Chrome Extension"]),

    t("meetgeek", "MeetGeek", "MeetGeek.ai", "AI meeting assistant that auto-records, transcribes, and shares call insights with team channels.",
      "meeting_notes", "meeting-transcription",
      "MeetGeek is an automated meeting recorder and analytics platform that captures video meetings and distributes AI summaries into company tools.",
      "MeetGeek focuses on automated team knowledge distribution, pushing highlights directly to Slack channels.",
      ["Pushing automated meeting summaries to dedicated Slack channels", "Tracking team meeting effectiveness metrics and talk-time distribution", "Creating searchable meeting repositories for team knowledge bases"],
      ["Team Leads", "Project Managers", "Remote Operations"],
      "Connect your Google/Outlook calendar and web conferencing app to MeetGeek.",
      ["Automated meeting recording, transcription, and summarization", "Auto-sharing rules for Slack, Trello, and Notion", "Meeting sentiment and engagement analytics"],
      freemium("5 hours of transcription/month on the free plan.", [
          {"name": "Pro", "price": "$19/user/month ($15/mo annually)", "notes": "20 hours transcription/month, HD video downloads."},
          {"name": "Business", "price": "$39/user/month ($29/mo annually)", "notes": "100 hours transcription/month, CRM integrations."}
      ]),
      "https://meetgeek.ai", "Official MeetGeek asset", ["otter_ai", "fireflies_ai"], 2021, ["Web"]),

    t("read_ai", "Read AI", "Read AI, Inc.", "Meeting analytics and summary assistant that measures participant engagement and sentiment.",
      "meeting_notes", "meeting-analytics",
      "Read AI is a meeting productivity assistant that generates transcripts, executive summaries, and real-time engagement and sentiment metrics.",
      "Read AI stands out by measuring meeting health, participant engagement levels, and sentiment during live video calls.",
      ["Measuring meeting effectiveness and team engagement scores", "Generating automated multi-meeting weekly digest reports", "Generating action item checklists post-call"],
      ["Executives", "Operations Leads", "Engineering Managers"],
      "Connect your calendar at read.ai and invite Read AI to video calls.",
      ["Meeting engagement and sentiment score dashboards", "Automated meeting summaries and action items", "Read Chief of Staff multi-meeting weekly report synthesis"],
      freemium("Free tier includes 2 meeting reports/month.", [
          {"name": "Pro", "price": "$29.75/user/month ($19.75/mo annually)", "notes": "Unlimited meeting reports, custom meeting templates."}
      ]),
      "https://www.read.ai", "Official Read AI asset", ["otter_ai", "fathom"], 2021, ["Web"])
])

# Category 8: Productivity & Workflow Automation
add_tools("productivity_automation", [
    t("raycast_ai", "Raycast AI", "Raycast Technologies", "Blazing fast macOS launcher extension with integrated LLMs for system-wide AI actions.",
      "productivity_automation", "desktop-assistant",
      "Raycast AI embeds conversational and generative AI directly into the Raycast macOS launcher, allowing developers to execute AI prompts system-wide.",
      "Raycast AI provides developers with instant, keyboard-driven AI access across all Mac desktop applications without opening a browser.",
      ["Asking quick programming questions and syntax lookups via hotkey", "Summarizing copied clipboard text or selected documents", "Translating selected text into different languages in any application"],
      ["Software Engineers", "Designers", "Mac Power Users"],
      "Press Option+Space to open Raycast on macOS, type your AI prompt or trigger an AI command.",
      ["Instant system-wide hotkey access on macOS", "Model selection (GPT-4o, Claude 3.5 Sonnet)", "Custom AI prompt commands and extensions"],
      freemium("Standard Raycast launcher is free. AI features require subscription.", [
          {"name": "Raycast Pro", "price": "$10/month ($8/mo annually)", "notes": "Unlocks Raycast AI, cloud sync, custom themes."}
      ]),
      "https://www.raycast.com", "Official Raycast asset", ["macgpt"], 2023, ["macOS"]),

    t("bardeen_ai", "Bardeen", "Bardeen Inc.", "AI browser automation tool that automates repetitive web workflows without code.",
      "productivity_automation", "browser-automation",
      "Bardeen is an AI-powered browser automation extension that scrapes web data, automates web research, and executes workflows across browser tabs.",
      "Bardeen simplifies web scraping and app integration directly inside the browser using simple natural language prompts.",
      ["Scraping LinkedIn lead data and saving directly to Google Sheets or HubSpot", "Summarizing open browser articles and emailing key points", "Automating repetitive data entry between web applications"],
      ["Sales SDRs", "Recruiters", "Growth Marketers", "Operations Leads"],
      "Install the Bardeen Chrome extension, click the extension icon, and select or prompt an automation playbook.",
      ["Natural language browser workflow builder", "One-click web scraper for tables and structured sites", "Integrations with Google Sheets, Notion, HubSpot, Slack"],
      freemium("Free plan includes 50 credit runs/month.", [
          {"name": "Pro", "price": "$15/month ($10/mo annually)", "notes": "500 credits/month, premium integrations, background automation."}
      ]),
      "https://www.bardeen.ai", "Official Bardeen asset", ["zapier_central", "make"], 2020, ["Chrome Extension"]),

    t("taskade_ai", "Taskade", "Taskade Inc.", "AI-powered productivity workspace combining project management, mind maps, and AI agents.",
      "productivity_automation", "workspace-management",
      "Taskade is a unified productivity platform that combines task lists, mind maps, project boards, and autonomous AI agents in one workspace.",
      "Taskade allows teams to build custom AI agents that work alongside project management workflows.",
      ["Generating project task breakdowns and mind maps from simple briefs", "Deploying custom AI team agents to summarize project status", "Collaborating on interactive workflow documents"],
      ["Project Managers", "Remote Teams", "Founders"],
      "Create a workspace at taskade.com, click 'New with AI', and generate project boards.",
      ["Multi-view project workflows (List, Board, Mind Map, Org Chart)", "Custom AI Agent builder for workspace task execution", "Real-time team chat and video collaboration"],
      freemium("Free tier includes 1 workspace and basic AI credits.", [
          {"name": "Pro", "price": "$20/month ($8/mo annually)", "notes": "3 users included, 10,000 AI credits/month."},
          {"name": "Business", "price": "$49/month ($19/mo annually)", "notes": "10 users included, custom AI agents."}
      ]),
      "https://www.taskade.com", "Official Taskade asset", ["notion_ai"], 2019, ["Web", "Desktop", "iOS", "Android"]),

    t("height_app", "Height App", "Height", "Autonomous AI project management tool that auto-updates tasks, triages bugs, and tracks progress.",
      "productivity_automation", "project-management",
      "Height is an AI-native project management tool designed for software engineering teams. Its AI engine automatically updates task statuses, triages incoming bug reports, and drafts release notes.",
      "Height reduces manual task management overhead by leveraging AI to keep project boards synchronized with real engineering work.",
      ["Automatically triaging incoming customer bug reports into engineering tasks", "Drafting product release notes based on completed task boards", "Asking natural language questions about project shipping deadlines"],
      ["Product Managers", "Software Engineers", "Engineering Leads"],
      "Import existing tasks into height.app and enable Copilot auto-triage workflows.",
      ["Auto-triage for incoming task routing", "Natural language chat search across project task boards", "Automated release notes generation"],
      freemium("Free for up to 10 team members with basic features.", [
          {"name": "Team", "price": "$12/user/month ($10/mo annually)", "notes": "Unlimited members, full AI copilot workflows, custom attributes."}
      ]),
      "https://height.app", "Official Height asset", ["jira", "linear"], 2021, ["Web", "Desktop", "iOS", "Android"])
])

print("Category 6, 7, 8 appended.")

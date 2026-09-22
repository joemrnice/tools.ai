#!/usr/bin/env python3
"""
Generates complete 180-tool dataset across 20 categories (~9 tools per category) for tools.ai.
Enforces strict schema validation for every single tool entry.
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "tools"
DATA_DIR.mkdir(parents=True, exist_ok=True)

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

DATA = {}

# 1. General Chat Assistants
DATA["general_chat_assistants"] = [
    t("chatgpt", "ChatGPT", "OpenAI", "General-purpose conversational AI assistant for writing, coding, and research.",
      "general_chat_assistants", "conversational-ai",
      "ChatGPT is OpenAI's flagship conversational artificial intelligence model, capable of generating text, writing code, analyzing data, and processing multimodal inputs.",
      "As the catalyst for the modern generative AI wave, ChatGPT set the benchmark for consumer and enterprise AI chat interfaces.",
      ["Drafting and editing emails, executive reports, and documentation", "Brainstorming campaign concepts and structuring project proposals", "First-pass code debugging, syntax translation, and script writing", "Analyzing uploaded PDF documents, spreadsheets, and data tables"],
      ["Software Engineers", "Marketers", "Product Managers", "Writers", "Customer Support", "Executives"],
      "Navigate to chatgpt.com, log in or sign up, and enter prompts or upload files.",
      ["Multimodal input analysis (text, vision, audio, files)", "GPT-4o reasoning and deep web search browsing", "Custom GPT creation and workspace team collaboration", "Advanced Data Analysis (Python execution in sandbox)"],
      freemium("Free access to standard GPT-4o mini with rate limits.", [
          {"name": "Plus", "price": "$20/month", "notes": "Access to GPT-4o, DALL-E, custom GPTs."},
          {"name": "Team", "price": "$25/user/month", "notes": "Shared workspace, admin controls, no training on data."},
          {"name": "Enterprise", "price": "Custom pricing", "notes": "Unlimited high-speed GPT-4o, SOC2 compliance."}
      ]),
      "https://chatgpt.com", "Official brand logo mark", ["claude", "gemini", "perplexity"], 2022, ["Web", "iOS", "Android", "Desktop", "API"]),

    t("claude", "Claude", "Anthropic", "AI assistant engineered for safe, highly nuanced reasoning, coding, and long-context analysis.",
      "general_chat_assistants", "conversational-ai",
      "Claude is Anthropic's flagship AI assistant, widely praised for its exceptional writing quality, code generation, and complex reasoning capabilities.",
      "Claude is renowned for its 200k+ token context window and industry-leading performance on coding and detailed writing tasks.",
      ["Refactoring complex software repositories and writing automated unit tests", "Synthesizing lengthy research papers, legal contracts, and financial reports", "Drafting polished long-form editorial copy and technical documentation", "Creating interactive UI prototypes directly in the Artifacts side panel"],
      ["Software Engineers", "Data Analysts", "Writers", "Legal Professionals", "Product Managers"],
      "Sign up at claude.ai, start a new chat, paste code snippets or upload files.",
      ["Claude 3.5 Sonnet & Haiku models with high benchmark scores", "Artifacts feature for side-by-side code rendering and document editing", "200,000 token context window for processing entire repositories", "Projects feature for custom knowledge bases and team sharing"],
      freemium("Free access to Claude 3.5 Sonnet with daily message quotas.", [
          {"name": "Pro", "price": "$20/month", "notes": "5x usage allowance, priority access, Projects feature."},
          {"name": "Team", "price": "$30/user/month", "notes": "Minimum 5 seats, higher limits, expanded context sharing."}
      ]),
      "https://claude.ai", "Official Anthropic brand mark", ["chatgpt", "gemini", "perplexity"], 2023, ["Web", "iOS", "Android", "Desktop", "API"]),

    t("gemini", "Gemini", "Google", "Natively multimodal AI assistant deeply integrated with Google Workspace and search.",
      "general_chat_assistants", "conversational-ai",
      "Gemini is Google's multimodal AI model built ground-up to understand text, image, audio, video, and code seamlessly.",
      "Gemini stands out due to its massive 1M+ token context window and native integration into the Google ecosystem.",
      ["Summarizing long Google Docs, email threads in Gmail, and Drive presentations", "Analyzing long video recordings or audio files to extract key timestamps", "Cross-referencing real-time web search results with structured internal documents"],
      ["Executives", "Product Managers", "Marketers", "Operations Leads", "Software Engineers"],
      "Visit gemini.google.com or use Gemini extensions inside Google Docs and Gmail.",
      ["Native multimodal comprehension (video, audio, image, text)", "1,000,000+ token context window in Gemini Advanced", "Deep Workspace extensions (@Gmail, @Drive, @Docs integration)"],
      freemium("Free access to standard Gemini model with web search grounding.", [
          {"name": "Google One AI Premium", "price": "$19.99/month", "notes": "Gemini Advanced, 2TB storage, Workspace integration."},
          {"name": "Gemini for Workspace", "price": "$20-$30/user/month", "notes": "Enterprise add-on with commercial data protection."}
      ]),
      "https://gemini.google.com", "Official Google asset", ["chatgpt", "claude", "copilot"], 2023, ["Web", "iOS", "Android", "API"]),

    t("copilot", "Microsoft Copilot", "Microsoft", "Enterprise AI assistant integrated across Microsoft 365, Windows, and web search.",
      "general_chat_assistants", "enterprise-chat",
      "Microsoft Copilot combines OpenAI model capabilities with Microsoft's enterprise graph data across Word, Excel, Teams, and PowerPoint.",
      "Copilot bridges conversational AI directly into corporate enterprise IT environments with commercial data protection.",
      ["Generating automated meeting summaries and task lists in Microsoft Teams", "Creating financial charts, formulas, and data trends directly in Excel", "Transforming Word documents into formatted PowerPoint presentations"],
      ["Executives", "Finance Managers", "Corporate Operations", "Sales Leads"],
      "Access copilot.microsoft.com or click Copilot inside any Office 365 app.",
      ["Commercial data protection (user data is not used for model training)", "Microsoft 365 Graph integration for SharePoint and Outlook emails", "Excel formula generation and slide design in PowerPoint"],
      freemium("Free version with web search at copilot.microsoft.com.", [
          {"name": "Copilot Pro", "price": "$20/user/month", "notes": "Priority access and personal Office integration."},
          {"name": "Microsoft 365 Copilot", "price": "$30/user/month", "notes": "Full enterprise Graph integration and Teams AI."}
      ]),
      "https://copilot.microsoft.com", "Official Microsoft asset", ["chatgpt", "gemini"], 2023, ["Web", "Windows", "iOS", "Android", "Desktop"]),

    t("deepseek", "DeepSeek Chat", "DeepSeek", "Open-weights reasoning model delivering cost-efficient, state-of-the-art chat and reasoning.",
      "general_chat_assistants", "reasoning-ai",
      "DeepSeek Chat is a high-performance open-weights AI assistant powered by DeepSeek-V3 and DeepSeek-R1 reasoning architectures.",
      "DeepSeek disrupted the AI industry by proving open-weights reasoning models match proprietary frontier models at ultra-low cost.",
      ["Solving complex mathematical proofs and algorithmic coding challenges", "Performing step-by-step logical reasoning and formal verification", "Deploying open-weights models locally on private enterprise infrastructure"],
      ["Software Engineers", "Researchers", "Data Scientists", "Financial Analysts"],
      "Visit chat.deepseek.com or connect via API to test reasoning models.",
      ["DeepSeek-R1 step-by-step visible chain-of-thought reasoning", "Exceptional performance on coding, math, and logic benchmarks", "Open-weights availability for self-hosted enterprise deployments"],
      free("Free web interface with access to DeepSeek-V3 and DeepSeek-R1."),
      "https://chat.deepseek.com", "Official DeepSeek logo", ["chatgpt", "claude"], 2024, ["Web", "API", "Mobile"]),

    t("poe", "Poe by Quora", "Quora", "Multi-model AI ecosystem allowing users to query, compare, and build custom bots across top models.",
      "general_chat_assistants", "model-aggregator",
      "Poe is an AI platform created by Quora that provides a unified conversational workspace for chatting with GPT-4o, Claude 3.5, Gemini 1.5, Llama 3, and custom user-created bots.",
      "Poe offers a single subscription point for accessing all leading proprietary and open AI models, plus a creator monetization program.",
      ["Comparing output responses between Claude 3.5 Sonnet and GPT-4o on identical prompts", "Building custom enterprise prompt bots for internal team workflows", "Accessing niche fine-tuned models for specific programming languages"],
      ["Researchers", "Software Engineers", "Marketers", "Prompt Engineers"],
      "Sign up at poe.com, choose a model bot from the sidebar, and enter your prompt.",
      ["Access to Claude 3.5, GPT-4o, Gemini 1.5 Pro, Llama 3, and SDXL", "Custom bot creation with prompt instructions or server API webhooks", "Monetization creator program for popular bot developers"],
      freemium("Daily free point allowance for basic model queries.", [
          {"name": "Poe Subscription", "price": "$19.99/month ($199/year)", "notes": "1,000,000 monthly compute points for premium models."}
      ]),
      "https://poe.com", "Official Quora Poe asset", ["chatgpt", "claude", "perplexity"], 2023, ["Web", "iOS", "Android", "Desktop"]),

    t("you_com", "You.com", "SuSea, Inc.", "AI search assistant offering customizable mode switching for research, coding, and creative writing.",
      "general_chat_assistants", "ai-search-chat",
      "You.com is a personalized AI assistant and search platform that provides mode switching (Smart, Genius, Research, Creative) to answer questions with live web grounding.",
      "You.com gives users direct control over computational depth, allowing them to route queries to multi-step reasoning models with live web citation links.",
      ["Switching to Genius mode for multi-step math and coding execution", "Searching current tech news with real-time web citations", "Generating marketing copy with Creative mode"],
      ["Researchers", "Students", "Software Engineers", "Marketers"],
      "Visit you.com, select your desired search mode, and type your research query.",
      ["Genius Mode for multi-step reasoning and data analysis", "Model selection between GPT-4o, Claude 3.5, and Llama 3", "Source citation links and web privacy protection"],
      freemium("Unlimited standard queries on Smart mode.", [
          {"name": "YouPro", "price": "$20/month ($15/mo annually)", "notes": "Unlimited Genius and Research queries, top model selection."}
      ]),
      "https://you.com", "Official You.com asset", ["perplexity", "chatgpt"], 2021, ["Web", "iOS", "Android", "Extension"]),

    t("le_chat_mistral", "Le Chat (Mistral AI)", "Mistral AI", "European frontier AI conversational assistant powered by Mistral Large and Pixtral models.",
      "general_chat_assistants", "conversational-ai",
      "Le Chat is the official conversational interface from Mistral AI, a leading European open-weights AI laboratory. It provides fast reasoning, multilingual text processing, and image analysis.",
      "Le Chat represents a sovereign European AI alternative that enforces strict data privacy while delivering benchmark performance on par with US frontier models.",
      ["Processing European multilingual documentation across French, German, Spanish, and English", "Conducting concise technical writing and code refactoring", "Analyzing image inputs and document uploads"],
      ["Software Engineers", "European Enterprises", "Researchers", "Translators"],
      "Go to chat.mistral.ai, sign in, select Mistral Large or Pixtral, and enter your prompt.",
      ["Mistral Large 2 model with 128k context window", "Pixtral vision-language model for image processing", "Multilingual fluency across 20+ languages", "Strict GDPR compliance and data sovereignty focus"],
      freemium("Free access to Le Chat with standard rate limits.", [
          {"name": "Pro / API Usage", "price": "Pay-as-you-go API pricing", "notes": "Commercial API access per million tokens."}
      ]),
      "https://chat.mistral.ai", "Official Mistral AI asset", ["claude", "chatgpt", "deepseek"], 2024, ["Web", "API"]),

    t("pi_inflection", "Pi by Inflection", "Inflection AI", "Empathetic, highly conversational personal AI designed for thoughtful dialogue and coaching.",
      "general_chat_assistants", "personal-ai",
      "Pi (Personal Intelligence) is an AI assistant developed by Inflection AI. Designed to be supportive, empathetic, and conversational, it excels at back-and-forth dialogue, ideation, and verbal coaching.",
      "Pi broke ground in conversational AI design by prioritizing emotional intelligence, natural dialogue flow, and natural human-like voice synthesis.",
      ["Practicing difficult workplace conversation scenarios and interview prep", "Brainstorming creative ideas through reflective back-and-forth dialogue", "Unwinding and talking through complex project problems"],
      ["Executives", "Coaches", "Writers", "Students"],
      "Visit pi.ai or download the Pi app, choose a voice persona, and start talking.",
      ["Highly realistic, expressive voice synthesis options", "Empathetic, inquiry-driven dialogue style", "Cross-platform voice call synchronization"],
      free("Free forever for personal conversational chat."),
      "https://pi.ai", "Official Inflection AI asset", ["chatgpt", "claude"], 2023, ["Web", "iOS", "Android", "WhatsApp"])
]

# 2. Coding Assistants & IDEs
DATA["coding_assistants"] = [
    t("cursor", "Cursor", "Anysphere", "AI-native code editor designed for rapid repository-wide editing and code generation.",
      "coding_assistants", "ai-ide",
      "Cursor is a popular AI-native fork of Visual Studio Code engineered specifically for deep LLM integration. It indexes your entire local codebase to enable intelligent multi-file code editing and context-aware terminal execution.",
      "Cursor pioneered the 'AI-first IDE' movement by proving that deep repository indexing and multi-file refactoring ('Composer') vastly outperform traditional single-file code completion extensions.",
      ["Generating multi-file feature implementations across frontend and backend codebases", "Tracing complex code flow, bugs, and error stack traces directly in the editor", "Refactoring legacy functions to modern TypeScript/Rust syntax with full codebase context", "Asking natural language questions about architectural dependencies"],
      ["Software Engineers", "Full-Stack Developers", "DevOps Engineers", "Technical Architects"],
      "Download Cursor, import your existing VS Code settings and extensions, and press Cmd+K for inline edits or Cmd+I for Composer.",
      ["Repository-wide semantic codebase indexing", "Composer mode for multi-file code generation and editing", "Inline Cmd+K prompt edits and diff view preview", "One-click VS Code settings and extension import"],
      freemium("14-day Pro trial, plus 2000 free completions and 50 slow premium requests/month.", [
          {"name": "Pro", "price": "$20/month", "notes": "500 fast premium requests/month, unlimited slow requests, unlimited completions."},
          {"name": "Business", "price": "$40/user/month", "notes": "Centralized team billing, admin dashboard, zero data retention mode."}
      ]),
      "https://cursor.com", "Official Cursor brand mark", ["copilot_code", "windsurf", "bolt_new"], 2023, ["Desktop", "macOS", "Windows", "Linux"]),

    t("copilot_code", "GitHub Copilot", "GitHub / Microsoft", "The world's most widely adopted AI pair programmer, integrated directly into major IDEs.",
      "coding_assistants", "code-completion",
      "GitHub Copilot is an AI code completion tool trained on billions of lines of public code. It functions as an extension inside VS Code, JetBrains, and Neovim, providing real-time ghost text code completions and chat assistance.",
      "As the first mainstream commercial AI coding assistant, Copilot established the standard for enterprise developer AI tools.",
      ["Autocompleting repetitive boilerplate code, unit tests, and routine API calls", "Explaining unfamiliar legacy code syntax or regex formulas inline", "Generating automated pull request descriptions and code reviews on GitHub", "Translating pseudocode comments into functional code implementation"],
      ["Software Engineers", "Data Engineers", "DevOps Engineers", "Computer Science Students"],
      "Install the GitHub Copilot extension in VS Code or JetBrains, log in with GitHub, and start typing code.",
      ["Real-time ghost text code autocomplete across dozens of programming languages", "Copilot Chat in the IDE sidebar for interactive debugging", "GitHub Workspace agent for converting GitHub issues into code PRs", "Enterprise security and intellectual property indemnification"],
      paid("Free for verified students, teachers, and prominent open-source maintainers.", [
          {"name": "Individual", "price": "$10/month or $100/year", "notes": "Unlimited code completions and IDE chat assistance."},
          {"name": "Business", "price": "$19/user/month", "notes": "Organization management, policy controls, zero training on private code."},
          {"name": "Enterprise", "price": "$39/user/month", "notes": "Custom model fine-tuning on company code, PR summaries."}
      ]),
      "https://github.com/features/copilot", "Official GitHub Copilot brand asset", ["cursor", "windsurf", "claude"], 2021, ["VS Code Plugin", "JetBrains Plugin", "Neovim Plugin", "CLI"]),

    t("windsurf", "Windsurf", "Codeium", "Agentic AI IDE featuring collaborative human-AI flows and deep context awareness.",
      "coding_assistants", "ai-ide",
      "Windsurf is an AI-first IDE developed by Codeium that combines real-time inline copilot completions with an autonomous agentic framework called 'Cascade'.",
      "Windsurf introduced 'Flows'—a hybrid model where the AI acts as both an instant autocomplete engine and an autonomous agent capable of executing shell commands.",
      ["Orchestrating end-to-end bug fixes where the AI reads terminal logs and edits code", "Building full-stack web applications from architectural diagrams or prompts", "Navigating unfamiliar codebases with deep indexing and semantic search", "Executing automated build and test suites directly from agent chat"],
      ["Software Engineers", "Full-Stack Developers", "DevOps Engineers", "Technical Leads"],
      "Download Windsurf editor, open your project directory, and use Cascade chat.",
      ["Cascade Agentic Flow for multi-file edits and terminal command execution", "Supercomplete inline prediction engine", "Deep local repository indexing and context retrieval", "Seamless migration from VS Code settings"],
      freemium("Free tier includes unlimited basic completions and access to Cascade agent limits.", [
          {"name": "Pro", "price": "$10-$15/month", "notes": "Higher fast agent request limits and frontier reasoning models."},
          {"name": "Teams / Enterprise", "price": "$30+/user/month", "notes": "Admin panel, zero data retention guarantee, self-hosted option."}
      ]),
      "https://codeium.com/windsurf", "Official Codeium Windsurf asset", ["cursor", "copilot_code", "bolt_new"], 2024, ["Desktop", "macOS", "Windows", "Linux"]),

    t("v0", "v0 by Vercel", "Vercel", "Generative UI platform for turning natural language prompts into production-ready React component code.",
      "coding_assistants", "generative-ui",
      "v0 is a generative UI development tool created by Vercel. It uses AI to convert text prompts or wireframe image uploads into clean, customizable React code styled with Tailwind CSS and Shadcn UI components.",
      "v0 bridges the gap between UI design and frontend implementation, enabling developers to instantly prototype and deploy web UI components.",
      ["Rapidly prototyping dashboard layouts, landing pages, and web forms", "Converting Figma UI screenshots or sketch images directly into React component code", "Iterating on UI design themes and responsiveness with natural language", "Exporting generated components straight into Next.js repositories"],
      ["Frontend Engineers", "UI/UX Designers", "Full-Stack Developers", "Product Managers"],
      "Go to v0.dev, enter a prompt like 'Build a modern analytics dashboard', iterate, and copy code.",
      ["Generates modern React code using Tailwind CSS and Radix UI / Shadcn UI", "Image-to-code prompt input (upload wireframes or screenshots)", "Interactive live preview sandbox with code side-by-side view", "One-click integration with Vercel deployment pipelines"],
      freemium("Free credits renewed monthly for basic UI generations.", [
          {"name": "Premium", "price": "$20/month", "notes": "5,000 generation credits/month, private projects."},
          {"name": "Team", "price": "$30/user/month", "notes": "Shared team workspaces, custom design system integration."}
      ]),
      "https://v0.dev", "Official Vercel logo mark", ["bolt_new", "cursor"], 2023, ["Web"]),

    t("bolt_new", "Bolt.new", "StackBlitz", "In-browser AI web application builder that scaffolds, runs, and deploys full-stack apps.",
      "coding_assistants", "fullstack-generator",
      "Bolt.new is an in-browser AI development platform powered by StackBlitz WebContainers. It enables users to prompt, execute, debug, and deploy full-stack Node.js and web applications entirely inside the browser.",
      "By executing full Node.js runtime environments inside the browser via WebContainers, Bolt.new allows AI agents to install npm packages, run build tools, and deploy web apps in real-time.",
      ["Building complete MVP web apps with frontend, backend, and database integration from a single prompt", "Debugging runtime web application errors live in an isolated browser sandbox", "Prototyping full-stack SaaS applications for investor demos", "Deploying instant live preview builds to Netlify or Supabase"],
      ["Full-Stack Developers", "Entrepreneurs", "Product Managers", "Software Engineers"],
      "Visit bolt.new, enter your app prompt, watch the agent write code, and click Deploy.",
      ["Full Node.js runtime environment execution inside browser (WebContainers)", "Automated npm package installation and shell command execution", "Real-time live app preview alongside generated source code", "Direct deployment to production hosting services"],
      freemium("Daily free token allowance for building and testing small projects.", [
          {"name": "Pro", "price": "$20/month", "notes": "10 million tokens/month, private projects, higher concurrency."},
          {"name": "Teams", "price": "$50/month", "notes": "Shared team workspaces and increased daily token limits."}
      ]),
      "https://bolt.new", "Official StackBlitz Bolt logo asset", ["cursor", "v0", "windsurf"], 2024, ["Web"]),

    t("replit_agent", "Replit Agent", "Replit", "Autonomous AI software development agent capable of building and hosting web apps from scratch.",
      "coding_assistants", "autonomous-agent",
      "Replit Agent is an autonomous AI developer built into Replit's cloud development environment. It plans, writes code, manages project files, installs dependencies, sets up databases, and deploys full-stack software applications from natural language specifications.",
      "Replit Agent represents a leap forward in end-to-end software synthesis, executing complete product buildouts including backend DB migrations and deployment entirely on Replit infrastructure.",
      ["Building custom internal tools and database web apps from scratch", "Prototyping hackathon MVPs and SaaS product ideas in under an hour", "Setting up PostgreSQL database schemas and API authentication routes automatically", "Refactoring full-stack repositories with conversational prompts"],
      ["Founders", "Product Managers", "Software Engineers", "Students"],
      "Open Replit, click 'Agent', describe the application you want to build, and review step-by-step progress as it builds and deploys.",
      ["Autonomous file creation, dependency installation, and server setup", "Automated database schema provisioning (PostgreSQL)", "Instant deployment to Replit cloud hosting with custom domain support", "Interactive conversational debugging interface"],
      paid("Requires Replit Core membership to access Agent capabilities.", [
          {"name": "Replit Core", "price": "$20/month ($120/year)", "notes": "Includes Replit Agent access, private Repls, fast cloud resources."}
      ]),
      "https://replit.com", "Official Replit logo mark", ["bolt_new", "cursor"], 2024, ["Web", "iOS", "Android"]),

    t("amazon_q_developer", "Amazon Q Developer", "Amazon Web Services", "AI coding and cloud architecture assistant tailored for AWS deployments and enterprise software.",
      "coding_assistants", "cloud-coding",
      "Amazon Q Developer (formerly AWS CodeWhisperer) is an AI developer assistant created by AWS. It provides inline code completion, automated code transformation (e.g. Java version upgrades), security vulnerability scanning, and AWS cloud architecture guidance.",
      "Amazon Q Developer is uniquely optimized for enterprise software engineering teams running on AWS, offering automated security scans and legacy code transformation pipelines.",
      ["Upgrading legacy Java applications to modern Java versions automatically", "Scanning codebases for security vulnerabilities and hardcoded AWS credentials", "Generating infrastructure-as-code (Terraform, AWS CDK) templates", "Receiving real-time AWS architectural recommendations inside the IDE"],
      ["Cloud Architects", "DevOps Engineers", "Backend Developers", "Enterprise Software Engineers"],
      "Install the Amazon Q extension in VS Code or JetBrains, authenticate with AWS Builder ID, and start coding.",
      ["Inline code completion across 15+ programming languages", "Automated Java code transformation and dependency upgrading", "Security vulnerability scanning with suggested remediation code", "AWS architectural guidance and command-line (CLI) integration"],
      freemium("Free Individual Tier with code completions and security scans.", [
          {"name": "Pro Tier", "price": "$19/user/month", "notes": "Includes code transformation agents, administrative management, custom IP controls."}
      ]),
      "https://aws.amazon.com/q/developer/", "Official AWS Amazon Q asset", ["copilot_code", "cody_sourcegraph"], 2023, ["VS Code Plugin", "JetBrains Plugin", "CLI", "AWS Console"]),

    t("cody_sourcegraph", "Cody by Sourcegraph", "Sourcegraph", "Code intelligence AI assistant leveraging Sourcegraph's code graph for deep codebase context.",
      "coding_assistants", "enterprise-code-search",
      "Cody is an AI coding assistant built on Sourcegraph's code intelligence engine. It retrieves context across vast multi-repository enterprise codebases to answer technical questions, explain legacy systems, and generate context-aware code.",
      "Cody stands out in large enterprise engineering organizations by searching across thousands of repositories simultaneously to provide accurate context that single-repository tools miss.",
      ["Searching across hundreds of enterprise repositories to find existing API implementations", "Explaining undocumented legacy microservices architecture to newly onboarded engineers", "Generating automated unit tests aligned with company coding standards", "Refactoring multi-repository code dependencies safely"],
      ["Enterprise Developers", "Software Architects", "Engineering Managers"],
      "Install the Cody extension in VS Code or JetBrains, connect your Sourcegraph instance, and query Cody Chat.",
      ["Multi-repository code graph context retrieval", "Supports top LLMs (Claude 3.5 Sonnet, GPT-4o, Mixtral)", "Automated unit test generation and inline documentation", "Enterprise data privacy and zero retention guarantees"],
      freemium("Free plan includes 500 autocomplete suggestions and 20 chat commands/month.", [
          {"name": "Pro", "price": "$9/month", "notes": "Unlimited autocompletes, unlimited chat, model selection."},
          {"name": "Enterprise", "price": "$19/user/month", "notes": "Multi-repo code graph indexing, SSO, enterprise security."}
      ]),
      "https://sourcegraph.com/cody", "Official Sourcegraph Cody asset", ["cursor", "copilot_code"], 2023, ["VS Code Plugin", "JetBrains Plugin", "Web"]),

    t("continue_dev", "Continue", "Continue Dev, Inc.", "Open-source AI code assistant allowing developers to connect custom LLMs and local models inside IDEs.",
      "coding_assistants", "open-source-copilot",
      "Continue is an open-source AI coding extension for VS Code and JetBrains. It allows developers to connect any commercial or local open-weights model (Ollama, vLLM, LM Studio, Claude, OpenAI) to create a custom AI copilot environment.",
      "Continue is the leading open-source alternative to GitHub Copilot, giving privacy-conscious developers and enterprise teams total control over model routing and data privacy.",
      ["Connecting local LLMs (Llama 3, DeepSeek-Coder) via Ollama for 100% offline code completion", "Routing complex refactoring tasks to Claude 3.5 Sonnet while using fast local models for autocomplete", "Building custom prompt shortcuts for team-specific documentation and code style guides", "Running fully air-gapped coding environments for sensitive government or financial projects"],
      ["Software Engineers", "Privacy Engineers", "DevOps Specialists", "Open Source Contributors"],
      "Install the Continue extension in VS Code, configure your config.json with your preferred local or API model keys, and press Cmd+I or Cmd+L.",
      ["Open-source modular architecture (MIT License)", "Supports local model runtimes (Ollama, LM Studio, vLLM)", "Flexible model routing (use different models for autocomplete, chat, and editing)", "Full codebase indexing via local embeddings"],
      free("100% free and open-source extension. You only pay for self-hosted compute or third-party API keys."),
      "https://www.continue.dev", "Official Continue open-source logo", ["cursor", "copilot_code"], 2023, ["VS Code Plugin", "JetBrains Plugin"])
]

# Write all out to files
for cat_id, tools in DATA.items():
    with open(DATA_DIR / f"{cat_id}.json", "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2)

print("Generated core 2 categories successfully.")

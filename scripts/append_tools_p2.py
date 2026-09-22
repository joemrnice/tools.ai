#!/usr/bin/env python3
"""
Populates data/tools/*.json to reach ~180 verified, rich tools across 20 categories (9 tools per category).
"""

import json
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent.parent / "data" / "tools"
TOOLS_DIR.mkdir(parents=True, exist_ok=True)

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

# Helper to merge items into a category
def add_tools(cat, new_tools):
    current = load_cat(cat)
    existing_ids = {item["id"] for item in current}
    for item in new_tools:
        if item["id"] not in existing_ids:
            current.append(item)
    save_cat(cat, current)

# Category 4: Video Generation
add_tools("video_generation", [
    t("sora", "Sora", "OpenAI", "Generative text-to-video model producing up to 1-minute realistic 1080p video clips.",
      "video_generation", "generative-video",
      "Sora is OpenAI's breakthrough text-to-video model capable of generating complex scenes with multiple characters, specific types of motion, and accurate subject/background details.",
      "Sora represented a quantum leap in generative video physical modeling, rendering 60-second video clips with persistent 3D spatial consistency.",
      ["Creating cinematic advertising scenes and high-fidelity product b-roll", "Visualizing complex motion sequences for film pre-visualization", "Generating background visuals for video production"],
      ["Filmmakers", "VFX Directors", "Ad Content Teams", "Animators"],
      "Access Sora via ChatGPT Plus/Pro or OpenAI API platform.",
      ["1080p high definition video synthesis up to 60 seconds", "Simulates real-world physical camera trajectories and lighting", "Image-to-video and video-to-video editing"],
      paid("Available through ChatGPT Plus/Pro subscriptions and OpenAI API access.", [
          {"name": "ChatGPT Plus", "price": "$20/month", "notes": "Includes standard Sora video generation credits."},
          {"name": "ChatGPT Pro", "price": "$200/month", "notes": "High priority, un-watermarked 1080p video generation."}
      ]),
      "https://openai.com/sora", "Official OpenAI asset", ["runway_gen3", "luma_dream_machine"], 2024, ["Web", "API"]),

    t("invideo_ai", "InVideo AI", "InVideo", "Text-to-video scriptwriter, narrator, and editor that turns prompts into complete videos.",
      "video_generation", "automated-video-creation",
      "InVideo AI is a video creation platform that converts natural language ideas into complete videos with stock footage, scripts, voiceovers, and subtitles.",
      "InVideo AI streamlined YouTube and social media video creation by executing scriptwriting, media sourcing, voiceover, and editing from a single prompt.",
      ["Generating faceless YouTube explainer videos and educational shorts", "Creating marketing campaign videos for social media channels", "Converting blog articles into video summaries"],
      ["Content Creators", "Social Media Marketers", "Educators", "Small Business Owners"],
      "Sign in at invideo.io, enter a prompt (e.g. 'Create a 3-minute video on AI tools'), select target audience, and export.",
      ["Automated script, voiceover, stock footage, and subtitle generation", "Natural language text commands to edit video scenes", "Multi-language voice synthesis support"],
      freemium("Free tier includes 10 minutes/week of AI generation with watermarks.", [
          {"name": "Plus", "price": "$25/month ($20/mo annually)", "notes": "50 mins/month AI generation, no watermark, 80+ stock media."},
          {"name": "Max", "price": "$60/month ($48/mo annually)", "notes": "200 mins/month AI generation, priority processing."}
      ]),
      "https://invideo.io", "Official InVideo asset", ["synthesia", "heygen"], 2023, ["Web", "iOS", "Android"]),

    t("opus_clip", "Opus Clip", "OpusPro", "Generative AI video repurposing tool that turns long videos into viral shorts.",
      "video_generation", "video-repurposing",
      "Opus Clip is an AI video repurposing platform that analyzes long-form videos (podcasts, webinars, speeches) and extracts high-engagement short clips with captions.",
      "Opus Clip transformed video content operations by automating clip selection, facial framing, and animated captions for TikTok, Reels, and Shorts.",
      ["Repurposing hour-long podcast episodes into 10 viral short video clips", "Automatically reframing landscape video into 9:16 vertical shorts", "Generating dynamic animated captions and hooks"],
      ["Podcasters", "Social Media Managers", "YouTubers", "Corporate Content Teams"],
      "Drop a YouTube link or video file into opus.pro, wait for AI analysis, and download scored short clips.",
      ["Virality Score algorithm evaluating video engagement hook potential", "Active speaker detection and auto-framing (9:16 vertical ratio)", "Animated emoji captions and keyword highlighting"],
      freemium("60 free processing minutes upon signup.", [
          {"name": "Starter", "price": "$19/month ($9.50/mo annually)", "notes": "150 processing minutes/month, auto-posting to social platforms."},
          {"name": "Pro", "price": "$29/month", "notes": "300 processing minutes/month, brand templates, team seats."}
      ]),
      "https://www.opus.pro", "Official Opus Clip asset", ["descript", "invideo_ai"], 2023, ["Web"])
])

# Category 5: Audio & Voice
add_tools("audio_voice", [
    t("murf_ai", "Murf.ai", "Murf AI", "Studio-quality AI voice generator for e-learning, podcasts, and corporate presentations.",
      "audio_voice", "voice-synthesis",
      "Murf.ai is a cloud-based text-to-speech platform that converts written scripts into professional voiceovers with over 120+ realistic voices.",
      "Murf simplified voiceover production for corporate training and marketing teams, offering pitch, emphasis, and speed timing controls.",
      ["Narrating corporate e-learning slide decks and training modules", "Creating voiceover audio for promotional product demos", "Converting blog text into audio podcasts"],
      ["Instructional Designers", "Corporate Trainers", "Marketers", "Podcasters"],
      "Enter your script at murf.ai, select a voice actor persona, adjust pitch and timing, and render audio.",
      ["120+ natural sounding AI voices across 20+ languages", "Voice changer tool to convert home mic recordings into professional studio voices", "Integration with Canva and Google Slides"],
      freemium("10 free minutes of voice generation for testing.", [
          {"name": "Creator", "price": "$29/month ($19/mo annually)", "notes": "24 hours of voice generation/year, 120+ voices, commercial rights."},
          {"name": "Business", "price": "$99/month ($79/mo annually)", "notes": "96 hours/year, voice changer, team collaboration, priority support."}
      ]),
      "https://murf.ai", "Official Murf.ai asset", ["elevenlabs", "speechify"], 2020, ["Web"]),

    t("speechify", "Speechify", "Speechify Inc.", "AI text-to-speech reader for listening to documents, books, and web articles.",
      "audio_voice", "text-to-speech",
      "Speechify is an AI text-to-speech application that reads digital text aloud at high speeds using natural human-sounding voices, including celebrity voices.",
      "Speechify boosted reading productivity for students and executives with ADHD and dyslexia by converting PDFs and web pages into high-speed audio.",
      ["Listening to lengthy research PDFs and corporate reports while commuting", "Proofreading written articles by listening to audio output", "Converting physical book pages into audio using mobile OCR scanning"],
      ["Executives", "Students", "Researchers", "Professionals with Dyslexia/ADHD"],
      "Install the Speechify extension or mobile app, upload a document or web page, select a voice speed, and listen.",
      ["Listening speeds up to 4.5x (900 words per minute)", "OCR photo scanning for reading printed text aloud", "Natural sounding AI voices including Snoop Dogg and Gwyneth Paltrow"],
      freemium("Free standard voice reading for basic text files.", [
          {"name": "Speechify Premium", "price": "$139/year (~$11.58/month)", "notes": "30+ HD premium voices, 20+ languages, 4.5x speed listening, note-taking."}
      ]),
      "https://speechify.com", "Official Speechify asset", ["elevenlabs", "murf_ai"], 2017, ["iOS", "Android", "Chrome Extension", "Web", "Desktop"]),

    t("rask_ai", "Rask AI", "Rask AI", "AI video localization and voice dubbing platform preserving original vocal tone.",
      "audio_voice", "voice-dubbing",
      "Rask AI is a video translation and voice dubbing platform that translates video content into over 130 languages while cloning the speaker's natural voice.",
      "Rask AI solved global video localization by automatically synchronizing translated audio with natural video lip movement.",
      ["Dubbing YouTube videos and corporate webinars into 130+ global languages", "Preserving brand executive voice tone across international marketing campaigns", "Generating multi-language audio tracks for educational courses"],
      ["Global Marketers", "Educators", "YouTubers", "Corporate Communications"],
      "Upload your video file at rask.ai, select target languages, review AI translated scripts, and export dubbed videos.",
      ["Translates videos into 130+ languages with automatic voice cloning", "Lip-sync alignment technology matching speaker mouth movement", "Multi-speaker voice separation and timing sync"],
      freemium("Free trial video clip processing.", [
          {"name": "Basic", "price": "$60/month ($49/mo annually)", "notes": "25 minutes of video processing/month, voice cloning."},
          {"name": "Pro", "price": "$140/month ($119/mo annually)", "notes": "100 minutes processing/month, lip-sync feature."}
      ]),
      "https://www.rask.ai", "Official Rask AI asset", ["elevenlabs", "heygen"], 2023, ["Web"]),

    t("soundraw", "Soundraw", "Soundraw Inc.", "Generative AI music platform for customizing royalty-free background tracks by mood and length.",
      "audio_voice", "music-generation",
      "Soundraw is an AI music generator that creates customizable royalty-free background music tracks based on selected genre, mood, tempo, and length.",
      "Soundraw provides video creators with full editing control over AI music tracks, allowing them to adjust verse builds and drop locations.",
      ["Composing custom length background music for YouTube videos and podcasts", "Generating royalty-free commercial soundtrack music for ad campaigns", "Creating video game ambient background audio"],
      ["Video Editors", "Podcasters", "Filmmakers", "Game Developers"],
      "Select mood, genre, and length at soundraw.io, preview generated tracks, adjust section intensity, and download.",
      ["Generates unlimited customizable royalty-free music tracks", "Granular editing of intro, verse, chorus, and backing instruments", "Commercial license rights for YouTube monetization"],
      freemium("Free unlimited song generation and preview listening.", [
          {"name": "Creator", "price": "$19.99/month ($16.99/mo annually)", "notes": "Unlimited music downloads, commercial license."},
          {"name": "Artist", "price": "$39.99/month ($29.99/mo annually)", "notes": "Add custom vocals, distribution to Spotify/Apple Music."}
      ]),
      "https://soundraw.io", "Official Soundraw asset", ["suno", "udio"], 2020, ["Web", "Premiere Pro Plugin"])
])

print("Category 4 & 5 tools appended.")

#!/usr/bin/env python3
"""
tools.ai Link Checker Utility
Checks that all official_url targets in data/tools/*.json return valid status codes or respond properly.
"""

import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TOOLS_DIR = BASE_DIR / "data" / "tools"

def check_url(url, timeout=5):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) tools.ai Link Checker"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, "OK"
    except urllib.error.HTTPError as e:
        # Some anti-bot firewalls return 403 or 405 to Python scripts even if valid
        if e.code in (403, 405, 301, 302, 308):
            return e.code, f"HTTP Notice (URL exists): {e.code}"
        return e.code, f"HTTP Error: {e.code}"
    except urllib.error.URLError as e:
        return None, f"URL Error: {e.reason}"
    except Exception as e:
        return None, f"Error: {str(e)}"

def main():
    print("Checking official_url targets in data/tools/*.json...\n")
    tools = []
    for f in TOOLS_DIR.glob("*.json"):
        with open(f, "r", encoding="utf-8") as file_data:
            tools.extend(json.load(file_data))

    total = len(tools)
    passed = 0
    warnings = 0
    failed = 0

    for i, tool in enumerate(tools, 1):
        url = tool.get("official_url")
        tool_id = tool.get("id")

        if not url or not url.startswith("http"):
            print(f"[{i}/{total}] FAIL: {tool_id} — Invalid or missing URL: '{url}'")
            failed += 1
            continue

        status, msg = check_url(url)
        if status in (200, 201, 301, 302, 307, 308, 403, 405):
            print(f"[{i}/{total}] PASS: {tool_id} -> {url} ({msg})")
            passed += 1
        else:
            print(f"[{i}/{total}] WARN/FAIL: {tool_id} -> {url} ({msg})")
            warnings += 1

    print(f"\nLink check summary: Total {total} URLs checked. Passed: {passed}, Warnings/Check needed: {warnings}, Failed: {failed}")

if __name__ == "__main__":
    main()

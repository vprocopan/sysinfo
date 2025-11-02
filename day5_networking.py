#!/usr/bin/env python3
"""
Day 5 — Networking & APIs
Author: Vitalie Procopan

Goal:
    Interact with APIs and network utilities using Python.

Exercises:
    1️⃣ Fetch public IP via https://api.ipify.org
    2️⃣ Query GitHub public API and print rate-limit info
    3️⃣ Handle HTTP errors and exceptions
    💡 Stretch: Check multiple URLs from a file and report status codes
"""

import requests
import json
import sys
from pathlib import Path

# ──────────────────────────────────────────────
# 1️⃣ Get your public IP
# ──────────────────────────────────────────────
def get_public_ip():
    print("\n🌐 Fetching public IP...")
    try:
        resp = requests.get("https://api.ipify.org?format=json", timeout=5)
        resp.raise_for_status()
        ip = resp.json().get("ip")
        print(f"✅ Your public IP is: {ip}")
        return ip
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to get public IP: {e}")
        return None


# ──────────────────────────────────────────────
# 2️⃣ Query GitHub API for rate-limit info
# ──────────────────────────────────────────────
def check_github_api():
    print("\n🐙 Checking GitHub API rate limits...")
    try:
        resp = requests.get("https://api.github.com", timeout=5)
        resp.raise_for_status()
        print(f"✅ GitHub API responded: {resp.status_code}")
        print("🔍 Response headers:")
        for key, value in resp.headers.items():
            if "ratelimit" in key.lower():
                print(f"  {key}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"❌ GitHub API error: {e}")


# ──────────────────────────────────────────────
# 3️⃣ Generic error-safe request helper
# ──────────────────────────────────────────────
def safe_get(url, timeout=5):
    """Perform an HTTP GET safely, returning (status_code, ok)."""
    try:
        r = requests.get(url, timeout=timeout)
        print(f"{url:<50} → {r.status_code}")
        return r.status_code, True
    except requests.exceptions.RequestException as e:
        print(f"{url:<50} → ❌ {e}")
        return None, False


# ──────────────────────────────────────────────
# 💡 Stretch Goal — check URLs from file
# ──────────────────────────────────────────────
def check_urls_from_file(file_path="urls.txt"):
    file = Path(file_path)
    if not file.exists():
        print(f"\n⚠️  File '{file}' not found. Creating an example one.")
        sample_urls = [
            "https://google.com",
            "https://github.com",
            "https://nonexistent.domain.fake"
        ]
        file.write_text("\n".join(sample_urls))
        print(f"✅ Created sample {file_path}. Re-run script to use it.")
        return

    print(f"\n📋 Checking URLs from: {file.resolve()}")
    urls = [line.strip() for line in file.read_text().splitlines() if line.strip()]
    for url in urls:
        safe_get(url)


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────
def main():
    print("🚀 Day 5 — Networking & APIs\n")
    get_public_ip()
    check_github_api()
    check_urls_from_file("urls.txt")
    print("\n✅ Networking & API checks completed.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\n🛑 Interrupted by user.")
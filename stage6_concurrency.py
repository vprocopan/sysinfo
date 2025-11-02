#!/usr/bin/env python3
"""
Stage 6 — Concurrency & Parallel Tasks
Author: Vitalie Procopan

Goal:
    Manage multiple remote or local operations concurrently.

Features:
    1️⃣ Parallel ping of multiple hosts
    2️⃣ Fetch multiple URLs concurrently
    3️⃣ Parallel SSH info gathering using Paramiko
"""

import subprocess
import platform
import re
import requests
import paramiko
from concurrent.futures import ThreadPoolExecutor, as_completed

# ──────────────────────────────────────────────
# 1️⃣ Parallel Ping of Multiple Hosts
# ──────────────────────────────────────────────
def ping_host(host):
    """Ping one host and return latency or status."""
    system = platform.system()
    cmd = ["ping", "-c", "1", host] if system != "Windows" else ["ping", "-n", "1", host]
    try:
        result = subprocess.run(cmd, text=True, capture_output=True, timeout=5)
        if result.returncode == 0:
            match = re.search(r"time[=<]([\d.]+)\s*ms", result.stdout)
            latency = match.group(1) if match else "?"
            return f"✅ {host} reachable ({latency} ms)"
        else:
            return f"❌ {host} unreachable"
    except subprocess.TimeoutExpired:
        return f"⏰ {host} timeout"
    except Exception as e:
        return f"❌ {host} error: {e}"

def parallel_ping(hosts):
    print("\n🌐 Parallel Ping Test\n────────────────────────")
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(ping_host, h): h for h in hosts}
        for f in as_completed(futures):
            print(f.result())


# ──────────────────────────────────────────────
# 2️⃣ Fetch Multiple URLs Concurrently
# ──────────────────────────────────────────────
def fetch_url(url):
    """Fetch URL and return status code or error."""
    try:
        resp = requests.get(url, timeout=5)
        return f"{url} → {resp.status_code}"
    except requests.exceptions.RequestException as e:
        return f"{url} → ❌ {e.__class__.__name__}"

def parallel_fetch(urls):
    print("\n🔗 Parallel URL Fetch\n────────────────────────")
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_url, u): u for u in urls}
        for f in as_completed(futures):
            print(f.result())


# ──────────────────────────────────────────────
# 3️⃣ Parallel SSH Info Gathering
# ──────────────────────────────────────────────
def get_remote_info(host, user="root", key_file=None, cmd="hostname"):
    """Gather basic info via SSH using Paramiko."""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, key_filename=key_file, timeout=5)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        output = stdout.read().decode().strip()
        ssh.close()
        return f"✅ {host}: {output}"
    except Exception as e:
        return f"❌ {host}: {e}"

def parallel_ssh(hosts, user="root", key_file="~/.ssh/id_rsa", cmd="hostname"):
    print("\n🔐 Parallel SSH Info Gathering\n────────────────────────")
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(get_remote_info, h, user, key_file, cmd): h for h in hosts}
        for f in as_completed(futures):
            print(f.result())


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────
def main():
    print("🚀 Stage 6 — Concurrency & Parallel Tasks\n")

    # Example host and URL lists — customize as needed
    hosts = ["8.8.8.8", "1.1.1.1", "blog.procopan.md", "cy.md"]
    urls = [
        "https://google.com",
        "https://github.com",
        "https://blog.procopan.md",
        "https://cy.md",
    ]

    parallel_ping(hosts)
    parallel_fetch(urls)

    ##ssh_hosts = ["server1.domain.com"]
    ##parallel_ssh(ssh_hosts, user="root", key_file="/Users/vprocopan/.ssh/id_rsa", cmd="uptime")

    print("\n✅ All concurrent tasks completed.\n")


if __name__ == "__main__":
    main()
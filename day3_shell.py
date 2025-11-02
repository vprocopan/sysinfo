#!/usr/bin/env python3
"""
Day 3 — Automating Shell Commands (Cross-Platform)
Author: Vitalie Procopan

Goal:
    Run and control system commands from Python, safely and cross-platform.

Features:
    1️⃣ Run 'ls -l' (or 'dir' on Windows)
    2️⃣ Check if Docker is installed
    3️⃣ Ping google.com and parse latency
    4️⃣ Check Docker service/daemon status:
        • systemctl (Linux)
        • pgrep Docker.app (macOS)
"""

import subprocess
import platform
import re
import sys


# ──────────────────────────────────────────────
# Utility function for running shell commands
# ──────────────────────────────────────────────
def run_command(cmd: list[str], desc: str):
    """Run a shell command safely and print its output."""
    print(f"\n⚙️  {desc}")
    try:
        result = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            check=False
        )
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.stderr.strip():
            print("⚠️  STDERR:", result.stderr.strip())
        return result.returncode, result.stdout + result.stderr
    except FileNotFoundError:
        print(f"❌ Command not found: {cmd[0]}")
        return 127, ""
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1, ""


# ──────────────────────────────────────────────
# 1️⃣ Run ls -l / dir
# ──────────────────────────────────────────────
def run_ls():
    if platform.system() == "Windows":
        cmd = ["cmd", "/c", "dir"]
    else:
        cmd = ["ls", "-l"]
    run_command(cmd, "Listing current directory contents")


# ──────────────────────────────────────────────
# 2️⃣ Check if Docker is installed
# ──────────────────────────────────────────────
def check_docker_installation():
    code, output = run_command(["docker", "--version"], "Checking if Docker is installed")
    if code == 0:
        print("✅ Docker is installed.")
    else:
        print("❌ Docker is not installed or not in PATH.")


# ──────────────────────────────────────────────
# 3️⃣ Ping google.com and parse latency
# ──────────────────────────────────────────────
def ping_google():
    if platform.system() == "Windows":
        cmd = ["ping", "-n", "2", "google.com"]
    else:
        cmd = ["ping", "-c", "2", "google.com"]
    _, output = run_command(cmd, "Pinging google.com")

    # Extract average latency
    match = re.search(r"time[=<]([\d.]+)\s*ms", output)
    if match:
        print(f"📶 Average latency: {match.group(1)} ms")
    else:
        print("⚠️  Could not parse latency — check your ping output or network.")


# ──────────────────────────────────────────────
# 4️⃣ Check Docker daemon / service status
# ──────────────────────────────────────────────
def check_docker_status():
    system = platform.system()
    print(f"\n🧩 Checking Docker service status on {system}")

    if system == "Linux":
        # systemd-based
        code, output = run_command(["systemctl", "is-active", "docker"], "Checking Docker daemon (Linux)")
        if "active" in output:
            print("✅ Docker daemon is running.")
        else:
            print("❌ Docker daemon is not active.")
    elif system == "Darwin":
        # macOS — Docker Desktop runs via launchd
        code, output = run_command(["pgrep", "-fl", "Docker"], "Checking for Docker Desktop processes")
        if "Docker.app" in output or "com.docker.backend" in output:
            print("✅ Docker Desktop is running.")
        else:
            print("❌ Docker Desktop is not running. Open it from Applications.")
    elif system == "Windows":
        run_command(["sc", "query", "com.docker.service"], "Checking Docker Windows service")
    else:
        print("⚠️  Unsupported OS for Docker service check.")


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────
def main():
    print("🚀 Day 3 — Automating Shell Commands (Cross-Platform)\n")

    run_ls()
    check_docker_installation()
    ping_google()
    check_docker_status()

    print("\n✅ All checks completed.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\n🛑 Interrupted by user.")
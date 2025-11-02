#!/usr/bin/env python3
"""
DevOps Info Utility
Collects basic system info, disk stats, and environment diagnostics.
"""

import os
import platform
import socket
import shutil
import argparse
import logging
from datetime import datetime

def banner():
    print("\n🚀 DevOps Diagnostics v1.0")
    print(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def system_info():
    print(f"💻 Hostname: {socket.gethostname()}")
    print(f"🧠 OS: {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"🐍 Python: {platform.python_version()}")
    print(f"👤 User: {os.getenv('USER') or os.getenv('USERNAME')}")
    print(f"📂 Working dir: {os.getcwd()}")

def disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    print(f"\n💾 Disk usage on {path}:")
    print(f"  Total: {total // (2**30)} GiB")
    print(f"  Used:  {used // (2**30)} GiB")
    print(f"  Free:  {free // (2**30)} GiB")

def show_env(limit=None):
    print("\n🌍 Environment Variables:")
    for i, (k, v) in enumerate(os.environ.items()):
        print(f"  {k}={v}")
        if limit and i >= limit:
            print("  ...")
            break

if __name__ == "__main__":
    logging.basicConfig(
        filename="devops_info.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    parser = argparse.ArgumentParser(description="DevOps System Diagnostic Tool")
    parser.add_argument("--path", default="/", help="Path for disk usage")
    parser.add_argument("--env", action="store_true", help="Show environment variables")
    parser.add_argument("--limit", type=int, help="Limit number of env vars shown")
    args = parser.parse_args()

    banner()
    try:
        system_info()
        disk_usage(args.path)
        if args.env:
            show_env(args.limit)
        logging.info("Diagnostics completed successfully")
    except Exception as e:
        logging.exception("Error in diagnostics")
        print(f"❌ Error: {e}")
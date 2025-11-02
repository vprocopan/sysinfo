#!/usr/bin/env python3
import os
import platform
import socket
import shutil
import argparse

def show_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    print(f"\n💾 Disk usage for {path}:")
    print(f"  Total: {total // (2**30)} GiB")
    print(f"  Used:  {used // (2**30)} GiB")
    print(f"  Free:  {free // (2**30)} GiB")

def show_env_vars(limit=5):
    print("\n🌍 Environment Variables:")
    for i, (k, v) in enumerate(os.environ.items()):
        print(f"  {k}={v}")
        if i >= limit:
            print("  ...")
            break

def main():
    print("🚀 Hello, DevOps World!\n")
    print(f"💻 Hostname: {socket.gethostname()}")
    print(f"🧠 OS: {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"📂 Current working directory: {os.getcwd()}")
    print(f"👤 Current user: {os.getenv('USER') or os.getenv('USERNAME')}")
    print(f"🐍 Python version: {platform.python_version()}")

    parser = argparse.ArgumentParser(description="Mini DevOps System Info Utility")
    parser.add_argument("--path", default="/", help="Path to check disk usage")
    parser.add_argument("--env", action="store_true", help="Show environment variables")
    parser.add_argument("--limit", type=int, default=5, help="Limit number of env vars shown")
    args = parser.parse_args()

    show_disk_usage(args.path)
    if args.env:
        show_env_vars(limit=args.limit)

if __name__ == "__main__":
    main()
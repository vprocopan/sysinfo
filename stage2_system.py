#!/usr/bin/env python3
"""
Stage 2 – Working with the System
Goal: Interact with the OS like a DevOps script.
"""

import os
import platform
import tempfile
import glob

def show_system_info():
    print("⚙️ System Information")
    print(f"OS: {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"Python version: {platform.python_version()}")
    print(f"Current working directory: {os.getcwd()}\n")

def list_files(path="."):
    print(f"📂 Listing files in: {os.path.abspath(path)}")
    for name in os.listdir(path):
        print(" •", name)
    print()

def count_log_files(path="."):
    pattern = os.path.join(path, "*.log")
    log_files = glob.glob(pattern)
    print(f"🧾 Found {len(log_files)} .log file(s) in {os.path.abspath(path)}")
    if log_files:
        for f in log_files:
            print("   -", os.path.basename(f))
    print()

def create_and_delete_temp_file():
    print("🧪 Creating and deleting a temporary file...")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".tmp") as tmp:
        tmp_path = tmp.name
        tmp.write(b"Temporary data\n")
    print(f"Created: {tmp_path}")
    os.remove(tmp_path)
    print("Deleted temporary file ✅\n")

if __name__ == "__main__":
    show_system_info()
    list_files(".")        # or change to '/tmp' if available
    count_log_files(".")   # count .log files in current directory
    create_and_delete_temp_file()
#!/usr/bin/env python3
import os
import platform
import socket

print("🚀 Hello, DevOps World!\n")

print(f"💻 Hostname: {socket.gethostname()}")
print(f"🧠 OS: {platform.system()} {platform.release()} ({platform.machine()})")
print(f"📂 Current working directory: {os.getcwd()}")
print(f"👤 Current user: {os.getenv('USER') or os.getenv('USERNAME')}")
print(f"🗓️  Python version: {platform.python_version()}")
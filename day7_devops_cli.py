#!/usr/bin/env python3
"""
Day 7 — Logging, CLI Arguments & Packaging
Author: Vitalie Procopan

Goal:
    Make DevOps Python scripts reusable, configurable, and production-ready.

Features:
    ✅ Command-line arguments (argparse)
    ✅ Structured logging to console & file
    ✅ Modular functions
    ✅ Ready for packaging with setuptools entry point
"""

import argparse
import logging
import platform
import os
import subprocess
import sys
from datetime import datetime

# ──────────────────────────────────────────────
# Logging Setup
# ──────────────────────────────────────────────
def setup_logging(log_file="devops.log", verbose=False):
    """Configure global logging."""
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    logging.info("🔧 Logging initialized.")
    logging.debug(f"Log file: {os.path.abspath(log_file)}")


# ──────────────────────────────────────────────
# Core DevOps Utility Functions
# ──────────────────────────────────────────────
def show_system_info():
    logging.info("🧠 Gathering system information...")
    info = {
        "Hostname": platform.node(),
        "OS": f"{platform.system()} {platform.release()}",
        "Architecture": platform.machine(),
        "Python": platform.python_version(),
        "CWD": os.getcwd(),
    }
    for k, v in info.items():
        logging.info(f"{k}: {v}")
    return info


def run_shell_command(cmd):
    """Run a shell command safely."""
    logging.info(f"💻 Executing: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, text=True, capture_output=True, check=False)
        if result.returncode == 0:
            logging.debug(result.stdout.strip())
        else:
            logging.warning(result.stderr.strip())
        return result.returncode, result.stdout.strip()
    except FileNotFoundError:
        logging.error(f"Command not found: {cmd[0]}")
        return 127, ""
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return 1, ""


def check_docker():
    """Check if Docker is installed and running."""
    logging.info("🐳 Checking Docker installation...")
    code, output = run_shell_command(["docker", "--version"])
    if code == 0:
        logging.info(f"✅ Docker installed: {output}")
    else:
        logging.warning("❌ Docker not found or not in PATH.")


def ping_host(host):
    """Ping a single host."""
    logging.info(f"🌐 Pinging {host}")
    cmd = ["ping", "-c", "2", host] if platform.system() != "Windows" else ["ping", "-n", "2", host]
    code, output = run_shell_command(cmd)
    if code == 0:
        logging.info(f"✅ {host} reachable")
    else:
        logging.warning(f"❌ {host} unreachable")


# ──────────────────────────────────────────────
# CLI Definition
# ──────────────────────────────────────────────
def parse_args():
    parser = argparse.ArgumentParser(
        description="Day 7 — DevOps Utility CLI with logging and packaging support."
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Show system information",
    )
    parser.add_argument(
        "--ping",
        metavar="HOST",
        help="Ping a host (example: --ping google.com)",
    )
    parser.add_argument(
        "--check-docker",
        action="store_true",
        help="Check if Docker is installed",
    )
    parser.add_argument(
        "--log-file",
        default="devops.log",
        help="Path to log file (default: devops.log)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug output",
    )
    return parser.parse_args()


# ──────────────────────────────────────────────
# Entry Point
# ──────────────────────────────────────────────
def main():
    args = parse_args()
    setup_logging(args.log_file, args.verbose)

    logging.info(f"🚀 DevOps Utility Started — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if args.info:
        show_system_info()
    if args.ping:
        ping_host(args.ping)
    if args.check_docker:
        check_docker()

    logging.info("🏁 DevOps Utility Finished.")


if __name__ == "__main__":
    main()
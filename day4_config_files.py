#!/usr/bin/env python3
"""
Day 4 — Config Files & JSON/YAML
Author: Vitalie Procopan

Goal:
    Parse and modify common configuration file types used in DevOps:
    JSON, YAML, and .env.

Exercises:
    1️⃣ Load and print a config.json file
    2️⃣ Update one key and save back
    3️⃣ Load and print a values.yaml file
    4️⃣ Parse a .env file into key/value pairs
"""

import json
import yaml
from pathlib import Path
from datetime import datetime

# ──────────────────────────────────────────────
# Utility functions
# ──────────────────────────────────────────────
def ensure_file_exists(path: Path, default_content: str):
    """Create the file with default content if it doesn’t exist."""
    if not path.exists():
        print(f"📁 Creating example file: {path}")
        path.write_text(default_content)
    else:
        print(f"✅ Found existing file: {path}")


# ──────────────────────────────────────────────
# 1️⃣ JSON: Read, modify, write
# ──────────────────────────────────────────────
def handle_json_config(file_path="config.json"):
    path = Path(file_path)
    ensure_file_exists(
        path,
        json.dumps(
            {
                "service": "api-server",
                "version": "1.0.0",
                "replicas": 2,
                "updated": str(datetime.now())
            },
            indent=4
        ),
    )

    print("\n📖 Reading JSON configuration...")
    with open(path) as f:
        data = json.load(f)
    print(json.dumps(data, indent=4))

    # Modify one field
    print("\n🛠️  Updating replicas → 3")
    data["replicas"] = 3
    data["updated"] = str(datetime.now())

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    print("✅ JSON config updated.")


# ──────────────────────────────────────────────
# 2️⃣ YAML: Read values.yaml
# ──────────────────────────────────────────────
def handle_yaml_config(file_path="values.yaml"):
    path = Path(file_path)
    ensure_file_exists(
        path,
        """# Example Helm-like values.yaml
app:
  name: demo-app
  image: demo:latest
  replicas: 2
resources:
  limits:
    cpu: "500m"
    memory: "256Mi"
"""
    )

    print("\n📖 Reading YAML configuration...")
    with open(path) as f:
        data = yaml.safe_load(f)

    # Display nested values
    print(f"App Name: {data['app']['name']}")
    print(f"Image: {data['app']['image']}")
    print(f"Replicas: {data['app']['replicas']}")
    print(f"Memory Limit: {data['resources']['limits']['memory']}")

    # Update a field
    data["app"]["replicas"] = 3
    with open(path, "w") as f:
        yaml.safe_dump(data, f, sort_keys=False)
    print("✅ YAML config updated (replicas → 3).")


# ──────────────────────────────────────────────
# 3️⃣ ENV: Parse .env file
# ──────────────────────────────────────────────
def parse_env_file(file_path=".env"):
    path = Path(file_path)
    ensure_file_exists(
        path,
        "ENV=production\nDB_HOST=localhost\nDB_PORT=5432\nSECRET_KEY=example123\n",
    )

    print("\n📖 Parsing .env file...")
    env_vars = {}
    for line in path.read_text().splitlines():
        if line.strip() and not line.strip().startswith("#"):
            key, _, value = line.partition("=")
            env_vars[key.strip()] = value.strip()

    for k, v in env_vars.items():
        print(f"{k} = {v}")

    print("✅ Parsed .env successfully.")
    return env_vars


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────
def main():
    print("🚀 Day 4 — Config Files & JSON/YAML\n")
    handle_json_config()
    handle_yaml_config()
    parse_env_file()
    print("\n✅ Configuration file exercises completed.\n")


if __name__ == "__main__":
    main()
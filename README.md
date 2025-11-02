Absolutely 💪 — here’s a clean, professional README.md tailored for your sysinfo.py script — ready to drop into your project.
It’s formatted for GitHub or any Markdown viewer.

⸻


# 🧠 SysInfo — Mini DevOps System Information Utility

A lightweight **Python DevOps diagnostic tool** that collects basic system information, environment variables, and disk usage stats.  
Perfect for quick health checks on local or remote machines.

---

## 🚀 Features

- Prints host, OS, user, and Python version information  
- Displays disk usage for any path  
- Optionally lists environment variables  
- Supports command-line arguments  
- Works on **Linux**, **macOS**, and **Windows**  
- Ideal for use in **DevOps scripts**, **Jenkins stages**, or **remote diagnostics**

---

## 🧩 Example Output

```bash
🚀 Hello, DevOps World!

💻 Hostname: devops-node01
🧠 OS: Linux 6.8.0-40-generic (x86_64)
📂 Current working directory: /home/vitalie/devops
👤 Current user: vitalie
🐍 Python version: 3.12.4

💾 Disk usage for /:
  Total: 475 GiB
  Used: 120 GiB
  Free: 355 GiB

🌍 Environment Variables:
  SHELL=/bin/bash
  USER=vitalie
  PATH=/usr/local/bin:/usr/bin:/bin
  HOME=/home/vitalie
  LANG=en_US.UTF-8
  ...


⸻

⚙️ Installation

Clone the repository and ensure you have Python 3.8+:

git clone https://github.com/<yourusername>/sysinfo.git
cd sysinfo
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt  # (optional if you add dependencies later)


⸻

🧾 Usage

Run the script directly:

python sysinfo.py

🔧 Options

Flag	Description	Example
--path	Specify path to check disk usage	--path /var
--env	Show environment variables	--env
--limit	Limit number of environment variables printed	--env --limit 10

Example Commands

python sysinfo.py
python sysinfo.py --path /var
python sysinfo.py --env
python sysinfo.py --env --limit 15


⸻

🧰 Integration Ideas

Use Case	Description
🔍 Pre-deploy checks	Add system info to Jenkins or ArgoCD pipelines
📦 Remote diagnostics	Run via SSH or Paramiko across multiple servers
🧾 Monitoring setup	Feed output into Prometheus or Datadog scripts
🧪 CI logs	Print system info before running tests


⸻

🧑‍💻 Code Overview

Main components:
	•	show_disk_usage() → Checks disk space usage
	•	show_env_vars() → Prints environment variables
	•	main() → Entry point that parses CLI arguments

All functions are lightweight and cross-platform.

⸻

🧱 Roadmap
	•	Add JSON output mode (--json)
	•	Add system metrics (CPU, RAM)
	•	Add remote mode (via Paramiko)
	•	Add Prometheus /metrics exporter

⸻

🪪 License

MIT License — free to use and modify.
Created by Vitalie Procopan￼ 🧩

⸻

💬 Contributing

Pull requests are welcome!
If you’d like to extend this tool (e.g., remote SSH, Kubernetes info), fork it and submit a PR.

⸻

🐍 Quick Run (no clone)

To test directly:

curl -O https://raw.githubusercontent.com/<yourusername>/sysinfo/main/sysinfo.py
python sysinfo.py --env

---

## 🪪 License
This project is licensed under the [MIT License](./LICENSE).
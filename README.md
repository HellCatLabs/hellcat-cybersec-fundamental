# HellCat CyberSec Fundamentals

Welcome to **hellcat-cybersec-fundamental** — a practical, hands-on learning series covering the fundamentals of cybersecurity, offensive techniques, and malware engineering.

This repository is designed for educational purposes, with real code, real labs, and real-world logic — but zero bullshit.

![Repo Banner](./.github/banner.png)


## What you’ll find here

- Scripting and system-level command execution
- Network attacks (MITM, ARP spoof, scanning)
- Basic malware techniques (RAT, keylogger, packing)
- Detection and self-protection principles

Each folder is a standalone module with:
- Source code
- Step-by-step guides
- Blue team insights when relevant

## 📂 Modules

- [00-intro](./00-intro) — Intro to CLI, permissions, scripting basics
- [01-basics](./01-basics) — File operations, basic Python, command usage
- [02-network-ops](./02-network-ops) — Interfaces, port scanning, sniffing
- [03-malware-basics](./03-malware-basics) — Encoded payloads, keyloggers, screenshotting, exfiltration
- [04-keyloggers-trojans](./04-keyloggers-trojans) — Modular malware simulation (keylogger, exfil, persistence)
- [05-misc](./05-misc) — Extra tools: fake data gen, DNS resolver, log spammer


## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/HellCatLabs/hellcat-cybersec-fundamental.git
cd hellcat-cybersec-fundamental

# Install all dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v
```

## 🧪 Tests

The project includes an automated test suite covering all modules:

```bash
pytest tests/ -v
```

Tests verify function behavior, CLI argument parsing, and output format.
Scripts requiring `scapy` or `pynput` are automatically skipped if not installed.


## ⚠️ Legal Notice

> This project is intended for educational and defensive purposes only.  
> Do **not** use these techniques on any system you do not own or have explicit authorization to test.


## 🐾 Maintained by [HellCatLabs](https://github.com/HellCatLabs)

Created by [@Sn0wAlice](https://github.com/sn0walice) for cybersecurity learners, SOC analysts, and future reverse engineers.
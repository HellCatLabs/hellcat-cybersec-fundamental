# 🔎 Simple Port Scanner

This script scans a target IP for open TCP ports between 20 and 1024.

## What You'll Learn

- How to use Python's `socket` module
- How port scanning works (very basic)
- Why open ports matter for attackers

## How to Use

Edit the target IP in the script:

```python
target = "192.168.1.1"
```

Then run:
```
python3 scanner.py
```

Example output:
```
[+] Port open: 22
[+] Port open: 80
```

## Blue Team Insight

Port scans are easy to detect with tools like Zeek, Suricata, or fail2ban.
Seeing a lot of connections to many ports in a short time is a clear sign of recon.
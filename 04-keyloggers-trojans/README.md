# 🧠 04 - Keyloggers & Trojans (Combined Lab)

This lab shows how real malware combines multiple behaviors into one script:

- Keystroke capture
- Local data storage
- (Optional) Data exfiltration
- (Optional) Startup persistence

## What You'll Learn

- How malware modules are structured
- How to organize Python code for stealth and persistence
- How keyloggers are embedded in backdoors and trojans

## Structure

```
trojan.py            → Main dropper / backdoor simulator
modules/keylogger.py → Keystroke logger module
modules/exfil.py     → Sends logs to remote server
modules/autostart.py → (Simulated) registry-based persistence
```

## Running the Lab

1. Install requirements:

```
pip install pynput requests
```

2. Run the trojan simulator:

```
python3 trojan.py
```

Output:
- Logs saved to `keylog.txt`
- (Optional) exfiltration to HTTP server
- (Optional) fake registry entry added for autostart

## Blue Team Insight

Real malware often looks like this:

- Modular code
- Passive keylogging / persistence
- Periodic beacon or exfil
- Disguised as benign app or background task

Detection strategy:
- Look for processes using `pynput` or `GetAsyncKeyState`
- Monitor file writes to log-like files
- Track outbound traffic or DNS beacons


## Bonus Challenge

- Add webcam screenshot capture
- Auto-remove logs after exfil
- Encrypt log file content

## Related Modules

- **Keylogger theory**: [03-malware-basics/04_keylogger](../03-malware-basics/04_keylogger) — Standalone keylogger lab
- **Exfiltration**: [03-malware-basics/06_exfil_via_http](../03-malware-basics/06_exfil_via_http) — HTTP exfil explained in detail
- **Persistence**: [03-malware-basics/01_persistence_registry](../03-malware-basics/01_persistence_registry) — Registry persistence deep dive
- **Network layer**: [02-network-ops](../02-network-ops) — Understand MITM, sniffing, and ARP used alongside trojans
- **Test data**: [05-misc](../05-misc) — Generate fake datasets to test your detection rules
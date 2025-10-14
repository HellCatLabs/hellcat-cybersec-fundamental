# 🕵️ 04 - ARP Spoofer

This lab simulates a basic **ARP spoofing attack** using Scapy.


## What You'll Learn

- What ARP is and why it’s vulnerable
- How attackers poison ARP tables to intercept traffic
- How to build and send forged ARP reply packets with Python
- How defenders detect and prevent ARP spoofing

## What is ARP Spoofing?

**ARP (Address Resolution Protocol)** maps IP addresses to MAC addresses on local networks.

In ARP spoofing, an attacker sends forged ARP replies to a victim, saying:

> “Hey, I’m the gateway (e.g., 192.168.1.1) — send your traffic to my MAC!”

This lets the attacker silently intercept traffic between the victim and the router — often used for **MITM attacks**.

## How to Use

1. Edit the script to set your `target_ip` and `gateway_ip`.

2. Run it with root privileges:

```
sudo python3 arp_spoof.py
```

You’ll see output like:

```
[*] Spoofing 192.168.1.10 into thinking we're 192.168.1.1...
[+] ARP packet sent
[+] ARP packet sent
...
```

Stop the attack anytime with `CTRL+C`.

## Bonus Ideas

- Use Scapy to auto-discover MAC addresses on the network
- Add a `restore()` function to clean up the ARP table after stopping
- Combine with your packet sniffer for a full MITM demo

## Blue Team Insight

Signs of ARP spoofing:
- Multiple IPs claiming the same MAC
- Unusual ARP traffic volume
- Inconsistent ARP cache entries

How to detect it:
- Tools: `arpwatch`, Zeek, Suricata
- Static ARP tables on critical hosts
- Switch-level protections: Dynamic ARP Inspection (DAI), port security

## Warning

This script is for **educational use only**.  
Never run ARP spoofing outside of isolated lab environments.
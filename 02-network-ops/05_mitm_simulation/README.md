# 🧪 05 - MITM Simulation (ARP Spoof + Sniff)

This lab combines ARP spoofing and packet sniffing to simulate a simple **Man-in-the-Middle attack** on a local network.

## What You'll Learn

- How ARP spoofing leads to MITM
- How to passively intercept traffic between two hosts
- How to build this in Python using Scapy
- How to detect such behavior on a network

## How to Use

1. Edit the script to set:

- `target_ip` → victim IP
- `gateway_ip` → router IP

2. Run with root permissions:

```
sudo python3 mitm.py
```

You’ll see output like:

```
[*] Starting ARP spoof between 192.168.1.10 and 192.168.1.1
[*] Starting packet sniffer...
Ether / IP / TCP 192.168.1.10:12345 > 93.184.216.34:http S
Ether / IP / UDP 192.168.1.10:55421 > 8.8.8.8:domain
...
```

3. Stop with `CTRL+C`

The script will restore ARP tables automatically.

## Bonus Ideas

- Log packets to a file
- Parse only HTTP or DNS
- Forward traffic instead of just sniffing (requires IP forwarding)
- Add MAC resolution with ARP who-has requests

## Blue Team Insight

Signs of active MITM:
- Frequent unsolicited ARP replies
- Device MAC addresses switching rapidly in logs
- Devices seeing unexpected traffic

Detection tips:
- Monitor ARP table changes
- Use Zeek or Suricata to detect MAC/IP mismatch
- Look for duplicate IPs or rogue gateways

## Warning

Only run this lab on isolated test environments.  
Never attempt MITM attacks on real or production networks.

You're doing this to **learn** — not to harm.
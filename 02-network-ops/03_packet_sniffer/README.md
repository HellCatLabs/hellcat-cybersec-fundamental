# 📥 03 - Packet Sniffer

This script shows how to capture raw network packets using Python and Scapy.

## What You'll Learn

- How to sniff packets using `scapy`
- What kind of network data can be observed
- Why this technique is used in offensive and defensive contexts

## How to Use

1. Install Scapy (if needed):

```bash
pip install scapy
```

2.	Run the script as root or using sudo:

```bash
sudo python3 sniffer.py
```

You should see output like:
```
Ether / IP / TCP 192.168.1.10:4321 > 192.168.1.1:http S
Ether / IP / UDP 192.168.1.10:1234 > 8.8.8.8:domain
```

Press CTRL+C to stop the sniffer.


## Try This
- Add a filter to show only DNS packets:
```bash
sniff(filter="udp port 53", prn=packet_callback, store=False)
```

- Log results to a file
- Print full packet content with packet.show()


## Blue Team Insight

Packet sniffing is often used in:
- ARP spoof attacks
- Credential harvesting (on insecure protocols)
- Network reconnaissance

Use tools like Wireshark, Suricata, or Zeek to detect suspicious sniffing behavior.
Promiscuous mode + traffic mirroring = high risk on open networks.
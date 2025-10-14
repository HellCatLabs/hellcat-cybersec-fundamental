# 📡 Network Interface Info

This script displays basic information about your local machine's network setup.

## What You'll Learn

- How to retrieve the hostname
- How to get the local IP address
- Why local network info matters in offensive operations

## How to Use

```bash
python3 iface_info.py
```

Example output:

```
Hostname: kali
Local IP: 192.168.56.101
```

## Blue Team Insight

Knowing the local IP helps attackers map internal networks.
On a compromised host, this is often the first step in lateral movement.


# 🔄 MAC Address Changer (Linux only)

This script demonstrates how to change the MAC address of a network interface using Python and the `subprocess` module.

> ⚠️ Requires **root privileges** and works only on **Linux** with `ifconfig` available.

## Why change your MAC address?

Changing your MAC address can be useful to:
- Evade basic network filters
- Test DHCP behavior
- Obfuscate device identity in lab environments

## How it works

The script:
1. Brings the network interface down
2. Changes its MAC address with `ifconfig`
3. Brings the interface back up

## Example

```bash
sudo python3 mac_changer.py
```

Expected output:
```
[+] Changing MAC address for eth0 to 00:11:22:33:44:55
[+] MAC address changed successfully.
```

#⚠️ Disclaimer
- This technique is for educational use in controlled environments only.
- Do not use it on production or unauthorized networks.
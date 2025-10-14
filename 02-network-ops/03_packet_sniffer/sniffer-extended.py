# ⚠️ Requires: pip install scapy
# ⚠️ Must be run as root (sudo)

from scapy.all import sniff, DNS, Raw
from datetime import datetime

LOG_FILE = "sniffer_log.txt"

def log_packet(pkt):
    """Write packet summary to log file."""
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {pkt.summary()}\n")

def process_packet(pkt):
    # Print and log every captured packet
    print(f"[+] Packet: {pkt.summary()}")
    log_packet(pkt)

    # DNS Request
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        try:
            queried = pkt[DNS].qd.qname.decode()
            print(f"    📡 DNS Query: {queried}")
        except:
            pass

    # Potential HTTP (port 80 + raw payload)
    if pkt.haslayer(Raw) and pkt.haslayer("TCP") and pkt["TCP"].dport == 80:
        payload = pkt[Raw].load
        try:
            if b"Host:" in payload or b"GET" in payload:
                print("    🌐 HTTP Payload:")
                print(payload.decode(errors="ignore").strip())
        except:
            pass

print("[*] Starting extended sniffer on default interface...")
print("[*] Logging to:", LOG_FILE)

# Sniff only TCP/UDP traffic (ignore ARP, ICMP, etc.)
sniff(filter="tcp or udp", prn=process_packet, store=False)
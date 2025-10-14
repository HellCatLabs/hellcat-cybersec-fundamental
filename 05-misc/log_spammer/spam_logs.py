#!/usr/bin/env python3
"""
spam_logs.py
Generate many log lines (syslog-like) to stress-test parsers or simulate noisy environments.
"""

import time
import random
import argparse
from datetime import datetime

LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]
SOURCES = ["auth", "kernel", "app", "web", "db", "proxy"]
MSGS = [
    "User login succeeded",
    "User login failed: invalid password",
    "Connection reset by peer",
    "Disk usage above threshold",
    "Service started",
    "Service stopped unexpectedly",
    "Database connection timeout",
    "HTTP 500 on /api/login",
    "Blocked attempt from blacklisted IP",
    "New session created"
]

def gen_line():
    ts = datetime.utcnow().isoformat() + "Z"
    level = random.choice(LEVELS)
    source = random.choice(SOURCES)
    msg = random.choice(MSGS)
    ip = f"{random.randint(10,200)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    return f"{ts} {level} [{source}] src={ip} msg=\"{msg}\""

def main(rate_per_sec, lines, outfile=None):
    count = 0
    f = open(outfile, "a") if outfile else None
    try:
        while lines < 0 or count < lines:
            line = gen_line()
            print(line)
            if f:
                f.write(line + "\n")
                f.flush()
            count += 1
            time.sleep(1.0 / rate_per_sec)
    except KeyboardInterrupt:
        print("\n[!] Stopped.")
    finally:
        if f:
            f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate spammy log lines")
    parser.add_argument("-r", "--rate", type=float, default=5.0, help="Lines per second")
    parser.add_argument("-n", "--number", type=int, default=-1, help="-1 for infinite")
    parser.add_argument("-o", "--outfile", default=None, help="Optional file to append logs")
    args = parser.parse_args()
    main(args.rate, args.number, args.outfile)
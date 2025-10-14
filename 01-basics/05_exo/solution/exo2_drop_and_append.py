# Exercise 2 — Drop-and-Append

from datetime import datetime
import os
import socket

filename = "report.log"
line = f"[{datetime.now()}] Run by {os.getlogin()}@{socket.gethostname()}\n"

with open(filename, "a") as f:
    f.write(line)

print(f"[+] Logged: {line.strip()}")
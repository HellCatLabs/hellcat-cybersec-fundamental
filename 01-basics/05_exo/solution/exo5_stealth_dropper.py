# Exercise 5 — Stealth Dropper (Hard)

import os
import random
import string
from pathlib import Path

# 1. Generate random file name
name = ''.join(random.choices(string.ascii_lowercase, k=8)) + ".bin"

# 2. Get temp folder
temp_path = Path(os.getenv("TEMP") or "/tmp")
full_path = temp_path / name

# 3. Write binary payload
with open(full_path, "wb") as f:
    f.write(b"\x90\x90\x90\xcc")

# 4. Log path in ~/.hellcat_log
log_path = Path.home() / ".hellcat_log"
with open(log_path, "a") as f:
    f.write(f"[STEALTH] {full_path}\n")

print(f"[+] Dropped stealth payload: {full_path}")
print(f"[+] Logged in: {log_path}")
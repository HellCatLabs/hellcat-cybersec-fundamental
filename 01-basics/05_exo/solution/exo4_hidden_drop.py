# Exercise 4 — Drop in Hidden Location

import os
from pathlib import Path

if os.name == "nt":
    # Windows
    drop_path = Path(os.getenv("APPDATA")) / "hidden_drop.txt"
else:
    # Linux
    drop_path = Path.home() / ".config" / "hidden_drop.txt"

with open(drop_path, "w") as f:
    f.write("This file is hidden in a common folder.\n")

print(f"[+] Dropped: {drop_path}")
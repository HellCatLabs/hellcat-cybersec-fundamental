import os
import random
import string
from pathlib import Path

# -----------------------------------------
# 🧠 GOAL: Simulate various file-dropper behaviors
# -----------------------------------------

def drop_text_file(filename="dropped.txt"):
    """1. Create a simple text file."""
    with open(filename, "w") as f:
        f.write("This is a test drop.\n")
    print(f"[+] Dropped file: {filename}")

def append_to_file(filename="dropped.txt"):
    """2. Append content to an existing file."""
    with open(filename, "a") as f:
        f.write("Appended line\n")
    print(f"[+] Appended to file: {filename}")

def drop_in_temp_folder():
    """3. Drop a file in the system's temp folder."""
    tmp_path = Path(os.getenv("TEMP") or "/tmp")
    full_path = tmp_path / "tempdrop.txt"
    with open(full_path, "w") as f:
        f.write("Dropped in temp folder.\n")
    print(f"[+] Dropped file in temp folder: {full_path}")

def drop_with_random_name(extension=".txt"):
    """4. Drop a file with a randomly generated name."""
    name = ''.join(random.choices(string.ascii_lowercase, k=8)) + extension
    with open(name, "w") as f:
        f.write("Random file drop\n")
    print(f"[+] Dropped file with random name: {name}")

def write_binary_file():
    """5. Write binary content to a file (simulating payload)."""
    with open("bin_payload.bin", "wb") as f:
        f.write(b"\x4d\x5a\x90\x00")  # Example: MZ header
    print("[+] Wrote binary payload")

def overwrite_existing_file(filename="dropped.txt"):
    """6. Overwrite the content of an existing file."""
    with open(filename, "w") as f:
        f.write("This file has been overwritten.\n")
    print(f"[!] Overwritten file: {filename}")

def drop_to_startup():
    """7. Drop a file into the Windows Startup folder (persistence test)."""
    startup = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
    if os.path.isdir(startup):
        path = os.path.join(startup, "startup_drop.txt")
        with open(path, "w") as f:
            f.write("Autostart test\n")
        print(f"[+] Dropped file to Startup folder: {path}")
    else:
        print("[!] Startup folder not found or not on Windows.")

# -----------------------------------------
# MAIN
# -----------------------------------------

if __name__ == "__main__":
    print("[*] Simulating dropper behaviors...\n")

    drop_text_file()
    append_to_file()
    drop_in_temp_folder()
    drop_with_random_name()
    write_binary_file()
    overwrite_existing_file()
    drop_to_startup()

    print("\n[*] Done.")
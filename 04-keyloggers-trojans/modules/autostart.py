# autostart.py — simulate registry persistence (without touching real system)

import os

def simulate_persistence():
    key_path = r"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    program_name = "WinHelper"
    program_path = os.path.abspath("trojan.py")

    print(f"[*] Simulating registry persistence:")
    print(f"    {key_path}\\{program_name} = {program_path}")
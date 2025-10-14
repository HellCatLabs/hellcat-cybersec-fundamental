# Exercise 3 — MAC Address Randomizer (Linux)

import subprocess
import random

def random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(5))

iface = "eth0"
mac = random_mac()

print(f"[*] Changing MAC of {iface} to {mac}")

subprocess.call(["sudo", "ifconfig", iface, "down"])
subprocess.call(["sudo", "ifconfig", iface, "hw", "ether", mac])
subprocess.call(["sudo", "ifconfig", iface, "up"])

print("[+] MAC address changed (temporarily)")
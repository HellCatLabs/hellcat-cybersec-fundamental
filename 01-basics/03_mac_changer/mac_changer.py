import subprocess
import argparse

parser = argparse.ArgumentParser(description="Change MAC address (Linux, requires root)")
parser.add_argument("-i", "--interface", default="eth0", help="Network interface (default: eth0)")
parser.add_argument("-m", "--mac", default="00:11:22:33:44:55", help="New MAC address")
args = parser.parse_args()

print(f"[*] Changing MAC of {args.interface} to {args.mac}")
subprocess.call(["sudo", "ifconfig", args.interface, "down"])
subprocess.call(["sudo", "ifconfig", args.interface, "hw", "ether", args.mac])
subprocess.call(["sudo", "ifconfig", args.interface, "up"])

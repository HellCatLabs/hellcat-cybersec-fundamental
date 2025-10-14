import subprocess

print("[*] Changing MAC of eth0 to 00:11:22:33:44:55")
subprocess.call(["sudo", "ifconfig", "eth0", "down"])
subprocess.call(["sudo", "ifconfig", "eth0", "hw", "ether", "00:11:22:33:44:55"])
subprocess.call(["sudo", "ifconfig", "eth0", "up"])
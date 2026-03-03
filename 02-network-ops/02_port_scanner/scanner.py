import socket
import argparse

parser = argparse.ArgumentParser(description="Basic TCP port scanner")
parser.add_argument("target", help="Target IP address (e.g. 192.168.1.1)")
parser.add_argument("--start-port", type=int, default=20, help="First port to scan (default: 20)")
parser.add_argument("--end-port", type=int, default=1024, help="Last port to scan (default: 1024)")
parser.add_argument("--timeout", type=float, default=0.3, help="Socket timeout in seconds (default: 0.3)")
args = parser.parse_args()

print(f"[*] Scanning {args.target} — ports {args.start_port}-{args.end_port} (timeout {args.timeout}s)")
for port in range(args.start_port, args.end_port + 1):
    try:
        sock = socket.socket()
        sock.settimeout(args.timeout)
        sock.connect((args.target, port))
        print(f"[+] Port open: {port}")
        sock.close()
    except:
        pass

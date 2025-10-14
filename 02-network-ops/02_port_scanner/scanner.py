import socket

target = "192.168.1.1"
for port in range(20, 1025):
    try:
        sock = socket.socket()
        sock.settimeout(0.3)
        sock.connect((target, port))
        print(f"[+] Port open: {port}")
        sock.close()
    except:
        pass
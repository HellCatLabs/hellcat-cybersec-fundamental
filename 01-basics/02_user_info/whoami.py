import os
import socket

# Print the current user's login name and the system's hostname
print("User:", os.getlogin())
print("Hostname:", socket.gethostname())
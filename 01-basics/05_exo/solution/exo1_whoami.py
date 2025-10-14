# Exercise 1 — Who Are You, Really?

import os
import socket
from pathlib import Path

print("Username :", os.getlogin())
print("Hostname :", socket.gethostname())
print("Home dir :", Path.home())
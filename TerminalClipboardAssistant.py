import time
import pyperclip

history = []
last = None

while True:
    current = pyperclip.paste()
    if current != last and current.strip():
        history.append(current)
        last = current
        print(f"Copied: {current}")
    time.sleep(0.5)


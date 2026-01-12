# Clipboard Monitor

A small Python script that monitors your system clipboard and records copied
text in real time.

The script watches for changes to the clipboard, keeps a history of copied
strings, and optionally prints or logs them as they occur.

> **THIS IS EXCLUSIVELY FOR EDUCATIONAL PURPOSES. THERE ARE SIMILAR AND MORE ADVANCED TOLLS AVAILABLE**

> **Privacy note:** This script captures everything you copy, including
> potentially sensitive information (passwords, tokens, private text). Use responsibly.

---

## Features

- Monitors clipboard changes in real time
- Captures text copied after the script starts
- Stores clipboard history in memory
- Optionally prints copied text to the terminal
- Easy to extend (save to file, limit history, filtering, etc.)
- Cross-platform (Linux, macOS, Windows)

---

## Requirements

- Python 3.8+
- `pyperclip`

On Linux, you may also need a clipboard backend:
- `xclip`, `xsel`, or `wl-clipboard`

---

## Run in a virtual environment & install pyperclip

> python3 -m venv .venv
> 
> source .venv/bin/activate
> 
> python -m pip install pyperclip


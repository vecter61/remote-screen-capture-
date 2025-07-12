# remote-screen-capture-
# Windows Screenshot Capture & Upload Tool

This is a Python-based tool that runs on Windows and:

- Takes screenshots of the user's desktop periodically (every X seconds),
- Saves them temporarily,
- Uploads them to a remote server via HTTP POST.

> ⚠️ This tool is for **educational and ethical use only**. You must have full legal authorization to run it on any device.

---

## 💻 Features

- Works on Windows 10/11
- Runs from the terminal or in the background (when bundled as `.exe`)
- Uploads screenshots via HTTP
- Lightweight (only standard and a few external Python libraries)

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install pyautogui requests

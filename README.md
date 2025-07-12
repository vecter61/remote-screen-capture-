# 🖥️ Remote Screen Capture (Windows Client + Flask Server)

This project lets you:

- 📸 Capture desktop screenshots on a Windows machine automatically
- 📤 Upload them to a central server (e.g., VPS or local host)
- 📁 Store screenshots in a secure upload folder
- 🧪 Ideal for research labs, device monitoring (with permission), and testing environments

> 🚨 WARNING: Before deploying this script on any Windows system, **you MUST convert it to a standalone `.exe`** using the instructions below. This ensures smooth background operation and better control over execution.

---

## 📁 Project Structure

```
remote-screen-capture/
├── client_capture.py        # Windows screenshot script
├── .gitignore
├── README.md
└── server/
    └── image_receiver.py    # Flask server to receive images
```

---

## ⚙️ Installation Instructions

### 🖥️ On the Windows Client (Screenshot Capturer)

#### ✅ 1. Install Python and dependencies

- Download Python 3.10+ from [python.org](https://www.python.org/downloads/windows/)
- During install, check **“Add Python to PATH”**

Then install dependencies:

```bash
pip install pyautogui requests pyinstaller
```

#### ✅ 2. Set server address

Open `client_capture.py` and **replace this line** with your server IP:

```python
SERVER_URL = "http://YOUR_SERVER_IP/upload"
```

Example:

```python
SERVER_URL = "http://192.168.1.30/upload"
```

---

### ❗ 3. Convert to `.exe` BEFORE running

> 💡 You MUST convert this to a `.exe` before running or deploying.

Run:

```bash
pyinstaller --onefile client_capture.py
```

This creates:

```
dist/client_capture.exe
```

> ✅ Use `client_capture.exe` to run on Windows systems  
> ⛔️ Do NOT run `.py` scripts directly for monitoring purposes — `.exe` is cleaner and safer

---

### 📤 On the Server (Flask Receiver)

#### 1. Install Python 3

#### 2. Install Flask

```bash
pip install flask
```

#### 3. Create uploads folder

```bash
mkdir uploads
```

#### 4. Run the server

```bash
python3 server/image_receiver.py
```

The server will be available at:

```
http://<your_server_ip>/upload
```

Uploaded screenshots will be saved in the `uploads/` directory.

---

## 🚀 Usage (Step-by-Step)

### On Windows Client

1. Edit the `SERVER_URL` in `client_capture.py`
2. Run `pyinstaller --onefile client_capture.py`
3. Navigate to the `dist/` folder
4. Double-click `client_capture.exe` to start sending screenshots

### On Server

1. Run `python3 server/image_receiver.py`
2. Watch `uploads/` fill with screenshot files

---

## 💡 What It Does

- Every 10 seconds:
  - Takes a screenshot using `pyautogui`
  - Saves it temporarily (e.g., `screenshot_1720781830.png`)
  - Uploads it to the Flask server
  - Deletes it locally after successful upload

---

## 🔐 Security & Ethics

- 📛 Never run this on any device without full, informed **legal permission**
- 🔐 Add HTTPS and API tokens for secure, authenticated uploads
- 📡 Only allow known IPs to connect to the server
- 🚫 Unauthorized monitoring may violate local or international privacy laws (e.g., GDPR, CFAA)

---

## ☕ Support This Project

If you find this project useful and would like to support its development, consider donating. Your contributions help keep open-source tools like this alive. ❤️

**Bitcoin (BTC) Wallet Address:**

```
bc1qlpw590fkykfdd9v92g9snfmx8hc8vwxvkz5npm
```

Or scan the QR code:


![Donate BTC]
(https://api.qrserver.com/v1/create-qr-code/?data=bitcoin:bc1qbc1qlpw590fkykfdd9v92g9snfmx8hc8vwxvkz5npm&size=200x200)

Thank you for your support! 🙏

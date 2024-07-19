"""
This script monitors a specified website and alerts the user with an on-screen message
when the website is back up. It periodically checks the website status at a defined interval.

Requirements:
- requests library
- tkinter library (comes with Python's standard library)

Usage:
- Set the website_url to the URL of the website you want to monitor.
- Set the check_interval to the desired time interval between checks (in seconds).
- Run the script. It will continuously check the website status and display an alert
  when the website is back up.
"""

import requests
import time
from tkinter import Tk, messagebox

# Configuration
website_url = "https://example.com"
check_interval = 60  # in seconds

def is_website_up(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

def show_alert(message):
    root = Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Website Status Alert", message)
    root.destroy()

def monitor_website(url, interval):
    while True:
        if is_website_up(url):
            show_alert(f"The website {url} is back up!")
            break
        else:
            print(f"The website {url} is still down.")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_website(website_url, check_interval)

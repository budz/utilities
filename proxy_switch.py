import os
import subprocess
import winreg
from plyer import notification

def toggle_proxy():
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    value_name = "ProxyEnable"

    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
            current_value, reg_type = winreg.QueryValueEx(key, value_name)
            
            new_value = 0 if current_value == 1 else 1
            winreg.SetValueEx(key, value_name, 0, reg_type, new_value)

            if new_value == 1:
                display_notification("Proxy Enabled", "Proxy is now enabled.", "Hand")
            else:
                display_notification("Proxy Disabled", "Proxy is now disabled.", "Hand")

def display_notification(title, message, icon):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # Path to a .ICO file can be specified here
        timeout=2,  # Notification duration in seconds
        toast=True
    )

if __name__ == "__main__":
    toggle_proxy()

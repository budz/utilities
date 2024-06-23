#Power Plan Auto Switching Script
# open terminal and run 'powercfg /list' to get available power plan guids
# make sure python is installed
# pip install plyer
# run change_power_plan.py in cmd  python change_power_plan.py
# when ran the script will get current power plan active and switch to the other.

import subprocess
from plyer import notification

# GUIDs for the power plans
BALANCED_GUID = "381b4222-f694-41f0-9685-ff5bb260df2e"
ULTIMATE_GUID = "5e85d9b9-da4d-450e-9317-ec31211407b9"  # Correct GUID from your system

def get_current_power_plan():
    result = subprocess.run(["powercfg", "/getactivescheme"], capture_output=True, text=True)
    output = result.stdout.strip()
    print(f"Current power plan output: {output}")
    try:
        current_guid = output.split(":")[1].strip().split()[0]
        print(f"Current power plan GUID: {current_guid}")
        return current_guid
    except IndexError:
        print("Failed to parse current power plan GUID.")
        return None

def is_power_plan_available(guid):
    result = subprocess.run(["powercfg", "/list"], capture_output=True, text=True)
    output = result.stdout.strip()
    print(f"Available power plans: {output}")
    return guid in output

def set_power_plan(guid):
    result = subprocess.run(["powercfg", "/setactive", guid], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully set power plan to {guid}")
    else:
        print(f"Failed to set power plan to {guid}. Error: {result.stderr}")

def display_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=2,
        toast=True
    )

def toggle_power_plan():
    current_guid = get_current_power_plan()
    
    if current_guid == BALANCED_GUID:
        if is_power_plan_available(ULTIMATE_GUID):
            set_power_plan(ULTIMATE_GUID)
            display_notification("Power Plan Changed", "Switched to Ultimate Performance")
        else:
            print("Ultimate Performance power plan is not available.")
    elif current_guid == ULTIMATE_GUID:
        if is_power_plan_available(BALANCED_GUID):
            set_power_plan(BALANCED_GUID)
            display_notification("Power Plan Changed", "Switched to Balanced")
        else:
            print("Balanced power plan is not available.")
    else:
        print("Unknown power plan GUID, unable to toggle.")

if __name__ == "__main__":
    toggle_power_plan()

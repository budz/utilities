import os
from pathlib import Path
import subprocess

# Define the path to the state file
state_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "displayState.txt")

# Check if the state file exists, if not, create it and set the initial state to 'on'
if not Path(state_file_path).exists():
    with open(state_file_path, 'w') as file:
        file.write("on")
    current_state = "on"
else:
    # Read the current state from the file
    with open(state_file_path, 'r') as file:
        current_state = file.read().strip()

# Output current state for debugging
print(f"Current display state is: {current_state}")

# Function to set monitor power mode using the command-line utility
def set_monitor_power_mode(mode):
    # Manually specify the monitor IDs to target
    monitor_ids = [3, 1]  # Adjust these IDs based on your actual setup, excluding primary monitor (usually ID 1)

    for monitor_id in monitor_ids:
        command = ["monitorcontrol", "--set-power-mode", mode, "--monitor", str(monitor_id)]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Monitor {monitor_id} set to {mode}.")
        else:
            print(f"Failed to set monitor {monitor_id} to {mode}. Error: {result.stderr}")

# Switch the display state based on the current state in the file
if current_state == "on":
    set_monitor_power_mode("suspend")
    with open(state_file_path, 'w') as file:
        file.write("suspend")
    print("Switched to suspend. Updating state to 'suspend'.")
else:
    set_monitor_power_mode("on")
    with open(state_file_path, 'w') as file:
        file.write("on")
    print("Switched to on. Updating state to 'on'.")

# Optional: Uncomment the next line to pause the script and see the output when running
# input("Press Enter to exit")

import os
from pathlib import Path
import subprocess

# Define the path to the state file
state_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "displayState.txt")

# Check if the state file exists, if not, create it and set the initial state to 'extend'
if not Path(state_file_path).exists():
    with open(state_file_path, 'w') as file:
        file.write("extend")
    current_state = "extend"
else:
    # Read the current state from the file
    with open(state_file_path, 'r') as file:
        current_state = file.read().strip()

# Output current state for debugging
print(f"Current display state is: {current_state}")

# Switch the display state based on the current state in the file
if current_state == "extend":
    subprocess.run(["DisplaySwitch.exe", "/internal"])
    with open(state_file_path, 'w') as file:
        file.write("internal")
    print("Switched to internal. Updating state to 'internal'.")
else:
    subprocess.run(["DisplaySwitch.exe", "/extend"])
    with open(state_file_path, 'w') as file:
        file.write("extend")
    print("Switched to extend. Updating state to 'extend'.")

# Optional: Uncomment the next line to pause the script and see the output when running
# input("Press Enter to exit")

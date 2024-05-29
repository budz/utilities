"""
Mouse Movement Tracker Script

Purpose:
This script tracks the mouse position and the frequency of mouse movements.
It records the X and Y coordinates of the mouse pointer every time it moves,
and it counts how many movements occur each second.

Usage:
1. Ensure you have the 'pynput' library installed. You can install it using:
   pip install pynput

2. Run the script in your Python environment. The script will start tracking
   the mouse movements as soon as it is run.

3. The script prints the latest X, Y coordinates of the mouse pointer and the
   frequency of movements every second.

4. To stop the script, press Ctrl+C. The script will stop tracking and print
   the final tracked data.

Note:
- The script uses a deque to store the last 60 movements and frequencies.
- You can adjust the 'maxlen' parameter of the deque if you want to store
  more or fewer movements.

Example Output:
After running the script, you will see lines like the following printed every second:
    X Y Frequency
where X and Y are the coordinates of the mouse pointer, and Frequency is the
number of movements detected in the last second.
"""

import time
from pynput import mouse
from collections import deque

# Initialize variables
positions = deque(maxlen=60)  # Store positions for the last 60 movements
frequencies = deque(maxlen=60)  # Store frequencies for the last 60 seconds

def on_move(x, y):
    global positions, frequencies
    positions.append((x, y))
    if len(frequencies) == 0 or time.time() - frequencies[-1][0] >= 1:
        frequencies.append((time.time(), 1))
    else:
        frequencies[-1] = (frequencies[-1][0], frequencies[-1][1] + 1)

def on_click(x, y, button, pressed):
    # This function can be used to handle mouse clicks if needed
    pass

def on_scroll(x, y, dx, dy):
    # This function can be used to handle mouse scrolls if needed
    pass

# Start the mouse listener
listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
listener.start()

try:
    while True:
        #time.sleep(1)  # Update frequency every second
        if positions:
            last_position = positions[-1]
            last_frequency = frequencies[-1][1] if frequencies else 0
            print(f"{last_position[0]} {last_position[1]} {last_frequency}")
except KeyboardInterrupt:
    # Stop the listener when interrupted
    listener.stop()
    print("Listener stopped.")

    # Print final results
    print("Final tracked data:")
    for t, pos in zip(frequencies, positions):
        print(f"{pos[0]} {pos[1]} {t[1]}")

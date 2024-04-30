import screen_brightness_control as sbc

# Function to safely decrease brightness by 10%
def decrease_brightness(display, decrement=10):
    try:
        current_brightness = sbc.get_brightness(display=display)
        if isinstance(current_brightness, list):
            current_brightness = current_brightness[0]  # Assume first value if multiple are returned

        new_brightness = max(current_brightness - decrement, 0)  # Cap brightness at 0 to avoid errors
        sbc.set_brightness(new_brightness, display=display)
        print(f"Brightness of display {display} set to {new_brightness}%")
    except Exception as e:
        print(f"Failed to set brightness for display {display}: {e}")

# Apply the brightness decrease to each monitor
for display in range(3):  # Adjust the range if there are more or fewer displays
    decrease_brightness(display)

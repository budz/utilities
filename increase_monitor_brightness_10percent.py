import screen_brightness_control as sbc

# Function to safely increase brightness by 10%
def increase_brightness(display, increment=10):
    try:
        current_brightness = sbc.get_brightness(display=display)
        if isinstance(current_brightness, list):
            current_brightness = current_brightness[0]  # Assume first value if multiple are returned

        new_brightness = min(current_brightness + increment, 100)  # Cap brightness at 100 to avoid errors
        sbc.set_brightness(new_brightness, display=display)
        print(f"Brightness of display {display} increased to {new_brightness}%")
    except Exception as e:
        print(f"Failed to increase brightness for display {display}: {e}")

# Apply the brightness increase to each monitor
for display in range(3):  # Adjust the range if there are more or fewer displays
    increase_brightness(display)

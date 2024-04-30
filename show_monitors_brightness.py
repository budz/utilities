import screen_brightness_control as sbc
# show the current brightness for each detected monitor
for monitor in sbc.list_monitors():
    print(monitor, ':', sbc.get_brightness(display=monitor), '%')
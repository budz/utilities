import screen_brightness_control as sbc

# get the brightness
brightness = sbc.get_brightness()
# get the brightness for the primary monitor
primary = sbc.get_brightness(display=0)

# set the brightness to 100%
sbc.set_brightness(65)
# set the brightness to 100% for the primary monitor
sbc.set_brightness(65, display=0)
sbc.set_brightness(65, display=1)
sbc.set_brightness(65, display=2)
# show the current brightness for each detected monitor
for monitor in sbc.list_monitors():
    print(monitor, ':', sbc.get_brightness(display=monitor), '%')
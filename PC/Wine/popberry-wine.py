#Final > Jedlueng 26/2/2024
#Potberrywine making version 1

import pyautogui
import time

# Specify the screen coordinates where you want to click
x, y = 1167, 786  # Change these values to the desired coordinates

# Enable failsafe - moving the mouse to the upper-left corner will abort the script
pyautogui.FAILSAFE = True

while True:
    # Move the mouse to the specified coordinates and click

    #Delayed after running a program
    time.sleep(2)

    #Click to make wine
    pyautogui.click(x, y)

    # Wait for 62 seconds
    time.sleep(63)


    #Collect Berry
    pyautogui.click(x, y)

    #Wait
    time.sleep(2)

    



# 1167, 786
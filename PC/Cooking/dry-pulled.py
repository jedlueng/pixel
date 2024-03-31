#Final > Jedlueng 26/2/2024
#Potberry making version 1

import pyautogui
import time

# Specify the screen coordinates where you want to click
x, y = 1165, 817  # Change these values to the desired coordinates

# Enable failsafe - moving the mouse to the upper-left corner will abort the script
pyautogui.FAILSAFE = True

while True:
    # Move the mouse to the specified coordinates and click

    #Delayed after running a program
    time.sleep(2)

    pyautogui.click(x, y)

    time.sleep(3)


    #Click to make potberry
    pyautogui.click(x, y)

    # Wait for 27 seconds
    time.sleep(2100)
    # time.sleep(1500)


    #Collect Berry
    pyautogui.click(x, y)

    #Wait
    time.sleep(2)

    



# 1167, 786
#Final > Jedlueng 26/2/2024
#Javapod making version 1

import pyautogui
import time

# Specify the screen coordinates where you want to click
x, y = 1167, 786  # Change these values to the desired coordinates

x_smith, y_smith = 209, 541

wood_x , wood_y = 1003, 998

x_iron, y_iron = 704, 556

x_quit, y_quit = 1349, 274

# Enable failsafe - moving the mouse to the upper-left corner will abort the script
pyautogui.FAILSAFE = True

while True:
    # Move the mouse to the specified coordinates and click

    #Delayed after running a program
    time.sleep(2)


    pyautogui.click(wood_x, wood_y)
    time.sleep(1)
    #Click to make potberry
    pyautogui.click(x_smith, y_smith)
    time.sleep(1)

    pyautogui.click(wood_x, wood_y)
    time.sleep(1)
    pyautogui.click(x_smith, y_smith)
    time.sleep(1)
    pyautogui.click(x_smith, y_smith)
    time.sleep(1)
    pyautogui.click(x_iron, y_iron)

    time.sleep(1)

    pyautogui.click(x, y)
    time.sleep(1)

    pyautogui.click(x_quit, y_quit)

    # Wait for 182 seconds
    time.sleep(32)

    pyautogui.click(x_smith, y_smith)


    #Wait
    time.sleep(2)

    



# 1167, 786
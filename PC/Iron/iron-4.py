#Final > Jedlueng 26/2/2024
#Javapod making version 1

import pyautogui
import time

# Specify the screen coordinates where you want to click
x, y = 1167, 786  # Change these values to the desired coordinates

x_smith, y_smith = 923, 404

x_smith2, y_smith2 = 1133, 395

x_smith3, y_smith3 = 895, 735

x_smith4, y_smith4 = 1153, 735

#SLOT 4 
wood_x , wood_y = 1003, 998

x_iron, y_iron = 646, 526

x_quit, y_quit = 1349, 274

# Enable failsafe - moving the mouse to the upper-left corner will abort the script
pyautogui.FAILSAFE = True

while True:
    # Move the mouse to the specified coordinates and click

    #Delayed after running a program
    time.sleep(2)

    #Smith 1 
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


    time.sleep(2)

    #Smith 2
    pyautogui.click(wood_x, wood_y)
    time.sleep(1)
    #Click to make potberry
    pyautogui.click(x_smith2, y_smith2)
    time.sleep(1)

    pyautogui.click(wood_x, wood_y)
    time.sleep(1)
    pyautogui.click(x_smith2, y_smith2)
    time.sleep(1)
    pyautogui.click(x_smith2, y_smith2)
    time.sleep(1)
    pyautogui.click(x_iron, y_iron)

    time.sleep(1)

    pyautogui.click(x, y)
    time.sleep(1)

    pyautogui.click(x_quit, y_quit)


    time.sleep(2)
    #Smith 3
    pyautogui.click(wood_x, wood_y)
    time.sleep(1)
    #Click to make potberry
    pyautogui.click(x_smith3, y_smith3)
    time.sleep(1)

    pyautogui.click(wood_x, wood_y)
    time.sleep(1)
    pyautogui.click(x_smith3, y_smith3)
    time.sleep(1)
    pyautogui.click(x_smith3, y_smith3)
    time.sleep(1)
    pyautogui.click(x_iron, y_iron)

    time.sleep(1)

    pyautogui.click(x, y)
    time.sleep(1)

    pyautogui.click(x_quit, y_quit)


    time.sleep(2)

    #Smith 4
    pyautogui.click(wood_x, wood_y)
    time.sleep(1)
    #Click to make potberry
    pyautogui.click(x_smith4, y_smith4)
    time.sleep(1)

    pyautogui.click(wood_x, wood_y)
    time.sleep(1)
    pyautogui.click(x_smith4, y_smith4)
    time.sleep(1)
    pyautogui.click(x_smith4, y_smith4)
    time.sleep(1)
    pyautogui.click(x_iron, y_iron)

    time.sleep(1)

    pyautogui.click(x, y)
    time.sleep(1)

    pyautogui.click(x_quit, y_quit)


    time.sleep(2)


    # Wait for 182 seconds
    #Harvest 
    time.sleep(32)

    pyautogui.click(x_smith, y_smith)
    time.sleep(1)
    pyautogui.click(x_smith2, y_smith2)
    time.sleep(1)
    pyautogui.click(x_smith3,y_smith3)
    time.sleep(1)
    pyautogui.click(x_smith4,y_smith4)


    #Wait
    time.sleep(2)

    



# 1167, 786
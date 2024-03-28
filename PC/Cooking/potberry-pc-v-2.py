#Final > Jedlueng 26/2/2024
#Potberry making version 1

import pyautogui
import time

# Specify the screen coordinates where you want to click
x, y = 1167, 786  # Change these values to the desired coordinates
cook_x , cook_y = 1116, 721
x_pot,  y_pot = 694, 585
x_quit, y_quit = 1349, 274
wood_x , wood_y = 1003, 998

# Enable failsafe - moving the mouse to the upper-left corner will abort the script
pyautogui.FAILSAFE = True           

while True:
    # Move the mouse to the specified coordinates and click

    #Delayed after running a program
    time.sleep(2)
    pyautogui.click(wood_x, wood_y)
    time.sleep(1)
    #Click to make potberry
    pyautogui.click(cook_x, cook_y)
    time.sleep(1)

    pyautogui.click(wood_x, wood_y)
    time.sleep(1)
    pyautogui.click(cook_x, cook_y)
    time.sleep(1)
    pyautogui.click(cook_x, cook_y)
    time.sleep(1)
   
    

    #Click to make potberry
    pyautogui.click(x, y)

    pyautogui.click(x_quit, y_quit)

    # Wait for 27 seconds
    time.sleep(30)



    #Collect Berry
    pyautogui.click(cook_x, cook_y)

    #Wait
    time.sleep(5)

    



# 1167, 786
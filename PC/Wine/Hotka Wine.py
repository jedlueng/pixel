#Final > Jedlueng 26/2/2024
#Javapod making version 1

import pyautogui
import time

# Specify the screen coordinates where you want to click
x, y = 1167, 786  # Change these values to the desired coordinates

x_wine1, y_wine1 = 854, 405

x_wine2, y_wine2 = 1207, 398

x_wine3, y_wine3 = 854, 665

x_wine4, y_wine4  =  1189, 648

x_hotka, y_hotka = 801, 451

x_quit, y_quit = 1349, 274

# Enable failsafe - moving the mouse to the upper-left corner will abort the script
pyautogui.FAILSAFE = True

while True:
    # Move the mouse to the specified coordinates and click

    #Delayed after running a program
    time.sleep(2)

    #Click to make potberry
    pyautogui.click(x_wine1, y_wine1)
    time.sleep(1)
    pyautogui.click(x_hotka,y_hotka)
    time.sleep(1)

    pyautogui.click(x, y)
    time.sleep(1)

    pyautogui.click(x_quit,y_quit)

    time.sleep(1)

    pyautogui.click(x_wine2, y_wine2)
    time.sleep(1)
    pyautogui.click(x_hotka,y_hotka)
    time.sleep(1)

    pyautogui.click(x, y)
    time.sleep(1)

    pyautogui.click(x_quit,y_quit)

    time.sleep(1)
     
    pyautogui.click(x_wine3, y_wine3)
    time.sleep(1)
    pyautogui.click(x_hotka,y_hotka)
    time.sleep(1)

    pyautogui.click(x, y)
    time.sleep(1)

    pyautogui.click(x_quit,y_quit)
    time.sleep(1)

    pyautogui.click(x_wine4, y_wine4)
    time.sleep(1)
    pyautogui.click(x_hotka,y_hotka)
    time.sleep(1)

    pyautogui.click(x, y)
    time.sleep(1)

    pyautogui.click(x_quit,y_quit)

    time.sleep(1)




    #Wait
    time.sleep(301)


    pyautogui.click(x_wine1,y_wine1)
    time.sleep(2)
    pyautogui.click(x_wine2,y_wine2)
    time.sleep(2)
    pyautogui.click(x_wine3,y_wine3)
    time.sleep(2)
    pyautogui.click(x_wine4,y_wine4)
    time.sleep(2)

    



# 1167, 786
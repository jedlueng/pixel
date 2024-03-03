#JEDLUENG 27/02/2024
#Potberry farm version 1 
#Go to farm 4514 from Terraview 
#Then move and farm 
#Now this is ok but I will improve later for more efficiency 
#Still better than doing it by myself
import pyautogui
import time

# Specify the screen coordinates where you want to click
x_travel, y_travel = 209, 141  # Change these values to the desired coordinates
#209, 141 > Travel 

#Bookmark position 1025, 356
x_bookmark, y_bookmark = 1025 , 356

#Land 4514
x_4514, y_4514 = 835, 606

#Base of w 1 + d 1 
x1, y1 = 904, 644
x2, y2 = 973, 643
x3, y3 = 1038, 641
x4, y4 = 1109, 645
x5, y5 = 1164, 644
x11, y11 = 905, 580
x12 ,y12 = 971, 574
x13, y13 = 1039, 580 
x14, y14 = 1100, 580
x15 , y15 = 1163, 580
x21, y21 = 904, 514
x22, y22 = 966, 514
x23, y23 = 1045, 514
x24, y24 = 1100, 516
x25, y25 = 1171, 516
x31, y31 = 902, 458 
x32, y32 = 975, 455
x33, y33 = 1039, 457
x34 ,y34 = 1104, 450
x35, y35 = 1169, 450

x_seed, y_seed = 856, 1006
x_water, y_water = 771, 1001
x_harvest, y_harvest = 924, 997



# Enable failsafe - moving the mouse to the upper-left corner will abort the script
pyautogui.FAILSAFE = True

arrived = True
while arrived == True:
    #Delayed after running a program
    time.sleep(3)

    #Click to travel
    pyautogui.click(x_travel, y_travel)
    time.sleep(1)
    pyautogui.click(x_bookmark,y_bookmark)
    time.sleep(1)
    pyautogui.click(x_4514,y_4514)
    time.sleep(60) #Wait for loading screen 

    #Move up for 4 seconds 
    # Press the 'w' key down
    pyautogui.keyDown('w')
    time.sleep(2)
    pyautogui.keyUp('w')

    pyautogui.keyDown('d')
    time.sleep(1)
    pyautogui.keyUp('d')
    time.sleep(2)
    arrived = False


 


while True:

    pyautogui.click(x_seed,y_seed)
    #pyautogui.click(x_water,y_water)
    pyautogui.click(x1, y1) 
    time.sleep(0.5)
    pyautogui.click(x2, y2)
    time.sleep(0.5)
    pyautogui.click(x3, y3)
    time.sleep(0.5)
    pyautogui.click(x4, y4)
    time.sleep(0.5)
    pyautogui.click(x5, y5)
    time.sleep(0.5)
    pyautogui.click(x11, x11)
    time.sleep(0.5)
    pyautogui.click(x12, y12)
    time.sleep(0.5)
    pyautogui.click(x13, y13)
    time.sleep(0.5)
    pyautogui.click(x14, y14)
    time.sleep(0.5)
    pyautogui.click(x15, y15)
    time.sleep(0.5)
    pyautogui.click(x21, y22)
    time.sleep(0.5)
    pyautogui.click(x23, y23)
    time.sleep(0.5)
    pyautogui.click(x24, y24)
    time.sleep(0.5)
    pyautogui.click(x25, y25)
    time.sleep(0.5)
    pyautogui.click(x31, y32)
    time.sleep(0.5)
    pyautogui.click(x33, y33)
    time.sleep(0.5)
    pyautogui.click(x34, y34)
    time.sleep(0.5)
    pyautogui.click(x35, y35)
    pyautogui.click(x_seed, y_seed)
    time.sleep(3)
    pyautogui.click(x_water,y_water)
    time.sleep(1)
    pyautogui.click(x1, y1) 
    time.sleep(0.5)
    pyautogui.click(x2, y2)
    time.sleep(0.5)
    pyautogui.click(x3, y3)
    time.sleep(0.5)
    pyautogui.click(x4, y4)
    time.sleep(0.5)
    pyautogui.click(x5, y5)
    time.sleep(0.5)
    pyautogui.click(x11, x11)
    time.sleep(0.5)
    pyautogui.click(x12, y12)
    time.sleep(0.5)
    pyautogui.click(x13, y13)
    time.sleep(0.5)
    pyautogui.click(x14, y14)
    time.sleep(0.5)
    pyautogui.click(x15, y15)
    time.sleep(0.5)
    pyautogui.click(x21, y22)
    time.sleep(0.5)
    pyautogui.click(x23, y23)
    time.sleep(0.5)
    pyautogui.click(x24, y24)
    time.sleep(0.5)
    pyautogui.click(x25, y25)
    time.sleep(0.5)
    pyautogui.click(x31, y32)
    time.sleep(0.5)
    pyautogui.click(x33, y33)
    time.sleep(0.5)
    pyautogui.click(x34, y34)
    time.sleep(0.5)
    pyautogui.click(x35, y35)
    pyautogui.click(x_water,y_water)
    time.sleep(124)
    pyautogui.click(x_harvest,y_harvest)
    time.sleep(1)
    pyautogui.click(x1, y1) 
    time.sleep(0.5)
    pyautogui.click(x2, y2)
    time.sleep(0.5)
    pyautogui.click(x3, y3)
    time.sleep(0.5)
    pyautogui.click(x4, y4)
    time.sleep(0.5)
    pyautogui.click(x5, y5)
    time.sleep(0.5)
    pyautogui.click(x11, x11)
    time.sleep(0.5)
    pyautogui.click(x12, y12)
    time.sleep(0.5)
    pyautogui.click(x13, y13)
    time.sleep(0.5)
    pyautogui.click(x14, y14)
    time.sleep(0.5)
    pyautogui.click(x15, y15)
    time.sleep(0.5)
    pyautogui.click(x21, y22)
    time.sleep(0.5)
    pyautogui.click(x23, y23)
    time.sleep(0.5)
    pyautogui.click(x24, y24)
    time.sleep(0.5)
    pyautogui.click(x25, y25)
    time.sleep(0.5)
    pyautogui.click(x31, y32)
    time.sleep(0.5)
    pyautogui.click(x33, y33)
    time.sleep(0.5)
    pyautogui.click(x34, y34)
    time.sleep(0.5)
    pyautogui.click(x35, y35)
    pyautogui.click(x_harvest,y_harvest)

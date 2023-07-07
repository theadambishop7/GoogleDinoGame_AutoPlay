# Meant for playing this game: https://elgoog.im/dinosaur-game/
# Make sure your window size is 1230px wide!


import pyautogui
import time
from PIL import Image
from mss import mss
import numpy as np

# Define the range of x-coordinates to check
START_X = 340
END_X = 370  # Adjust this value as needed

# Define the range of x-coordinates to check
JUMP_RISK = 589
DUCK_RISK = 521


def check_for_jump(screenshot, mode):
    # Check each pixel in the line
    for x in range(START_X, END_X + 1):
        if mode == "light":
            if screenshot[JUMP_RISK, x] < 100:
                return True
        else:
            if screenshot[JUMP_RISK, x] > 100:
                return True
    return False


def check_for_duck(screenshot, mode):
    # Check each pixel in the line
    for x in range(START_X - 50, END_X - 49):
        if mode == "light":
            if screenshot[DUCK_RISK, x] < 100:
                return True
        else:
            if screenshot[DUCK_RISK, x] > 100:
                return True
    return False


time.sleep(2)
pyautogui.press('space')

while True:
    # Take a screenshot
    with mss() as sct:
        mss_image = sct.grab(sct.monitors[1])  # mss object
        im = Image.frombytes("RGB", mss_image.size, mss_image.bgra, "raw", "BGRX").convert('L')
        '''there is a bug in PIL module which does not let frombyte fuction to convert image directly to 
        grayscale (denoted by L) once its fixed you can use L directly in place of RGB as an argument'''
        screenshot = np.array(im)

    # Check which mode we're in (light or dark)
    if screenshot[640, 400] > 220:
        # Light Mode
        print("light mode")
        if check_for_jump(screenshot, "light"):
            print("press UP")
            pyautogui.press('up')
        if check_for_duck(screenshot, "light"):
            print("press DOWN")
            pyautogui.keyDown('down')
            time.sleep(.2)
            pyautogui.keyUp('down')
    else:
        # Dark Mode
        print("dark mode")
        if check_for_jump(screenshot, "dark"):
            print("press UP")
            pyautogui.press('up')
        if check_for_duck(screenshot, "dark"):
            print("press DOWN")
            pyautogui.keyDown('down')
            time.sleep(.2)
            pyautogui.keyUp('down')

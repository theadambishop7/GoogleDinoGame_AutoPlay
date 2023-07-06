import pyautogui
import time
from PIL import Image, ImageGrab
from mss import mss

# Define the range of x-coordinates to check
START_X = 360
END_X = 395  # Adjust this value as needed

LIGHT = (255, 255, 255)
DARK = (32, 33, 35)


def check_for_jump(screenshot, mode):
    # Check each pixel in the line
    for x in range(START_X, END_X + 1):
        pixel = screenshot.getpixel((x, 589))
        if pixel[:3] != mode:  # Ignore the alpha channel if present
            return True
    return False


def check_for_duck(screenshot, mode):
    # Check each pixel in the line
    for x in range(START_X, END_X + 1):
        pixel = screenshot.getpixel((x, 521))  # Print debug information
        if pixel[:3] != mode:  # Ignore the alpha channel if present
            return True
    return False


current_mode = "light"

time.sleep(2)
pyautogui.press('space')

while True:
    # Take a screenshot
    with mss() as sct:
        # Grab the first monitor
        monitor = sct.monitors[1]
        # Get raw pixels from the screen
        sct_img = sct.grab(monitor)

        # Create the Image
        screenshot = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

    # Check which mode we're in (light or dark)
    if screenshot.getpixel((640, 400))[:3] == (255, 255, 255):
        # Light Mode
        print("light mode")
        if check_for_jump(screenshot, LIGHT):
            print("press UP")
            pyautogui.press('up')
        if check_for_duck(screenshot, LIGHT):
            print("press DOWN")
            pyautogui.keyDown('down')
            time.sleep(.2)
            pyautogui.keyUp('down')
    else:
        # Dark Mode
        print("dark mode")
        if current_mode == "light":
            time.sleep(2)
            current_mode = "dark"
        if check_for_jump(screenshot, DARK):
            print("press UP")
            pyautogui.press('up')
        if check_for_duck(screenshot, DARK):
            print("press DOWN")
            pyautogui.keyDown('down')
            time.sleep(.2)
            pyautogui.keyUp('down')

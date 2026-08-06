from pyautogui import pixelMatchesColor, moveTo
from mouse import click
from time import sleep
import win32gui, win32api, win32con

window = win32gui.FindWindow(None, "Human Benchmark - Reaction Time Test - Google Chrome")
moveTo(952, 280)

def fast_click():
    global window
    lparam = win32api.MAKELONG(200, 200)  # relative coords
    win32gui.PostMessage(window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lparam)
    win32gui.PostMessage(window, win32con.WM_LBUTTONUP, 0, lparam)

# continuously checks if the pixel at (952, 280) is green
# right-clicks twice if it is
while True:
    if pixelMatchesColor(952, 280, (75, 219, 106)):
        fast_click()
        sleep(0.1)
        fast_click()


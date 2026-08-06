from pyautogui import screenshot, locate, center, locateCenterOnScreen
from mouse import click, move
from PIL import Image, ImageGrab
import win32gui, win32api, win32con
from keyboard import is_pressed
from time import sleep
import numpy as np
import cv2
sleep(1)

region = (830, 134, 230, 95)

window = win32gui.FindWindow(None, "Human Benchmark - Aim Trainer - Google Chrome")
def fast_click(x, y):
    global window
    lparam = win32api.MAKELONG(x, y)  # relative coords
    win32gui.PostMessage(window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lparam)
    win32gui.PostMessage(window, win32con.WM_LBUTTONUP, 0, lparam)

while not is_pressed("escape"):
    if is_pressed("p"):
        click(951, 166)
        i = 120
        while i > 0:
            i -= 1

            img = np.array(ImageGrab.grab().crop((region[0], region[1], region[2] + region[0], region[3] + region[1])))

            pos = np.argwhere(img[:, :, -1] == 253)

            if pos.any():
                # click(pos[0][1] + 829 + 5, pos[0][0] + 142 + 5)
                fast_click(pos[0][1] + 829 + 5, pos[0][0] + 142 + 5)

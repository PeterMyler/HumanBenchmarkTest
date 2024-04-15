from pyautogui import screenshot, locate, center, locateCenterOnScreen
from mouse import click, move
from PIL import Image, ImageGrab
from keyboard import is_pressed
from time import sleep
import numpy as np
import cv2

sleep(1)

region = (830, 134, 240, 95)

while not is_pressed("escape"):
    if is_pressed("p"):
        click(951, 166)
        i = 120
        while i:
            i -= 1

            img = np.array(ImageGrab.grab().crop((region[0], region[1], region[2] + region[0], region[3] + region[1])))

            pos = np.argwhere(img[:, :, -1] == 253)
            #print(pos)

            try:
                click(pos[0][1] + 829 + 5, pos[0][0] + 142 + 5)
            except:
                pass

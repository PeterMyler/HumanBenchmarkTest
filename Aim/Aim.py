from pyautogui import screenshot, locate, center, locateCenterOnScreen
from mouse import click, move
from PIL import Image, ImageGrab
from keyboard import is_pressed
from time import sleep
import cv2
target = Image.open(r"small_target.png")
sleep(1)
x, y = 0, 5

region = (840, 134, 240-10, 95)

while not is_pressed("escape"):
    if is_pressed("p"):
        click(951, 166)
        i = 42
        while i:
            i -= 1
            pos = locate(target, ImageGrab.grab().crop((region[0], region[1], region[2] + region[0], region[3] + region[1])), grayscale=True, confidence=0)
            #ImageGrab.grab().crop((region[0], region[1], region[2] + region[0], region[3] + region[1])).save("screenie.png");exit()

            if pos:
                click(pos.left + region[0] + 10, pos.top + region[1] + 15)
                sleep(0.009)

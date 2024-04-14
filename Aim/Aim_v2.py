from pyautogui import screenshot, locate, center, locateCenterOnScreen
from mouse import click, move
from PIL import Image
from keyboard import is_pressed
from time import sleep
import cv2
target = Image.open(r"small_target.png")
sleep(1)



while not is_pressed("escape"):
    if is_pressed("p"):
        click(951, 166)
        while is_pressed("p"):
            pos = locate(target, screenshot(region=(829, 130, 245, 103)), grayscale=True, confidence=0)

            if pos:
                click(pos.left + 829 + 5, pos.top + 142 + 5)

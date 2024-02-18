from pyautogui import screenshot, locate, center, locateCenterOnScreen
from mouse import click, move
from PIL import Image
from keyboard import is_pressed
from time import sleep
import cv2
target = Image.open(r"small_target.png")
sleep(1)

OperaGX = False


while not is_pressed("escape"):
    if is_pressed("p"):
        # 951, 182  - chrome
        # 973, 180  - opera gx
        if OperaGX: click(973, 180)
        else: click(951, 182)
        while is_pressed("p"):
            pos = locate(target, screenshot(region=(829 + 22 * OperaGX, 132 - 2 * OperaGX, 245, 103)), grayscale=True, confidence=0)

            if pos:
                pos = center(pos)
                click(pos.x + 829 + 22 * OperaGX, pos.y + 132 - 2 * OperaGX +10)

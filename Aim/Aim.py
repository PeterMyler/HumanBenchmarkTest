from pyautogui import screenshot, moveTo, click, locate, center, locateCenterOnScreen
from PIL import Image
from keyboard import is_pressed
from time import sleep
import cv2
target = Image.open(r"target3.png")
sleep(1)

while not is_pressed("escape"):
    # search for "typing" on screen and click "play"
    while not locateCenterOnScreen(r"aim_trainer.png"): pass
    pos = locateCenterOnScreen(r"aim_trainer.png")
    click(pos.x + 220, pos.y)
    sleep(0.4)
    click(951, 500)

    count = 0
    while not is_pressed("escape") and count < 32:
        screen = screenshot(region=(2265-1920, 234, 1213, 530))
        pos = locate(target, screen, grayscale=True, confidence=0.8)

        if pos:
            pos = center(pos)
            click(pos.x + 344, pos.y + 228+50)
            count += 1

    while not locateCenterOnScreen("save_score.png"): pass
    click(locateCenterOnScreen("save_score.png"))

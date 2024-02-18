from pyautogui import moveTo, screenshot, center, locateOnScreen, locate
from keyboard import is_pressed
from mouse import click
from time import sleep
import cv2
sleep(1)
# zoom website to 125%, no f11

max_number = 4  # limit starts at 4
moveTo(40, 400)
while not is_pressed("p"):
    # screenshot screen
    screen = screenshot(region=(507, 225, 889, 570))
    number_locs = []  # pixel coords in order
    # screen.save("screenie.png")

    # find all numbers one-by-one in the screenshot
    for num in range(1, max_number+1):
        point = center(locate(f"ChimpTest numbers v2\\{num}.png", screen, confidence=0.95))
        number_locs.append((point.x + 507, point.y + 225))

    # click on coords
    for x, y in number_locs:
        click(x, y)
        sleep(0.15)

    # increase number limit, leave loop if limit is >40
    max_number += 1
    if max_number >= 41: break

    # wait for "continue" to appear and click on it
    moveTo(40, 400)
    while not locateOnScreen(r"continue.png", confidence=0.9): pass
    click(950, 670)
    moveTo(40, 400)
    while not locateOnScreen(r"ChimpTest numbers v2\1.png", confidence=0.9): pass




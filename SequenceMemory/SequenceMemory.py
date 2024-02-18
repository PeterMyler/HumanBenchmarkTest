from pyautogui import screenshot, locateCenterOnScreen, pixelMatchesColor, locateOnScreen
from mouse import click, move
from keyboard import is_pressed
from time import sleep
import cv2


def waitAndClick(img):
    move(40, 400)
    while not locateCenterOnScreen(img): pass
    x, y = locateCenterOnScreen(img)
    click(x, y)
    move(40, 400)


waitAndClick(r"start.png")
sleep(0.1)

level = 1
sequence = []
while not is_pressed("escape"):
    pos = locateCenterOnScreen("white_square.png")

    if pos and (not sequence or ((abs(pos.x-sequence[len(sequence)-1][0]) + abs(pos.y-sequence[len(sequence)-1][1])) > 20)):
        sequence.append(pos)

    if level == len(sequence):
        sleep(0.4)

        for x, y in sequence:
            click(x, y)
            sleep(0.01)

        move(40, 400)
        level += 1
        sequence = []
        sleep(0.1)


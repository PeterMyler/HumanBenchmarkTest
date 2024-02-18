from pyautogui import screenshot, locateCenterOnScreen, pixelMatchesColor, locateOnScreen
from mouse import click, move
from keyboard import is_pressed
from time import sleep
from math import sqrt
import cv2

gaps = (20, 14, 12, 10, 8, 6, 6, 6, 4, 4, 4, 4, 2, 2)
width = 480
pixel_tolerance = 10


def waitAndClick(img):
    move(40, 400)
    while not locateCenterOnScreen(img): pass
    x, y = locateCenterOnScreen(img)
    click(x, y)
    move(40, 400)


waitAndClick(r"start.png")
sleep(0.1)
for score in range(1, 100):
    print("Score:", score)
    # wait for white squares to appear
    while not locateOnScreen("white_square.png"): pass
    sleep(0.3)

    if score < 94: screen = screenshot(region=(710, 300, 490, 490))
    else: screen = screenshot(region=(2639-1920, 294, 465, 494))
    screen.save(f"RoundSc\\round_{score}.png")

    squares = []

    n = int(sqrt(score / 3 + 1))
    k1 = (n - 1) * (n - 1)
    k2 = 2*(n+1)
    k3 = n + 2
    rows = ((score + k1) // k2) + k3

    # rows = ((score + (n - 1)**2 ) // (2*(n+1)) + n + 2
    print("Rows:", rows)
    print("n:", k2)

    x_gap = gaps[min(rows - 3, len(gaps)-1)]
    x_step = round((width - x_gap * (rows - 1)) / rows)
    x_half_step = round(x_step / 2)

    if score < 94:
        y_gap, y_step, y_half_step = x_gap, x_step, x_half_step
    else:
        y_gap = 4
        y_step = round((width - y_gap * (rows - 1)) / rows)
        y_half_step = round(y_step / 2)

    for x in range(rows):
        x_pixel = x_half_step + (x_gap+x_step)*x

        for y in range(rows):
            y_pixel = y_half_step + (y_gap+y_step)*y

            r, g, b = screen.getpixel((x_pixel, y_pixel))
            if (abs(r - 255) + abs(g - 255) + abs(b - 255)) < pixel_tolerance*3:
                squares.append((x_pixel + 710, y_pixel + 300))

    print("Squares:", squares, "\n")

    # wait for white squares to disappear
    while locateOnScreen("white_square.png"): pass
    sleep(0.05)

    # clicks
    for xPos, yPos in squares:
        click(xPos, yPos)
        sleep(0.01)
        if is_pressed("s"): sleep(0.15)

    move(40, 400)
    sleep(1.5)





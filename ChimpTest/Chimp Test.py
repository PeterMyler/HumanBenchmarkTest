from pyautogui import moveTo, screenshot, locateAll, center, locateOnScreen, locate
from mouse import click
from PIL import Image
from time import sleep
import cv2
sleep(1)

max_number = 4

moveTo(40, 400)
while max_number <= 40:
    # screenshot screen
    screen = screenshot(region=(507, 225, 889, 552))
    screen.save("screen.png")
    # screen = Image.open("screen.png")

    number_locs = [(0, 0)] * max_number  # pixel coords in order
    square_locs = {}  # coords in pixels

    # find squares in screenshot
    squares = list(locateAll(r"ChimpTest numbers\square_top.png", screen))
    name_number = 100
    for square in squares:
        square_img = screen.crop((square.left+1, square.top+1, square.left+101, square.top+101))
        square_img.save(f"ChimpTest current numbers\\{name_number}.png")
        square_locs[name_number] = (square.left + 50 + 507, square.top + 50 + 225)
        name_number += 1

    # find out what numbers are in the squares
    for i in range(100, name_number):
        curr_square = Image.open(f"ChimpTest current numbers\\{i}.png")
        curr_number = ""
        x1, x2 = 0, 0

        # look for numbers where both digits are equal
        for num in range(11, 35, 11):
            all_nums = locate(f"ChimpTest numbers\\{num}.png", curr_square, confidence=0.96)

            if all_nums:
                curr_number += str(num)

        if curr_number == "":
            # look for digits (can't handle two of the same digit)
            for num in range(0, 10):
                all_nums = locate(f"ChimpTest numbers\\{num}.png", curr_square, confidence=0.96)

                if all_nums:
                    curr_number += str(num)

                    if x1 == 0: x1 = all_nums.left
                    else: x2 = all_nums.left

            if x2 != 0 and x1 > x2: curr_number = curr_number[::-1]

        print(curr_number)
        number_locs[int(curr_number)-1] = square_locs[i]

    # execute
    print(number_locs)
    for x, y in number_locs:
        click(x, y)
        sleep(0.05)

    max_number += 1

    # wait for and then click "continue"
    moveTo(40, 400)
    while not locateOnScreen(r"ChimpTest numbers\continue.png"): pass
    click(950, 670)
    moveTo(40, 400)
    while not locateOnScreen(r"ChimpTest numbers\square_top.png"): pass





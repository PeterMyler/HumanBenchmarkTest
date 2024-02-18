from pyautogui import screenshot, locateCenterOnScreen, locateAll, click, moveTo
from keyboard import is_pressed, write, press_and_release
from time import sleep
from math import ceil
import pytesseract, cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
sleep(1)
print("running")
count = 233

# click start
"""
while not locateCenterOnScreen("start.png"): pass
click(locateCenterOnScreen("start.png"))
moveTo(40, 400)
sleep(0.2)
"""


def find_nums(image):
    global count

    nums = []  # [(x position, number)]

    if count < 31: folder = r"BigNums"
    else: folder = r"SmallerNums"

    for n in range(0, 10):
        num_list = list(locateAll(folder + f"\\{n}.png", image, confidence=0.97))

        for num in num_list:
            nums.append([num.left, n])

    nums.sort()

    lefts_nums = [x[0] for x in nums]
    baddies = []
    for i in range(len(lefts_nums)-1):
        if lefts_nums[i+1] - lefts_nums[i] <= 5: baddies.append(i)

    # remove baddies
    baddies.sort(reverse=True)
    for baddy in baddies:
        nums.pop(baddy)

    int_nums = [x[1] for x in nums]
    return ' '.join(map(str, int_nums)).replace(" ", "").replace("\n", "")

    # return pytesseract.image_to_string(image, config="digits").replace("\n", "").replace(" ", "")


while not is_pressed("escape"):
    screenshot().save(f"RoundsSc\\round_{count}.png")

    if count < 18:  # one row,  big text
        screen = screenshot(region=(314, 442, 1283, 100))

        number = find_nums(screen)
    elif count < 31:  # two rows, big text
        screen = screenshot(region=(314, 380, 1283, 100))
        screen2 = screenshot(region=(314, 506, 1283, 100))

        number = find_nums(screen)
        number += find_nums(screen2)
    else:  # small text
        number = ""
        rows = ceil(count/29)
        screens = []
        for offset in range(-(rows//2), rows - (rows//2)):
            screen = screenshot(region=(314, 461 + (75 * offset) + (37 * (rows % 2 == 0)), 1283, 63))
            number += find_nums(screen)
            print(find_nums(screen))

    print(number, len(number))
    while not locateCenterOnScreen("submit.png"): pass

    write(number)













    press_and_release("enter")
    press_and_release("enter")
    sleep(0.3)

    count += 1


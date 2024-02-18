from pyautogui import screenshot, locateCenterOnScreen, locateAll, click, moveTo
from keyboard import is_pressed, write, press_and_release
from PIL import Image
from time import sleep
import pytesseract, cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print("running")

screen = Image.open("test.png")

count = 100

if count < 4:
    nums = []  # [(x position, number)]
    for n in range(0, 10):
        num_list = list(locateAll(f"BigNums\\{n}.png", screen, confidence=0.98))

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

    print(nums)
    int_nums = [x[1] for x in nums]
    number = ' '.join(map(str, int_nums)).replace(" ", "")
else:
    number = pytesseract.image_to_string(screen, config="-c tessedit_char_whitelist=0123456789").replace("\n", "").replace(" ", "")

print(number)



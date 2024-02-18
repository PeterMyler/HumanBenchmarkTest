from pyautogui import screenshot, locateCenterOnScreen, moveTo, click, locateOnScreen
import keyboard
from time import sleep
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

auto_run = False

manual_fixes = {
    "|": "I",
    "\n": " ",
    "  ": " ",
    "Anewcomer ": "A newcomer ",
    " ona ": " on a ",
    "How many words per minute can you type?": "",
    " Start typing to begin.": ""}

sleep(1)
print("running")

while not keyboard.is_pressed("escape"):
    if auto_run:
        # search for "typing" on screen and click "play"
        while not locateOnScreen(r"typing.png"): pass
        pos = locateCenterOnScreen(r"typing.png")
        click(pos.x + 270, pos.y)

        # wait till page loads
        while not locateOnScreen(r"typing_test.png"): pass

    # move to the side and screenshot the text
    moveTo(40, 400)

    # take screenshot
    img = screenshot(region=(2221-1920, 415, 1334, 415))

    # get text from the screenshot
    text = pytesseract.image_to_string(img).strip()

    # fix text
    # implement manual changes:
    for s in manual_fixes:
        text = text.replace(s, manual_fixes[s])
    # remove first character if the cursor was mistaken as a letter
    if not text[0].isalpha() or text[1].isupper(): text = text[1:]

    # write out the string
    keyboard.write(text)

    print(text)

    if not auto_run: break

    # while not locateOnScreen(r"C:\Users\peter\PycharmProjects\HumanBenchmarkTest\Typing\save_score.png"): pass
    # click(locateCenterOnScreen(r"C:\Users\peter\PycharmProjects\HumanBenchmarkTest\Typing\save_score.png"))

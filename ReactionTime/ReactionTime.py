from pyautogui import pixelMatchesColor, moveTo, screenshot, locateOnScreen, click
from time import sleep
import win32gui, win32api, win32con
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

window = win32gui.FindWindow(None, "Human Benchmark - Reaction Time Test - Google Chrome")
# window = win32gui.FindWindow(None, "Human Benchmark - Reaction Time Test — Mozilla Firefox")

green = (75, 219, 106)
# green = (30, 151, 80)

screenshot_region = (2709 - 1920, 406, 330, 101)
save_score_button = (875, 605)
try_again_button = (1035, 605)

lparam = win32api.MAKELONG(500, 700)  # relative coords
def fast_click():
    global window
    win32gui.PostMessage(window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lparam)
    win32gui.PostMessage(window, win32con.WM_LBUTTONUP, 0, lparam)

# continuously check if the pixel at (952, 280) is green - right-click twice if it is
count = 0
current_times = [11, 8, 10, 9, 10]
while True:
    if pixelMatchesColor(952, 280, green):
        fast_click()
        sleep(0.15)
        fast_click()
        count += 1

        # round has been played
        if count == 5:
            sleep(0.5)
            count = 0

            # get current score
            img = screenshot(region=screenshot_region)
            text = pytesseract.image_to_string(img)
            current_score = int(text.replace("ms", ""))
            print(current_score)

            # analyse average score
            if sum(current_times)/5 >= (sum(current_times[:-1])+current_score)/5:
                # save score
                click(save_score_button)
                sleep(1.5)
                current_times = [current_score] + current_times[:-1]
                print(current_times, sum(current_times)/5)
                # find game again
                p = locateOnScreen("rt.png", confidence=0.69)
                x = int(p.left) + 262
                y = int(p.top) + 37
                click(x, y)
                sleep(1.5)
                click(300, 600)
            else:
                # try again
                click(try_again_button)
                sleep(0.5)
                click(300, 600)



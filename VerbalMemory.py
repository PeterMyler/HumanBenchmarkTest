from pyautogui import screenshot
from mouse import click
from keyboard import is_pressed
from time import sleep
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
sleep(1)
print("running")

words = []
unique_words = 0

while not is_pressed("escape"):
    word_img = screenshot(region=(2470-1920, 460, 807, 78))
    word_string = pytesseract.image_to_string(word_img).replace("\n", "").replace(" ", "")

    # if prev_word == word_string: continue

    if word_string in words:
        click(868, 603)  # click "seen"
    else:
        words.append(word_string)
        click(1036, 603)  # click new
        unique_words += 1

        if unique_words % 100 == 0: print(unique_words, "unique words reached")

    sleep(0.02)





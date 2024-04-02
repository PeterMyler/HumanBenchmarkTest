from pyautogui import screenshot
from mouse import click
from keyboard import is_pressed
from time import sleep
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
sleep(1)
# 125% zoom, not full-screen, no bookmarks

# (x, y) screen coords
seen_pos = (868, 603)
new_pos = (1036, 603)
# (x, y, w, h)
word_region = (550, 435, 800, 90)

words = set()
unique_words = 0

while not is_pressed("p"):
    word_img = screenshot(region=word_region)
    word_string = pytesseract.image_to_string(word_img)
    word_string = word_string.strip().replace(" ", "").lower()

    if word_string in words:
        click(*seen_pos)  # click "seen"
    else:
        words.add(word_string)
        click(*new_pos)  # click "new"
        unique_words += 1

        if unique_words % 100 == 0:
            print(unique_words, "unique words reached")

    sleep(0.02)





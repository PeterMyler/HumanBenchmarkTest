from pyautogui import pixelMatchesColor, moveTo
from mouse import click
from time import sleep
moveTo(500, 620)

# continuously checks if the pixel at (952, 280) is green
# right-clicks twice if it is
while True:
    if pixelMatchesColor(952, 280, (81, 218, 114)):
        click()
        sleep(0.1)
        click()

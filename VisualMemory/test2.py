from pyautogui import screenshot, locateOnScreen, moveTo, center

e = locateOnScreen("white_square.png", grayscale=False)
print(e)
moveTo(center(e))

from pyautogui import screenshot, locateOnScreen, center, moveTo
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

p = locateOnScreen("rt.png", confidence=0.69)
x = int(p.left) + 262
y = int(p.top) + 37
moveTo(x, y)
print(p)



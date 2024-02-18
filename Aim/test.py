from pyautogui import screenshot, moveTo, click, locate, center, locateCenterOnScreen
from PIL import Image
from keyboard import is_pressed
from time import sleep
import cv2

screen = screenshot(region=(355, 245, 1200, 500))
screen.save("screenie.png")

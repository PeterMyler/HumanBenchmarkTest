import cv2
import numpy as np
from time import time, sleep

im = cv2.imread('screenie2.png')
print(im[:, :, -1])

t = time()

for i in range(1_000):
    a1 = np.argwhere(im[:, :, -1] == 255)
    #Y, X = np.where(np.all(im == [255, 255, 255], axis=2))

print(a1)
print(round(time() - t, 5))

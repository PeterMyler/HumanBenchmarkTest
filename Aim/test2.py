from PIL import Image
import numpy as np
import time
from time import time

pim = Image.open('screenie2.png').convert('RGB')


t = time()
for i in range(10_000):
    im = np.array(pim)
    a1 = np.where(im[:, :, -1] == 255)

print(a1)
print(round(time() - t, 5))

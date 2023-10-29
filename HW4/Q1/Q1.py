from tools import *
from skimage.restoration import wiener
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("retina_motionblurred.jpg", 0)

#A
kernel = np.eye(13, 13)/13

#B
w = wiener(normal(img), kernel, 0.075)
restored = n_range(w)

#C
ax = plt.subplot(2, 2, 1)
ax.set_title('retina')
ax.imshow(img, vmin=0, vmax=255, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 2)
ax.set_title('restored')
ax.imshow(restored, vmin=0, vmax=255, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 3)
ax.set_title('magnitude spectrum')
ax.imshow(logmagnitude(img), cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 4)
ax.set_title('magnitude spectrum')
ax.imshow(logmagnitude(restored), cmap = 'gray')
ax.axis('off')

plt.show()

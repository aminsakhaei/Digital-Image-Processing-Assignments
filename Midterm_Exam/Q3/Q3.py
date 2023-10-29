import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('lung.png', 0)

img_2 = cv.medianBlur(img, 3)

img_3 = cv.Sobel(img_2, cv.CV_64F, dx=0, dy=1)

plt.figure()
plt.suptitle('Problem 3 Figure')

plt.subplot(1, 3, 1)
plt.title('Original')
plt.imshow(img, cmap='gray')
plt.axis(False)

plt.subplot(1, 3, 2)
plt.title('Denoised')
plt.imshow(img_2, cmap='gray')
plt.axis(False)

plt.subplot(1, 3, 3)
plt.title('Gradient')
plt.imshow(img_3, cmap='gray')
plt.axis(False)

plt.show()
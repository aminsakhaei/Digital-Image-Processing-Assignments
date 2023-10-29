import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math

#Power law transformation
def power_t(img, gamma):
    c = 255**(1-gamma)
    img_pow = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_pow[i, j] = c*(img[i, j]**gamma)
    img_pow = img_pow.astype('uint8')
    return img_pow

#Log transformation
def log_t(img, k):
    max = np.amax(img)
    min = np.amin(img)
    c = 255 / (math.log(max, k))
    img_log = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_log[i, j] = math.log((1 + img[i, j]), k)
    img_log = c * img_log
    img_log = img_log.astype('uint8')
    return img_log

img = cv.imread("brains.png", 0)

#B
cv.imshow("gamma = 1.5", power_t(img, 1.5))

#C
img_p = power_t(img, 0.6)

ax = plt.subplot(2, 3, 1)
ax.set_title('γ=0.6')
ax.imshow(img_p, cmap='gray', vmin=0, vmax=255)
ax.axis('off')

#D
ax = plt.subplot(2, 3, 4)
ax.hist(img_p.ravel(), bins=256, range=(0, 255))
ax.set_title('histogram')
ax.axes.get_yaxis().set_visible(False)

#E
cv.imshow("log10",log_t(img, 10))

img_l = log_t(img,3)

ax = plt.subplot(2, 3, 2)
ax.set_title('k=3')
ax.imshow(img_l, cmap='gray', vmin=0, vmax=255)
ax.axis('off')

ax = plt.subplot(2, 3, 5)
ax.hist(img_l.ravel(), bins=256, range=(0, 255))
ax.set_title('histogram')
ax.axes.get_yaxis().set_visible(False)

#F
ax = plt.subplot(2, 3, 3)
ax.set_title('original')
ax.imshow(img, cmap='gray', vmin=0, vmax=255)
ax.axis('off')

ax = plt.subplot(2, 3, 6)
ax.hist(img.ravel(), bins=256, range=(0, 255))
ax.set_title('histogram')
ax.axes.get_yaxis().set_visible(False)

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

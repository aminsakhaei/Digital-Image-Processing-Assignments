import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img_1 = cv.imread("retina.jpg", 0)
print(img_1.shape)
print(img_1.dtype)

# A
print("size=", img_1.shape[0] * img_1.shape[1] * 8)

# B
plt.figure()
plt.hist(img_1.ravel(), bins=256)

# C
img_2 = cv.imread("retina_sub.jpg", 0)
hist_2 = cv.calcHist([img_2], [0], None, [64], [0, 255])
hist_2 = cv.normalize(hist_2, 0, 255, cv.NORM_MINMAX)
min = 10000
# loop for comparing histograms
for i in range(0, img_1.shape[0] - img_2.shape[0], 50):
    for j in range(0, img_1.shape[1] - img_2.shape[1], 50):
        d = 0
        cut = img_1[i:i + img_2.shape[1], j:j + img_2.shape[1]]
        hist_1 = cv.calcHist([cut], [0], None, [64], [0, 255])
        hist_1 = cv.normalize(hist_1, 0, 255, cv.NORM_MINMAX)
        for x in range(hist_1.shape[0]):
            if hist_1[x] == 0:
                d = d + 0
            else:
                d = d+ (((hist_1[x] - hist_2[x])**2)/(hist_1[x]))
        if d < min:
            min = d
            m, n = i, j

print("d=", min)
cut = img_1[m: m + img_2.shape[1], n:n + img_2.shape[1]]
ax = plt.subplot(2, 2, 1)
ax.set_title('Retina_sub')
ax.imshow(img_2, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 2)
ax.set_title('The most similar')
ax.imshow(cut, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 3)
ax.set_title('Histogram1')
ax.hist(img_2.ravel(), bins=256)


ax = plt.subplot(2, 2, 4)
ax.set_title('Histogram2')
ax.hist(cut.ravel(), bins=256)

plt.show()
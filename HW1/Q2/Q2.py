import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#A: extract section specified
a = cv.imread("dental_xray.tif")
b = cv.imread("dental_xray_mask.tif")
a = cv.cvtColor(a, cv.COLOR_BGR2GRAY)
b = cv.cvtColor(b, cv.COLOR_BGR2GRAY)
print(a.shape)
for i in range(674):
    for j in range(882):
        if(b[i, j]==0):
            a[i, j] = 0
"""cv.imshow("extract", a)"""

#B: display image and its complement
img = cv.imread("partial_body_scan.tif")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(img.shape)
img_m = img.copy()
for i in range(1482):
    for j in range(750):
        img_m[i, j] = 255-img[i,j]
add = cv.add(img, img_m)
add = cv.cvtColor(add, cv.COLOR_BGR2RGB)
#original image
ax = plt.subplot(1, 3, 1)
ax.set_title('orginal')
ax.imshow(img, cmap='gray')
ax.axis('off')
#comlement image
ax = plt.subplot(1, 3, 2)
ax.set_title('complement')
ax.imshow(img_m, cmap='gray')
ax.axis('off')
#community image
ax = plt.subplot(1, 3, 3)
ax.set_title('community')
ax.imshow(add, cmap='gray')
ax.axis('off')

plt.show()

#C: complement the difference
img_o = cv.imread("angiography_live.tif")
img_m = cv.imread("angiography_mask.tif")
res = cv.absdiff(img_o, img_m)
res = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
print(res.shape)
for i in range(420):
    for j in range(420):
        res[i, j] = 255-res[i, j]

cv.imshow("complement the difference",res)
normalized = np.zeros((420, 420))
normalized = cv.normalize(res,  normalized, 0, 255, cv.NORM_MINMAX)
cv.imshow("MINMAX normalize", normalized)

cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#A
#vectorize
def vhistogram(x):
    dicts = {}
    v = np.zeros(256)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            v[x[i, j]] = v[x[i, j]]+1
            dicts[x[i, j]] = v[x[i, j]]
    return v, dicts

#B
#Cumulative distribution function
def cdf_func(c, dicts):
    for i in range(255):
        c[i] = c[i] + c[i-1]
        dicts[i] = c[i]
    return c, dicts
#normalize
def normalize(img):
    l = 256
    m, n = img.shape
    vhisto, dicts = vhistogram(img)
    cdf, dicts = cdf_func(vhisto, dicts)
    h = np.zeros(l)
    for i in range(l-1):
        h[i] = ((cdf[i]-cdf.min())/((m*n)-cdf.min()))*(l-1)
        h[i] = h[i].astype('uint8')
        dicts[i] = h[i]
    for i in range(m):
        for j in range(n):
            img[i, j] = dicts.get((img[i,j]))
    return img

#C
img_L_o = cv.imread("Lowcontrast.tif", 0)
img_L_n = img_L_o.copy()

img_D_o = cv.imread("Dark.tif", 0)
img_D_n = img_D_o.copy()


img_B_o = cv.imread("Bright.tif", 0)
img_B_n = img_B_o.copy()

#lowcontrast
img_L_n = normalize(img_L_n)
plt.figure()
ax = plt.subplot(2, 2, 1)
ax.set_title('lowcontrast')
ax.imshow(img_L_o, cmap='gray', vmin=0, vmax=255)
ax.axis('off')

ax = plt.subplot(2, 2, 2)
ax.set_title('lowcontrast improved')
ax.imshow(img_L_n, cmap='gray', vmin=0, vmax=255)
ax.axis('off')

ax = plt.subplot(2, 2, 3)
ax.hist(img_L_o.ravel(), bins=256,  range=(0, 255))
ax.set_title('Histogram')
ax.axes.get_yaxis().set_visible(False)

ax = plt.subplot(2, 2, 4)
ax.hist(img_L_n.ravel(), bins=256)
ax.set_title('Histogram.i')
ax.axes.get_yaxis().set_visible(False)

#Dark
plt.figure()
img_D_n = normalize(img_D_n)
ax = plt.subplot(2, 2, 1)
ax.set_title('Dark')
ax.imshow(img_D_o, cmap='gray', vmin=0, vmax=255)
ax.axis('off')

ax = plt.subplot(2, 2, 2)
ax.set_title('Dark improved')
ax.imshow(img_D_n, cmap='gray', vmin=0, vmax=255)
ax.axis('off')

ax = plt.subplot(2, 2, 3)
ax.hist(img_D_o.ravel(), bins=256,  range=(0, 255))
ax.set_title('Histogram')
ax.axes.get_yaxis().set_visible(False)

ax = plt.subplot(2, 2, 4)
ax.hist(img_D_n.ravel(), bins=256)
ax.set_title('Histogram.i')
ax.axes.get_yaxis().set_visible(False)

#Bright
plt.figure()
img_B_n = normalize(img_B_n)
ax = plt.subplot(2, 2, 1)
ax.set_title('Bright')
ax.imshow(img_B_o, cmap='gray', vmin=0, vmax=255)
ax.axis('off')

ax = plt.subplot(2, 2, 2)
ax.set_title('Bright improved')
ax.imshow(img_D_n, cmap='gray', vmin=0, vmax=255)
ax.axis('off')

ax = plt.subplot(2, 2, 3)
ax.hist(img_B_o.ravel(), bins=256,  range=(0, 255))
ax.set_title('Histogram')
ax.axes.get_yaxis().set_visible(False)

ax = plt.subplot(2, 2, 4)
ax.hist(img_B_n.ravel(), bins=256)
ax.set_title('Histogram.i')
ax.axes.get_yaxis().set_visible(False)

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
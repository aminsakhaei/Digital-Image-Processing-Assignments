import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#B
def transform(img):
    img_t = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_t[i, j] = np.round(255 *np.sin((np.pi/510)*img[i, j]))
    return img_t

def plot(x):
    for i in range(len(x)):
        y = np.round(255 * np.sin((np.pi / 510) * x))
    return y

img_1 = cv.imread("CT_1.tif", 0)
img_2 = cv.imread("CT_2.tif", 0)

ax = plt.subplot(2, 2, 1)
ax.set_title('CT_1')
ax.imshow(img_1, vmin=0,vmax=255 , cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 2)
ax.set_title('CT_2')
ax.imshow(img_2, vmin=0,vmax=255 , cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 3)
ax.set_title('CT_1 transformed')
ax.imshow(transform(img_1), vmin=0,vmax=255 , cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 4)
ax.set_title('CT_1 transformed')
ax.imshow(transform(img_2), vmin=0,vmax=255 , cmap = 'gray')
ax.axis('off')

#C
plt.figure()
x = np.linspace(0, 255, 256)
plt.plot(x, plot(x),'darkorange', label='Transform')
plt.plot(x, x,'c',label=' Identity')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("plot")
plt.legend()

plt.show()
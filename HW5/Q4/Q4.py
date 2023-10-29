import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("sonography.jpg", 0)

sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
sobel = sobelx + sobely

kernelx = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
prewittx = cv.filter2D(img, -1, kernelx)
prewitty = cv.filter2D(img, -1, kernelx)
prewitt = prewittx + prewitty

kernel = np.array([[0,0,1,0,0],[0,1,2,1,0],[1,2,-16,1,2],[0,1,2,1,0],[0,0,1,0,0]])
LoG = cv.filter2D(img, -1, kernel)

canny = cv.Canny(img,100,200)

kernelx = np.array([[-1,0],[0,1]])
kernely = np.array([[0,-1],[1,0]])
robertsx = cv.filter2D(img, -1, kernelx)
robertsy = cv.filter2D(img, -1, kernely)
roberts = robertsx + robertsy

ax = plt.subplot(2, 3, 1)
ax.set_title('image')
ax.imshow(img, vmin=0, vmax=255, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 3, 2)
ax.set_title('Sobel')
ax.imshow(sobel, vmin=0, vmax=255, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 3, 3)
ax.set_title('Prewitt')
ax.imshow(prewitt, vmin=0, vmax=255, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 3, 4)
ax.set_title('LoG')
ax.imshow(LoG, vmin=0, vmax=255, cmap = 'gray')
ax.axis('off')


ax = plt.subplot(2, 3, 5)
ax.set_title('Canny')
ax.imshow(canny, vmin=0, vmax=255, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 3, 6)
ax.set_title('Roberts')
ax.imshow(roberts, vmin=0, vmax=255, cmap = 'gray')
ax.axis('off')

plt.show()
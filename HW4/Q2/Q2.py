import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("noisy_rectangle.png", 0)
kernel = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(15, 15))

#A
dilation = cv.dilate(img,kernel,iterations = 1)
erosion = cv.erode(img, kernel, iterations=1)
#plt.imshow(dilation, cmap = 'gray')
#plt.imshow(erosion, cmap = 'gray')

#B
kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(39, 44))
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
#plt.imshow(opening, cmap = 'gray')

#C
kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(29, 32))
closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
#plt.imshow(closing, cmap = 'gray')

plt.show()
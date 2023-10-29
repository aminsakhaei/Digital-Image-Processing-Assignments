import cv2 as cv
import matplotlib.pyplot as plt

#A
img1 = cv.imread("fingerprint.png", 0)
kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(3, 3))
opening = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)

#B
img2 = cv.imread("headCT.png", 0)
dilation1 = cv.dilate(img2,kernel,iterations = 1)
erotion1 = cv.erode(img2,kernel,iterations = 1)
gradient1 = dilation1 - erotion1

kernel2 = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(7, 7))
dilation2 = cv.dilate(img2,kernel2,iterations = 1)
erotion2 = cv.erode(img2,kernel2,iterations = 1)
gradient2 = dilation2 - erotion2

#C
img3 = cv.imread("rice.tif", 0)
kernel3 = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(90, 90))
tophat = cv.morphologyEx(img3, cv.MORPH_TOPHAT, kernel3)
_, thresh = cv.threshold(tophat, 60, 255, cv.THRESH_BINARY)

#plot
#ax = plt.subplot(1, 2, 1)
#ax.set_title('image')
#ax.imshow(img3, vmin=0, vmax=255, cmap = 'gray')
#ax.axis('off')

#ax = plt.subplot(1, 2, 2)
#ax.set_title('threshold')
#ax.imshow(thresh, vmin=0, vmax=255, cmap = 'gray')
#ax.axis('off')

#plt.show()
import cv2 as cv
import numpy as np

def trans_1(x):
    if x >= 160 and x <= 240:
        return 150
    else:
        return 20

def trans_2(y):
    if y >= 100 and y <= 165:
        return 200
    else:
        return y

img = cv.imread("kidney.tif")

#A
v = np.vectorize(trans_1)
img_1 = v(img)
img_1 =  img_1.astype('uint8')
cv.imshow("transformation with figure:1", np.hstack((img, img_1)))

#B
v = np.vectorize(trans_2)
img_2 = v(img)
img_2 =  img_2.astype('uint8')
cv.imshow("transformation with figure:2", np.hstack((img, img_2)))

cv.waitKey(0)
cv.destroyAllWindows()
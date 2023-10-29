import cv2 as cv
import numpy as np

img = cv.imread("redcell.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT, 1, img.shape[0]/10, param1=245, param2=13, minRadius=0,maxRadius=45)
if circles is not None:
    circles = np.uint16(np.around(circles))
    w = 0
    r = 0
    for i in circles[0, :]:
        center = (i[0], i[1])
        cv.circle(img, center, 1, (0, 255, 255), 3)
        radius = i[2]
        #print(radius)

        if radius > 40:
            cv.circle(img, center, radius, (255, 255, 255), 3)
            w = w + 1
        else:
            cv.circle(img, center, radius, (0, 0, 255), 2)
            r = r + 1

cv.imshow("HoughCircles", img)
print("White blood cells = ",w)
print("Red blood cells = ",r)
cv.waitKey(0)

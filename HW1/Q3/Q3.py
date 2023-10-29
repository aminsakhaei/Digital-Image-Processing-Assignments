import cv2 as cv
import numpy as np
import math


img = cv.imread("T.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(img.shape)

#Scaling
img_scaled = cv.resize(img, None, fx=0.75, fy=0.75, interpolation=0)
"""cv.imshow("scaled", img_scaled)"""

#Translation
translation_matrix = np.float32([[1,0,70], [0,1,110]])
img_translation = cv.warpAffine(img, translation_matrix, (607, 655))
"""cv.imshow("Translated", img_translation)"""

#Horizontal Shear
horizental_matrix = np.float32([[1, 0, 0], [0.2, 1, 0]])
img_sh = cv.warpAffine(img, horizental_matrix, (607, 655))
"""cv.imshow("Horizontal Shear", img_sh)"""

#Vertical Shear
vertical_matrix = np.float32([[1, 0.2, 0], [0, 1, 0]])
img_sv = cv.warpAffine(img, vertical_matrix, (607, 655))
"""cv.imshow("Vertical Shear", img_sv)"""

#Rotation
forward = np.zeros((607, 655),dtype="uint8")
backward = np.zeros((607, 655),dtype="uint8")
x = 300
y = 300
angle = 60.0
angle = angle*(math.pi/180)
for i in range(607):
    for j in range(655):
        for_x = int((i - x) * math.cos(angle) - (j - y) * math.sin(angle) + x)
        for_y = int((i - x) * math.sin(angle) + (j - y) * math.cos(angle) + x)
        back_x = int((i - x) * math.cos(angle) + (j - y) * math.sin(angle) + x)
        back_y = int(-(i - x) * math.sin(angle ) + (j - y) * math.cos(angle) + x)
        if (for_x<607) and (for_y<655) :
            forward[i, j] = img[for_x, for_y ]
        if (back_x<607) and (back_y<655) :
            backward[i, j] = img[back_x, back_y]

"""cv.imshow("Forward Rotation", forward)
cv.imshow("Backward Rotation", backward)"""

cv.waitKey(0)
cv.destroyAllWindows()
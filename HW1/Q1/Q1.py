import cv2 as cv

#define for transformation [0, 255] to [0, a]
def map(x, y):
    min = 0
    max = 255
    x = ((x-min)/(max-min))*y     #mapping
    x = x.astype('uint8')     #Convert float to uint8
    return x
#reding image
img = cv.imread("mandrill.jpg")

#A: dimensions and type
print(img.shape)
print(type(img))

#B: convert BGR to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray scale", img_gray)

#C: change the brightness level
cv.imshow("64 level", map(img_gray, 64))
cv.imshow("16 level", map(img_gray, 16))
cv.imshow("2 level", map(img_gray, 2))

#D: crop
a = img[0:512 , 0:256]
b = img[0:512 , 256:512]
cv.imshow("crop", cv.hconcat([a, b]))

#E: flip
flip_rtol = cv.flip(img, 1)
flip_utod = cv.flip(img, 0)
"""cv.imshow("flip right to left", flip_rtol)
cv.imshow("flip right to left", flip_utod)"""

#F: save the up to down flip
cv.imwrite("flipped.jpg", flip_utod)

#G: change scale
img_repeat_u  = cv.resize(img_gray, None, fx=3, fy=3,interpolation = cv.INTER_AREA)
img_linear_u = cv.resize(img_gray, None, fx=3, fy=3,interpolation = cv.INTER_LINEAR)
img_nn_u = cv.resize(img_gray, None, fx=3, fy=3,interpolation = cv.INTER_NEAREST)
img_repeat_d = cv.resize(img_gray, None, fx=1/3, fy=1/3,interpolation = cv.INTER_AREA)
img_linear_d = cv.resize(img_gray, None, fx=1/3, fy=1/3,interpolation = cv.INTER_LINEAR)
img_nn_d = cv.resize(img_gray, None, fx=1/3, fy=1/3,interpolation = cv.INTER_NEAREST)
"""cv.imshow("Scaled up(lenear)", img_linear_u)
cv.imshow("Scaled down(lenear)", img_linear_d)
cv.imshow("Scaled up(repeat pixels)", img_repeat_u)
cv.imshow("Scaled down(repeat pixels)", img_repeat_d)
cv.imshow("Scaled up(nearest neighbor)", img_nn_u)
cv.imshow("Scaled down(nearest neighbor)", img_nn_d)"""

cv.waitKey(0)
cv.destroyAllWindows()

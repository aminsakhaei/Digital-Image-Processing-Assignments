import cv2 as cv
import numpy as np

def get_points(img, points):
    cv.imshow("image", img)

    def click_event(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONUP:
            print(x, ' ', y)
            points.append((x, y))
            font = cv.FONT_HERSHEY_SIMPLEX
            cv.putText(img, str(x) + ',' + str(y), (x, y), font, 0.5, (0, 0, 255), 1)
            cv.circle(img, (x, y), 3, (0, 0, 255), -1)
            cv.imshow('image', img)

    while True:
        cv.setMouseCallback('image', click_event)
        k = cv.waitKey(0)
        if k == ord('n'):
            cv.destroyAllWindows()
            break

imgf = cv.imread("MRIF.png")
imgf_c = imgf.copy()
points_f = []
imgs = cv.imread("MRIS.png")
imgs_c = imgs.copy()
points_s = []

print("click 3 point then press n")
get_points(imgf_c, points_f)
points_f = np.float32(points_f)
print("click 3 point then press n")
get_points(imgs_c, points_s)
points_s = np.float32(points_s)

Affine = cv.getAffineTransform(points_s, points_f)
print(Affine)

img_transformed = cv.warpAffine(imgs, Affine, (imgf.shape[1], imgf.shape[0]))
cv.imshow('new image', img_transformed)
cv.waitKey(0)
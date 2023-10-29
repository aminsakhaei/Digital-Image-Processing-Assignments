import cv2 as cv
import numpy as np


def hole_filling(img):
    cv.imshow("image", img)

    def click_event(event, x, y, flags, param):
        global img
        _, thresh = cv.threshold(img, 20, 255, cv.THRESH_BINARY)
        img_n = 255 - thresh
        img_r = np.zeros(img.shape, dtype='uint8')
        test = np.zeros(img.shape, dtype='uint8')
        kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
        if event == cv.EVENT_LBUTTONUP:
            print(x, ' ', y)
            img_r[y, x] = 255

            while (np.any(img_r!=test)):
                test = img_r
                img_r = cv.dilate(img_r, kernel, iterations=1)
                img_r = cv.bitwise_and(img_r, img_n)
            img = cv.bitwise_or(img_r, img)
            cv.imshow("result", img)

    while True:
        cv.setMouseCallback('image', click_event)
        k = cv.waitKey(0)
        if k == 27:
            cv.destroyAllWindows()
            break

img = cv.imread("reflections.jpg", 0)
hole_filling(img)

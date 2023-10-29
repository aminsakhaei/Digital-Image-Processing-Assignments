import cv2 as cv
import numpy as np

#define for average capture of two received frames
def avg(frame1, frame2):
    frame1_32 = np.float32(frame1)
    frame2_32 = np.float32(frame2)
    sub = frame1_32 - frame2_32
    average = np.sqrt((sub[0:480, :]**2 + sub[:, 0:640]**2) / (255**2 + 255*2))
    result = np.uint8(average * 255)
    return result

capture = cv.VideoCapture(0)
_, frame1 = capture.read()
_, frame = capture.read()
frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
while True:
    _, frame2 = capture.read()
    cv.imshow("frame", frame2)
    frame2 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    delta = avg(frame1, frame2)
    cv.imshow("motion", delta)
    frame1 = frame
    frame = frame2
    _, stdev = cv.meanStdDev(delta)
    if stdev > 10 :
        print("motion detected")
    if cv.waitKey(1) & 0xff == ord('q') :
        break




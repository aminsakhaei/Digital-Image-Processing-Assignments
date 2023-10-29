import cv2 as cv
import numpy as np

capture = cv.VideoCapture('Q_three.AVI')

_, frame = capture.read()
frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
rows, cols = frame.shape

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc, 20.0, (rows, cols))

summation = np.zeros((rows, cols), np.float32)

frames = []
grays = []

while True:
    _, frame = capture.read()
    if frame is None:
        break
    frames.append(frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    grays.append(gray)
    summation += gray

capture.release()

avg = summation/len(grays)
avg = avg.astype('uint8')

for i in range(len(frames)):
    d = cv.absdiff(avg, grays[i])
    _, thresh = cv.threshold(d, 40, 255, cv.THRESH_BINARY)
    cv.imshow('Difference', thresh)
    cv.imshow("Video", frames[i])
    for j in range (rows):
        for k in range(cols):
            if (thresh[j, k]==255):
                frames[i][j, k]= (0, 0, 255)
    cv.imshow("Motion detector", frames[i])

    if cv.waitKey(1) & 0xff == ord('q'):
        break
    out.write(frames[i])

cv.destroyAllWindows()
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

#A
def filter(img, x):
    #median filter
    if type(x) == str and x=='median':
        image = cv.copyMakeBorder(img, 1, 1, 1, 1, cv.BORDER_REFLECT)
        image = cv.medianBlur(image, 3)
        """imgm = np.zeros(image.shape[0], image.shape[1])
        for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        cut = imgm[i:i + 3, j:j + 3]
                        imgm[i, j] = cut[1, 1]
        return imgm"""
        return image
    #average filter
    elif (x.shape[0] == 3 and x.shape[1]==3):
        img_f = img.copy()
        img_f = cv.copyMakeBorder(img, 1, 1, 1, 1, cv.BORDER_REFLECT)
        img_f = cv.filter2D(img_f, -1, x/9)
        img_f = img_f.astype('uint8')
        """imga = np.zeros(img_f.shape[0], img_f.shape[1])
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                cut = img_f[i:i + 3, j:j + 3]
                imga[i, j] = np.average(x * cut)
                if (imga[i, j] < 0):
                    imga[i, j] = 0
                if (imga[i, j] > 255):
                    imga[i, j] = 255
        return imga"""

        return img_f

    else:
        return False

#B
img = cv.imread("bone-scan.png", 0)

r = 'median'
img_med = filter(img, r)
res = np.hstack((img,img_med[1:img_med.shape[0]-1, 1:img_med.shape[1]-1]))
cv.imshow("median", res)

#C
kernel = np.ones((3, 3), np.float32)
img_avg = filter(img, kernel)
res = np.hstack(((img,img_avg[1:img_med.shape[0]-1, 1:img_avg.shape[1]-1])))
cv.imshow("average", res)

#D
#laplacian filter
def laplaciann(img_med, k):
    img_l = np.zeros((img_med.shape[0], img_med.shape[1]))
    for i in range( img.shape[0]):
        for j in range(img.shape[1]):
            cut = img_med[i:i+3, j:j+3]
            img_l[i, j] = np.sum(k*cut)
    img_l = img_l.astype('uint8')
    return img_l
#kernel
k = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

img_l = laplaciann(img_med, k)
img_l2 = cv.Laplacian(img_med, cv.CV_64F)
test = np.all(img_l2==img_l)
print(test)

#E
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
l = plt.imshow(img_med, cmap='gray', vmin=0,vmax=255)
ax.axis('off')
plt.title('Adding laplacian mask to original image with varying C')

axcolor = 'lightgoldenrodyellow'
axc = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sc = Slider(axc, 'C', -20, 20, valstep=0.1, valinit=0)

def update(val):
    c = sc.val
    k = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    l.set_data(img_med + laplaciann(img_med, c*k))
    fig.canvas.draw_idle()

sc.on_changed(update)
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
def reset(event):
    sc.reset()
button.on_clicked(reset)

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

#define filtering function
def filter(img, filter, ftype, D0, n):
    rows, cols = img.shape
    # zero padding
    img1 = cv.copyMakeBorder(img, 0, rows, 0, cols, cv.BORDER_CONSTANT, value=(0, 0, 0))
    # fourier transform & shift
    dft = cv.dft(np.float32(img1), flags=cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    if ftype == 'ideal':
        for u in range(dft_shift.shape[0]):
            for v in range(dft_shift.shape[1]):
                D = math.sqrt(((u - rows) ** 2) + ((v - cols) ** 2))
                if filter == 'highpass':
                    if D<D0 :
                        dft_shift[u, v] = 0
                if filter == 'lowpass':
                    if D>D0 :
                        dft_shift[u, v] = 0

    if ftype == 'Butterworth':
        for u in range(dft_shift.shape[0]):
            for v in range(dft_shift.shape[1]):
                D = math.sqrt(((u - rows) ** 2) + ((v - cols) ** 2))
                if filter == 'highpass':
                    dft_shift[u, v] = dft_shift[u, v] * ((D ** (2 * n)) / ((D ** (2 * n)) + (D0 ** (2 * n))))
                elif filter == 'lowpass':
                    dft_shift[u, v] = dft_shift[u, v] / (1 + ((D / D0) ** (2 * n)))

    if ftype == 'Gaussian':
        for u in range(dft_shift.shape[0]):
            for v in range(dft_shift.shape[1]):
                D = np.sqrt(((u - rows) ** 2) + ((v - cols) ** 2))
                if filter == 'highpass':
                    dft_shift[u, v] = dft_shift[u, v] * (1 - np.exp(-(D ** 2) / (2 * D0 ** 2)))
                if filter == 'lowpass':
                    dft_shift[u, v] = dft_shift[u, v] * (np.exp(-(D ** 2) / (2 * D0 ** 2)))

    dft_ishift = np.fft.ifftshift(dft_shift)
    img_back = cv.idft(dft_ishift)
    img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    img_back = cv.normalize(img_back, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)
    img_back = img_back[0:rows, 0:cols]
    return img_back

img = cv.imread('a.tif',0)


#plot highpass
plt.figure()
ax = plt.subplot(1, 4, 1)
ax.set_title('Input Image')
ax.imshow(img, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(1, 4, 2)
ax.set_title('IHPF 50')
ax.imshow(filter(img, 'highpass', 'ideal', 50, 0), cmap = 'gray')
ax.axis('off')

ax = plt.subplot(1, 4, 3)
ax.set_title('BHPF 50,2')
ax.imshow(filter(img, 'highpass', 'Butterworth', 50, 2), cmap = 'gray')
ax.axis('off')


ax = plt.subplot(1, 4, 4)
ax.set_title('GHPF 50')
ax.imshow(filter(img, 'highpass', 'Gaussian', 50, 0), cmap = 'gray')
ax.axis('off')

##plot lowpass
plt.figure()
bx = plt.subplot(1, 4, 1)
bx.set_title('Input Image')
bx.imshow(img, cmap = 'gray')
bx.axis('off')

bx = plt.subplot(1, 4, 2)
bx.set_title('ILPF 50')
bx.imshow(filter(img, 'lowpass', 'ideal', 50, 0), cmap = 'gray')
bx.axis('off')

bx = plt.subplot(1, 4, 3)
bx.set_title('BLPF 50,2')
bx.imshow(filter(img, 'lowpass', 'Butterworth', 50, 2), cmap = 'gray')
bx.axis('off')


bx = plt.subplot(1, 4, 4)
bx.set_title('GLPF 50')
bx.imshow(filter(img, 'lowpass', 'Gaussian', 50, 0), cmap = 'gray')
bx.axis('off')

plt.show()
cv.waitKey(0)

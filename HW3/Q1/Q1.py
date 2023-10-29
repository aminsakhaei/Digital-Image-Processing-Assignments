import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("chest.tif", 0)

#A
#Fourier transform
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
#Shift
dft_shift = np.fft.fftshift(dft)

#Magnitude & Phase
mag, phase = cv.cartToPolar(dft_shift[:, :, 0], dft_shift[:, :, 1])
magnitude_spectrum = 20*np.log(mag)

#B
#Reverse shift
dft_ishift = np.fft.ifftshift(dft_shift)
#Reverse fourier transform
img_back = cv.idft(dft_ishift)
img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])
#Normalize
img_back = cv.normalize(img_back, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

#C
#Mirror
[dft_shift[:, :, 0], dft_shift[:, :, 1]] = cv.polarToCart(mag, -phase)

#Reverse shift
dft_ishift_m = np.fft.ifftshift(dft_shift)

#Reverse fourier transform
img_mir = cv.idft(dft_ishift_m)
img_mir = cv.magnitude(img_mir[:, :, 0], img_mir[:, :, 1])

#Normalize
img_mir = cv.normalize(img_mir, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

#Plot
#A
plt.figure()
ax = plt.subplot(1, 3, 1)
ax.set_title('Input Image')
ax.imshow(img, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(1, 3, 2)
ax.set_title('Magnitude')
ax.imshow(magnitude_spectrum, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(1, 3, 3)
ax.set_title('Phase')
ax.imshow(phase, cmap = 'gray')
ax.axis('off')

#B
plt.figure()
ax = plt.subplot(1, 2, 1)
ax.set_title('Input Image')
ax.imshow(img, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(1, 2, 2)
ax.set_title('Image back')
ax.imshow(img_back, cmap = 'gray')
ax.axis('off')

#C
plt.figure()
ax = plt.subplot(1, 2, 1)
ax.set_title('Input Image')
ax.imshow(img, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(1, 2, 2)
ax.set_title('Mirrored')
ax.imshow(img_mir, cmap = 'gray')
ax.axis('off')


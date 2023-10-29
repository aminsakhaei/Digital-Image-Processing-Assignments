import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_1 = cv.imread("mandrill.tif", 0)
img_2 = cv.imread("clown.tif", 0)

#Fourier transform
dft_1 = cv.dft(np.float32(img_1), flags=cv.DFT_COMPLEX_OUTPUT)
dft_2 = cv.dft(np.float32(img_2), flags=cv.DFT_COMPLEX_OUTPUT)

#Shift
dft_shift_1 = np.fft.ifftshift(dft_1)
dft_shift_2 = np.fft.ifftshift(dft_2)

#Magnitude & Phase
mag_1, phase_1 = cv.cartToPolar(dft_shift_1[:, :, 0], dft_shift_1[:, :, 1])
mag_2, phase_2 = cv.cartToPolar(dft_shift_2[:, :, 0], dft_shift_2[:, :, 1])

#Displacement Phase
[dft_shift_1[:, :, 0], dft_shift_1[:, :, 1]] = cv.polarToCart(mag_1 , phase_2)
[dft_shift_2[:, :, 0], dft_shift_2[:, :, 1]] = cv.polarToCart(mag_2 , phase_1)

#Reverse shift
dft_ishift_1 = np.fft.ifftshift(dft_shift_1)
dft_ishift_2 = np.fft.ifftshift(dft_shift_2)

#Reverse fourier transform
img_back_1 = cv.idft(dft_ishift_1)
img_back_2 = cv.idft(dft_ishift_2)

img_back_1 = cv.magnitude(img_back_1[:, :, 0], img_back_1[:, :, 1])
img_back_2 = cv.magnitude(img_back_2[:, :, 0], img_back_2[:, :, 1])

#Plot
ax = plt.subplot(2, 2, 1)
ax.set_title('Input Image 1')
ax.imshow(img_1, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 3)
ax.set_title('Image back 1')
ax.imshow(img_back_1, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 2)
ax.set_title('Input Image 2')
ax.imshow(img_2, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 2, 4)
ax.set_title('Image back 2')
ax.imshow(img_back_2, cmap = 'gray')
ax.axis('off')


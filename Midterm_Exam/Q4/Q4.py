import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("xray_checkered.png", 0)
rows, cols = img.shape

#Fourier transform
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)

#Shift
dft_shift = np.fft.fftshift(dft)

mag1, _ = cv.cartToPolar(dft_shift[:, :, 0], dft_shift[:, :, 1])
magnitude_spectrum1 = 20*np.log(mag1)

#cut magnitude
mag_l = magnitude_spectrum1[:, 0:100]
mag_u = magnitude_spectrum1[0:100, :]
for i in range(mag1.shape[0]):
  for j in range(mag1.shape[1]):
    if(magnitude_spectrum1[i, j] == np.max(mag_l)):
        dft_shift[i, j] = (dft_shift[i + 1, j] + dft_shift[i - 1, j] + dft_shift[i, j + 1] + dft_shift[i, j - 1]) / 4
    elif (magnitude_spectrum1[i, j] == np.max(mag_u)):
        dft_shift[i, j] = (dft_shift[i + 1, j] + dft_shift[i - 1, j] + dft_shift[i, j + 1] + dft_shift[i, j - 1]) / 4

mag2, _ = cv.cartToPolar(dft_shift[:, :, 0], dft_shift[:, :, 1])
magnitude_spectrum2 = 20*np.log(mag2)
#Reverse shift
dft_ishift = np.fft.ifftshift(dft_shift)
#Reverse fourier transform
img_back = cv.idft(dft_ishift)
img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])
#normalize
img_back = cv.normalize(img_back, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

plt.imshow(img_back, cmap = 'gray')
plt.title("Denoised image")
plt.axis('off')
plt.show()
#cv.imwrite("denoised.jpg", img_back)
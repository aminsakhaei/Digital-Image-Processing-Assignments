import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#A
img = cv.imread("noisy_skull.png", 0)
strip = img[:img.shape[0], :170]
plt.hist(strip.ravel(), bins=256, density=True)

m_n = np.mean(strip)
v_n = np.var(strip)
print("Noise mean = ",m_n)
print("Noise variance = ", v_n)

#C
dst = cv.copyMakeBorder(img, 4, 4, 4, 4, cv.BORDER_REFLECT)
img_adv = np.zeros(dst.shape)
for i in range (img.shape[0]):
    for j in range (img.shape[1]):
        cut = dst[i:i+9, j:j+9]
        m_l = np.mean(cut)
        v_l = np.var(cut)
        img_adv[i, j] = np.round(dst[i,j] - ((v_n/v_l) * (dst[i,j] - m_l)))
img_adv = img_adv[4:dst.shape[0]-4, 4:dst.shape[1]-4]

#D
dst = cv.copyMakeBorder(img, 3, 3, 3, 3, cv.BORDER_REFLECT)
img_med = cv.medianBlur(dst, 7)
img_med = img_med[3:dst.shape[0]-3, 3:img.shape[1]-3]

#E
plt.figure()
ax = plt.subplot(2, 3, 1)
ax.set_title('noisy')
ax.imshow(img, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 3, 2)
ax.set_title('Adaptive')
ax.imshow(img_adv, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 3, 3)
ax.set_title('Median')
ax.imshow(img_med, cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 3, 4)
plt.hist(strip.ravel(), bins=256, range=(0,255), density=True)
plt.ylim(0, 0.3)

ax = plt.subplot(2, 3, 5)
plt.hist(img_adv[:img.shape[0], :170].ravel(), bins=256, range=(0,255), density=True)
plt.ylim(0, 0.3)

ax = plt.subplot(2, 3, 6)
plt.hist(img_med[:img.shape[0], :170].ravel(), bins=256, range=(0,255), density=True)
plt.ylim(0, 0.3)

plt.show()
cv.waitKey(0)
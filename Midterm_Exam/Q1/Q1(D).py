import numpy as np
import cv2
import matplotlib.pyplot as plt

#def decimal2binary(n):
    #a = np.zeros(8)
    #i = 0
    #while n > 0:
        #a[7-i] = (n % 2)
        #n //= 2
        #i = i+1
    #return a

# Convert decimal to binary
def change_binary(img):
    binary_list = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            bin = np.binary_repr(img[i, j], width=8)
            #bin = decimal2binary(img[i, j])
            binary_list.append(bin)
    return binary_list

# Convert to (bits)th image
def convert2img(binary_list,bits):
    bit_img = np.array([int(i[8-bits])*(2**(bits - 1)) for i in binary_list],dtype=np.uint8)
    print(int(i[8-bits])for i in binary_list)
    bit_img = bit_img.reshape(img.shape[0], img.shape[1])
    return bit_img

img = cv2.imread('retina.jpg', 0)
img_binarry = change_binary(img)

#plot
ax = plt.subplot(2, 4, 1)
ax.set_title('8th bit(MSB)')
ax.imshow(convert2img(img_binarry, 8), cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 4, 2)
ax.set_title('7th bit')
ax.imshow(convert2img(img_binarry, 7), cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 4, 3)
ax.set_title('6th bit')
ax.imshow(convert2img(img_binarry, 6), cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 4, 4)
ax.set_title('5th bit')
ax.imshow(convert2img(img_binarry, 5), cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 4, 5)
ax.set_title('4th bit')
ax.imshow(convert2img(img_binarry, 4), cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 4, 6)
ax.set_title('3th bit')
ax.imshow(convert2img(img_binarry, 3), cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 4, 7)
ax.set_title('2th bit')
ax.imshow(convert2img(img_binarry, 2), cmap = 'gray')
ax.axis('off')

ax = plt.subplot(2, 4, 8)
ax.set_title('1th bit(LSB)')
ax.imshow(convert2img(img_binarry, 1), cmap = 'gray')
ax.axis('off')

plt.show()
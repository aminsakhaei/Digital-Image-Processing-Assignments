import numpy as np
import matplotlib.pyplot as plt

#define for transformation [a, b] to [0, 255]
def map(x):
    min = x.min()
    max = x.max()
    x = ((x-min)/(max-min))*255     #mapping
    x = x.astype('uint8')     #Convert float to uint8
    return x

#define and fill the matrix with random number
a = np.random.uniform(-3.2, 9.3,size=(50, 40, 3))
#calling function
a = map(a)
#show result
plt.imshow(np.array(a))
plt.show()

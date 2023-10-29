import numpy as np
import matplotlib.pyplot as plt

#define derivative function
def deriv(x):
    der = np.arange(len(x)-1)
    # loop for build derivative coefficients
    for i in range(len(x)):
        der[i-1] = x[i]*i
    return der     #return derivative coefficients
#define polynomial function
def poly(a, x):
    # define the variable
    sum = 0
    #loop for build polymonial
    for i in range(len(a)):
        sum = sum+(a[i]*(x**i))
    return  sum     #return polomonial


a = [-3,7,0,-6,3,2]     #Polynomial coefficients
x = np.linspace(-10, 10, 100)      #range
plt.plot(x, poly(a,x),'darkorange',linewidth=3, label='polynomial')
a= deriv(a)
print(a)
plt.plot(x, poly(a,x),'c--',label=' first polynomial derivation')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("plot")
plt.legend()
plt.axis([-10, 10, -30, 40])
plt.show()


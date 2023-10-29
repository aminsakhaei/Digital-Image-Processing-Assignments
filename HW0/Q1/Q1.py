import math

a = -3          #left bound
b = 4           #right bound
h = 1/200       #step length
#numbers of trapezoids
n = int((b-a)/h)
#define the variable
area = 0
#loop to calculate the area of each trapezoid and sum
for i in range (n):
    # location of the trapezoid
    x = a+ (i*h)
    # calculate area of the trapezoid
    x = math.sin(x**2)
    # sum of the areas
    if i==0 or i==n:
        area = (x * (h/2)) + area
    else:
        area = ((h/2)*(x * 2)) + area

#print the result
print('result=', area)
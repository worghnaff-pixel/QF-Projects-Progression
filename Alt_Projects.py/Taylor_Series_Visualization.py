import matplotlib.pyplot as plt
import numpy as np

n = 10

def factorial(n):
    fct = []
    num = 1
    for i in range(1,n+1):
        num = i*num
        fct.append(num)
    return fct

x = np.linspace(0,5,100)
f = np.e**x


center = 4

def taylor(factorial,f,center):
    approx = []
    for i in range(0,n):
        approx.append(f*((x-center)**i)/factorial(n)[i])

    return approx
#print(taylor(factorial,f,center))

data_array = np.array(taylor(factorial,f,center))
sum_array = data_array.sum(axis=0)


plt.plot(x,sum_array)
plt.plot(x,f)
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Random points creation
npoints = 10
xcords = []
ycords = []
for i in range(0,npoints):
    xval = np.random.random()
    yval = 4*np.random.random()
    xcords.append(xval)
    ycords.append(yval)



#Best fit RSS
a = 0
b = 0
x = 0

diffs = []

for avals in range(0,10):
    a = avals
    for bvals in range(0,10):
        b = bvals
        for i in range(0,len(ycords)):
            line = a*x + b
            x = xcords[i]
            diff = (ycords[i] - line)**2
            diffs.append(diff)  

N = len(xcords)

sumx = 0
sumy = 0


for x,y in zip(xcords,ycords):
    sumx += x
    sumy += y

print(sumx)
print(sumy)
x = np.linspace(0,1,50)
y = ((sumy / sumx) * x)


#Plotting
plt.scatter(xcords,ycords)

plt.plot(x,y)
plt.xlim(0,4)
plt.ylim(0,4)
plt.show()
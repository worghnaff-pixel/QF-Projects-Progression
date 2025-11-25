import numpy as np
import matplotlib.pyplot as plt

steps = 100

def path(steps):
    pos = 0
    positions = [0]
    for i in range(0,steps-1):   
        rand = np.random.random()
        if rand > 0.5:
            pos = pos + 1
        else:
            pos = pos -1
        positions.append(pos)
    return positions
x = np.arange(steps)
plt.step(x,path(steps))
plt.show()
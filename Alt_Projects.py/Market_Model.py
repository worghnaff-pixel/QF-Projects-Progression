# generate an initial market price that follwos sinusoidal pattern
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#market has to be discrete, so sinusoidal discrete
#make market follow continuous sinusoidal at start, but
#have to pass discrete filter

def sinprice(t, step = 0.05):
    base = np.sin(t)
    quantized = np.round(base / step) * step
    
    return quantized
t = np.linspace(0,10,50)
prices = sinprice(t,0.05)

market = pd.DataFrame({'time' : t, 'price': prices})

print(market)
plt.step(t,sinprice(t,0.05))
plt.show()

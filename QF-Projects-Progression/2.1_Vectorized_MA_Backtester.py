import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

data = yf.download('^GSPC',start="2024-1-1",end="2025-1-1")

data['20SMA'] = data['Close'].rolling(20).mean()
data['100SMA'] = data['Close'].rolling(100).mean()


x = np.arange(0,len(data['20SMA']))
plt.plot(x,data['20SMA'])
plt.plot(x,data['100SMA'])
plt.plot(x,data['Close'])
plt.show()
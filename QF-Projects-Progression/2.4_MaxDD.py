import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


# Efficient way:
# drawdown = data['Close'] / data['Close'].cummax() - 1
# main idea is (current price / max price up to now) -1

data = yf.download('AAPL',start="2020-1-1", end="2024-1-1")

def maxDD(data):
    maxprice = []
    maxdrawdown = []
    closes = data['Close']
    for i in range(len(closes)):
        price = closes.iloc[i].item() # convert series element of closes to scalar
        if len(maxprice) == 0 or price > maxprice[-1]:
            maxprice.append(price)
        else:
            maxprice.append(maxprice[-1])
        diff = (price / maxprice[-1]) - 1
        maxdrawdown.append(diff)
    return maxdrawdown


plt.plot(maxDD(data))
plt.show()





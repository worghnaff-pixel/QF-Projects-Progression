import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = yf.download('^GSPC', start="2020-01-01", end="2025-01-01")[['Close']]
m = 200
n = 50
def short_term_ma(data, n):
    data = data.copy()
    short_vals = []
    closes = data['Close']
    for i in range(n, len(closes) + 1):
        window = closes.iloc[i-n:i]
        ma = np.mean(window)
        short_vals.append(ma)
    return short_vals

def long_term_ma(data, m):
    data = data.copy()
    long_vals = []
    closes = data['Close']
    for i in range(m, len(closes) + 1):
        window = closes.iloc[i-m:i]
        ma = np.mean(window)
        long_vals.append(ma)
    return long_vals

def strat(data,long_term_ma,short_term_ma):
    closes = data['Close']
    buy_prices = []
    sell_prices = []
    longma = long_term_ma(data,m)
    shortma = short_term_ma(data,n)
    for i in range(m,len(closes)- m -1):
        if longma[i] > shortma[i] and len(buy_prices) == len(sell_prices):
            buynow = closes.iloc[i]
            buy_prices.append(buynow)
        elif longma[i] > shortma[i] and len(buy_prices) != len(sell_prices):
            continue
        elif longma[i] < shortma[i] and len(buy_prices) == len(sell_prices):
            continue
        elif longma[i] < shortma[i] and len(buy_prices) != len(sell_prices):
            sellnow = closes.iloc[i]
            sell_prices.append(sellnow)
    return buy_prices,sell_prices

def equity(strat):
    equity = 1
    buy_elements, sell_elements = strat(data,long_term_ma,short_term_ma)
    for i in range(0,len(sell_elements)-1):
        equity *= (sell_elements[i]/buy_elements[i])
    return equity


print(equity(strat))




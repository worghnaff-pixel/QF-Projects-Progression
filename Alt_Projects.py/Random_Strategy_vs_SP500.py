import yfinance as yf
import random
import matplotlib.pyplot as plt
import numpy as np

data = yf.download('^GSPC',start = "2024-1-1",end="2025-1-1")

def strat(data):
    rand = []
    buy = []
    sell = []
    for i in range(0,len(data['Close'])-1):
        r = random.random()
        rand.append(r)
    for j in range(0,len(data['Close'])-1):
        if rand[j] > 0.5 and len(buy) == len(sell):
            buy.append(data['Close'].iloc[j])
            sell.append(data['Close'].iloc[j+1])
        else:
            continue
    returns = []
    for k in range(0,len(sell)):
        returns.append(sell[k]/buy[k])
    value = 1
    price = []
    for f in range(0,len(returns)):
        value = value * returns[f]
        price.append(value)
        
    return price

prices = []
for i in range(0,30):
    prices.append(strat(data))

for plot in range(0,len(prices)):
    plt.plot(prices[plot])

def EV(prices):
    fin_prices = []
    for i in range(0,len(prices)):
        fin_price = prices[i][-1]
        fin_prices.append(fin_price)
    return np.mean(fin_prices)

print(EV(prices))
sp500value = (1+data['Close'].pct_change()).cumprod()
print(sp500value.iloc[-1])
plt.show()

#implement adding money at random or adding money at drops or at highs
#repeat with sp500
"""
def measureDD(data):
    maxDD = []
    maxoutliers = []
    maxi = []
    mini = []
    minoutliers = []
    parsed = []
    for i in data['Close']:
        parsed.append(data['Close'].iloc[data['Close'].iloc[i]])
        if data['Close'].iloc[data['Close'].iloc[i]] > max(parsed):
            maxoutliers.append(data['Close'].iloc[data['Close'].iloc[i]])
            maxi.append(i)
        if data['Close'].iloc[data['Close'].iloc[i]] < min(parsed):
            minoutliers.append(data['Close'].iloc[data['Close'].iloc[i]])
            mini.append(i)
    for j in range(0,max(len(maxi) or len(mini))):
        maxval = max(maxoutliers)
        maxpos = maxoutliers.index(maxval)
        maxcrit = maxi[maxpos]
        minval = min(minoutliers)
        minpos = minoutliers.index(minval) 
        mincrit = mini[minpos]
        if maxcrit > mincrit:
            maxDD.append(1-mincrit/maxcrit)
        else:
            minoutliers.pop(mini)
            mini.pop(minoutliers.index(minval))
    return maxDD
print(measureDD(data))

#agghghghgh
"""     
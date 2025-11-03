import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt



def eq_weighted_portfolio(data, f):
    returns = data.pct_change().dropna()
    #create an array of weight to later apply to aapl and msft
    weights = np.array([f,1-f])
    weighted_returns = returns @ weights # Nx2 x 2x2 = N x 1 boss
    return weighted_returns

def cum_ret(f):
    TICKERS = ('AAPL','MSFT')
    data = yf.download(TICKERS,start="2024-01-01",end="2025-01-01")[['Close']]
    weighted_returns = eq_weighted_portfolio(data,f)
    cumret = 1
    for i in range(1,len(weighted_returns)):
        cumret = cumret*(1+weighted_returns[i])
    return cumret

def risk_curve():
    rets = []
    vals_i = [i*0.1 for i in range(11)]
    for i in vals_i:
        rets.append(cum_ret(i))
    return rets
print(risk_curve())

x = np.arange(0,1.1,0.1)
plt.plot(x,risk_curve())
plt.show()




import yfinance as yf
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

TICKERS = ['PEP','KO','AAPL','MSFT']
start="2010-1-1"
end=datetime.now()

data = yf.download(TICKERS, start="1962-01-02", end=datetime.now())['Close']

individual_data = []
individual_returns = {}

for ticker in TICKERS:
    dirty = data[ticker]
    clean = dirty.dropna()
    individual_data.append(clean)

for i in range(0,len(individual_data)): print(TICKERS[i] , " has " , len(individual_data[i]) , " data points")
RETURN = ['PEP_Return','KO_Return','AAPL_Return','MSFT_Return']
data['PEP_Return'] = data['PEP'].pct_change()
data['KO_Return'] = data['KO'].pct_change()
data['AAPL_Return'] = data['AAPL'].pct_change()
data['MSFT_Return'] = data['MSFT'].pct_change()



for i in RETURN: individual_returns[i] = ((data[i]+1).cumprod())
for t in range(0,len(TICKERS)): print("The returns of " , TICKERS[t], " since inception is ", individual_returns[RETURN[t]].iloc[-1])

sns.set_theme(style="darkgrid",palette="pastel")
plt.figure(figsize=(12, 6))
plt.plot(individual_returns['PEP_Return'], label='PEP')
plt.plot(individual_returns['KO_Return'], label='KO')
plt.plot(individual_returns['AAPL_Return'], label='AAPL')
plt.plot(individual_returns['MSFT_Return'], label='MSFT')
plt.title('Cumulative Returns of Selected Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.show()

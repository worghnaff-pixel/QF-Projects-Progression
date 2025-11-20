import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf

data = yf.download('BTC-USD',"2018-1-2","2022-7-9")['Close']
path = pd.read_csv("fear_and_greed_index.csv")

buy = []
sell = []
for i in range(0,len(path)):
    if path['fng_classification'].iloc[i] <= 15:
        if len(buy)== 0 or len(buy) == len(sell):
            buy.append(pd.to_datetime(path['fng_value'].iloc[i], dayfirst=True))
    elif path['fng_classification'].iloc[i] >= 60:
        if len(sell) != len(buy):
            sell.append(pd.to_datetime(path['fng_value'].iloc[i], dayfirst=True))


if len(buy) == len(sell):
    del buy[-1]

buy.reverse()
sell.reverse()

returns = []
totbuy = []
totsell = []
for i in range(0,len(buy)-1):
    buyprice = data.loc[buy[i]]
    sellprice = data.loc[sell[i]] 
    totbuy.append(buyprice)
    totsell.append(sellprice)

df = {'Buy': totbuy, 'Sell': totsell}

positions = pd.DataFrame(df)
positions['Returns'] = positions['Sell'] / positions['Buy']
cum = positions['Returns'].cumprod()
plt.figure(figsize=(10,5))
plt.plot(cum.index, cum.values, label='Strategy Cumulative Return')
plt.xlabel("Trade Number")
plt.ylabel("Cumulative Return (×)")
plt.title("Fear & Greed Strategy Performance")
plt.grid(True)
plt.legend()
plt.show()




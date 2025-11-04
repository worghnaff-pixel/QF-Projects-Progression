import yfinance as yf
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

start = "2020-1-1"
end = datetime.now()
data = yf.download('^GSPC', start, end)
data.columns = [col[0] for col in data.columns]  # flatten multiindex as it has ^GSPC for each type


def bolinger_bands(data):
    # Bollinger bands are SMA_price +/- k*std_(n past days)
    data['SMA'] = data['Close'].rolling(10).mean()
    data['Std'] = data['Close'].rolling(10).std()

    return data  

data = bolinger_bands(data)

data = data.dropna(subset=['SMA', 'Std'])

def strat(data):
    data['Middle'] = data['SMA']
    data['Low'] = data['SMA'] - 2*data['Std']
    buy = []
    sell = []
    
    for i in range(11, len(data['Close']) - 1):
        buy_signal  = 1 if data['Close'].iloc[i] < data['Low'].iloc[i] else 0
        sell_signal = 1 if data['Close'].iloc[i] > data['Middle'].iloc[i] else 0

        if len(buy) == len(sell) and buy_signal == 1:
            buy.append(data['Close'].iloc[i])
        elif len(buy) != len(sell) and sell_signal == 1:
            sell.append(data['Close'].iloc[i])

    return buy, sell

buy, sell = strat(data)

vals = {'Buy':buy, 'Sell': sell}

df = pd.DataFrame(vals)

df['Return'] = df['Sell'] / df['Buy'] -1
df['Equity'] = (1 + df['Return']).cumprod()
print(df)

# Calculate and plot equity curve + add parameter tunning for rolling mean...   






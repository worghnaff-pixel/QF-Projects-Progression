import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf


sp500 = pd.read_csv("sp500_daily_full_history.csv")
path = pd.read_csv("fear_and_greed_index.csv")

buy = []
sell = []
for i in range(0,len(path)):
    if path['fng_classification'].iloc[i] <= 20:
        if len(buy)== 0 or len(buy) == len(sell):
            buy.append(path['fng_value'].iloc[i])
    elif path['fng_classification'].iloc[i] >= 60:
        if len(sell) != len(buy):
            sell.append(path['fng_value'].iloc[i])
j = 0
'''''
for i in sp500['Date']:
    if i == buy[j] or i == buy[j].timedelta(1):
        print(sp500['Close'].iloc[i])
        j = j +1
'''

print(path['fng_value'].iloc[0])
print(path['fng_value'].iloc[0].timedelta(1))

import yfinance as yf
import pandas as pd
import datetime
from datetime import datetime
import matplotlib as plt
import numpy as np

TICKER = 'AAPL'
data = yf.download(TICKER,start="2024-1-1", end="2025-1-1")[['Close']]

data['Return'] = data['Close'].pct_change()


def num_pos_vs_neg_days(data):
    positive = []
    negative = []
    for i in data:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(i)
    return len(positive), len(negative)

print("The number of positive vs negative days are: " , num_pos_vs_neg_days(data['Return']))

def cum_ret(data):
    cum_ret = 1
    for i in range(1,len(data['Return'])):
        cum_ret = cum_ret*(1 + data['Return'][i])
    return cum_ret

print("The cumulative return of " , TICKER, " is ", cum_ret(data))

def std_dev_returns(data):
    mean = data['Return'].mean()
    diff = []
    for i in range(1,len(data['Return'])):
        diff.append(data['Return'][i]-mean)
    diff_array = np.array(diff)
    var = (diff_array@ diff_array)/(len(data['Return'])-1)
    std = np.sqrt(var)
    return std

print("The standard deviation of the set of values is " , std_dev_returns(data))
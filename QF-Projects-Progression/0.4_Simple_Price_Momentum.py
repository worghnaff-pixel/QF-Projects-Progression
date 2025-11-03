import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2024-01-01", end="2025-01-01")

data['Diff'] = data['Close'].diff()
data['Change'] = data['Close'].pct_change()
data['Signal'] = np.where(data['Diff']> 0,1,0) # np.where (condition, res_if condition satisfied, else)

data['Equity'] = (1+data['Change']).cumprod()

print(data['Strat'])
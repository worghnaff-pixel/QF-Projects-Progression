import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.getcwd())


data = yf.download("^GSPC", start="2020-01-01", end="2021-1-1")
logchange = []

data['LogChange'] = np.log(data['Close'] / data['Close'].shift(1))
print(data['LogChange'])


csv = pd.read_csv("fear_and_greed_index.csv")
print(csv)
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = yf.download('^VIX',"2020-1-1","2025-1-1")
data['Returns'] = data['Close'].pct_change()
data['Returns'] = data['Returns'].abs()
corr = []
for t in range(1,10):
    data['Returns_t-1'] = data['Returns'].abs().shift(t)
    df_corr = data[['Returns','Returns_t-1']]
    corr_1 = df_corr.corr()
    corr.append(corr_1.loc['Returns','Returns_t-1'])
x = np.arange(1,10,1)
plt.plot(x,corr)
plt.show()    

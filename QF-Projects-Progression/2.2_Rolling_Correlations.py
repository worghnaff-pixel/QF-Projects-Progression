##Asset correlations over time
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

TKS = ('KO',"LMT")
start = "2020-1-1"
end = datetime.now()
data = yf.download(TKS,start,end)['Close']
for i in TKS: data[i] = data[i].rolling(20).mean()

df_SMA = data[['KO','LMT']]
correlation = df_SMA.corr()
print(correlation)
corrs = []
for i in range(20,len(df_SMA['KO'])-20):
    df_SMA = data[['KO','LMT']].iloc[i-20:i]
    curr_corr = df_SMA.corr()
    corrs.append(curr_corr['KO']['LMT'])
plt.plot(corrs)
plt.show()

corr = df_SMA.corr().values
upper = np.triu(corr, k=1)  # k=1 excludes the diagonal
mean_corr = upper[upper != 0].mean()
print(mean_corr)

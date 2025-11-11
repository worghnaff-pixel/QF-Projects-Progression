import yfinance as yf
import numpy as np
import pandas as pd

TCKRS = ('AAPL','^GSPC','MSFT','KO','PEP','TSLA','AMZN','GOOGL','META','NVDA','JPM','V','MA','DIS','NFLX','ADBE','PYPL')
start = "2010-1-1"
end = "2020-1-1"
data = yf.download(TCKRS, start, end)
returns = data['Close'].pct_change()

#for ticker in TCKRS: df[f'Var_{ticker}'] = df[ticker].rolling(30).var()
#print(df['Var_KO'].head(-5))
for i in TCKRS:
    returns[f'Beta_{i}'] = returns[i].rolling(30).cov(returns['^GSPC']) / returns['^GSPC'].rolling(30).var()
    returns[f'Mean_Beta_{i}'] = returns[f'Beta_{i}'].mean()


maxbeta = returns.max(axis=1)


print(maxbeta)
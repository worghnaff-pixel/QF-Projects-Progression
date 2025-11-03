import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

TKS = ('KO','LMT')
start = "2020-1-1"
end = datetime.now()
data = yf.download(TKS,"1980-1-1",datetime.now())['Close']

df = data[['KO','LMT']]
for ticker in TKS: df[ticker] = data[ticker].pct_change()

correlation = df['KO'].rolling(200).corr(df['LMT'])

plt.plot(correlation)
plt.show()
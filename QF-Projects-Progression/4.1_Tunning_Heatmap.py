import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = yf.download('^GSPC', start="2020-01-01", end="2025-01-01")[['Close']]


def equity_calculation(data, s, l):
    df = data.copy()  # make an isolated copy
    df['MAs'] = df['Close'].rolling(s).mean()
    df['MAl'] = df['Close'].rolling(l).mean()
    df['Signal'] = np.where(df['MAs'] > df['MAl'], 1, 0)
    df['Return'] = df['Close'].pct_change()
    df['StratReturn'] = df['Signal'].shift(1) * df['Return']
    df['Equity'] = (1 + df['StratReturn']).cumprod()
    return df['Equity'].iloc[-1]

def tunning(equity_calculation):
    returns = []
    for s in range(50,120,10):
        for l in range(125,401,25):
            equity = equity_calculation(data,s,l)
            returns.append({'Short': s, 'Long':l,'Equity': equity})
    return pd.DataFrame(returns)

final = tunning(equity_calculation)
            
## Plot this shit


pivot = final.pivot(index='Short', columns='Long', values='Equity')

plt.figure(figsize=(8,6))
sns.heatmap(pivot, annot=True, fmt=".2f", cmap="viridis", cbar_kws={'label': 'Final Equity'})
plt.title('SMA Strategy Performance (Short vs Long)')
plt.xlabel('Long Window')
plt.ylabel('Short Window')
plt.show()



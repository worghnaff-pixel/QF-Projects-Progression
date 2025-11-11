import yfinance as yf
import matplotlib.pyplot as plt


data = yf.download('AAPL',"2020-1-1","2020-12-1")

data['Returns'] = data['Close'].pct_change()

data['Mean_10'] = data['Returns'].rolling(10).mean()

data['Var_10'] = data['Returns'].rolling(10).var()
data['Var_50'] = data['Returns'].rolling(50).var()
data['Std_10'] = data['Var_10']**0.5
data['Std_50'] = data['Var_50']**0.5
data['Std_10'].plot()
data['Std_50'].plot()
plt.show()


import numpy as np
import random

n = 5
prices = []
for i in range(0,n):
    prixs = random.random()
    prices.append(prixs)

def daily_returns(prices):
    ret = []
    for i in range(0,len(prices)-1):
        ret.append(prices[i+1]/prices[i])
    return ret
print(prices)
print(daily_returns(prices))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

steps = 100

def path(steps):
    pos = 0
    positions = [0]
    for i in range(0,steps-1):   
        rand = np.random.random()
        if rand > 0.5:
            pos = pos + 1
        else:
            pos = pos -1
        positions.append(pos)
    return positions

data = pd.DataFrame(path(steps), columns=['Position'])
step = []
for i in range(0,len(data['Position'])):
    step.append(i)
data['Step'] = pd.DataFrame(step,columns=['Step'])
data['Buy'] = np.zeros(len(data['Position']))
for i in range(0,len(data['Position'])):
    if data['Position'].iloc[i] > np.sqrt(data['Step'].iloc[i]):
        data['Buy'].iloc[i] = 1
    else: 
        continue

#compute and plot time in buy zone in red over position plot
plt.figure(figsize=(10,6))
plt.step(data['Step'], data['Position'], label='Rademacher Walk', color='blue')
plt.fill_between(data['Step'], data['Position'], where=(data['Buy'] == 1), color='red', alpha=0.5, label='Buy Zone')
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.7)
x = np.log(data['Step'])
y = np.sqrt(data['Step'])
plt.plot(data['Step'], y, color='green', linestyle='--', label='y = √x')
plt.show()



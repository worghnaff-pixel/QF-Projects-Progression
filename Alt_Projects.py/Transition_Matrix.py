import numpy as np

P = np.array([[0.7,0.3],[0.6,0.4]])

N= 3 
C = P
for i in range(0,N):
    C = C @ P
print(C)
import numpy as np 
import random as r
import math as m
import matplotlib.pyplot as plt
def pdf(x,landa):
    y=[]
    for i in range(len(x)):
        y.append(landa**x[i]*np.exp(-landa)/m.factorial(x[i]))
    return y

N=100000
landa=13
k=0
X=[]
for i in range(N):
    U=r.uniform(0,1)
    ra=1
    k=0
    while(ra*U>=m.exp(-landa)):
        ra*=U
        k+=1
        U=r.uniform(0,1)
    X.append(k)
    
fig, ax=plt.subplots(1,1)
X.sort()
ax.hist(X,bins=range(int(max(X))),density=True)
plt.plot(X, pdf(X,landa), color = 'r')
plt.show()

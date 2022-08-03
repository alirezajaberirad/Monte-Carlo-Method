import numpy as np
import math as m
import random
import matplotlib.pyplot as plt

def pdf(x,landa):
    y=[]
    for i in range(len(x)):
        y.append(landa*m.exp(-landa*x[i]))
    return y



landa=2.5 #it refers to lambda, just for simplicity it is named landa
N=100000
U=[]
X=[]
for i in range(N):
    U.append(random.uniform(0,1))
    X.append((-1/landa)*m.log(1-U[i]))


fig, ax=plt.subplots(1,1)
X.sort()
ax.hist(X,bins=100,density=True)
plt.plot(X, pdf(X,landa), color = 'r')
plt.show()

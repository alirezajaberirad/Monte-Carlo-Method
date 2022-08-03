import numpy as np 
import numpy.random as r
import math as m
import matplotlib.pyplot as plt

def pmf(x,p): #Probability mass function
    return ((1-p)**(x-1))*p

p=0.3
N=100000

U=r.uniform(size=N)
X=np.ceil(np.log(1-U)/np.log(1-p))

fig, ax=plt.subplots(1,1)

X.sort()
ax.hist(X,bins=range(int(max(X))),density=True)
plt.plot(X, pmf(X,p), color = 'r')
plt.show()


import numpy as np
import math as m
import random
import matplotlib.pyplot as plt

def pdf(X):
    y=[]
    for i in range(len(X)):
        y.append(1.5*m.sqrt(X[i]))
    return y

N=100000
x=[]
y=[]
acceptedones=[]
function=np.array([])
for i in range(N):
    x.append(random.uniform(0,1))
    y.append(random.uniform(0,1.5))
    if(y[i]<1.5*m.sqrt(x[i])):
        acceptedones.append(x[i])
x.sort()
fig, ax = plt.subplots(1, 1)
ax.hist(acceptedones,bins=100,density=True)
ax.plot(x, pdf(x) , color='r')
plt.show()

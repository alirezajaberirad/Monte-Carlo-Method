import numpy as np 
import numpy.random as r
import math as m
import matplotlib.pyplot as plt

N=100000
x=-1+2*r.uniform(size=N)
y=-1+2*r.uniform(size=N)
inCircle=0
k=0
for i in range(N):
    k=x[i]**2+y[i]**2
    if(k<1):
        inCircle+=1;
print("Pi approximately is= ",4*inCircle/N)
print("Pi - result = ",m.pi-4*inCircle/N)

import numpy as np 
import numpy.random as r
import math as m
import matplotlib.pyplot as plt

N=100000
x=-1+2*r.uniform(size=N) #generates random numbers between -1 and 1 and indicates the horizontal position of a random point inside a 2x2 square
y=-1+2*r.uniform(size=N) #generates random numbers between -1 and 1 and indicates the vertical position of a random point inside a 2x2 square
inCircle=0
k=0
for i in range(N):
    k=x[i]**2+y[i]**2
    if(k<1):
        inCircle+=1;
print("Pi approximately is= ",4*inCircle/N)
print("Pi - result = ",m.pi-4*inCircle/N)

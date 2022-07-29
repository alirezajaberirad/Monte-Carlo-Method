import random
import pygal
import math as m
import numpy as np
import random as r
from scipy.stats import poisson

totalSumOfErrors=0
m=0
BProbability=0
N=10000
for i in range(N):
    numberOfDays=0
    landa=[28,22,18]
    k=18
    sumOfErrors=sum(landa)
    while(k>0):
        ra=r.random()
        k=0
        while(ra >= np.exp(-min(landa))):
            k += 1
            ra = ra * r.random()
        numberOfDays+=1
        sumOfErrors+=k
        landa.append(k)
        landa.pop(0)
    numberOfDays-=1
    m+=numberOfDays
    if(numberOfDays>21):
        BProbability += 1
    totalSumOfErrors+=sumOfErrors
totalSumOfErrors=totalSumOfErrors/N
BProbability=BProbability/N
m=m/N
print("a)Estimated number of days to recognize all errors: ",m)
print("b)Probability of errors which remain after 21 days: ",BProbability)
print("c)Estimated number of errors totally: ",totalSumOfErrors)

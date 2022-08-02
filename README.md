# Monte Carlo Method
 The final project of the Engineering Probability and Statistics course - Fall 2018

## Description
There are 5 tasks included in this project. Each task is explain below.

### Task 1
In this task, the Rejection Method is used to make a random variable generator with the desired distribution function from a standard uniform random variable generator. The desired distribution function in this task is f(x) = 1.5sqrt(x). First, I explained in the report how to generate a random variable with a distribution function of 1.5sqrt(x) using a standard uniform variable generator. I found the equation to achieve this goal. After that, to prove the result of the obtained conversion equation, by generating many uniform random variables and feeding the equation with it, and comparing the output with 1.5sqrt(x), the functionality of the obtained equation has shown to be correct. A picture of a histogram illustrating the results provided in the report file.

### Task 2
In this task, in three steps, the Inverse Transform Method is used to generate 1. exponential random variable with a desired lambda parameter 2. geometric random variable with the desired p parameter, and finally 3.  Poisson random variable with the desired lambda parameter.
A picture of simulating each step with a large number of random numbers and comparing it with its distribution function is provided in the report file.

### Task 3
In this task, I have proved the Box-Muller conversion generates a pair of standard normal random variables that are independent of each other. The proof is given in the report file.

### Task 4
This task is very interesting! As we know, Area of a circle with unit radius is equal to Pi. This circle can be fitted inside a 2x2 square. This mean that area of the circle divided by the area of 2x2 square is equal to Pi/4. Assume x and y are two uniform random numbers between -1 and 1 which indicate a point inside the 2x2 square (the reference point is the mutual center of the circle and square). If sqrt(x^2+y^2) is less than 1, it mean that the point is inside the circle. By generating large number of uniform random numbers between -1 and 1, and counting number of points which are included inside the circle and finally dividing it by the total generated point and multipling it by four, an estimation of Pi number has been achieved.

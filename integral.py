from math import exp

def f(x):
    return x*exp(-x)

intgrl = 0.0
x = 0
xmax = 10
dx = 0.001
while x < xmax:
    intgrl += dx * f(x)
    x += dx
    
print("Integral = ", intgrl, "Error = ", abs(1-intgrl)) 

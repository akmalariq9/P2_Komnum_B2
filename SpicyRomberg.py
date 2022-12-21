import numpy as np
from scipy import integrate

def func(x) :
    return 1/(1+2+x)
calc = integrate.romberg(func, 0, 2, show = True)
print(calc)
# To get the modulus of Gaussian complex numbers
import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
#Factorize Gaussian integer
n = 55 
def gaussian_factorization(n):
    a = 0
    b = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a = i
            b = n // i
    return a, b
print(gaussian_factorization(n))
def gaussian_complex(n):
    a, b = gaussian_factorization(n)
    return complex(a, b)
print(gaussian_complex(n))
def qubit(n):
    a, b = gaussian_factorization(n)
    return np.array([a, b])
print(qubit(n))

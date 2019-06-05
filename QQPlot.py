import numpy as np
from numpy import exp, sqrt, e, pi
import matplotlib.pyplot as plt
from scipy.integrate import quad as integrate
from scipy.special import erf, erfinv

def n(x, m = 0, s = 1):
    return 1 / sqrt(2 * pi * s) * exp(- (x - m)**2 / (2 * s))

def phi(x):
    return 1 / 2 * (1 + erf(x / sqrt(2)))

def phiinv(x):
    return sqrt(2) * erfinv(2*x - 1)

def f(i, n):
    a = 0
    return (i - a)/ (n + 1 - 2 * a)

def Z(x, m, s):
    return (x - m) / s

xi = np.array([2.0, 5.0, 2.5, 2.5, 4.5, 5.5, 3.0, 6.0, 3.0, 2.5])
yi = np.array([2.9, 11.5, 5.1, 7.9, 9.7, 11.0, 8.6, 13.8, 5.7, 2.4])
b = 2.2
eps = np.sort(yi - b*xi)
n = 100
s = 2   
n = len(xi)
m = 0
x = np.linspace(-s, s, n)
xr = np.sort(np.random.normal(m, s, n))

frac = np.zeros(n)
for i in range(n):
    frac[i] = f(i, n)

plt.plot(phiinv(frac), eps / s, ".")
plt.plot(x, phiinv(phi(x)))
plt.show()
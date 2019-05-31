import sympy as sp
import numpy as np
from numpy import e, pi, cos, sin, tan, exp
from numpy import log as ln
from sympy import oo as inf
from sympy import integrate, Function, symbols
from scipy.special import gamma, laguerre, legendre, hermite, chebyc

hbar = 1.05457e-34
h = hbar * 2*pi
kB = 1.38066e-23
c = 2.99792e8
G = 6.672e-11
mElektron = 9.10953e-31
mProton = 1.67262e-27
fineSC = 1 / 137.036
q_e = 1.60218e-19

x, y, z, t = symbols("x, y, z, t")
k, l, m, n = symbols("k, l, m, n", integer=True)
f, g, h = symbols("f, g, h", cls=sp.Function)

def JouleToeV(E):
    return E / q_e

def eVToJoule(E):
    return E * q_e

def factorial(n):
    return gamma(n + 1)


# The sum of f(i) from f(0), to and including n
def sigma(f, i, n):
    s = 0
    for j in range(1, n + 1):
        s += f(j)
    return s

if __name__ == "__main__":
    
    print(sigma(lambda x : x, 0, 5))

import numpy as np
import sympy as sp
from numpy import e, pi, cos, sin, tan, exp, sqrt, arcsin, arccos
from numpy import log as ln
from sympy import oo as inf
from sympy import integrate, Function, symbols
from scipy.special import gamma, laguerre, legendre, hermite, chebyc
from matplotlib import pyplot as plt


# All constants are in SI units if applicable

hbar = 1.05457e-34
h = hbar * 2*pi
kB = 1.38066e-23
c = 2.99792e8
G = 6.672e-11
m_e = 9.10953e-31
m_p = 1.67262e-27
fineSC = 1 / 137.036
q_e = 1.60218e-19 # Charge of electron
eV = q_e # 1 electron volt in jouls
AU = 1.495978707e11 # Astronomical units
ly = 9.4607e15  # light year
m_earth = 5.9722e24  # earth mass
R_earth = 6.371e6


def factorial(n):
    return gamma(n + 1)


# The sum of f(i) from f(0), to and including n
def sigma(f, i, n):
    s = 0
    for j in range(1, n + 1):
        s += f(j)
    return s

# Print scientific format
def sci(a):
    print("{:.3e}".format(a))

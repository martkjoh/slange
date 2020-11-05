import sympy as sp
import numpy as np
from numpy import e, pi
from scipy.special import factorial, comb as choose
from scipy.integrate import quad as integrate
from matplotlib import pyplot as plt
from sympy.interactive import printing

printing.init_printing()

hbar = 1.05457e-34
h = hbar * 2*pi
kB = 1.38066e-23
c = 2.99792e8
G = 6.672e-11
mElektron = 9.10953e-31
mProton = 1.67262e-27
fineSC = 1 / 137.036


def JouleToeV(E):
    return E / 1.60218e-19

def eVToJoule(E):
    return E * 1.60218e-19

def binomialDist(x, n, p):
    return choose(n, x) * p**x * (1 - p)**(n - x)

def hypergeometric(n, k, N, K):
    return choose(n, k) * choose(N - n, K - k) / choose(N, n)

def plot(f, xs):
    f = sp.lambdify(x, f, modules=[np, sp])
    plt.plot(xs, f(xs))
    plt.show()

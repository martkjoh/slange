import sympy as sp
import numpy as np
from numpy import e, pi
from sympy import oo as inf
from sympy import integrate, Function, symbols

hbar = 1.05457e-34
h = hbar * 2*pi
kB = 1.38066e-23
c = 2.99792e8
G = 6.672e-11
mElektron = 9.10953e-31
mProton = 1.67262e-27
fineSC = 1 / 137.036

x, y, z, t = symbols("x, y, z, t")
k, l, m, n = symbols("k, l, m, n", integer=True)
f, g, h = symbols("f, g, h", cls=sp.Function)

def JouleToeV(E):
    return E / 1.60218e-19

def eVToJoule(E):
    return E * 1.60218e-19


import numpy as np
from numpy import exp, sqrt, log, cos, sin, pi


global antall
antall = 0

def f(x):
    global antall
    antall += 1
    return sin(x**2)

def s(a, b, fa, fb):
    return (b - a) * (fa + fb) / 2

def adaptivTrapes(f, a, b, a0, b0, fa, fb, tol):
    c = (b + a) / 2
    fc = f(c)
    Sab = s(a, b, fa, fb)
    Sac = s(a, c, fa, fc)
    Scb = s(c, b, fc, fb)
    if (1/3 * abs(Sab - Sac - Scb)) < ((b - a) / (b0 - a0)) * tol:
        return Sac + Scb

    else:
        return adaptivTrapes(f, a, c, a0, b0, fa, fc, tol) + adaptivTrapes(f, c, b, a0, b0, fc, fb, tol)


a = 0
b = 5
fa = f(a)
fb = f(b)
print(adaptivTrapes(f, a, b, a, b, fa, fb, 1e-7))
print(antall)

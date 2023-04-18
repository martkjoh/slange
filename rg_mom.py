import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad as i


plt.rc("font", family="serif", size=16)
plt.rc("mathtext", fontset="cm")
plt.rc("lines", lw=2)
plt.rc("axes", grid=True)


# Mass squared / temperature
r=1e-1

def f(x, y):
    return 1 / (x**2 + r) / (y**2 + r) / ((x - y)**2 + r)

def F0(l):
    return i(f, 0, l, 0, l)[0]
F = np.vectorize(F0)

dl = np.logspace(-.5, -3, 100)
dF =  F(1) - F(1 - dl)
plt.loglog(dl, dF, 'r', label="$F(1) - F(1 - \\delta \ell) $")
plt.loglog(dl, dF[0]*dl, 'k--', label="$\\propto \\delta \ell$")

plt.xlabel("$\\delta \\ell$")
plt.ylabel("$\\Delta F$")

plt.legend()
plt.show()

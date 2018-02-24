import numpy as np
from matplotlib import pyplot as plt
from main.numerikk import *

e = 1.602e-19
m = 9.1e-31
d = 0.8
Vs = (20, 40, 60)
legends = ("$U = 20 gauss$", "$U = 40 gauss$", "$U = 60 gauss$")
r = d/2


def r(B, V):
    B = B * 1e-4 # gauss / tesla
    return 1 / B * np.sqrt((2 * V / (e / m)))

def B_av_I(I):
    return (7.25*I + 0.24) / 1e4


def eperm(V, I, d):
    return 2 * V / B_av_I(I)**2 / (d/2)**2


fig, ax = plt.subplots(1, 1)
B = np.linspace(0, 15, 1000)
for V in Vs:
    ax.loglog(B, r(B, V))
ax.legend(legends)
ax.plot(B, B/B * 0.04)
ax.set_xlabel("$B[gauss]$")
ax.set_ylabel("$r[m]$")
plt.show()

gauss = gauss_usikkerhetsforplantning(eperm, (200, 1.51, 0.085), (1, 0.01, 0.005))
print(gauss/eperm(*(200, 1.51, 0.085)))
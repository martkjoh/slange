import numpy as np
from numpy import exp, log, sin, cos, sqrt, e, pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as anim

def fourier(x, fx):
    delta = pi / (x[-1] - x[0])
    return exp(- 1j * np.outer(x, x) * delta) @ fx * delta / len(x)

def f(x):
    m = 0
    s = 1
    return 1 / sqrt(2*pi) * exp(-x**2 / 2)

a = 1
n = 4000
x = np.linspace(-a, a, n)
fx = f(x)
fHat = fourier(x, fx)

fig, ax = plt.subplots(1, 2)
ax[0].plot(x, fx)
ax[1].plot(x, fHat.real)
plt.show()

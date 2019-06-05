import numpy as np
from numpy import exp, log, sin, cos, sqrt
from numpy import e, pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as anim

def naive(x, fx):
    return (exp(- 2 * pi * 1j * np.outer(x, x)) @ fx)

def f(x, n):
    m = 0
    s = 0.1
    xn = np.zeros(n)
    xe = 1 / sqrt(2 * pi * s) * exp(-(x - m)**2 / 2 / s)
    return np.concatenate([xn, xe[n:-n], xn])

a = 15
n = 2000
x = np.linspace(-a, a, n)

fig, ax = plt.subplots(1, 2)

def animate(n):
    n += 950
    ax[0].cla()
    ax[1].cla()
    fx = f(x, n)
    l = ax[0].plot(x, fx)
    l += ax[1].plot(x, (naive(x, fx)))
    return l

a = anim(fig, animate, blit = True)
plt.show()
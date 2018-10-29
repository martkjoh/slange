from matplotlib import pyplot as plt
from matplotlib import animation
from math import *
import numpy as np


fig = plt.figure()
ax = plt.subplot()


def make_blob(n, xrange, yrange, form):
    x = np.zeros((n, n))
    for i in range(n):
        x[i] = np.linspace(xrange[0], xrange[1],  n) # The range of the real values of the plot

    y = np.zeros((n, n))
    for i in range(n):
        y[i] = form(x[i], (i / (n - 1)*2 - 1)*yrange)

    return x + 1j*y

frames = 40
form = lambda x, i: (1)*(i)
z1 = make_blob(100, (-2, 2), 2, form)

def animate(n):
    ax.cla()
    t = n * 0.05
    deg = floor(t) + 1
    t -= deg
    z = z1**deg
    w = z1**(deg + 1)
    artist = ax.contour(z1.real, z1.imag, w.imag * t + z.imag * (1 - t), np.linspace(-5, 5, 31), colors="blue").collections
    return artist


anim = animation.FuncAnimation(fig, animate, interval=0.01, frames=frames, blit=True)

plt.show()

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.colors import LogNorm
from matplotlib.animation import FuncAnimation as FA

plt.rcParams['mathtext.fontset'] = 'cm'
font = {'family' : 'serif', 
        'size': 20}
plt.rc('font', **font)
plt.rc('lines', lw=2)

def line_plot():
    x = np.linspace(-10, 10, 1000)

    fig, ax = plt.subplots()
    ax.plot(x, x ** 2)

    ax.set_xlabel("$x /  [x] = \mathrm{m \, s^{-1}}$")
    ax.set_ylabel("$f(x) /  [f] = \mathrm{J}$")

    plt.show()

def histogram():
    x = np.random.randn(10000)
    fig, ax = plt.subplots()
    ax.hist(x, bins=100, density=True)

    plt.show()

def histogram2D():
    n = 1_000
    x = np.random.randn(2, n)

    fig, ax = plt.subplots()
    a = ax.hist2d(x[0], x[1], bins=20, cmin=1)
    fig.colorbar(a[3])
    
    plt.show()

def surface_3D():
    x, y = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1.5, 100))

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(
        x, y, x** 2*(x** 2 - y** 2)** 2,
        cmap=cm.viridis
        )
    fig.colorbar(surf)
    
    plt.show()

def animate_line():
    fig, ax = plt.subplots()
    x = np.linspace(-1, 1, 1000)
    f = lambda x, t, s: 1/np.sqrt(4*np.pi * s  *t) * np.exp(-x**2 / (4*s*t))
    dt = 0.001; s = 0.1
    l = [ax.plot(x, f(x, dt, s))[0], ]

    def anim(n):
        l[0].set_data(x, f(x, (n+1)*dt, s))
        return l

    a = FA(fig, anim, blit=True, interval=10)
    a.save("filename.mp4")


surface_3D()

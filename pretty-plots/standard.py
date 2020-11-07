import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.colors import LogNorm

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
    x = np.random.randn(n, n)

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


surface_3D()

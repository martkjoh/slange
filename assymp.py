import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.colors import LogNorm
from matplotlib.animation import FuncAnimation as FA

plt.rc("font", family="serif", size=16)
plt.rc("mathtext", fontset="cm")
plt.rc("lines", lw=2)
plt.rc("axes", grid=True)


f = lambda x : 1 / (1 + x)
g = lambda x, n : np.sum([x**m for m in range(n)])

n = np.array([i for i in range(10)])
x = 1.1
gl = [g(x, m) for m in n]

plt.plot(n, f(x) * np.ones_like(n))
plt.plot(n, gl, '.')
plt.show()

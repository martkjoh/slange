from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
from math import *
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(dpi=400)
ax = fig.gca(projection='3d')
ax.set_zlim(0,10)

x = np.arange(-2, 2, 0.015)
y = np.arange(-2, 2, 0.015)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
E = np.divide(1, r**2)

for a in range(len(E)):
    for b in range(len(E[a])):
        if E[a][b] > 20:
            E[a][b] = 20

surf = ax.plot_surface(x, y, E)

plt.show()
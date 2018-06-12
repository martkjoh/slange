from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def f(x, y):
    return 2 * np.sqrt(x**2 + y**2)


fig = plt.figure()
ax = Axes3D(fig)
cut_top = True
cut_bottom = True
contour = False
height = 10

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
x, y = np.meshgrid(x, y)

z = f(x, y)

z_min, z_max = min([min(x) for x in z]),  max([max(x) for x in z])

if cut_top:
    for a in range(len(z)):
        for b in range(len(z[a])):
            if z[a][b] > height:
                z[a][b] = height
    z_max = height

if cut_bottom:
    for a in range(len(z)):
        for b in range(len(z[a])):
            if z[a][b] < -height:
                z[a][b] = -height
    z_min = -height

ax.set_zlim(z_min, z_max)
ax.plot_surface(x, y, z, cmap="viridis")

if contour:
    z_min -= 1
    bottom = ax.contour(x, y, z, zdir='z', cmap="viridis", offset=z_min)

plt.show()

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def f(x, y):
    return (1 - 2 * x * y) / (x**2 + y**2)


fig = plt.figure()
ax = Axes3D(fig)
cut_top = True
cut_bottom = False
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

b = 0
for a in z:
    b = np.append(b, min(a))
print(min(b))
print(f(np.sqrt(2), np.sqrt(2)))

ax.set_zlim(z_min, z_max)
surf = ax.plot_surface(x, y, z, cmap="plasma")

plt.show()

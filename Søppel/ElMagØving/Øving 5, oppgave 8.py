from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def V_a(x, z):
  return z/(z**2 + x**2)**(3/2)


def V(x, z):
  return (1 / np.sqrt(x**2 + (z - 1/2)**2) - 1 / np.sqrt(x**2 + (z + 1/2)**2))


cut_top = True
cut_bottom = True
contour = False
height = 1
width = 1


x = np.linspace(-width, width, 1000)
y = np.linspace(-width, width, 1000)
x, y = np.meshgrid(x, y)

funcs = (V, V_a, lambda x, y: abs((V(x, y) - V_a(x, y))/V_a(x, y)))

for f in funcs:
  fig = plt.figure()
  ax = Axes3D(fig)
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  ax.set_zlabel("z")

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


plt.show()

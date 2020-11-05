import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1.5, 100)
x, y = np.meshgrid(x, y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, x ** 2*(x ** 2 - y ** 2)** 2)

plt.show()

import numpy as np
from numpy import pi, cos, sin
import matplotlib.pyplot as plt

from matplotlib import cm


r = np.linspace(0, 1.26, 100)
theta = np.linspace(0, 2*pi, 100)
r, theta = np.meshgrid(r, theta)


ax = plt.axes(projection='3d')
a=2
surf = ax.plot_surface(r*cos(theta), r*sin(theta), (1-r**2)**2/a, cmap=cm.cool, alpha=1, zorder=1)
# surf = ax.plot_wireframe(r*cos(theta), r*sin(theta), (1-r**2)**2/a, lw=.4, color='black', zorder=10, alpha=.2)


ax.set_zlim3d(0, 1)
# ax.set_box_aspect((1, 1, 1))
plt.show()

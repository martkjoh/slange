import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1.5, 100)
x, y = np.meshgrid(x, y)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(
    x, y, x** 2*(x** 2 - y** 2)** 2,
    cmap=cm.viridis
    )

plt.show()

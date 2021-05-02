import numpy as np
import matplotlib.pyplot as plt


# One day
# https://github.com/nordam/ComputationalPhysics/blob/master/Notebooks/12%20-%20Partial%20Differential%20Equations.ipynb

N = 101
x = np.linspace(-1, 1, N)
y = np.linspace(-1, 1, N)
x, y = np.meshgrid(x, y)

v = np.array([-x, y])

plt.quiver(x, y, *v)
plt.show()
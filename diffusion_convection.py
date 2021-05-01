import numpy as np
import matplotlib.pyplot as plt


N = 101
x = np.linspace(-1, 1, N)
y = np.linspace(-1, 1, N)
x, y = np.meshgrid(x, y)

v = np.array([-x, y])

plt.quiver(x, y, *v)
plt.show()
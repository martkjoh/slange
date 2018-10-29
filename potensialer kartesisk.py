from matplotlib import pyplot as plt
import numpy as np
from numpy import e, pi, sin, cos, arctan


k = 0.1
x = np.linspace(-1, 1, 100)
y = np.linspace(-0.5, 0.5, 100)
x, y, = np.meshgrid(x, y)

def phi(x, y):
    return k * arctan(y/x)

plt.contour(x, y, phi(x, y), np.linspace(-1, 1, 100))
plt.show()

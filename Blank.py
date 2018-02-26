from matplotlib import pyplot as plt
import numpy as np

def f(x, y):
    return 1 / np.sqrt(x**2 + (y - 1/2)**2) - 1 / np.sqrt(x**2 + (y + 1/2)**2)


x = np.linspace(-2, 2, 1000)
fig, ax = plt.subplots(1)
ax.plot(x, f(0, x))
plt.show()

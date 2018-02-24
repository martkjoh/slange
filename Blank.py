from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 100, 100)
y = x**2
z = np.sqrt(x)

fig = plt.figure()
ax = fig.add_subplot(121)
ax.plot(x, y)
ax = fig.add_subplot(122)
ax.plot(x, z)

plt.show()

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm

plt.rc("font", family="serif", size=16)
plt.rc("mathtext", fontset="cm")
plt.rc("lines", lw=2)
plt.rc("axes", grid=True)


def E(m, t, u, v):
    return t*m**2/2 + u*m**4 + v*m**6

m = np.linspace(-1, 1)
N = 10
ts = np.linspace(-1, 1, N)

for i, t in enumerate(ts):
    plt.plot(m, E(m, t, 1, 1), color = cm.viridis(i/N))

plt.show()

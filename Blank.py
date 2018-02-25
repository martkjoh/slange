from matplotlib import pyplot as plt
import numpy as np


def polar_transform(r, theta):
    return r * np.cos(theta), r * np.sin(theta)


def r(theta):
    return 6 * np.cos(theta)


def r_2(theta):
    return 5 / np.cos(theta)


fig, ax = plt.subplots(1)
ax.set_xlim(-1, 8)
ax.set_ylim(-5, 5)
theta = np.linspace(-np.arccos(np.sqrt(5/6)), np.arccos(np.sqrt(5/6)), 1000)
plt.plot(*polar_transform(r(theta), theta))
plt.plot(*polar_transform(r_2(theta), theta))
plt.show()

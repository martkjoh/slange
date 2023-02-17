import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.colors import LogNorm
from matplotlib.animation import FuncAnimation as FA

plt.rc("font", family="serif", size=16)
plt.rc("mathtext", fontset="cm")
plt.rc("lines", lw=2)
plt.rc("axes", grid=True)


def drdl(u,r):
    return 2*r + u - u*r

eps=1
def dudl(u,r):
    return (eps - 3*u)*u

u = np.linspace(0, .5)
r = np.linspace(-.5, .5)

u, r = np.meshgrid(u, r)
v, w = dudl(u, r), drdl(u, r)

fig, ax = plt.subplots()
ax.streamplot(u, r, v, w,  density=2., linewidth=1)
ax.set_xlabel("$u$")
ax.set_ylabel("$r$")

plt.show()


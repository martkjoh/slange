from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def r(t):
    return (5 * 3 * np.cos(t), 5 * np.sin(t), 5 * np.cos(t))


def generate(t):
    return r(t)


def animate(n):
    n = n * speed
    ax.cla()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim(-15, 15)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)
    t = np.linspace(range[0], n, space_res*n)
    xs, ys, zs = generate(t)
    line = ax.plot(xs, ys, zs)
    #ax.legend()
    return line


fig = plt.figure()
ax = Axes3D(fig)

range = [0, 2 * np.pi]
speed = 0.05
space_res = 100

anim = animation.FuncAnimation(fig, animate, interval=1, blit=False, frames=int(range[1]/speed*1.02))

plt.show()

from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def x(t):
    return np.sin(7*np.pi*t)


def y(t):
    return np.cos(5*np.pi*t)



def z(t):
    return np.sin(np.pi*t)

def generate(t):
    return x(t), y(t), z(t)


def animate(n):
    n = n * speed
    ax.cla()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    t = np.linspace(range[0], n, space_res*n)
    xs, ys, zs = generate(t)
    line = ax.plot(xs, ys, zs)
    ax.legend()
    return line


fig = plt.figure()
ax = Axes3D(fig)

range = [0, 2]
speed = 0.005
space_res = 1000

anim = animation.FuncAnimation(fig, animate, interval=1, blit=True, frames=int(range[1]/speed*1.02))

plt.show()

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

v_init = 1
x_init = 1
x_range = np.array([0, 1])
centre = np.array([0.5, 0.5])
dt = 0.01
N = 100

c1 = 0.2        # Attraction parametre
c2 = 0.05       # Alignment factor
c3 = 0.01       # Centering factor
c4 = 0.05**2    # Size
c5 = -0.01      # Avoidance
c6 = 1.**2      # Speed limit

def init_boids():
    return np.random.random((2, 2, N)) * v_init

def step(boids):
    outside = np.logical_or(boids[0]<x_range[0], boids[0]>x_range[1])
    boids[1, outside] = -1*boids[1, outside]
    # boids[0, 0, outside[0]] += c3*(boids[1, 0, outside[0]] - centre[0])
    # boids[0, 1, outside[1]] += c3*(boids[1, 1, outside[1]] - centre[1])
    boids[0] += boids[1]*dt

def congregate(boids):
    ave_x = np.einsum("ij -> i", boids[0])
    diff = (ave_x - boids[0].T).T
    boids[1] += c1 * diff

def align(boids):
    ave_v = np.einsum("ij -> i", boids[1]) / N
    diff = (ave_v - boids[0].T).T
    boids[1] = (c2 * diff + boids[1])

def repell(boids):
    for i in range(N):
        diff = (boids[0].T - boids[0, : , i]).T
        near = np.einsum("ij -> j", diff**2) < c4
        near[i] = False
        vec = np.einsum("ij -> i", diff[:, near])
        boids[1, :, i] += c5*vec

def speed_limit(boids):
    speeds = np.einsum("ij -> j", boids[1]**2)
    too_fast = speeds>c6
    boids[1, 0, too_fast] *= c6 / speeds[too_fast]
    boids[1, 1, too_fast] *= c6 / speeds[too_fast]


def anim(n, lines, boids):
    congregate(boids)
    align(boids)
    repell(boids)
    speed_limit(boids)
    step(boids)
    lines[0].set_data(*boids[0])
    return lines


boids = init_boids()

fig, ax = plt.subplots()
ax.set_xlim(*x_range)
ax.set_ylim(*x_range)
lines = [ax.plot(*boids[0], ".")[0]]

anim = FuncAnimation(fig, anim, fargs=(lines, boids), blit=True, interval=10)

plt.show()

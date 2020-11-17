import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

v_init = 1
x_init = 1
x_range = np.array([0, 1])
centre = np.array([0.5, 0.5])
dt = 0.01
N = 100

# Attraction parametre
c1 = 0.5
# Alignment factor
c2 = 0.2
# Centering factor
c3 = 0.1
# Size
c4 = 0.01
# Avoidance
c5 = 0.1
# Speed limit
c6 = 1

def init_boids():
    x = np.random.random((2, N))
    v = (np.random.random((2, N)) - 1/2) * 2 * v_init
    return np.array([x, v])

def step(boids):
    boids[0] = boids[0] % 1
    boids[0] += boids[1]*dt

def congregate(boids):
    ave_x = np.einsum("ij -> i", boids[0]) / N
    diff = (ave_x - boids[0].T).T
    boids[1] += c1 * diff

def align(boids):
    ave_v = np.einsum("ij -> i", boids[1]) / N
    diff = (ave_v - boids[1].T).T
    new_dir = (c2 * diff + boids[1])
    new_dir *= 1 / np.sqrt(np.einsum("ij -> j", new_dir**2))
    speed = np.sqrt(np.einsum("ij -> j", boids[1]**2))
    boids[1] = new_dir * speed

def repell(boids):
    for i in range(N):
        diff = (boids[0].T - boids[0, : , i]).T
        near = np.einsum("ij -> j", diff**2) < c4**2
        near[i] = False
        vec = np.einsum("ij -> i", diff[:, near])
        boids[1, :, i] += c5*vec

def speed_limit(boids):
    speeds = np.einsum("ij -> j", boids[1]**2)
    too_fast = speeds > c6**2
    boids[1, 0, too_fast] *= c6**2 / speeds[too_fast]
    boids[1, 1, too_fast] *= c6**2 / speeds[too_fast]


def anim(n, lines, boids):
    congregate(boids)
    align(boids)
    repell(boids)
    # speed_limit(boids)
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

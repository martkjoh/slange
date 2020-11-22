import numpy as np
from numpy import sqrt, pi, sin, cos
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as anim


dt = 0.01
T = 500
N = int(T / dt)

# Initial conditions
n = 3
R = np.linspace(1, 4, n)
theta = np.linspace(0, pi, n)
m = np.diag(np.ones_like(R))
for i in range(n):
    for j in range(i + 1, n):
        m[i, j] = 0.04
x0 = np.empty((n, 2, 2))
for i in range(n):
    x0[i] = np.array([
        [R[i]*cos(theta[i]),            R[i]*sin(theta[i])],
        [-1/sqrt(R[i])*sin(theta[i]),   1/sqrt(R[i])*cos(theta[i])]
    ])

def acc(x):
    a = np.zeros((n, 2))
    for i in range(n):
        a[i] += - m[i, i] * x[i] / (x[i, 0]** 2 + x[i, 1]** 2)**(3/2)
        for j in range(i+1, n):
            r2_rel = (x[i, 0] - x[j, 0])** 2 + (x[i, 1] - x[j, 1])** 2
            dist = np.array([x[i, 0] - x[j, 0], x[i, 1] - x[j, 1]])
            a[i] -= m[i, j] * dist / r2_rel**(3/2)
            a[j] += m[i, j] * dist / r2_rel**(3/2)
    return a

def f(x):
    a = acc(x[:, 0])
    b = np.empty((n, 2, 2))
    for i in range(n):
        b[i] = np.array([x[i, 1], a[i]])
    return b

def potential_energy(x):
    E = np.zeros((len(x), n))
    for i in range(n):
        E[:, i] += - m[i, i] / (x[:, i, 0, 0]** 2 + x[:, i, 0, 1]** 2)**(1/2)
        for j in range(i+1, n):
            r2_rel = (x[:, i, 0, 0] - x[:, j, 0, 0])** 2 + (x[:, i, 0, 1] - x[:, j, 0, 1])** 2
            E[:, i] -= m[i, j] / r2_rel**(1/2)
            E[:, j] -= m[i, j] / r2_rel**(1/2)
    return np.einsum("tn -> t", E)

def kinetic_energy(x):
    return np.einsum("tn -> t", m[i, i] * (x[:, :, 1, 0]**2 + x[:, :, 1, 1]**2) / 2)

def RK4step(x, t, dt):
    k1 = f(x[t]) * dt
    k2 = f(x[t] + 1 / 2 * k1) * dt
    k3 = f(x[t] + 1 / 2 * k2) * dt
    k4 = f(x[t] + k3)  * dt
    x[t + 1] = x[t] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    
def simulate_orbit(x0, dt, T):
    # x[t, n, i, j] = step t of planet n's i'th diff. of the j'th coord.
    x = np.empty((N, n, 2, 2))
    x[0] = x0
    for t in range(N-1):
        RK4step(x, t, dt)
    return x

def plot_orb(x):
    fig, ax = plt.subplots()
    for i in range(n):
        ax.plot(x[:, i, 0, 0], x[:, i, 0, 1])
        ax.plot(x[-1, i, 0, 0], x[-1, i, 0, 1], "ok")
    ax.plot(0, 0, "oy")
    plt.show()

def plot_E(x):
    PE = potential_energy(x)
    KE = kinetic_energy(x)
    ts = np.linspace(0, T, N)
    fig, ax = plt.subplots()
    ax.plot(ts, PE)
    ax.plot(ts, KE)
    ax.plot(ts, KE + PE)
    plt.show()


def anim_orb(x):
    fig, ax = plt.subplots()
    R_max = np.max(R) +1
    line = [ax.plot([], [])[0] for _ in range(n)]
    line.extend([ax.plot([], [], "ok")[0] for _ in range(n)])
    line.append(ax.plot([], [], "oy")[0])
    ax.set_ylim((-R_max, R_max))
    ax.set_xlim((-R_max, R_max))
    frameskip = 12
    tail_length = int(1 / dt)

    def animate(frame):
        frame = frame * frameskip + tail_length
        total = []
        for i in range(n):
            xi = x[frame-tail_length:frame, i, 0]
            line[i].set_data(xi[:, 0], xi[:, 1])
            line[n + i].set_data(xi[-1, 0], xi[-1, 1])
        line[-1].set_data(0, 0)
        return line
        
    a = anim(fig, animate, interval=1)
    plt.show()

x = simulate_orbit(x0, dt, T)
plot_orb(x)
plot_E(x)
anim_orb(x)

import numpy as np
import matplotlib.pyplot as plt

from scipy import sparse
from scipy.sparse.linalg import eigs as sparse_eig
from scipy.linalg import sqrtm
from matplotlib import cm
from matplotlib.animation import FuncAnimation as FA

Nx = 100
Nt = 1000
dt = 0.01

daig_0 = -2 * np.ones(Nx)
diag_1 = np.ones(Nx - 1)

# Single derivative
Dx = sparse.diags(
        [-(1 / 2), -(1/2)*diag_1, -(1/2)*diag_1, -(1 / 2)],
        [-(Nx - 1), -1, 1, (Nx - 1)]
    ).toarray()

# Double derivative
D2x = sparse.diags(
        [1, diag_1, daig_0, diag_1, 1],
        [-(Nx - 1), -1, 0, 1, (Nx - 1)]
    ).toarray()

def get_inital(f0, derivs):
    f = np.empty((Nt, Nx, derivs), dtype="complex128")
    f[0] = f0
    return f
    
def time_step(f, A, i, g, dt, order, steps):
    f_new = f[i - 1]
    for _ in range(steps):
        f_new[:, 0] += g(f_new[:, -1], A[i-1]) * dt
        for j in range(1, order):
            f_new[:, j] += f_new[:, j-1] * dt
    f[i] = f_new

def plot_field_surface(f):
    x, t = np.meshgrid(np.linspace(0, 1, Nx), np.linspace(0, 1, Nt))

    fig, ax = plt.subplots(1,figsize=(20, 10), subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(x, t, f.real[:, :, -1], cmap=cm.viridis)
    fig.colorbar(surf)
    
    plt.show()

def animate_field_line(f, A):
    fig, ax = plt.subplots(figsize=(20, 10))
    x = np.linspace(0, 1, Nx)
    l = [ax.plot([], [])[0] for i in range(2)]
    ax.set_xlim(0, 1)
    ax.set_ylim(-np.max(np.abs(f)), np.max(np.abs(f)))

    def anim(n):
        l[0].set_data(x, f[n,:, -1].real)
        l[1].set_data(x, A[n])
        return l

    a = FA(fig, anim,  interval=100, frames=Nt)
    plt.show()


# Equations of motion for different fields

def heat_eq(f, A, c=2):
    return c * D2x @ f

def wave_eq(f, A, c=1):
    return c * D2x @ f

def KG(f, A, m=0.2):
    return (D2x - m ** 2 * np.identity(Nx)) @ f

# Gaugeing is fixed to A_0 = 0, so A is in effect a scalar
def KG_interaction(f, A, m=0.2, q=0.1):
    interaction = q/2 * (Dx @ f) * A - q**2 * f * A**2
    return (D2x - m ** 2 * np.identity(Nx)) @ f + interaction


def KG_energy(f, m=0.2):
    # Need the time derivative.... Kachelriess 7.4
    return np.abs(D2x @ f)**2 + 1/2 * np.abs(f)**2

def mexican_hat(f, m=1, l=0.01):
    return D2x @ f - m**2 * f + 4 * l * f**3


def simulate_field(g, A, f0, order, steps):
    f = get_inital(f0, order)
    for i in range(1, Nt):
        time_step(f, A, i, g, dt, order, steps)

    
    # animate_field_line(f, A)
    # plot_field_surface(f)


# TODO: add energy plot, vector-equations(?)


x = np.linspace(0, 1, Nx)
gaussian = np.exp(-(x - 1 / 2)** 2 * 200)
shape = np.exp(1j*x * (2*np.pi))

# f0 = np.array([gaussian,]).T
# simulate_field(heat_eq, f0, 1, 50)

# f0 = np.array([np.zeros(Nx), gaussian,]).T
# simulate_field(wave_eq, f0, 2, 100)

# f0 = np.array([np.zeros(Nx), gaussian,]).T
# simulate_field(KG, f0, 2, 150)

# f0 = np.array([np.zeros(Nx), shape, ]).T
# simulate_field(mexican_hat, f0, 2, 100)

f0 = np.array([gaussian, np.zeros(Nx)]).T
x, t = np.meshgrid(np.linspace(0, 1, Nx), np.linspace(0, 1, Nt))

ws = [45, 47, 50, 52, 55]

for w in ws:
    A = np.sin((x - w * t)* 2*np.pi)
    simulate_field(KG_interaction, A, f0, 2, 100)


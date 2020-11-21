import numpy as np
import matplotlib.pyplot as plt

from scipy import sparse
from scipy.sparse.linalg import eigs as sparse_eig
from scipy.linalg import sqrtm
from matplotlib import cm
from matplotlib.animation import FuncAnimation as FA

Nx = 100
Nt = 500
dt = 0.01

def get_D2x():
    """ 3 point stencil for second derivative with periodic bc's """
    daig_0 = -2 * np.ones(Nx)
    diag_1 = np.ones(Nx - 1)
    return sparse.diags(
        [1, diag_1, daig_0, diag_1, 1],
        [-(Nx - 1), -1, 0, 1, (Nx - 1)]
        ).toarray()

def get_Dx():
    """ 2 point stencil for first derivative with periodic bc's """
    diag_1 = -(1 / 2) * np.ones(Nx-1)
    return sparse.diags(
        [-(1 / 2), diag_1, diag_1, -(1 / 2)],
        [-(Nx - 1), -1, 1, (Nx - 1)]
        ).toarray()

def get_inital(f0, derivs):
    f = np.empty((Nt, Nx, derivs), dtype="complex128")
    f[0] = f0
    return f

def time_step(f, i, Dt, dt, order, steps):
    f_new = f[i - 1]
    for _ in range(steps):
        f_new[:, 0] += (Dt @ f_new[:, -1]) * dt
        for j in range(1, order):
            f_new[:, j] += f_new[:, j-1] * dt
    f[i] = f_new
    
def time_step2(f, i, g, dt, order, steps):
    f_new = f[i - 1]
    for _ in range(steps):
        f_new[:, 0] += g(f_new[:, -1]) * dt
        for j in range(1, order):
            f_new[:, j] += f_new[:, j-1] * dt
    f[i] = f_new

def plot_field_surface(f):
    x, t = np.meshgrid(np.linspace(0, 1, Nx), np.linspace(0, 1, Nt))

    fig, ax = plt.subplots(1, subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(x, t, f.real[:, :, -1], cmap=cm.viridis)
    fig.colorbar(surf)
    
    plt.show()

def animate_field_line(f):
    fig, ax = plt.subplots()
    x = np.linspace(0, 1, Nx)
    l = [ax.plot([], [])[0]] * 2
    ax.set_xlim(0, 1)
    ax.set_ylim(np.min(f.real), np.max(f.real))

    def anim(n):
        l[0].set_data(x, f[n, :, -1].real)
        return l

    a = FA(fig, anim,  interval=100, frames=Nt)
    plt.show()


# Equations of motion for different fields

def get_heat_eq(c=20):
    return c * get_D2x()

def get_wave_eq(c=1):
    return c * get_D2x()

def get_KG(m=0.2):
    return get_D2x() - m ** 2 * np.identity(Nx)

def mexican_hat(f, m=1, l=0.01):
    D2x = get_D2x()
    return D2x @ f - m**2 * f + 4 * l * f**3


def simulate_field(get_Dt, f0, order, steps):
    f = get_inital(f0, order)
    Dt = get_Dt(Nx)

    for i in range(1, Nt):
        time_step(f, i, Dt, dt, order, steps)
    
    animate_field_line(f)

def simulate_field2(g, f0, order, steps):
    f = get_inital(f0, order)

    for i in range(1, Nt):
        time_step2(f, i, g, dt, order, steps)
    
    animate_field_line(f)


# TODO: add coupling term, non-linear eqs. of motion, 
# TODO: make the list arbitrary long in t-direction, vector-equations(?)


x = np.linspace(0, 1, Nx)
gaussian = np.exp(-(x - 1 / 2)** 2 * 200)
shape = np.sin(x * (2*np.pi))

# f0 = np.array([gaussian,]).T
# simulate_field(N, get_heat_eq, f0, 1, 50)

# f0 = np.array([np.zeros(N), gaussian,]).T
# simulate_field(N, get_wave_eq, f0, 2, 100)

# f0 = np.array([np.zeros(N), gaussian,]).T
# simulate_field(N, get_KG, f0, 2, 150)

f0 = np.array([np.zeros(Nx), shape, ]).T
simulate_field2(mexican_hat, f0, 2, 100)

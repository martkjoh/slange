import numpy as np
import matplotlib.pyplot as plt

from scipy import sparse
from scipy.sparse.linalg import eigs as sparse_eig
from scipy.linalg import sqrtm
from matplotlib import cm


def get_D2x(N):
    """ 3 point stencil for second derivative with periodic bc's """
    daig_0 = -2 * np.ones(N)
    diag_1 = np.ones(N - 1)
    return sparse.diags(
        [1, diag_1, daig_0, diag_1, 1],
        [-(N - 1), -1, 0, 1, (N - 1)]
        ).toarray()

def get_Dx(N):
    """ 2 point stencil for first derivative with periodic bc's """
    diag_1 = -(1 / 2) * np.ones(N-1)
    return sparse.diags(
        [-(1 / 2), diag_1, diag_1, -(1 / 2)],
        [-(N - 1), -1, 1, (N - 1)]
        ).toarray()

def get_inital(N, f0, derivs):
    f = np.empty((N, N, derivs), dtype="complex128")
    f[0] = f0
    return f

def time_step(f, i, Dt, dt, order, steps):
    f_new = f[i - 1]
    for _ in range(steps):
        f_new[:, 0] += (Dt @ f_new[:, -1]) * dt
        for j in range(1, order):
            f_new[:, j] += f_new[:, j-1] * dt
    f[i] = f_new
    
def plot_field_real(f, N):
    x, t = np.meshgrid(np.linspace(0, 1, N), np.linspace(0, 1, N))

    fig, ax = plt.subplots(1, subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(x, t, f.real[:, :, -1], cmap=cm.viridis)
    fig.colorbar(surf)
    
    plt.show()

# Equations of motion for different fields

def get_heat_eq(N, c=20):
    return c * get_D2x(N)

def get_wave_eq(N, c=1):
    return c * get_D2x(N)

def get_KG(N, m=0.2):
    return get_D2x(N) - m ** 2 * np.identity(N)
    

def simulate_field(N, get_Dt, f0, order, steps):
    f = get_inital(N, f0, order)
    Dt = get_Dt(N)
    dt = 1 / (N - 1)

    for i in range(1, N):
        time_step(f, i, Dt, dt, order, steps)
    
    plot_field_real(f, N)

# TODO: Add animation, coupling term, vector-equations

N = 100

x = np.linspace(0, 1, N)
gaussian = np.exp(-(x - 1 / 2)** 2 * 100)

# f0 = np.array([gaussian,]).T
# simulate_field(N, get_heat_eq, f0, 1, 50)
# 
# f0 = np.array([np.zeros(N), gaussian,]).T
# simulate_field(N, get_wave_eq, f0, 2, 100)

f0 = np.array([np.zeros(N), gaussian,]).T
simulate_field(N, get_KG, f0, 2, 150)

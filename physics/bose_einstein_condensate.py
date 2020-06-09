import numpy as np
import scipy as sp
from numpy import exp, sqrt, log
from numba import njit
from matplotlib import pyplot as plt
from matplotlib import cm


n = 200
d = 250
m_max = 20

@njit
def n_k(m, Ng, b):
    return (exp(b*m@m)*(1+1/Ng) - 1)**(-1)

@njit
def get_init():
    Ns = np.ones(n)
    Ngs = np.zeros(n)
    ms = np.arange(m_max) * 1.
    return Ns, Ngs, ms

@njit
def loop(b, d):
    Ns, Ngs, ms = get_init()
    Ng = 0.1

    for i in range(1, n):
        N = 0
        for mx in ms:
            N0 = N
            for my in ms:
                for mz in ms:
                    m = np.array([mx, my, mz])
                    N += n_k(m, Ng, b)

        Ns[i] = N        
        Ngs[i] = Ng

        Ng += d * (Ngs[i]-Ngs[i-1])/(Ns[i]-Ns[i-1])

    return Ngs, Ns


def plot_one(b):
    Ngs, Ns = loop(b, d)
    fig, ax = plt.subplots()

    ax.plot(
        Ns, Ngs/Ns, 
        label="$\\beta={:.5f}$".format(b)
        )

    ax.legend()
    ax.set_ylim(0, 1)
    plt.show()

def task_b():
    n = 3
    Betas = 10.**(-1*np.linspace(1, 5, n))
    
    for i, b in enumerate(Betas):
        Ngs, Ns = loop(b, d)

        plt.plot(
            Ns, Ngs/Ns, 
            color=cm.viridis(i/n), 
            label="$\\beta={:.5f}$".format(b)
            )

    plt.legend()
    plt.show()


def task_c():
    n = 5
    Betas = 10.**(-1*np.linspace(1, 4, n))

    for i, b in enumerate(Betas):
        Ngs, Ns = loop(b, d*log(2/b))
        plt.plot(
            Ns*(1/sqrt(b))**3, Ngs/Ns, 
            color=cm.viridis(i/n), 
            label="$\\beta={:.3f}$".format(b)
            )

    plt.legend()
    plt.show()



# plot_one(1e-2)
# task_b()
task_c()

import numpy as np
from numpy import exp, sqrt, log
from matplotlib import pyplot as plt
from matplotlib import cm


def n_k(m, Ng, b):
    mm = np.einsum("i..., i... -> ...", m, m)
    return np.sum((exp(b*mm)*(1+1/Ng) - 1)**(-1))


def get_init_3D(n, m=40):
    Ns = np.empty(n)
    Ngs = np.empty(n)
    Ns[0] = 0
    Ngs[0] = 0
    ms = np.array((np.mgrid[
        0:m:(m+1)*1j, 
        0:m:(m+1)*1j, 
        0:m:(m+1)*1j
        ]))

    return Ns, Ngs, ms

def get_init_2D(n, m=50):
    Ns = np.empty(n)
    Ngs = np.empty(n)
    Ns[0] = 0.01
    Ngs[0] = 0
    ms = np.array((np.mgrid[
        0:m:(m+1)*1j, 
        0:m:(m+1)*1j
        ]))

    return Ns, Ngs, ms


def loop(b, N, n, d):
    Ns, Ngs, ms = get_init_3D(n)
    Ng = 0.1  # can't be zero

    for i in range(1, n):
        Ns[i] = n_k(ms, Ng, b)
        Ngs[i] = Ng
        Ng += d*(Ngs[i]-Ngs[i-1])/(Ns[i]-Ns[i-1])

    return Ngs, Ns

def bisec(N, n, b):
    _, _, ms = get_init_3D(n)

    step = N/2
    Ng = N/2
    for i in range(20):
        n = n_k(ms, Ng, b)
        if n<N: Ng += step/2
        else: Ng -= step/2
        step = step/2
    return Ng

def loop2(N, n, T):
    _, _, ms = get_init_3D(n)
    Ngs = np.empty(n)

    for i, b in enumerate(1/T):
        Ngs[i] = bisec(N, n, b)

    return Ngs

def plot_one(b, N, n):
    Ngs, Ns = loop(b, N, n, N/n)
    fig, ax = plt.subplots()

    ax.plot(Ns, Ngs/Ns, label="$\\beta={:.5f}$".format(b))

    ax.legend()
    ax.set_ylim(0, 1)
    plt.show()

def task_b(N, n):
    fig, ax = plt.subplots()
    num_plots = 10
    bs = 10**(-1*np.linspace(1, 5, num_plots))

    for i, b in enumerate(bs):
        Ngs, Ns = loop(b, N, n, N/n)
        
        ax.plot(
            Ns, Ngs/Ns, 
            label="$\\beta={:.5f}$".format(b),
            color = cm.viridis(i/num_plots)
            )

    ax.legend()
    ax.set_ylim(0, 1)
    plt.show()

def task_c(N, n):
    fig, ax = plt.subplots()
    num_plots = 10
    bs = 10**(-1*np.linspace(1, 5, num_plots))

    for i, b in enumerate(bs):
        d = N/n/b**(3/2)
        Ngs, Ns = loop(b, N, n, d)
        ax.plot(
            Ns*b**(3/2), Ngs/Ns, 
            label="$\\beta={:.5f}$".format(b),
            color = cm.viridis(i/num_plots)
            )

    ax.legend()
    ax.set_ylim(-.1, 1.1)
    plt.show()

def task_d1(N, n):
    fig, ax = plt.subplots()
    num_plots = 10
    bs = 10**(-1*np.linspace(1, 5, num_plots))

    for i, b in enumerate(bs):
        d = N/n
        Ngs, Ns = loop(b, N, n, d)
        ax.plot(
            Ns, Ngs/Ns, 
            label="$\\beta={:.5f}$".format(b),
            color = cm.viridis(i/num_plots)
            )

    ax.legend()
    ax.set_ylim(-.1, 1.1)
    plt.show()

def task_d2(N, n):
    fig, ax = plt.subplots()
    num_plots = 10
    bs = 10**(-1*np.linspace(1, 5, num_plots))

    for i, b in enumerate(bs):
        d = N/n/b
        Ngs, Ns = loop(b, N, n, d)
        ax.plot(
            Ns*b, Ngs/Ns, 
            label="$\\beta={:.5f}$".format(b),
            color = cm.viridis(i/num_plots)
            )

    ax.legend()
    ax.set_ylim(-.1, 1.1)
    plt.show()

def task_e(N, n):
    T = np.linspace(1, 500, n)
    Ngs = loop2(N, n, T)

    fig, ax = plt.subplots()
    ax.plot(T, Ngs/N)
    plt.show()


# Resolution
n = 100
# Particles
N = 10_000

# plot_one(1e-2, N, n)
# task_b(N, n)
task_c(20, n)
# task_d1(N, n)
# task_d2(100, n)

task_e(N, n)

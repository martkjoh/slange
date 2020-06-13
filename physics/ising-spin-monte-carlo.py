import numpy as np
from numpy import exp, sqrt, log as ln
from numpy.random import choice, randint, rand
from matplotlib import pyplot as plt

Tc = 2/(ln(1+sqrt(2)))


def get_s(N):
    """ Return lattice of spins, randomly oriented """
    return choice((-1, 1), (N, N))

def magnetization(s, N):
    return np.abs(np.sum(s)) / N**2


# Changing spins one-by-one in the Monte carlo sweep
def serial_sweeps(s, N, T, num_sweeps):
    def get_delta_H(s, N, i, j):
        """ retrns changin in energy from flipping spin (i, j) """
        sum_neigh = s[i - 1, j] + s[(i + 1) % N, j]+ s[i, j - 1]+ s[i, (j + 1) % N]
        B = 0.01
        return 2*s[i, j] * (sum_neigh + B)
        
    def MC_sweep(s, N, T):
        """ One sweep of the hastings algorithm """
        for _ in range(N ** 2):
            i, j = randint(N, size=2)
            delta_H = get_delta_H(s, N, i, j)
            if delta_H < 0:
                s[i, j] *= -1
                continue
            if exp(-delta_H / T) > rand():
                s[i, j] *= -1

    for j in range(num_sweeps):
        MC_sweep(s, N, T)

# Changing all spins in the lattice w porbability c
def paralell_sweeps(s, N, T, num_sweeps):
    def get_delta_H(s, N):
        """ retrns lattice with change in energy from flipping each spin"""
        sum_neigh = np.zeros_like(s)
        for j in range(2):
            for n in (-1, 1):
                sum_neigh += np.roll(s, n, axis=j)

        B = 0.01
        return 2*s*(sum_neigh + B)

    def MC_sweep(s, N, T):
        """ MC-hastings sweep, with prob. c of trying to flipping each spin each loop """
        c = 0.5
        for i in range(1 + int(1 / c)):
            to_flip = rand(N, N) < c
            delta_H = get_delta_H(s, N)
            pos = delta_H > 0
            to_flip2 = exp(-delta_H[pos] / T) > rand(np.sum(pos))
            to_flip[pos] = np.logical_and(to_flip[pos], to_flip2)
            s[to_flip] *= -1

    for j in range(num_sweeps):
        MC_sweep(s, N, T)


def plot_equilibration(sweep_func):
    N = 20
    m = 6
    num_sweeps = 10
    Ts = np.linspace(0.01, 1.2*Tc, m)

    fig, ax = plt.subplots(2, m)    

    for j, T in enumerate(Ts):
        s = get_s(N)
        ax[0, j].set_title("$T = {:.3f}$".format(T))
        ax[0, j].imshow(s)
        paralell_sweeps
        sweep_func(s, N, T, num_sweeps)
        ax[1, j].imshow(s)

    plt.show()


def plot_magnetization(sweep_func):
    n = 100
    m = 10
    equibliration = 1000
    Ns = [10, 20, 30]
    Ts = np.linspace(0.01, 1.2*Tc, m)

    fig, ax = plt.subplots()    

    for i, N in enumerate(Ns):
        M = np.empty(m)
        for j, T in enumerate(Ts):
            s = get_s(N)
            M_ave = 0
            sweep_func(s, N, T, equibliration)
            for _ in range(n):
                M_ave += magnetization(s, N)            
            M[j] = M_ave/n
        ax.plot(Ts, M)
    plt.show()


if __name__ == "__main__":
    # plot_equilibration(paralell_sweeps)
    # plot_equilibration(serial_sweeps)
    plot_magnetization(paralell_sweeps)
    
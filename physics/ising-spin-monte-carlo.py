import numpy as np
from numpy import exp, sqrt, log as ln
from numpy.random import choice, randint, rand
from matplotlib import pyplot as plt
from os.path import expanduser


# Critical temprature of the 2D ising model
Tc = 2 / (ln(1 + sqrt(2)))
# Strength of the external magnetic filed
B = 0


# utillities

def get_s(N):
    """ Return lattice of spins, randomly oriented """
    return choice((-1, 1), (N, N))

def get_delta_H(s, N):
    """ retrns lattice with change in energy from flipping each spin"""
    sum_neigh = np.zeros_like(s)
    for j in range(2):
        for n in (-1, 1):
            sum_neigh += np.roll(s, n, axis=j)

    return 2*s*(sum_neigh + B)

def MC_sweep(s, N, T):
    """ MC-hastings sweep, with prob. c of trying to flipping each spin each loop """
    c = 0.5
    for _ in range(int(1 / c)):
        to_flip = rand(N, N) < c
        delta_H = get_delta_H(s, N)
        pos = delta_H > 0
        to_flip2 = exp(-delta_H[pos] / T) > rand(np.sum(pos))
        to_flip[pos] = np.logical_and(to_flip[pos], to_flip2)
        s[to_flip] *= -1


def sample(s, N, observables):
    """ samples a set of observables from a configuration of s """
    obs = np.empty(len(observables))
    for i, key in enumerate(observables):
        obs[i] = observables[key](s, N)
    return obs


def get_samples(N, T, n, m, equib, observables):
    """ 
    Creates m N*N matrices, equilibrates them for equib steps, then does
    n MC-sweeps and at temprature T samples all the observables, 
    returning an array of the samples
    """
    obs = np.zeros(len(observables))
    for _ in range(m):
        s = get_s(N)
        for _ in range(equib):
            MC_sweep(s, N, T)
        for _ in range(n):
            MC_sweep(s, N, T)
            obs += sample(s, N, observables)
    return obs / (n*m)



# Observables

def absolute_magnetization(s, N):
    return np.abs(np.sum(s)) / N ** 2
    
def magnetization_squared(s, N):
    return (np.sum(s) / N**2)**2

def energy_density(s, N):
    sum_neigh = np.zeros_like(s)
    for j in range(2):
        for n in (-1, 1):
            sum_neigh += np.roll(s, n, axis=j)

    return - 1 / 2 * np.sum(s * sum_neigh) / N ** 2
    
def energy_density_squared(s, N):
    return energy_density(s, N)** 2


# functinos of observables

def heat_capacity(samples):
    return samples["E2"] - samples["E"]**2
    
def susceptibility(samples):
    return samples["M^2"] - samples["|M|"]**2


# Plotting functions
    
def plot_equilibration():
    N = 50
    k = 6
    equib = 100_000
    Ts = np.linspace(0.01, 1.2*Tc, k)

    fig, ax = plt.subplots(2, k, figsize=(16, 8))
    fig.suptitle("$N={}$\n".format(N) + "{} sweeps".format(equib))

    for i, T in enumerate(Ts):
        print(i)
        s = get_s(N)
        ax[0, i].set_title("$T = {:.3f}$".format(T))
        ax[0, i].imshow(s)
        for _ in range(equib):
            MC_sweep(s, N, T)
        ax[1, i].imshow(s)

    plt.tight_layout()
    plt.savefig(expanduser("~") + "/Desktop/test2"  + ".png")
    plt.close(fig)

def plot_observables():
    observables = {
        "E": energy_density,
        "|M|": absolute_magnetization
    }

    equib = 100_000
    n = 100_000
    m = 1
    k = 20
    l = len(observables)

    Ns = [8, 16]
    Ts = np.linspace(1.5, 1.2*Tc, k)

    fig, ax = plt.subplots(l, figsize=(10, 10))

    if l==1: ax = [ax,]

    for i, N in enumerate(Ns):
        print(i)
        samples = np.empty((k, l))
        for j, T in enumerate(Ts):
            samples[j] = get_samples(N, T, n, m, equib, observables)
        for j, key in enumerate(observables):
            ax[j].plot(Ts, samples[:, j], ".", label="$N ={}$".format(N))
            ax[j].legend()
            ax[j].set_title = "$" + key + "$"
    
    plt.tight_layout()
    plt.savefig(expanduser("~") + "/Desktop/test"  + ".png")
    plt.close(fig)

def plot_heat_capacity():
    observables = {
        "energy_density": energy_density,
        "energy_density_squared": energy_density_squared
    }

    samples = {}
    equib = 1000
    n = 100
    m = 2
    k = 10
    l = len(observables)

    Ns = [8, 16]
    Ts = np.linspace(0.1, 1.2*Tc, k)

    fig, ax = plt.subplots(l)

    if l == 1: ax = [ax,]
    

    for i, N in enumerate(Ns):
        print(i)
        samples = np.empty((k, l))
        for j, T in enumerate(Ts):
            samples[j] = get_samples(N, T, n, m, equib, observables)

        heat_cap = samples[:, 1] - samples[:, 0]**2 
        ax[j].plot(Ts, heat_cap, ".", label="$N ={}$".format(N))

    plt.tight_layout()
    plt.savefig(expanduser("~") + "/Desktop/test3"  + ".png")
    plt.close(fig)
    

if __name__ == "__main__":
    # plot_equilibration()
    plot_observables()
import numpy as np
from matplotlib import pyplot as plt
from numba import njit
from tqdm import trange
from multiprocessing import Pool, cpu_count

N = 16
sweeps = 10
equill = 10000
num_samples = 10000
J=1


@njit()
def dE(S, i, j):
    Sij = S[i, j]
    return 2 * J * Sij * (
        S[i-1, j] + S[(i + 1)%N, j] + S[i, j-1] + S[i, (j+1)%N]
    )

@njit()
def sweep(S, T):
    for i in range(N**2):
        i, j = np.random.randint(0, N, 2)
        r = np.random.random()
        w = np.exp(-dE(S, i, j)/T)
        if w>r:
            S[i, j] = -S[i, j]


def mag(S, T):
    return np.abs(np.sum(S))/N**2

def mag2(S, T):
    return mag(S, T)**2

def energy(S, T):
    return np.sum(J*S*(
        np.roll(S, 1, 0) + np.roll(S, -1, 0) \
        + np.roll(S, 1, 1) + np.roll(S, -1, 1)
        ))/N**2

def energy2(S, T):
    return energy(S, T)**2


sample_funcs = {
    "Mag" :     mag,
    "Mag2" :    mag2,
    "Energy" :  energy,
    "Energy2":  energy2,
}

def get_samples(S, T, samples):
    for key in samples:
        samples[key] += sample_funcs[key](S, T)
    return samples


def simulate(T, num_samples):
    print("T = {:.3f}".format(T))
    # S = np.random.choice([-1, 1], (N, N))
    S = np.ones((N, N))
    samples = {
    "Mag" :     0,
    "Mag2" :    0,
    "Energy" :  0,
    "Energy2":  0,
    }

    for _ in range(equill): sweep(S, T)
    i = 0
    while i<num_samples:
        for _ in range(sweeps): sweep(S, T)
        get_samples(S, T, samples)
        i += 1
    for key in samples:
        samples[key] *= 1/num_samples
    return samples


# Ts = np.linspace(0.1, 5, 100)
# avs = [np.sum(simulate(T))/N**2 for T in Ts]
# plt.plot(Ts, avs, ".")
# plt.show()

# Ts = np.linspace(0.1, 5, 10)
# fig, ax = plt.subplots(1, 10)
# Ss = [simulate(T) for T in Ts]
# [ax[i].imshow(Ss[i]) for i in range(len(Ss))]
# plt.show()

import numpy as np
from matplotlib import pyplot as plt
from numba import njit
from tqdm import trange
from multiprocessing import Pool, cpu_count



@njit()
def dE(S, i, j):
    return 2 * J * S[i, j] * (
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

@njit()
def mag(S, T):
    return np.abs(np.sum(S))/N**2

@njit()
def mag2(S, T):
    return mag(S, T)**2

@njit()
def energy(S, T):
    return np.sum(J*S*(
        np.roll(S, 1, 0) + np.roll(S, -1, 0) \
        + np.roll(S, 1, 1) + np.roll(S, -1, 1)
        ))/N**2

@njit()
def energy2(S, T):
    return energy(S, T)**2


@njit()
def sample(S, m, T, num_samples):
    for i in range(num_samples):
        for _ in range(sweeps): 
            sweep(S, T)
        m += mag(S, T)
    m *= 1/num_samples
    return m


@njit()
def equilibrate(S, T):
    for _ in range(equill): sweep(S, T)


def simulate(T, num_samples):
    print("T = {:.3f}".format(T))
    S = np.ones((N, N))
    m = 0

    equilibrate(S, T)
    m = sample(S, m, T, num_samples)
    return m


def gen_grid(T):
    print(T)
    S = np.ones((N, N))
    for i in range(equill): 
        sweep(S, T)
    return S




N = 96
J=1

sweeps = 1
equill = 1000
num_samples = 1000
n = 40

Ts = np.linspace(1, 3.5, n)
avs = [simulate(T, num_samples) for T in Ts]
plt.plot(Ts, avs, ".")
plt.show()


# N = 100
# J=1

# Ts = np.linspace(0.1, 5, 10)
# fig, ax = plt.subplots(1, 10)
# Ss = [gen_grid(T) for T in Ts]
# [ax[i].imshow(Ss[i]) for i in range(len(Ss))]
# plt.show()

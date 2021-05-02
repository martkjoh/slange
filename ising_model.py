import numpy as np
from matplotlib import pyplot as plt
from numba import njit
from tqdm import trange


N = 10
sweeps = 100
equill = 1000
num_samples = 100
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


def energy(S, T):
    return np.sum(J*S*(
        np.roll(S, 1, 0) + np.roll(S, -1, 0) \
        + np.roll(S, 1, 1) + np.roll(S, -1, 1)
        ))/N**2

def energy2(S, T):
    return energy(S, T)**2


sample_funcs = {
    "Magnetization" :   mag,
    "Energy" :          energy,
    "Energy2":          energy2,
}

def get_samples(S, T, samples):
    for key in samples:
        samples[key].append(
            sample_funcs[key](S, T)
        )
    return samples


def simulate(T):
    S = np.random.choice([-1, 1], (N, N))
    samples = {
    "Magnetization" :   [],
    "Energy" :          [],
    "Energy2":          [],
    }

    for _ in range(equill): sweep(S, T)
    i = 0
    while i<num_samples:
        for _ in range(sweeps): sweep(S, T)
        samples = get_samples(S, T, samples)
        i += 1
    return S, samples

# Ts = np.linspace(0.1, 5, 100)
# avs = [np.sum(simulate(T))/N**2 for T in Ts]
# plt.plot(Ts, avs, ".")
# plt.show()

# Ts = np.linspace(0.1, 5, 10)
# fig, ax = plt.subplots(1, 10)
# Ss = [simulate(T) for T in Ts]
# [ax[i].imshow(Ss[i]) for i in range(len(Ss))]
# plt.show()

Temps = 10
Ts = np.linspace(0.1, 5, Temps)
Es = np.empty(Temps)
Ms = np.empty(Temps)
Hc = np.empty(Temps)


for i in range(Temps):
    S, samples = simulate(Ts[i])
    Es[i] = np.sum(samples["Energy"]) / num_samples
    Ms[i] = np.sum(samples["Magnetization"]) / num_samples
    Hc[i] = (np.sum(samples["Energy2"]) - np.sum(samples["Energy"])**2) / num_samples / Ts[i] 

plt.plot(Ts, Ms, "kx")
plt.show()
plt.plot(Ts, Es, "kx")
plt.show()
plt.plot(Ts, Hc, "kx")
plt.show()
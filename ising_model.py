import numpy as np
from matplotlib import pyplot as plt
from numba import njit

N = 100
sweeps = 1000
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
    return S


def simulate(T):
    S = np.random.choice([-1, 1], (N, N))
    for i in range(sweeps):
        S = sweep(S, T)
    return S

# Ts = np.linspace(0.1, 5, 100)
# avs = [np.sum(simulate(T))/N**2 for T in Ts]
# plt.plot(Ts, avs, ".")
# plt.show()

Ts = np.linspace(0.1, 5, 10)
fig, ax = plt.subplots(1, 10)
Ss = [simulate(T) for T in Ts]
[ax[i].imshow(Ss[i]) for i in range(len(Ss))]
plt.show()
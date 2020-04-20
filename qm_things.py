import numpy as np
from numpy import pi, exp, sin, cos, ceil
from matplotlib import pyplot as plt
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigs
from scipy.linalg import eigh_tridiagonal as eigsh2

V0 = 1e3

def V(x):
    n = len(x)
    m = int(ceil(n/3))
    V = np.zeros(n)
    V[m:2*m] = V0*np.ones(m)
    return V

def get_H(N, V):
    I = np.empty(3*(N-1)-2, dtype=int)
    J = np.empty(3*(N-1)-2, dtype=int)
    H = np.empty(3*(N-1)-2)
    x = np.linspace(1/N, 1-1/N, N-1)

    I[0::3] = J[0::3] = np.arange(N-1)
    I[1::3] = J[2::3] = np.arange(N-2)
    I[2::3] = J[1::3] = np.arange(1, N-1)
    H[0::3] = V(x) + 2*N**2*np.ones(N-1)
    H[1::3] = H[2::3] = -N**2*np.ones(N-2)

    return coo_matrix((H, (I, J)))


def get_eig(N, V, nev):
    print("making hamiltonian...")
    H = get_H(N, V)
    print("finding eigenvalues...")
    l, v = eigs(H, k=nev, which='SM', tol=1e-2)
    for i in range(nev):
        if v[1, i] - v[0, i] < 0:
            v[:, i] = -v[:, i]
    return l, v

def get_eig2(N, V, nev):
    x = np.linspace(1/N, 1-1/N, N-1)
    H1 = V(x) + 2*N**2*np.ones(N-1)
    H2 = -N**2*np.ones(N-2)
    l, v = eigsh2(H1, H2, select="i", select_range=(0,nev))
    return l, v
    


def plot_eig_vec1(N, V, nev):
    l, v = get_eig(N, V, nev)
    fig, ax = plt.subplots()
    x = np.linspace(1/N, 1-1/N, N-1)
    print("plotting...")
    for i in range(nev):
        print(l[i])
        ax.plot(x, v[:, i].real)

    plt.show()

def plot_eig_vec2(N, V, nev):
    l, v = get_eig2(N, V, nev)
    fig, ax = plt.subplots()
    x = np.linspace(1/N, 1-1/N, N-1)
    print("plotting...")
    for i in range(nev):
        print(l[i])
        ax.plot(x, v[:, i].real)

    plt.show()

N = int(1e6)
nev = 4

plot_eig_vec2(N, V, nev)

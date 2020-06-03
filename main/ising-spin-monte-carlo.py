import numpy as np
from numpy import exp, ceil, sqrt, log as ln
from numpy.random import choice, randint, rand
from matplotlib import pyplot as plt
from numba import njit

Tc = 2/(ln(1+sqrt(2)))

def get_s(N):
    return choice([-1., 1.], (N, N))

@njit()
def get_boundary(bc, s=0, i=0):
    if bc==0: return (1, 1)         # Plus-plus
    elif bc==1: return (1, -1)      # Plus-minus
    else: raise Exception("Boundary condition not recognized")


@njit()
def get_neighbours(s, i, j, N, bc) -> np.ndarray:
        s_neigh = np.zeros((2, 2))
        s_neigh[0, 0] = s[i, j-1]; s_neigh[0, 1] = s[i, (j+1)%N]
        boundary = get_boundary(bc, s, i)
        if (i==0): s_neigh[1, 0] = boundary[0]
        else: s_neigh[1, 0] = s[i-1, j]
        if (i==N-1): s_neigh[1, 1] = boundary[1]
        else: s_neigh[1, 1] = s[i+1, j]
        return s_neigh

@njit()
def MC_sweep_serial(s, N, T, bc=0):
    for i in range(N**2):
        i, j = randint(0, N, size=2)
        s_neigh = get_neighbours(s, i, j, N, bc)
        delta_H = 2*s[i,j]*np.sum(s_neigh)
        if delta_H<0:
            s[i, j] *= -1
            continue
        W = exp(-delta_H/T)
        a = rand()
        if W>a: 
            s[i, j] *= -1

@njit()
def run_sweeps_serial(s, N, T, num_sweeps, bc=0):
    for j in range(num_sweeps):
        MC_sweep_serial(s, N, T, bc=bc)


def run_sweeps_paralell(s, N, T, num_sweeps, bc=0):
    def apply_bc(s, N, bc):
        """ Rerturns copy of lattice w/ boundary conditions attached"""
        row = np.ones((1, N))
        vals = get_boundary(bc)
        return np.concatenate((vals[0]*row, s, vals[1]*row))


    def sum_neigh_lattice(s, N, bc=0):
        """ sum over product of neares neighbours of lattice """
        s_w_bound = apply_bc(s, N, bc)
        sum_neigh = np.zeros_like(s)
        for j in range(2):
            for n in [-1, 1]:
                sum_neigh += np.roll(s_w_bound, n, axis=j)[1:-1]
        return s*sum_neigh


    def MC_sweep_paralell(s, N, T, bc=0):
        """ MC-hastings sweep, with prob. c of flipping each spin each loop """
        c = 0.5
        for i in range(1+int(1/c)):
            delta_H = 2*sum_neigh_lattice(s, N, bc=bc)
            W = np.ones_like(delta_H)
            pos = delta_H>0
            W[pos] = exp(-delta_H[pos]/T)
            indx = np.logical_and(W>rand(N, N), c>rand(N, N))
            s[indx] *= -1

    for j in range(num_sweeps):
        MC_sweep_paralell(s, N, T, bc=bc)


def plot_equilibration(N, m, bc, num_sweeps, sweep_func):
    Ts = np.linspace(0.01, Tc, m)
    tau = np.empty(m)

    fig, ax = plt.subplots(2, m)

    for i, T in enumerate(Ts):
        print(i)
        s = get_s(N)
    
        ax[0, i].set_title("$T = {:.3f}$".format(T))
        ax[0, i].imshow(s)
        sweep_func(s, N, T, num_sweeps, bc=bc)
        ax[1, i].imshow(s)

    plt.show()

if __name__ == "__main__":
    plot_equilibration(50, 4, 1, 1_000, run_sweeps_serial)

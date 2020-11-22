import numpy as np
from numpy import sqrt, pi
import matplotlib.pyplot as plt


a = 0.1

def acc(x):
    r2 = x[0]** 2 + x[1]** 2
    x_hat = x / sqrt(r2)
    return - x_hat / r2 * (1 + a / r2)

def f(x):
    return np.array( [x[1], acc(x[0])] )

def RK4step(x, t, dt):
    k1 = f(x[t]) * dt
    k2 = f(x[t] + 1 / 2 * k1) * dt
    k3 = f(x[t] + 1 / 2 * k2) * dt
    k4 = f(x[t] + k3)  * dt
    x[t + 1] = x[t] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

def energy(x):
    r2 = x[:, 0, 0]** 2 + x[:, 0, 1]** 2
    v2 =  sqrt(x[:, 1, 0]**2 + x[:, 1, 1]**2)
    return - 1/sqrt(r2) +  1 / 2 * v2 
    
def find_min(x):
    min_ts = []
    for t in range(1, len(x) - 1):
        r = x[t - 1:t + 3:, 0, 0]** 2 + x[t - 1:t + 3:, 0, 1]** 2
        if (r[0] > r[1]) and (r[2] > r[1]):
            min_ts.append(t)
    return min_ts

def simulate_orbit(x0, dt, T):
    N = int(T / dt)
    x = np.empty((N, 2, 2)) # x[t,i,j] = step t of i'th diff. of j'th coord.
    x[0] = x0
    for t in range(N-1):
        RK4step(x, t, dt)
    return x
        
def plot_orb(x):
    fig, ax = plt.subplots()

    ax.plot(x[:, 0, 0], x[:, 0, 1],)
    min_ts = find_min(x)
    for t in min_ts:
        ax.plot(x[t, 0, 0], x[t, 0, 1], "xk")
    ax.set_xlim((-1, 1))
    ax.set_ylim(-1, 1)
    plt.show()

def plot_dE(x, T):
    N = len(x)
    t = np.linspace(0, T, N)
    E = energy(x)
    dE = np.abs((E - E[0] * np.ones_like(E)) / E[0])
    fig, ax = plt.subplots()
    ax.plot(t, dE)
    plt.show()

def plot_dE_afo_dt(x0):
    T = 2 * pi
    n = 20
    dts = np.logspace(-3, -0.1, n)
    dEs = np.empty(n)
    for i, dt in enumerate(dts):
        x = simulate_orbit(x0, dt, T)
        E = energy(x)
        dEs[i] = np.abs((E[0] - E[-1]) / E[0])

    fig, ax = plt.subplots()
    ax.loglog(dts, dEs, ".")
    plt.show()



x0 = np.array([[1, 0], [0, 1]])
dt = 0.01
T = 2*pi * 20
x = simulate_orbit(x0, dt, T)


plot_orb(x)

# Only works for a=0
plot_dE(x, T)
plot_dE_afo_dt(x0)

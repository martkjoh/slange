import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
from matplotlib import cm


N = 100

t0 = 0
T = 2

x0 = np.ones(N)
t = np.linspace(t0 - T, t0 + T, N)
dt = 2 * T / N 

def f(t, y):
    return - t * y 

# returns a array representing g(t) = \int_t0^t f(s, y(s)) ds
def integrate(f, t0, t, y, dt):
    if (t[0] >= t0): return np.cumsum(f(t, y) * dt)
    if (t[-1] <= t0): return None
    n = 0
    while(t[n] < t0): n += 1
    a = np.cumsum(f(t[:n], y[:n]) * dt)
    a -= a[-1] * np.ones(n)
    return np.concatenate((a, np.cumsum(f(t[n:], y[n:]) * dt)))

def picard_iter(yn, t):
    return x0 + integrate(f, t0, t, yn, dt)

n = 10
ys = np.zeros((n, N))
ys[0] = x0
plt.plot(t, ys[0])
for i in range(n - 1):
    ys[i + 1] = picard_iter(ys[i], t)
    plt.plot(t, ys[i + 1], color = cm.viridis(i / n))

plt.grid()
plt.show()
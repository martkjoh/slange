import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


N = 100
beta = 1
t0 = 0

x0 = np.ones(N)
t = np.linspace(t0 - beta, t0 + beta, N)
dt = beta / N

def f(y, t):
    return y

def T(y, t):
    return x0

def picard_iter(yn, t):
    return x0 + np.add.accumulate(f(yn, t) * dt)

n = 10
ys = np.zeros((n, N))
ys[0] = x0
for i in range(n - 1):
    ys[i + 1] = picard_iter(ys[i], t)
    if ((i * 10 ) % n == 0):
        plt.plot(t, ys[i], color = cm.viridis(i / n))

plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt


Nsteps = 10000
Nwalkers = 1000
eta = 1
tau = 1
dt = 0.1
s = np.sqrt(dt)

t = np.linspace(0, dt*Nsteps, Nsteps+1)
v = np.empty((Nwalkers, Nsteps+1))
v[:, 0] = np.zeros(Nwalkers)

dW = np.random.normal(0, s, (Nwalkers, Nsteps))

dv = np.empty_like(dW)
for i in range(Nsteps):
    dv[:, i] = -1/tau*v[:, i] * dt + eta * dW[:, i]
    v[:, i+1] = v[:, i] + dW[:, i]

x = np.empty((Nwalkers, Nsteps+1))
x[:, 0] = np.zeros(Nwalkers)
x[:, 1:] = np.cumsum(dv, axis=1) * dt

[plt.plot(t, x[i], c="royalblue", alpha=0.1) for i in range(Nwalkers)]
plt.show()

[plt.plot(t, v[i], c="royalblue", alpha=0.1) for i in range(Nwalkers)]
plt.show()

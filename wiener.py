import numpy as np
import matplotlib.pyplot as plt

Nsteps = 100
Nwalkers = 1000
s = 1

steps = np.random.normal(0, s, (Nwalkers, Nsteps))
pos = np.empty((Nwalkers, Nsteps+1))
pos[:, 0] = np.zeros(Nwalkers)
pos[:, 1:] = np.cumsum(steps, axis=1)

num_steps = np.arange(0, Nsteps+1)
[plt.plot(num_steps, pos[i], c="royalblue", alpha=0.05) for i in range(Nwalkers)]
plt.plot(num_steps, 2*np.sqrt(num_steps), "k")
plt.plot(num_steps, -2*np.sqrt(num_steps), "k")
plt.show()


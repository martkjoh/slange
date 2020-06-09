import numpy as np
from numpy import exp, sin, pi
from matplotlib import pyplot as plt

a = 3.6
B = -1
k = 1.12
xv = np.arange(-10*a, 10*a, 0.01)
period = np.arange(-10*a, 10*a, a)

u_k = exp(-B*sin(pi/a*xv)**2)

pw = exp(1j*k*xv)

psi = u_k*pw

fig, ax = plt.subplots(4)

ax[0].plot(period, np.zeros_like(period), "r.")
ax[0].plot(xv, u_k)

ax[1].plot(xv, pw.real)
ax[1].plot(xv, pw.imag)

ax[2].plot(xv, psi.real)
ax[2].plot(xv, psi.imag)

ax[3].plot(period, np.zeros_like(period), "r.")
ax[3].plot(xv, np.conj(psi)*psi)

plt.show()
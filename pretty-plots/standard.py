import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['mathtext.fontset'] = 'cm'
font = {'family' : 'serif', 
        'weight' : 'normal', 
        'size': 20}
        
plt.rc('font', **font)
plt.rc("lines", lw=2)

x = np.linspace(-10, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, x ** 2)

ax.set_xlabel("$x /  [x] = \mathrm{m \, s^{-1}}$")
ax.set_ylabel("$f(x) /  [f] = \mathrm{J}$")

plt.show()
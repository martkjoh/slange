import numpy as np
from matplotlib import pyplot as plt

plt.rc("font", family="serif", size=16)
plt.rc("mathtext", fontset="cm")
plt.rc("lines", lw=2)
plt.rc("axes", grid=True)


omega = lambda a, x: x*((x -1)**2 + a)
fig, ax = plt.subplots()

a = [0, .2, .4, .6]
x = np.linspace(0, 1.6)
for aa in a:
    ax.plot(omega(aa, x), x, 'k--')

ax.set_xlabel("$(\\Omega /  2V[\\Delta + J])^2 $")
ax.set_ylabel("$(\\Gamma /  [\\Delta + J])^2$")

plt.show()

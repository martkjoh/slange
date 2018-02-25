# Skrevet av Martin Johnsrud, 25/02-2018
# Dette scriptet har til hensikt å drive kurvetilpassning å regresjonsanalyse
import numpy as np
from matplotlib import pyplot as plt
import os
from linreg import *
from matplotlib import rc

plt.style.use("bmh")

x, y = np.loadtxt("data.dat", unpack=True)

a_0, a_1, f, D_y = lineær_regresjon(x, y, y_func=lambda x: x)

x_kont = np.linspace(min(x), max(x), 1000)

fit = np.polyfit(x, y, deg=5)
print(fit)

fig1, ax1 = plt.subplots(1)
fig2, ax2 = plt.subplots(1)

ax1.plot(x, y, "x", ms=4)
ax1.set_xlabel("$I\,[\mathrm{A}]$", fontsize=18)
ax1.set_ylabel("$m\,[\mathrm{g}]$", fontsize=18)
ax1.set_title("Vekt som funksjon av strøm", fontsize=18)
ax1.plot(x_kont, f(x_kont), lw=2)
ax1.legend(("$I_{målt}$", "$I_{reg}$"), fontsize=18)

ax2.plot(x, D_y,)
ax2.set_xlabel("$I\,[\mathrm{A}]$", fontsize=18)
ax2.set_ylabel("$m\,[\mathrm{g}]$", fontsize=18)
ax2.set_title("Avvik", fontsize=18)
ax2.legend(("$I_{målt}$", "$I_{reg}$"), fontsize=18)

plt.tight_layout()
plt.show()

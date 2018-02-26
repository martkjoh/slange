# Skrevet av Martin Johnsrud, 25/02-2018
# Dette scriptet har til hensikt å drive kurvetilpassning å regresjonsanalyse
import numpy as np
from matplotlib import pyplot as plt
from ElMagØving.kurvetilpassning.linreg import *

plt.style.use("bmh")

x, y = np.loadtxt("data.dat", unpack=True)

# avgjør regresjonskoeffisientene, y(x)=a_0 + a_1 * x, samt en vektor D_y, som er avviket delta_y = y_i-f(x_i)
a_0, a_1, f, D_y = lineær_regresjon(x, y, y_func=lambda x: x)

x_kont = np.linspace(min(x), max(x), 1000)

# fig1 er regresjonsanalysen, mens fig2 viser avviket
fig1, ax1 = plt.subplots(1)
fig2, ax2 = plt.subplots(1)

ax1.plot(x, y, "x", ms=4)
ax1.set_xlabel("$I\,[\mathrm{A}]$", fontsize=18)
ax1.set_ylabel("$m\,[\mathrm{g}]$", fontsize=18)
ax1.set_title("Vekt som funksjon av strøm", fontsize=18)
ax1.plot(x_kont, f(x_kont), lw=2)
ax1.legend(("$I_{målt}$", "$I_{reg}$"), fontsize=18)

ax2.plot(x, D_y, "x", color="k")
ax2.set_xlabel("$I\,[\mathrm{A}]$", fontsize=18)
ax2.set_ylabel("$m\,[\mathrm{g}]$", fontsize=18)
ax2.set_title("Avvik", fontsize=18)
ax2.legend(("$I_{målt}$", "$I_{reg}$"), fontsize=18)

plt.tight_layout()
plt.show()

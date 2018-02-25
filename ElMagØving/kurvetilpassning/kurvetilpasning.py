# Skrevet av Martin Johnsrud, 25/02-2018
# Dette scriptet har til hensikt å drive kurvetilpassning å regresjonsanalyse
import numpy as np
from matplotlib import pyplot as plt
import os
os.chdir("C:/Users/Martin/Google Drive/slange/")
from main.numerikk import liner_regresjon
os.chdir("C:/Users/Martin/Google Drive/slange/ElMagØving/kurvetilpassning")

plt.style.use("bmh")

x, y = np.loadtxt("data.dat", unpack=True)

a_0, a_1, f, D_y = liner_regresjon(x, y, y_func=lambda x: x)

x_kont = np.linspace(min(x)-5, max(x)*2, 1000)

fit = np.polyfit(x, y, deg=5)
print(fit)

fig1, ax1 = plt.subplots(1)
fig2, ax2 = plt.subplots(1)

ax1.plot(x, y, "x", ms=4)
ax1.set_xlabel("$I\,[A]$", fontsize=18)
ax1.set_ylabel("$m\,[g]$", fontsize=18)
ax1.set_title("Vekt som funksjon av strøm", fontsize=18)
ax1.plot(x_kont, f(x_kont), lw=2)
ax1.plot(x_kont, fit[5] + fit[4]*x_kont + x_kont**2 *fit[3] + x_kont**3 *fit[2] + x_kont**4 *fit[1] + x_kont**5 *fit[0], color='red')
ax1.legend(("$I_{målt}$", "$I_{reg}$"), fontsize=18)

ax2.plot(x, D_y,)
ax2.set_xlabel("$I\,[A]$", fontsize=18)
ax2.set_ylabel("$m\,[g]$", fontsize=18)
ax2.set_title("Avvik", fontsize=18)
ax2.legend(("$I_{målt}$", "$I_{reg}$"), fontsize=18)

plt.tight_layout()
plt.show()

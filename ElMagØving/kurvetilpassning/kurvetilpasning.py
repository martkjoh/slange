# Skrevet av Martin Johnsrud, 25/02-2018
# Dette scriptet har til hensikt å drive kurvetilpassning å regresjonsanalyse
import numpy as np
from matplotlib import pyplot as plt
import os
os.chdir("C:/Users/Martin/Google Drive/slange/")
from main.numerikk import liner_regresjon
os.chdir("C:/Users/Martin/Google Drive/slange/ElMagØving/kurvetilpassning")

x, y = np.loadtxt("data.dat", unpack=True)
#x, y = np.loadtxt("sinus.dat", unpack=True)

# Gjøres kurvetilpasning til en funksjon av a_0 + a_1 * y_func(x)

a_0, a_1, f, D_y = liner_regresjon(np.sin(x), y, y_func=lambda x: x)

labels1 = ["$I\,[A]$", "$m\,[g]$", "Vekt som funksjon av strøm", "$I_m$", "$I_t$", "$\Delta m$"]
labels2 = ["$\theta$", "$F\,[N]$", "Vekt som funksjon av strøm", "$\theta_m$", "$\theata_t$", "$\Delta F$"]
labels = labels1

x_kont = np.linspace(min(x), max(x), 1000)

fig1, ax1 = plt.subplots(1)
fig2, ax2 = plt.subplots(1)

ax1.plot(x, y, "x", ms=4)
ax1.set_xlabel(labels[0])
ax1.set_ylabel(labels[1])
ax1.set_title(labels[2])
ax1.plot(x_kont, f(x_kont), lw=2)
ax1.legend((labels[3], labels[4]))

ax2.plot(x, D_y, "x")
ax2.set_xlabel(labels[0])
ax2.set_ylabel(labels[1])
ax2.set_title(labels[2])
ax2.legend((labels[-1],))

plt.tight_layout()
plt.show()

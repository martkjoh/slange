# Skrevet av Martin Johnsrud, 25/02-2018
# Dette scriptet har til hensikt å drive kurvetilpassning å regresjonsanalyse
import numpy as np
from matplotlib import pyplot as plt
import os
os.chdir("C:/Users/Martin/Google Drive/slange/")
from main.numerikk import liner_regresjon
os.chdir("C:/Users/Martin/Google Drive/slange/ElMagØving/kurvetilpassning")
plt.style.use("bmh")
print(plt.style.available)

theta, y = np.loadtxt("sinus.dat", unpack=True)

x_kont = np.linspace(min(theta), max(theta), 1000)
sintheta = (np.sin(theta))
a_0, a_1, f, D_y = liner_regresjon(sintheta, y, y_func=lambda x: np.sin(x))

fig1, ax1 = plt.subplots(1)
fig2, ax2 = plt.subplots(1)


theta_fit = np.linspace(min(theta), max(theta))
sin_theta_fit = f(theta_fit)
ax1.plot(theta, y, "x", ms=10)
ax1.set_xlabel("$\\theta$", fontsize=18)
ax1.set_ylabel("$F\,[N]$", fontsize=18)
ax1.set_title("Kraft som en funksjon av vinkel", fontsize=15)
ax1.plot(theta_fit, sin_theta_fit, lw=2)
ax1.legend(("$F_{målt}$", "$F_{reg}$"))

ax2.plot(sintheta, y, "x", ms=10)
ax2.plot(sintheta, f(theta), lw=2)
ax2.set_xlabel("$\\sin(\\theta)$", fontsize=18)
ax2.set_ylabel("$F\,[N]$", fontsize=18)
ax2.set_title("Kraft som en funksjon av sinus til vinkel", fontsize=15)
ax2.legend(("$F_{målt}$", "$F_{reg}$"), fontsize=18)

plt.tight_layout()
plt.show()

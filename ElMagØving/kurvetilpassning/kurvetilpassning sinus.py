# Skrevet av Martin Johnsrud, 25/02-2018
# Dette scriptet har til hensikt å drive kurvetilpassning å regresjonsanalyse
import numpy as np
from matplotlib import pyplot as plt
from ElMagØving.kurvetilpassning.linreg import *

plt.style.use("bmh")

theta, y = np.loadtxt("sinus.dat", unpack=True)
sintheta = (np.sin(theta))

# Utfører regresjonanalyse, og returnerer regresjonskoeffesienter, en funksjon av form y(x) = a_0 + a_1 * sin(theta),
# og avviket i en vektor D_y
f, D_y = lineær_regresjon(theta, y, y_func=lambda x: np.sin(x))

# fig1 viser y som en funksjon av theta, både måleverider og verdier fra regresjonsanalysen
# fig2 viser y som en funksjon av sin(theta), både måleverdier og verdier fra reg.an.
fig1, ax1 = plt.subplots(1)
fig2, ax2 = plt.subplots(1)

# 'Kontinuerlig' verider for theta
theta_fit = np.linspace(min(theta), max(theta))
sin_theta_fit = f(theta_fit)

ax1.plot(theta, y, "x", ms=10)
ax1.set_xlabel("$\\theta$", fontsize=18)
ax1.set_ylabel("$F\,[N]$", fontsize=18)
ax1.set_title("Kraft som en funksjon av vinkel", fontsize=15)
ax1.plot(theta_fit, sin_theta_fit, lw=2)
ax1.legend(("$F_{målt}$", "$F_{reg}$"), fontsize=18)

ax2.plot(sintheta, y, "x", ms=10)
ax2.plot(sintheta, f(theta), lw=2)
ax2.set_xlabel("$\\sin(\\theta)$", fontsize=18)
ax2.set_ylabel("$F\,[N]$", fontsize=18)
ax2.set_title("Kraft som en funksjon av sinus til vinkel", fontsize=15)
ax2.legend(("$F_{målt}$", "$F_{reg}$"), fontsize=18)

plt.tight_layout()
plt.show()

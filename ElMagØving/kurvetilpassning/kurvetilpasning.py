# Skrevet av Martin Johnsrud, 25/02-2018
# Dette scriptet har til hensikt å drive kurvetilpassning å regresjonsanalyse
import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt("data.dat", unpack=True)
sinus = np.loadtxt("sinus.dat", unpack=True)

N_d = len(data[0])
S_x = np.sum(data[0])
S_y = np.sum(data[1])
S_xx = np.sum(data[0]**2)
S_xy = np.sum(data[0] * data[1])
delta = N_d * S_xx - S_x ** 2
a_0 = (S_y * S_xx - S_x * S_xy) / delta
a_1 = (N_d * S_xy - S_x * S_y) / delta


def f(x):
    return a_0 + a_1 * x

D_y = f(data[0]) - data[1]
S = sum(D_y**2)

print(a_0, a_1)
Da_0 = np.sqrt(1 / (N_d - 2) * (S * S_xx) / delta)
Da_1 = np.sqrt(N_d / (N_d - 2) * S / delta)
print(Da_0, Da_1)
x = np.linspace(0, max(data[0]), 1000)

print(S_x, S_y)

fig1, ax1 = plt.subplots(1)
fig1, ax2 = plt.subplots(2)

ax1.plot(data[0], data[1], "x", ms=4)
ax1.set_xlabel("$I\,[A]$")
ax1.set_ylabel("$m\,[g]$")
ax1.set_title("Vekt som funksjon av strøm")
ax1.plot(x, f(x), lw=2)
ax1.legend(("$I_m$", "$I_t$"))
#ax[1].plot(sinus[0], sinus[1], ".")

plt.tight_layout()
plt.show()

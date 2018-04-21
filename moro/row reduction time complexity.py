import numpy as np
from matplotlib import pyplot as plt
from ElMagØving.kurvetilpassning.linreg import *

n, t = np.loadtxt("nxn matrise row reduce", unpack=True)

f, D = lineær_regresjon(n, t, lambda x: x**4)

x = np.linspace(0, len(n), 1000)
fig, ax = plt.subplots(2, sharex=True)
ax[0].plot(n, t, ".")
ax[0].plot(x, f(x))
plt.xlabel("Størrelsen på $n\\times n$ matrisa")
plt.ylabel("Tid, [s]")
ax[1].plot(n, D)
ax[0].legend(("Tid for å utføre row reduce på en $n \\times n$ matrise", "kurvetilpasning $a_0 + a_1 n^4$"))
ax[1].legend(("Avvik",))
ax[0].grid(True)
ax[1].grid(True)
# 9925.269708493684
print(f(600)/60/60)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


fig=plt.figure()
V_0 = 0
################################### Experimental data
volum, potensial = np.loadtxt("data.txt", skiprows=1, unpack=True)
volum -= V_0

################################### Plot
plt.figure()
plt.plot(volum, potensial, "-x", marker="x", markeredgecolor="k")

################################### save plot
plt.ylabel('$E$ [mV]')
plt.xlabel('$V$ [ml]')
plt.savefig('plot_lab8.pdf')
plt.show()

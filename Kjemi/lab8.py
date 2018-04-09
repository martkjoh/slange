import matplotlib.pyplot as plt
import numpy as numpy


fig=plt.figure()

################################### Experimental data
Volum = [15.7, 20.4, 26, 31.6, 36.8, 42.2, 47.1]  # ml
Volum = [v-Volum[0] for v in Volum]
Potential = [-131, -129, -115, 0, 180, 190, 204]  # mV

################################### Plot
plt.plot(Volum, Potential, "-x", marker="x", markeredgecolor="k")

################################### save plot
plt.ylabel('$E$ [mV]')
plt.xlabel('$V$ [ml]')
plt.savefig('plot_lab8.pdf')
plt.show()

import numpy as np
import matplotlib.pyplot as plt


x_dag, x_tid, y = np.loadtxt("C:\\Users\\Martin\\Google Drive\\Mat og drikke\\--navn kommer--v.2\\plupp pr sek.tsv", comments="#", unpack=True, dtype=str)

y = np.array(y, dtype="float32")
x_dag = np.array(x_dag, dtype="float32")
x_tid = np.array([a.split(":") for a in x_tid])
x_tid = np.array([int(a[0]) * 60 + int(a[1]) for a in x_tid])
x = 24*60 * x_dag + x_tid

a = np.polyfit(x, y, 3)

x_2 = np.linspace(0, x[-1], 100)
y_2 = a[3] + a[2]*x_2 + a[1]*x_2**2 + a[0]*x_2**3
plt.plot(x, y, "-x")
plt.plot(x_2, y_2)
plt.show()

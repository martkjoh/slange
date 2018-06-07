import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("C:\\Users\\Martin\\Google Drive\\slange")
from Søppel.ElMagØving.kurvetilpassning.linreg import *


def get_data():

    a, b = np.loadtxt("C:\\Users\\Martin\\Google Drive\\Mat og drikke\\--navn kommer--v.2\\oecshle data.txt", unpack=True, dtype=str)
    a = np.array([float(x.replace(",", ".")) for x in a])
    b = np.array([float(x.replace(",", ".")) for x in b])

    return a, b 


a, b = get_data()

g = lambda t: t

A = g(np.concatenate([[a], [np.ones_like(a)]], axis=0).T)
b = np.array(b).T
x = np.dot(np.linalg.inv(np.dot(A.T, A)), np.dot(A.T, b))

f = lambda t: x[1] + x[0] * g(t)

print(x[1], x[0])

plt.plot(a, b, "X")
plt.plot(np.linspace(a[0], a[-1], 100), f(np.linspace(a[0], a[-1], 100)))
plt.show()

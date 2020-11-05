import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("C:\\Users\\Martin\\Google Drive\\slange")
from Søppel.ElMagØving.kurvetilpassning.linreg import *


def get_data():

    x_dag, x_tid, y = np.loadtxt("C:\\Users\\Martin\\Google Drive\\Mat og drikke\\--navn kommer--v.2\\plupp pr sek.csv", unpack=True, dtype=str, delimiter=",")

    y = np.array(y, dtype="float32")
    x_dag = np.array(x_dag, dtype="float32")
    x_tid = np.array([a.split(":") for a in x_tid])
    x_tid = np.array([int(a[0]) * 60 + int(a[1]) for a in x_tid])
    x = 24*60 * x_dag + x_tid

    a, b = x[:], y[:]
    return a, b 


a, b = get_data()

g = lambda t: t

A = g(np.concatenate([[a], [np.ones_like(a)]], axis=0).T)
b = np.array(b).T
x = np.dot(np.linalg.inv(np.dot(A.T, A)), np.dot(A.T, b))

f = lambda t: x[1] + x[0] * g(t)

plt.plot(a, b, "X")
plt.plot(np.linspace(a[0], a[-1], 100), f(np.linspace(a[0], a[-1], 100)))
plt.show()

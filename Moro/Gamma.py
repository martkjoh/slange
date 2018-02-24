from math import gamma

from matplotlib import pyplot as plt
import sys
sys.setrecursionlimit(1500)


def Γ(z, aprox=10000):
    y = 1
    for n in range(1, aprox + 1):
        y *= ((1 / (1 + z/n)) * (1 + 1/n)**z)
    return y


def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fact(n - 1) * n


z = [z/100 for z in range(1, 1000)]
y = [Γ(z) for z in z]
y_2 = [gamma(z) for z in z]
x = [x for x in range(8)]
f = [fact(x) for x in x]

#plt.semilogy()
plt.grid()
plt.plot(z, y, label="hejemmelaga")
plt.plot(z, y_2, label="innebygd")
plt.plot(x, f, label="fact")
plt.legend()
plt.show()

from main.numerikk import *
from matplotlib import pyplot as plt
from math import sin


def g(x, y):
    try:
        return sin(x)*sin(y)
    except:
        return 0
    # 2*x /(1 + y**2)

colors = ["blue", "cyan"]

for a in range(0, 10, 1):
    x, y = eulers_metode(g, -10, a, 10, 0.01)
    if a > 1:
        plt.plot(x, y)
    x, y = eulers_metode(g, -10, -a, 10, 0.01)
    if a > 1:
        plt.plot(x, y)


plt.show()

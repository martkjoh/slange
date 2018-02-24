from matplotlib import pyplot as plt
from math import pi, e, cos, sin


# Gitt en funksjon på formen dy/dx = f(x, y)
def f(x, y):
    return x - y

# Kan pluggen in analytisk løsning for å sammenligne med
def f_ana(x):
    return x + 2 * e**(-x) - 1


def eulers_method(func, x_0, y_0, h, n):
    x = [x_0]
    y = [y_0]
    x_n = x_0
    y_n = y_0
    for a in range(n - 1):
        x_np1 = x_n + h
        y_np1 = y_n + h*(func(x_n, y_n))
        x.append(x_np1)
        y.append(y_np1)
        x_n = x_np1
        y_n = y_np1
    return x, y


#x, y = eulers_method(0, 1, 0.1, 100)

#for i, a in enumerate(x):
#    print(format(a, ".2f"), format(y[i], ".6f"))

#plt.plot(x, y)
#plt.plot(x, [f_ana(x) for x in x])
#plt.show()

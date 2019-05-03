import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + 12 * x**2)

def NDD(f, x, n):

    # y[x_a ... x_(a + b)] = y[a, b]
    y = np.zeros((n, n))
    y[:,0] = f(xSample)

    for i in range(1, n + 1):
        for j in range(n - i):
            y[j, i] = (y[j + 1, i - 1] - y[j,  i - 1]) / (x[j + i] - x[j])

    def P(x, n):
        s = y[0, 0]
        for i in range(1, n):
            p = y[0, i]
            for j in range(i):
                p *= (x - xSample[j])
            s += p
        return s

    return P

n = 11
xRange = 1
xSample = (np.random.rand(n) - 0.5) * 2 * xRange
xSample = np.linspace(-xRange, xRange, n)
xSample.sort()
# xSample = np.linspace(-xRange, xRange, n)

P = NDD(f, xSample, n)

xKont = np.linspace(-xRange, xRange, 100)
plt.plot(xSample, f(xSample), "xr")
plt.plot(xKont, f(xKont))
plt.plot(xKont, P(xKont, n))

plt.show()
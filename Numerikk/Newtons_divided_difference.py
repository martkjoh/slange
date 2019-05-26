import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + 12 * x**2)
    # return x**2 + x - 1

def NDD(f, x, n):
    # L[x_a ... x_(a + b)] = y[a, b]
    y = np.zeros((n, n))
    y[:,0] = f(x)
    for i in range(1, n + 1):
        for j in range(n - i):
            y[j, i] = (y[j + 1, i - 1] - y[j,  i - 1]) / (x[j + i] - x[j])

    return y[0, :]

n = 5
x = np.linspace(1, n, n)
L = NDD(f, x, n)

def P(x0):
    s = L[0]
    for i in range(1, n):
        p = L[i]
        for j in range(i):
            p *= (x0 - x[j])
        s += p
    return s

C = np.zeros((n, n))
C[0, 0] = 1
for i in range(1, n):
    C[i, i] = 1
    C[0, i] = - C[0, i - 1] * x[i]
    for j in range(1, i - 1):
        C[j, i] = - C[j, i - 1] * x[i] + C[j - 1, i - 1]
    print(C)


A = C @ L
X = np.zeros(n)
print(A)
print(L)

def G(x0):
    s = 0
    for i in range(n):
        s += A[i] * x0**i
    return s

xKont = np.linspace(1, n, 100)
plt.plot(xKont, P(xKont))
plt.plot(x, f(x), "xr")
plt.plot(xKont, G(xKont))

plt.show()
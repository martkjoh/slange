import numpy as np
import matplotlib.pyplot as plt

# parameters
# Number of times to run the iterationn
N = 10
# Resolution
M = 3000
# Threashold
thresh = 2
# The boundaries of the values to check
im = 1.2
re = 2
x = np.linspace(-2, 1, M)
y = np.linspace(-im, im, M)
vals = np.empty((M, M))

def f(z, c):
    return z**2 + c

def findDiv(c):
    z = f(0, c)
    for i in range(N):
        z = f(z, c)
        if abs(z) > thresh:
            return abs(z)
    else:
        return 0

for i in range(M):
    for j in range(M):
        vals[j, i] = findDiv(x[i] + 1j * y[j])

plt.imshow(vals)
plt.savefig("mandel.pdf")
plt.show()

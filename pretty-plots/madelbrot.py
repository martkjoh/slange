import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# parameters
# Number of times to run the iterationn
N = 100
# Resolution
M = 1000
# Threashold
thresh = 2
# The boundaries of the values to check
im = 1
re = 2
x = np.linspace(-2, 1, M).astype(np.float64)
y = np.linspace(-im, im, M).astype(np.float64)
x, y = np.meshgrid(x, y)
c = x + y * 1j

def f(z, c):
    return z**2 + c

def findDiv(c):
    z = f(0.9, c)
    mesh = np.greater(abs(z), thresh).astype(int)
    vals = mesh
    for i in range(1, N):
        z = f(z, c)
        mesh = np.greater(abs(z), thresh).astype(int)
        vals += mesh
        print(i)
    
    return vals 

vals = findDiv(c)

plt.imshow(vals, cmap = cm.coolwarm)
plt.savefig("mandel.pdf")
plt.show()

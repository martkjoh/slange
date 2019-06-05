import numpy as np
from numpy import exp, sqrt
from scipy.special import laguerre, gamma
from matplotlib import pyplot as plt
from matplotlib import cm

n = 10
x = np.linspace(0.01, 30, 500)
for i in range(n):
    plt.plot(x, exp(- x / i) * laguerre(i)(2 * x / i) / i**2, color = cm.viridis(i /n))
plt.show()
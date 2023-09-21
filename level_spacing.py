#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn_zeros

from matplotlib import cm
from matplotlib.colors import LogNorm
from matplotlib.animation import FuncAnimation as FA

plt.rc("font", family="serif", size=16)
plt.rc("mathtext", fontset="cm")
plt.rc("lines", lw=2)
plt.rc("axes", grid=True)

#%%
def E(n):
    return n

 
N = 1000
nn = np.linspace(1, N, N)
DEs = []
for i in range(N):
    for j in range(i, N):
        DE = np.abs(E(nn[i]) - E(nn[j]))
        DEs.append(DE)

DEs = np.array(DEs)
plt.hist(DEs, bins=N, density=True)

a = 3e-6
b = np.max(DEs)
x = np.linspace(0, b)
# plt.loglog(x,  a * np.exp((-a*x)))
plt.show()
# %%
def E(n):
    return n**2
 
N = 1000
nn = np.linspace(1, N, N)
DEs = []
for i in range(N):
    for j in range(i, N):
        DE = np.abs(E(nn[i]) - E(nn[j]))
        DEs.append(DE)

DEs = np.array(DEs)
plt.hist(DEs, bins=N, density=True)

a = 3e-6
b = np.max(DEs)
x = np.linspace(0, b)
# plt.loglog(x,  a * np.exp((-a*x)))
plt.show()
#%%
def E(n, m):
    return jn_zeros(n, m)**2
 
N = 100
nn = np.linspace(1, N, N)
DEs = []
for i in range(N):
    for j in range(N):
        DE = np.abs(E(i, N) - E(j, N))
        DEs.append(DE)

DEs = np.array(DEs)
DEs = DEs.flatten()
plt.hist(DEs, bins=N, density=True)

a = 1.8e-4
b = np.max(DEs)
x = np.linspace(0, b)
plt.plot(x,  a * np.exp((-a*x)))
plt.show()
# %%

aa = [.5, 1., 1.2, 1.5]
rho = lambda a, r : (1 - a**2 / np.sqrt(1 + (2 * a * r)**2))

for a in aa:
    if a < 1: 
    else: mi =  np.sqrt(np.abs(a**2 - 1))
    ma = np.sqrt(a**2 + 1)
    r = np.linspace(mi, ma)
    plt.plot(r, rho(a, r))


# %%

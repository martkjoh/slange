
#%%

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib import colors
from matplotlib.animation import FuncAnimation as FA

plt.rc("font", family="serif", size=16)
plt.rc("mathtext", fontset="cm")
plt.rc("lines", lw=2)
plt.rc("axes", grid=True)



def Psi(m, h, par):
    return par[0]*m**2/2 + par[1] * m**4 + par[2] * m**6 - h*m


#%%
fig, ax = plt.subplots(figsize=(30, 15))
n = 1000
m = np.linspace(-1.,0, n)


N = 10
ts = np.linspace(-.1, 2/3, N)

for i, t in enumerate(ts):
    c = cm.viridis(i/N)
    u, v = -1, 1
    p = Psi(m, 0, (t, u, v))
    ax.plot(m, p, color=c)
    
    I = np.argmin(p)
    ax.plot(m[I], p[I], "ko")

    mp = -np.sqrt( (-4*u + np.sqrt((4*u)**2 - 4*6*v*t))/(12*v) )
    mm = -np.sqrt( (-4*u - np.sqrt((4*u)**2 - 4*6*v*t))/(12*v) )
    ax.plot(mp, Psi(mp, 0, (t, u, v)), "rx")
    ax.plot(mm, Psi(mm, 0, (t, u, v)), "bx")

norm = colors.Normalize(vmin=ts[0], vmax=ts[-1])
cmap = cm.ScalarMappable(norm=norm, cmap=cm.viridis)
cb = fig.colorbar(cmap, ax=ax, label="t")

plt.show()

  # %%
print(np.sqrt(1/2))
# %%

u, v = 1, 1

fig, ax = plt.subplots(figsize=(30, 15))
n = 1000
m = np.linspace(-.5, 0, n)


N = 100
ts = np.linspace(-1, 1, N)

for i, t in enumerate(ts):
    c = cm.viridis(i/N)
    p = Psi(m, 0, (t, u, v))
    ax.plot(m, p, color=c)
    
    I = np.argmin(p)
    ax.plot(m[I], p[I], "ko")

    mp = -np.sqrt( (-4*u + np.sqrt((4*u)**2 - 4*6*v*t))/(12*v) )
    mm = -np.sqrt( (-4*u - np.sqrt((4*u)**2 - 4*6*v*t))/(12*v) )
    ax.plot(mp, Psi(mp, 0, (t, u, v)), "rx")
    ax.plot(mm, Psi(mm, 0, (t, u, v)), "bx")

norm = colors.Normalize(vmin=ts[0], vmax=ts[-1])
cmap = cm.ScalarMappable(norm=norm, cmap=cm.viridis)
cb = fig.colorbar(cmap, ax=ax, label="t")

plt.show()

# %%
fig, ax = plt.subplots(figsize=(30, 15))

n = 200
m = 500
ts = np.linspace(-1, 1, n)
us = np.linspace(-1, 1, n)
m = np.linspace(-1.1, 0, m)
v = 1
m_min = np.empty((n, n))


for i, t in enumerate(ts):
    for j, u in enumerate(us):
        p = Psi(m, 0, (t, u, v))
        I = np.argmin(p)
        m_min[i, j] = m[I]


ax.pcolormesh(ts, us, m_min)
u = np.linspace(-1, 0)
ax.plot(u, u**2/2, '--k')
plt.plot()
# %%

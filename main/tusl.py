import matplotlib as mpl
from matplotlib import cm
from matplotlib.animation import FuncAnimation as anim
import matplotlib.pyplot as plt
import scipy.linalg as la
import numpy as np
from numpy import pi

font = {'family' : 'serif', 
        'weight' : 'normal', 
        'size'   : 25}
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
plt.rc("lines", lw=2)
plt.rc('font', **font)

def solveTUSL(v, LStar):
    
    # Hjj are diagonal values, HOD are of the diagonal
    deltaq = LStar / (len(v) + 1)
    Hjj = 2 / deltaq**2 * np.ones(len(v)) + v
    HOD = -1 / deltaq**2 * np.ones(len(v) - 1)
    return la.eigh_tridiagonal(Hjj, HOD)

def makeChrystal(Nw, v0, w=10, b=3, B=10):
    v = np.zeros(B * w)
    if Nw:
        v = np.concatenate((v, v0 * np.ones(w)))    
    for i in range(Nw - 1):
        v = np.concatenate((v, np.zeros(b), v0 * np.ones(w)))
    v = np.concatenate((v, np.zeros(B * w)))

    LStar = len(v) / w
    q = np.linspace(0, LStar, len(v))
    eps, psi = solveTUSL(v, LStar)
    return eps, psi, v, q

def f(q, var, p0, q0):
    return (2 * np.pi * var)**(-1/4) * np.exp(-(q - q0)**2 / (4 * var) + 1j * p0 * (q - q0))

def getPsi(eps, psi, v, q, f, p0, q0, var):
    if q0 is None:
        q0 = q[-1]/2 
    c = psi.T @ f(q, var, p0, q0)
    Psi = lambda t: psi @ (c * np.exp(-1j*eps*t))
    return Psi, c


Nw = 1
v0 = 40


fig, ax = plt.subplots(figsize=(18, 10))

def animate(n):
    ax.cla()
    eps, psi, v, q = makeChrystal(Nw, v0, w = 10 * n, b = 2* n % 10 + 10)
    l = ax.plot(q, v, "k")
    l += ax.plot(q, (psi[:, 10]) * 10 * v0, "--")
    l += ax.plot(q, (psi[:, 9]) * 10 * v0, "--")
    l += ax.plot(q, (psi[:, 10] + psi[:, 9]) * 5 * v0)
    return l,

# a = anim(fig, animate, interval = 2000)
eps, psi, v, q = makeChrystal(Nw, v0, w = 10, b = 38, B = 20)
ax.plot(q, v, "k")
ax.plot(q, (psi[:, 10]) * 10 * v0, "--")
ax.plot(q, (psi[:, 11]) * 10 * v0, "--")
ax.plot(q, (psi[:, 10] + psi[:, 11]) * 5 * v0)
plt.show()

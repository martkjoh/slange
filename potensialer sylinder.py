from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from numpy import pi, e, cos, sin, sqrt, arctan
from numpy import log as ln


U = 1
K = 2
a = 3
p = U*a**2
def phi_1(theta, r):
    return -p/r * np.cos(theta)

def phi_2(theta, r):
    return -K * ln(r)

def phi_3(theta, r):
    return -p/r * sin(theta)

def phi_4(theta, r):
    return U*r*sin(theta)

def phi_sup(theta, r):
    return phi_4(theta, r) + phi_3(theta, r) + phi_2(theta, r) - ln(a)

def phi(theta, r):
    return U*(r - a**2/r)*sin(theta) - K*ln(r/a)

def Phi(x, y):
    return arctan()

r = np.linspace(0, 10, 1000)
theta = np.linspace(0, 2*pi, 1000)
R, T = np.meshgrid(r, theta)
fig = plt.figure()
ax = plt.subplot(111, projection="polar")

ax.contour(T, R, phi_sup(T, R), np.linspace(-10, 10, 20))
zero = ax.contour(T, R, phi(T, R), [0], colors="red", label="$\Psi = 0$")
plt.clabel(zero, manual=[(pi/2,3), (pi/4, 7)])


plt.show()

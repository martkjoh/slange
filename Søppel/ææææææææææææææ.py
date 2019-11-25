import numpy as np
from numpy import pi, cos, exp, sin
from cmath import sqrt
import matplotlib.pyplot as plt
from matplotlib import cm

font = {
    'family' : 'serif', 
    'weight' : 'normal', 
    'size'   : 16
}
    
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
plt.rc("lines", lw = 1.5)
plt.rc('font', **font)
plt.rc("legend", fontsize = 12)


# Implementation of the analytical solution, given parametres an initial conditions
# Initial condititions and w0 is set in the first code box (?) and never touched after

def getTheta(q, *inits):
    (theta_0, thetaDot_0) = inits
    # Checkin assumption 1
    if q/2 == w0:
        print("Critically damped")
        return lambda x : theta_0 * exp(- x*q/2) * (1 + x*(q / 2 + thetaDot_0 / theta_0))
    
    if w0 > q / 2:
        # Checking assumption 2.1
        w = sqrt(w0**2 - (q/2)**2)
        assert(w.imag == 0 and not (w == 0))
        print("Underdamped")
        
        C = sqrt(theta_0**2 + ((theta_0*q / 2 - thetaDot_0) / w)**2)
        phi = np.arctan2(-((-theta_0*q / 2 + thetaDot_0) / w).real, (theta_0).real)
        return lambda x :  C * exp(- x*q/2) * cos(w*t - phi)

    # Checking assumption 2.2
    z = sqrt((q/2)**2 - w0**2)
    assert(z.imag == 0 and not (z == 0))
    print("Overdamped")
    
    lambda_p = -q/2 + z
    lambda_m = -q/2 - z
    A = (theta_0 * lambda_m - thetaDot_0) / (lambda_m - lambda_p)
    B = (theta_0 * lambda_p - thetaDot_0) / (lambda_p - lambda_m)
    return lambda x: exp(- x*q/2) * (A * exp(z*x) + B * exp(-z*x))

def RK4(y, f, dt, i, *args):
    k1 = f(y[i], *args) * dt
    k2 = f(y[i] + k1 / 2, *args) * dt
    k3 = f(y[i] + k2 / 2, *args) * dt
    k4 = f(y[i] + k3, *args) * dt
    y[i + 1]  = y[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

def fd(y, *args):
    t, q, wd = args
    
    return np.array([
        y[1], 
        -q * y[1] - w0**2 * y[0] + Fd * sin(wd * t)
    ])

def f(y, *args):
    (q,) = args
    return np.array([
        y[1],
        -q * y[1] - w0**2 * y[0]
    ])

def theta_n(t, q, wd):
    return Fd / ((w0**2 - wd**2)**2 + (q*wd)**2) * (-q*wd*cos(wd * t) + (w0**2 - wd**2) * sin(wd * t))

def init(q, wd):
    A = Fd / ((w0**2 - wd**2)**2 + (q * wd)**2)
    return (q, theta_0 + A*q*wd, A*(w0**2 - wd**2) * wd)


m = 1
l = 2
g = 9.81
w0 = abs(sqrt(g / l / m))
theta_0 = 0.2
thetaDot_0 = 0
Fd = 0.2

T = 10
n = 1001
t = np.linspace(0, T, n)
dt = t[1] - t[0]
print("dt = : {}".format(dt))

wd = 0
q = 1

y = np.empty((n, 2))
y0 = np.array([theta_0, thetaDot_0])
y[0] = y0
for wd in np.linspace(0.1, 4*w0, 10):
    y = np.empty((n, 2))
    y0 = np.array([theta_0, thetaDot_0])
    y[0] = y0
    for j in range(n-1): RK4(y, fd, dt, j, t[j], q, wd)

    plt.plot(t, getTheta(*init(q, wd))(t) + theta_n(t, q, wd), "r")
    plt.plot(t, y[:, 0], "k--")
    plt.title("$w_d = ${}".format(wd))
    plt.show()

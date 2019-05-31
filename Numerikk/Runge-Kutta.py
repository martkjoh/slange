import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as anim
from mpl_toolkits.mplot3d import Axes3D

def RKStep(f, w0, a, b, h):
    F = np.zeros((len(w0), len(a)))
    for i in range(len(a)):
        F[:,i] = f(*(w0 + h * (F @ a[i].T)))
    return w0 + h * (F @ b)

# rk4
A = np.array([
    [0, 0, 0, 0],
    [0.5, 0, 0, 0],
    [0, 0.5, 0, 0],
    [0, 0, 1, 0]])

b = [1/6., 1/3., 1/3., 1/6.]

# euler
Ae = np.array([[0]])
be = np.array([1])

# (x, y, z)' = f(x, y, z)
def f(x, y, z):
    s = 10
    r = 28
    b = 8/5.
    return np.array([-s*x + s*y, -x*z + r*x - y, x*y - b*z], dtype=np.float)

def setAx(ax):
    ax.cla()
    ax.set_zlim(10, 40)
    ax.axis((-20, 20, -20, 20))
    ax.set_axis_off()

def y(n):
    global ys, ye, ax
    setAx(ax)
    ys = np.concatenate([ys, [RKStep(f, ys[-1], A, b, 0.01)]])
    ye = np.concatenate([ye, [RKStep(f, ye[-1], Ae, be, 0.01)]])
    return ax.plot(*ys.T) + ax.plot(*ye.T)

if __name__ == "__main__":
    ys = np.array([np.array([10, 0.1, 25.])])
    ye = np.copy(ys)
    fig = plt.figure()
    ax = Axes3D(fig)    
    a = anim(fig, y, interval = 10, blit = True)
    plt.show()
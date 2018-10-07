from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import pi
import scipy
from scipy import integrate


def main():

    def bølge(f, L, c, n):

        def b(n):

            return 2 / L * integrate.quad(lambda x: f(x) *  np.sin(p(n) * x), 0, L)[0]

        def p(n):
            return n*pi/L

        def u_n(x, t, n):
            return b(n) * np.sin(p(n) * x) * np.cos(p(n)**2 * c* t)

        def u(x, t, n):
            s = 0
            for i in range(1, n + 1):
                s += u_n(x, t, i)

            return s

        return u

    def varm_pinne(f, L, c, n): # u(0, t) = u(L, t) = 0

        def b(n):

            return 2 / L * integrate.quad(lambda x: f(x) *  np.sin(p(n) * x), 0, L)[0]

        def p(n):
            return n*pi/L

        def u_n(x, t, n):
            return b(n) * np.sin(p(n) * x) * np.exp(- p(n)**2 * c**2 * t)

        def u(x, t, n):
            s = 0
            for i in range(1, n + 1):
                s += u_n(x, t, i)

            return s

        return u


    def isolert_pinne(f, L, c, n):  # d_x u(0, t) = d_xu(L, t) = 0, isolert pinne


        a_0 = 1/L * integrate.quad(lambda x: f(x), 0, L)[0]

        def a(n):
            return 2 / L * integrate.quad(lambda x: f(x) *  np.cos(p(n) * x), 0, L)[0]

        def p(n):
            return n*pi/L

        def u_n(x, t, n):
            return a(n) * np.cos(p(n) * x) * np.exp(- p(n)**2 * c**2 * t)

        def u(x, t, n):
            s = a_0
            for i in range(1, n + 1):
                s += u_n(x, t, i)

            return s

        return u


    def f(x):
        return x**3 - L**2*x

    L = pi
    xs = np.linspace(0, L, 500)
    intervall = 0.001
    h = max(max(f(xs)), -min(f(xs)))
    c = 1
    k = 1
    n = 50

    fig = plt.figure()
    ax = plt.subplot(111) #Axes3D(fig)

    plt.xlim(0, L)
    plt.ylim(-h, h)

    u = bølge(f, L, c, n)


    def animate(m):

        t = m/100
        zs = u(xs, t, n)
        ys = np.zeros_like(xs)
        line = ax.plot(xs, zs, color="blue")
        return line

    plt.interactive(False)
    anim = animation.FuncAnimation(fig, animate, interval=intervall, blit=True)
    #ax.plot(xs, u(xs, 0, 50), label="$u(x, 0)$")

    plt.show()


main()

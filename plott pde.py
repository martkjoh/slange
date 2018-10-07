from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import pi
import scipy
from scipy import integrate


print("hello world")
# Animerer dataen
def main():

    L = pi
    h = 1
    dt = 0.01
    intervall = 1/dt
    c = 1
    k = 1
    n = 50

    fig = plt.figure()
    ax = plt.subplot(111) #Axes3D(fig)
    plt.xlim(0, L)
    plt.ylim(-h, h)
    xs = np.linspace(0, L, 100)

    def endimensjonal_bolge_Fourier():

        def B(n):
            #return 0
            #return 2 * k / (n*L)**2 * ( - np.sin(n*L/4) + np.sin(n*L*3/4))
            return 4*k / (n * L)**3 * ((-1)**n - 1)

        def B_astr(n):
            return 0
            #return 0.02 / (n**3 * L) * 2 * sin(L/2*n) * 100

        def u_n(x, t, n):
            return (B(n) * cos(c*pi*n*t/L) + B_astr(n) * np.sin(c*pi*n*t/L))*np.sin(n*pi*x/L)

        def u(x, t, n):
            s = 0
            for i in range(1, n + 1):
                s += u_n(x, t, i)

            return s

        return u


    def varm_pinne(): # u(0, t) = u(L, t) = 0

        def b(n):

            return 2 / L * integrate.quad(f(x) *  np.sin(p(n) * x), 0, L, args=(x))
            if n%2 == 0:
                return 0
            return h*L/(n**2*pi**2)*(-1)**(n+1)
            return 2*h/(n*L)*(1 - np.cos(n*pi))

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


    def isolert_pinne(f, L, c, n): # d_x u(0, t) = d_xu(L, t) = 0, isolert pinne

        def a(n, L):
            return 2/L integrate(f(x) * np.cos(p(n) * x), 0, L, args(x))

        def p(n):
            return n*pi/L

        def u_n(x, t, n):
            return a(n) * np.cos(p(n) * x) * np.exp(- p(n)**2 * c**2 * t)

        def u(x, t, n):
            s = 0
            for i in range(1, n + 1):
                s += u_n(x, t, i)

            return s

        return u

    def f(x):
        if x < 0 or x < L/2
            return x
        else:
            return L - x

    u = varm_pinne(f, L, c, n)


    def animate(m):

        #ax.cla()
        t = m*0.01
        zs = u(xs, t, n)
        ys = np.zeros_like(xs)
        line = ax.plot(xs, zs, color="blue")
        ax.set_xlim(0, L)
        ax.set_ylim(-h, h)
        return line


    plt.interactive(False)
    anim = animation.FuncAnimation(fig, animate, interval=intervall, blit=True)
    #plt.plot(xs, u(xs, 0, 50))

    plt.show()


main()

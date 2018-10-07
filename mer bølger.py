from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from math import sin, cos, pi


# Animerer dataen
def main():

    fig = plt.figure()
    ax = fig.add_subplot(111)
    lines = ax.plot([], [])
    plt.xlim(0, pi)
    plt.ylim(-1.5, 1.5)
    x1_var = np.linspace(0, 2*pi, 100)
    dt = 0.1
    intervall = 1/dt
    c = 1
    k = 2
    n = 10
    L = pi

    def B(n):
        return 0
        return 2 * k / (n*pi)**2 * ( - np.sin(n*pi/4) + np.sin(n*pi*3/4))
        return 4*k / (n * pi)**3 * ((-1)**n - 1)

    def B_astr(n):
        #return 0
        return 0.02 / (n**3 * pi) * 2 * sin(pi/2*n) * 100

    def u_n(x, t, n):
        return (B(n) * cos(c*pi*n*t/L) + B_astr(n) * np.sin(c*pi*n*t/L))*np.sin(n*pi*x/L)

    def u(x, t, n):
        s = 0
        for i in range(1, n+1):
            s += u_n(x, t, i)

        return s


    def init():
        return lines

    def animate(m):

        t = m*0.01
        y1_var = u(x1_var, t, n)
        lines[0].set_data(x1_var, y1_var)
        return lines


    plt.interactive(False)
    anim = animation.FuncAnimation(fig, animate, init_func=init, interval=intervall, blit=True)
    plt.plot(x1_var, u(x1_var, 0, 50))

    plt.show()


main()

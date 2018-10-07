from matplotlib import pyplot as plt
from matplotlib import animation
from math import sin, cos, pi


# Animerer dataen
def main():

    # Liste med alle labels
    labels = ["$y_1 = \sin(k_1x - \\omega_1t + \\phi_1)$",
              "$y_2 = \sin(k_1x - \\omega_1t + \\phi_1)$",
              "$y_1 + y_2$", "modulation wave"]

    # Lager en figur, samt akser
    fig1, (ax1, ax2) = plt.subplots(2, 1, sharex="all", sharey="all")

    # Konstruerer en liste med Line2D objekter
    lines = [ax1.plot([], [], label=labels[a])[0] for a in range(2)]
    lines.append(ax2.plot([], [], label=labels[2])[0])
    lines.append(ax2.plot([], [], label=labels[3])[0])
    lines.append(ax2.plot([], [], color="orange")[0])
    plt.xlim(0, 2 * pi)
    plt.ylim(-2, 2)

    # Permanente lister
    c = 20

    λ_1 = 0.11 * pi
    k_1 = 1 * pi / λ_1
    ω_1 = 10 * k_1
    φ_1 = 0
    dir_1 = 0       # 0 => høyre, 1 => venstre

    λ_2 = 0.1 * pi
    k_2 = 1 * pi / λ_2
    ω_2 = c * k_2
    φ_2 = 0
    dir_2 = 0

    dt = 0.1
    intervall = 1/dt

    Δk = -(k_1 - k_2)
    Δω = -(ω_1 - ω_2)

    print("v1 = ", ω_1 / k_1)
    print("v2 = ", ω_2 / k_2)

    x1_var = [x/k_1 * dt for x in range(int(2*pi*k_1*intervall) + 100)]

    def init():
        print("hei")
        return lines

    def animate(n):
        t = n*0.001
        y1_var = [sin((-1)**dir_1*k_1*x - ω_1*t + φ_1) for x in x1_var]
        y2_var = [sin((-1)**dir_2*k_2*x - ω_2*t + φ_2) for x in x1_var]
        y3_var = [y + y2_var[i] for i, y in enumerate(y1_var)]
        y4_var = [2*cos(Δk/2*x - Δω/2*t) for x in x1_var]

        lines[0].set_data(x1_var, y1_var)
        lines[1].set_data(x1_var, y2_var)
        lines[2].set_data(x1_var, y3_var)
        lines[3].set_data(x1_var, y4_var)
        lines[4].set_data(x1_var, [-x for x in y4_var])
        return lines

    plt.interactive(False)
    anim = animation.FuncAnimation(fig1, animate, init_func=init, interval=intervall, blit=True)

    ax1.legend(loc=1)
    ax2.legend(loc=1)
    plt.show()


main()

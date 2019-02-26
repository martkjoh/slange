from matplotlib import pyplot as plt
from matplotlib import animation
from math import sin, cos


# Genererer data
def theta():
    t_tot = 30  # Hvor lenge simuleringen kjører
    dt = 0.01   # Tidsintervall
    theta_0 = 0 # Startvinkel
    v = 3       # Startfart
    L = 1       # Lengde på pendel
    g = 9.81    # Tyngdeakselerasjon
    m = 1       # Masse til pendel
    c = 0.01    # Prop.koeff. for luftmotstand
    F_res = 10  # Ytre kraft
    a = 1.7     # Vinkelfart for ytre kraft
    phi = 0     # Faseforskyvning for ytre kraft
    x = []
    y = []
    k = []
    u = []

    def K(v):
        return (1 / 2) * m * v ** 2

    def U(theta):
        return m * g * L * (1 - cos(theta))

    for t in range(int(t_tot/dt)):
        F = \
            (
                -1 * m * g * sin(theta_0)           # Tyngdekraft
                + F_res * (sin(a * (t * dt) + phi)) # Ytre kraft
                - c * v                             # Luftmotstand
            )
        v = v + F / m * dt
        theta_0 = theta_0 + v/L * dt
        y.append(theta_0)
        x.append(t * dt)
        k.append(K(v))
        u.append(U(theta_0))
    return x, y, k, u


# Gjør klar all data, og lager Line2D objekter
def fetch_data():
    # Henter ut de forskjellige listene med data
    x1_var, y1_var, y2_var, y3_var = theta()
    y4_var = [y2_var[a] + y3_var[a] for a, b in enumerate(y2_var)]

    # y1_var = [x**(1/2) for x in x1_var]
    # y2_var = [x**(9/8) for x in x1_var]
    # y3_var = x1_var
    # y4_var = [(1.1)**x for x in x1_var]

    # Legger alle lister med x-data i én liste med lister,sammme med y
    x_data = [x1_var]
    y_data = [y1_var, y2_var, y3_var, y4_var]
    # En liste hvor indexen svarer til y-data, og elementet x-data
    x_y_match = [0, 0, 0, 0]
    # Labels hører til y-data med samme index
    labels = ["Tetha","U", "K", "E"]
    # Begge to må ha like mange elementer som y-data

    # Finner den høyesete verdien i vær listeog så den høeste av dem, samme med minste
    plt.xlim((min([min(a) for a in x_data])), max([max(a) for a in x_data]))
    plt.ylim((min([min(a) for a in y_data])), max([max(a) for a in y_data]))
    # Lager en liste med linjer, og legger til label
    lines = [plt.plot([], [], label=labels[a])[0] for a, line in enumerate(y_data)]
    return x_data, y_data, lines, x_y_match


# Animerer dataen
def main():
    x_data, y_data, lines, x_y_match = fetch_data()

    # Lager en figur, samt akser
    fig = plt.figure(1)
    ax1 = fig.add_subplot(1, 1, 1)

    # Antall frames og hoppe over i animasjonen. 1 betyr at alle rendres
    frameskip = 1

    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    def animate(n):
        n = n * frameskip
        for i, line in enumerate(lines):
            line.set_data(x_data[x_y_match[i]][:n], y_data[i][:n])
        return lines

    anim = animation.FuncAnimation(fig, animate, init_func=init, interval=1, blit=True)

    plt.legend()
    plt.show()

main()

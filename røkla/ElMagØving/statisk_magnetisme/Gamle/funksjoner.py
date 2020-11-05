import numpy as np

N = 330                 # Antall viklinger for sploen
N_s = 358               # Antall viklinger for solenoiden
I = 1                   # Strømm
mu_0 = 4.0e-7 * np.pi   # Magnetisk permabilitet
R = 0.07                # Radius for spolen
R_s = 0.05              # Radius for solenoiden
l = 0.4                 # Lengden Av solenoiden
Delta_I = 0.05          # Usikkerhet for de forskjellige verdiene
Delta_R = 0.0005
Delta_x = 0.0005
Delta_a = 0.0005
Delta_z = Delta_x
Delta_l = Delta_x


# Magnetfelt fra solenoide
def magnetflet_solenoide(z):
    def cos_1(z):
        return z / np.sqrt(z ** 2 + R_s ** 2)

    def cos_2(z):
        return - (l - z) / np.sqrt((l - z) ** 2 + R_s ** 2)

    return N_s * mu_0 * I / 2 / l * (cos_1(z) - cos_2(z)) * 1e4


# Magnetfelt fra enkel spole
def magnetfelt_spole(x):
    return N * mu_0 * I / 2 / R / (1 + x**2 / R **2)**(3/2)*1e4


# Magnetfelt fra Helmoltzspole
def magnetfelt_helmholtzspole(x, a):
    return N * mu_0 * I / 2 / R * \
           (1 / (1 + (x - a/2)**2 / R**2)**(3/2) +
            1 / (1 + (x + a/2)**2 / R**2)**(3/2)) * 1e4


# Feilforplantning for magnetfelt fra enkel spole
def usikkerhet_spole(B, x):
    return np.sqrt((Delta_I / I)**2 +
                   (Delta_R * (2 * x**2 - R ** 2) / (R**3 + R * x**2))**2 +
                   (Delta_x * (3 * x) / (R ** 2 + x ** 2))**2) * B


def spole_del_I(B, x):
    return x/x*I* B/20


def spole_del_R(B, x):
    return ((2 * x**2 - R ** 2) / (R**3 + R * x**2))/20 * B/20


def spole_del_x(B, x):
    return ((3 * x) / (R ** 2 + x ** 2))/20 * B/20


# Feilforplantnign for kort Helmholtzspole
def usikkerhet_helmholtzspole(B, x, a):
    return np.sqrt((Delta_x *
                     (6 * (a + 2 * x) / ((a + 2 * x)**2 + 4 * R**2) +
                      6 * (a - 2 * x) / ((a - 2 * x)**2 + 4 * R**2)))**2
                   + (Delta_a *
                     (3 * (a + 2 * x) / ((a + 2 * x)**2 + 4 * R**2) +
                      3 * (a - 2 * x) / ((a - 2 * x)**2 + 4 * R**2)))**2
                   + (Delta_R *
                     (2/R + 12 * R / ((a - 2 * x)**2 + 4 * R**2) +
                     (2/R + 12 * R / ((a + 2 * x)**2 + 4 * R**2))))**2
                   + (Delta_I / I)**2) * B


def helmoltz_del_x(B, a, x):
    return (6 * (a + 2 * x) / ((a + 2 * x) ** 2 + 4 * R ** 2)\
           + 6 * (a - 2 * x) / ((a - 2 * x) ** 2 + 4 * R ** 2))/20


def helmoltz_del_a(B, a, x):
    return (3 * (a + 2 * x) / ((a + 2 * x) ** 2 + 4 * R ** 2) +\
           3 * (a - 2 * x) / ((a - 2 * x) ** 2 + 4 * R ** 2))/20 * B/20


def helmoltz_del_R(B, a, x):
    return (2 / R + 12 * R / ((a - 2 * x) ** 2 + 4 * R ** 2) +\
           (2 / R + 12 * R / ((a + 2 * x) ** 2 + 4 * R ** 2)))/20 * B/20


def helmoltz_del_I(B, x):
    return x/x * I * B/20


# Feilforplantning for solenoide
def usikkerhet_solenoide(B, z):
    return np.sqrt(
        (Delta_z *
                   ((l - z)**2 / ((l - z)**2 + R**2)**(3 / 2) - 1 / np.sqrt((l - z)**2 + R**2) + 1 /
                    np.sqrt(R**2 + z**2) - z**2 / (R**2 + z**2)**(3 / 2)) /
                    (z / np.sqrt(R**2 + z**2) + (l - z) / np.sqrt((l - z)**2 + R**2)))**2 +
                   (Delta_l *
                   (R**2/(((l - z)**2 + R**2)**(3/2) * ((l - z) / np.sqrt((l - z)**2 + R**2) +
                    z / np.sqrt(R**2 + z**2))) - 1/l))**2 +
                   (Delta_R *
                    (-(R * (l - z)) / ((l - z)**2 + R**2)**(3 / 2) - (R*z) / (R**2 + z**2)**(3 / 2)) / (
                        z / np.sqrt(R**2 + z**2) + (l - z) / np.sqrt((l - z)**2 + R**2)))**2 +
                   (Delta_I / I)**2) * B


# Usikkerhet i målt verid for B, i følge gaussmeteret
def usikkerhet_målte_verdier(B):
    return 0.1 + 0.004 * B + 0.01


# Funksjon for å printe en 2D np-array, kollonevis
def print_table(data, header=[]):
    if header:
        print("-" * 20 * len(data))
        for entry in header:
            print((" " + entry).ljust(20), end="")
        print()
        print("-" * 20 * len(data))
    for i in range(len(data[0])):
        for column in data:
            if column[i] < 0:
                print(str(column[i]).ljust(20), end="")
            else:
                print((" " + str(column[i])).ljust(20), end="")
        print()
    print("-" * 20 * len(data))


# Henter data med headere fra csv fil, returnerer 2D np-array med data i kolloner, og liste med headere
def get_data(filnavn):
    fil = open(filnavn, "r")
    data = [[float(y.strip()) for y in x.split(",")] for x in fil.readlines()[1:]]
    data = np.array(data).T
    fil.seek(0)
    header = [[y.strip() for y in x.split(",")] for x in fil.readlines()[:1]][0]
    fil.close()
    return data, header

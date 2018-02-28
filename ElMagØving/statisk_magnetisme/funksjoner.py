import numpy as np

mu_0 = 4.0e-7 * np.pi   # Magnetisk permabilitet
N = 330                 # Antall viklinger for sploen
N_s = 358               # Antall viklinger for solenoiden


# Magnetfelt fra solenoide
def magnetflet_solenoide(x, R, I, l):
    def cos_1(x):
        return x / np.sqrt(x ** 2 + R ** 2)

    def cos_2(x):
        return - (l - x) / np.sqrt((l - x) ** 2 + R ** 2)

    return N_s * mu_0 * I / 2 / l * (cos_1(x) - cos_2(x)) * 1e4


# Magnetfelt fra enkel spole
def magnetfelt_spole(x, R, I):
    return N * mu_0 * I / 2 / R / (1 + x**2 / R **2)**(3/2)*1e4


# Magnetfelt fra Helmoltzspole
def magnetfelt_helmholtzspole(x, R, I, a):
    return N * mu_0 * I / 2 / R * \
           (1 / (1 + (x - a/2)**2 / R**2)**(3/2) +
            1 / (1 + (x + a/2)**2 / R**2)**(3/2)) * 1e4


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

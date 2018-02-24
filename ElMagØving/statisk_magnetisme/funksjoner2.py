import numpy as np

N = 330
mu_0 = 4.0e-7 * np.pi


def magnetfelt_spole(x, R, I):
    return N * mu_0 * I / 2 / R / (1 + x**2 / R **2)**(3/2)*1e4


def usikkerhet_målte_verdier(B):
    return 0.1 + 0.004 * B + 0.01


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


def get_data(filnavn):
    fil = open(filnavn, "r")
    data = [[float(y.strip()) for y in x.split(",")] for x in fil.readlines()[1:]]
    data = np.array(data).T
    fil.seek(0)
    header = [[y.strip() for y in x.split(",")] for x in fil.readlines()[:1]][0]
    fil.close()
    return data, header

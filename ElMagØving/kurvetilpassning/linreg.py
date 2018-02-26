# Skrevet av Martin Johnsrud, 25/02-2018
import numpy as np


def lineær_regresjon(x, y, y_func=lambda x: x, values=False):

    N = len(x)
    S_x = np.sum(x)
    S_y = np.sum(y)
    S_xx = np.sum(x ** 2)
    S_xy = np.sum(x * y)
    delta = N * S_xx - S_x ** 2
    a_0 = (S_y * S_xx - S_x * S_xy) / delta
    a_1 = (N * S_xy - S_x * S_y) / delta

    def f(x):
        return a_0 + a_1 * y_func(x)

    # Avvik fra regresjonsmodellen
    D_y = f(x) - y
    S = np.sum(D_y ** 2)
    # Standaravvik
    Da_0 = np.sqrt(1 / (N - 2) * (S * S_xx) / delta)
    Da_1 = np.sqrt(N / (N - 2) * S / delta)
    print("a_0:", a_0, "a_1:", a_1)
    print("Da_0:", Da_0, "Da_1:", Da_1)

    if values:
        return a_0, a_1, f, D_y, (N, delta, S_x, S_y, S_xx, S_xy)
    return a_0, a_1, f, D_y
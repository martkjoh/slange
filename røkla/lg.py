from main.numerikk import eulers_metode as e


def f(x, y):
    return x + y


e(f, 1, 0, 2.0000001, 0.00001, print_verdier=True)
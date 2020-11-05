from main.numerikk import eulers_metode as e
from math import sin

def g(x, y):
    return sin(x)*sin(y)

print(e(g, 0, 2, 1, 1/4))
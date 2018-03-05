import numpy as np
from matplotlib import pyplot as plt
from main.numerikk import *


def a_1(l, B, g):
    return l * B / g


def b_1(I, B, g):
    return I * B / g

g = 9.82
l = 3.76 #cm
B = 832  #gauss
I = 2.113
delta_g = 0.01
delta_l = 0.005
delta_B = 10
delta_I = 0.005

print(gauss_usikkerhetsforplantning(b_1, (I, B, g), (delta_I, delta_B, delta_g))/b_1(I, B, g))


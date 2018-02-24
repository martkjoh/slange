from math import *


def print_bin(a):
    x = [2**int(log(y, 2)) for y in range(1, a + 1)]
    print(x)


a = 0x11
b = 0x22

print(a, b)
print_bin(a); print_bin(b)
a = a ^ b
b = a ^ b
a = b ^ a

print(a, b)
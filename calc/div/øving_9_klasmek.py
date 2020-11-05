# Several imports may caus namespace collisions
# from numerics import *
from algebra import *
# from integrals import *
# from tensors import *

from matplotlib import pyplot as plt
import numpy as np
import sympy as sp

A = sp.Matrix([
    [2, -1],
    [-1, 1]
])

# sp.pprint(A.eigenvects())

w, m, M, g, k, l = symbols("w, m, M, g, k, l", real=True)

A = sp.Matrix([
    [2*k, 0, 0],
    [0, m*g*l, 0],
    [0, 0, m*g*l]
])
m = sp.Matrix([
    [M + 2*m, m*l, m*l],
    [m*l, m*l** 2, 0],
    [m*l, 0, m*l**2]
])
pprint(sp.factor(sp.det(A-w*m)))

m = sp.Matrix([
    [2, 1],
    [1, 1]
])
A = sp.Matrix([
    [2, 0],
    [0, 1]
])

v1, v2 = symbols("v1, v2")
v = sp.Matrix([v1, v2])
char_eq = sp.det(A - w * m)
ws,_ = (sp.solve(char_eq), w)

# print(ws)
# pprint(sp.solve((A - w*m).subs(w, ws[0]) * v, v2))
# pprint(sp.solve((A - w * m).subs(w, ws[1]) * v, v2))

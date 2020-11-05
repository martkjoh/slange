from tensors import *

from matplotlib import pyplot as plt
import numpy as np
import sympy as sp

t, r, theta = symbols("t, r, θ")
x1 = r * cos(theta)
x2 = r * sin(theta)


# Flat metric
g0 = sp.diag(*[-1, 1, 1])
var = (t, r, theta)

J = Matrix([t, x1, x2]).jacobian(var)
g = simplify(J.T @ g0 @ J)
# pprint(g)

f = sp.Function("f")(r)

g = np.array(g)
g[0, 0] *= f
g[1, 1] *= 1 / f
g = sp.Matrix(g)

C = Christoffel(g, var)
Christoffel_print(C, var)
R = Riemann_tensor(C, var)
Ricci = Ricci_tensor(R)

# curve = Ricci_scalar(Ricci)
pprint(Ricci[0, 0])
pprint(Ricci[1, 1])
pprint(Ricci[2, 2])



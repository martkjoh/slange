import differentialGeometry3 as dG
from tensors import Christoffel, Christoffel_print

from sympy import symbols, Matrix, cos, sin, diff
import numpy as np

t, r, th, ph = symbols("t, r, th, ph")
var = np.array([t, r, th, ph])
M, a = symbols("M, a")

rho = r**2 + a**2*cos(th)**2
delta = r ** 2 - 2 * M * r + a ** 2
dim = 4
var = (t, r, th, ph)
g = np.zeros((dim, dim), dtype=type(t))

g[0, 0]  = 1 - 2 * M * r / rho**2
g[0, 2] = g[2, 0] = 2 * M * r * sin(th)**2 / rho**2
g[1, 1] = - rho**2 / delta
g[2, 2] = rho**2
g[3, 3] = (r ** 2 + a ** 2 + 2 * M * r * a ** 2 * sin(th) / rho ** 2) * sin(th)** 2

g = Matrix(g)
c = Christoffel(g, var)
Christoffel_print(c, var)

# g_x = np.zeros((dim, dim, dim), dtype=type(t))
# for i in range(dim):
#     for j in range(dim):
#         for k in range(dim):
#             g_x[i, j, k] = diff(g, var[i])

# c8n = dG.christoffel(g, g_x)
# c8nx = dG.dconnection(c8n, var)
# r5n = dG.riemann(c8n, c8nx)
# r4i_ = dG.ricci_(r5n)
# curv = dG.scalarcurvature(g, r4i_)


# geometry = dG.computeGeometry(dG.ginv(g), var)

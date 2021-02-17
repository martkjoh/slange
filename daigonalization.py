import sympy as sp
import numpy as np

A = sp.Matrix([
    [2j, 1],
    [1, 0]
])

P, J = A.jordan_form()


print(np.array(P * J * P**-1))

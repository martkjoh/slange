import sympy
import numpy as np


def f(a_0, a_1, x, n):
    if n == 0:
        return a_0
    else:
        return f(a_1, sympy.simplify(-a_0 + x * a_1), x, n - 1)


def det(A):
    if np.shape(A) == (0, 0) or np.shape(A) == (0,):
        return 1
    else:
        D = 0
        for i, k in enumerate(A[0]):
            D += k * det(np.concatenate(((A[1:][..., 0:i]).T, (A[1:][..., i+1:]).T)).T) * (-1)**i
        return D


a_0, a_1, x, 𝜆 = sympy.symbols("a_0 a_1 c 𝜆")


A =([],
    [[-𝜆]],
    [[-𝜆, 1],
     [1, -𝜆]],
    [[-𝜆, 1, 0],
     [1, -𝜆, 1],
     [0, 1, -𝜆]],
    [[-𝜆, 1, 0, 0],
     [1, -𝜆, 1, 0],
     [0, 1, -𝜆, 1],
     [0, 0, 1, -𝜆]],
    [[-𝜆, 1, 0, 0, 0],
     [1, -𝜆, 1, 0, 0],
     [0, 1, -𝜆, 1, 0],
     [0, 0, 1, -𝜆, 1],
     [0, 0, 0, 1, -𝜆]],
    [[-𝜆, 1, 0, 0, 0, 0],
     [1, -𝜆, 1, 0, 0, 0],
     [0, 1, -𝜆, 1, 0, 0],
     [0, 0, 1, -𝜆, 1, 0],
     [0, 0, 0, 1, -𝜆, 1],
     [0, 0, 0, 0, 1, -𝜆]])


n = 20

solution = f(a_0, a_1, x, n)
subbed = solution.subs([(a_1, -𝜆), (a_0, 1), (x, -𝜆)])
print(sympy.simplify(subbed))
#print(sympy.simplify(det(np.array(A[n]))))



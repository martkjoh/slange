import numpy as np
import numpy.linalg as la
from matplotlib import pyplot as plt
import numpy.random as r
import time


def det(A):

    def proj(v, u):
        return sum(u * v) / sum(u * u) * u

    def orthogonolize(A, v):
        if np.shape(A) == (1, len(A[0])):
            return v - proj(v, A[-1])
        else:
            return orthogonolize(A[:-1], v - proj(v, A[-1]))

    for i in range(1, len(A)):
        A[i] = orthogonolize(A[:i], A[i])

    return np.prod([np.sqrt(sum(u * u)) for u in A])


n = 500
W = r.randint(0, 10, size=(n, n)).astype("float64")
W = r.rand(n, n)
t = time.time()
print(la.det(W))
t = time.time() - t
print(t, "\n")

t = time.time()
print(det(W))
print(time.time() - t)

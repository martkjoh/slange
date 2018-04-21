import numpy as np
import numpy.linalg as la


def det(A):
    B = np.zeros_like(A)
    def proj(v, u):
        return sum(u * v) / sum(u * u) * u

    def orthogonolize(A, v):
        if np.shape(A) == (1, len(A[0])):
            return v - proj(v, A[-1])
        else:
            return orthogonolize(A[:-1], v - proj(v, A[-1]))

    for i in range(1, len(A)):
        B[i] = orthogonolize(A[:i], A[i])

    return np.prod([np.sqrt(sum(u * u)) for u in A])

n = 100
A = 0
A = np.random.randint(0, 10, size=(n, n)).astype("float64")

print(la.det(A))
print(det(A))

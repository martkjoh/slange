import numpy as np

# Returns equivalent system of upper-triangle matrix U and vector b
def gauss(A, b):
    N, _ = np.shape(A)
    U = np.copy(A)
    b = np.copy(b)
    for i in range(1, N):
        for j in range(i, N):
            m = U[j, i - 1] / U[i - 1, i - 1]
            for k in range(i - 1, N):
                U[j, k] -= m * U[i - 1, k]
            b[j] -= m * b[i - 1]
    return U, b

# Solves Ux = b for x assuming U is an uppper-triangle matrix
def backSub(U, b):
    x = np.zeros(N)
    x[N -1] = b[N-1] / U[N - 1, N - 1]
    for i in range(N - 2, -1, -1):
        s = b[i]
        for j in range(N - 1, i, -1):
            s -= x[j] * U[i, j]
        x[i] = s / U[i, i]
    return x


N = 4
A = np.random.rand(N, N) * 100
b = np.random.rand(N)

U, c = gaus(A, b)
c = backSub(U, c)

np.set_printoptions(2)
print(U @ x - c)
print(A @ x - b)
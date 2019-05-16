import numpy as np
# np.set_printoptions(1)

# Returns upper-trinagle matrix LU and lower-trinagel matrix L such that LU = A[P]
def LUFactor(A):
    N, _ = np.shape(A)
    LU = np.copy(A) 
    P = np.array([i for i in range(N)])

    for i in range(N - 1):

        k = i
        m = abs(LU[P[i], i])
        for j in range(i + 1, N):
            if abs(LU[P[j], i]) > m:
                m = abs(LU[P[j], i])
                k = j
        P[i], P[k] = P[k], P[i]
            
        for j in range(i + 1, N):
            LU[P[j], i] /= LU[P[i], i]
            for k in range(i + 1, N):
                LU[P[j], k] -= LU[P[j], i] * LU[P[i], k]
    
    return LU[P], P

# Solves Ux = b for c assuming LU is an uppper-triangle matrix
def backSub(LU, b):
    N = len(b)
    c = np.zeros(N)
    x = np.zeros(N)

    c[0] = b[0]
    for i in range(1, N):
        s = b[i]
        for j in range(i):
            s -= c[j] * LU[i, j]
        c[i] = s

    x[N-1] = c[N-1] / LU[N-1, N-1]
    for i in range(N-2, -1, -1):
        s = c[i]
        for j in range(N-1, i, -1):
            s -= x[j] * LU[i, j]
        x[i] = s / LU[i, i]

    return x

def splitLU(LU):
    U = np.copy(LU)
    L = np.copy(LU)
    n = len(LU)
    for i in range(n):
        L[i, i] = 1
        for j in range(i + 1, n):
            L[i, j] = U[j, i] = 0
    return L, U


# Solves a general system Ax = b
def solve(A, b):
    LU, P = LUFactor(A)
    return backSub(LU, b), P



if __name__ == "__main__":

    N = 8
    A = np.random.rand(N, N)
    b = np.zeros(N)
    LU, P = LUFactor(A)
    L, U = splitLU(LU)

    x, P = solve(A, b)

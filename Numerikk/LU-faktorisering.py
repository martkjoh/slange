import numpy as np
np.set_printoptions(1)

# Returns upper-trinagle matrix U and lower-trinagel matrix L such that LU = A[P]
def LUFactorize(A, pivot = True):
    N, _ = np.shape(A)
    U = np.copy(A)
    L = np.zeros((N, N))    
    P = np.array([i for i in range(N)])

    for i in range(1, N):

        if pivot:        
            index = i - 1
            m = abs(U[P[i - 1], i - 1])
            for j in range(i, N):
                if abs(U[P[j], i - 1]) > m:
                    m = abs(U[P[j], i - 1])
                    index = j
            P[[i - 1, index]] = P[[index, i - 1]]
            
        for j in range(i, N):
            L[P[j], i - 1] = U[P[j], i - 1] / U[P[i - 1], i - 1]
            for k in range(i - 1, N):
                U[P[j], k] -= L[P[j], i - 1] * U[P[i - 1], k]

    for i in range(N):
        L[P[i], i] = 1
    
    return L, U, P

# Solves Ux = b for x assuming U is an uppper-triangle matrix
def backSub(U, b, P):
    N = len(b)
    x = np.zeros(N)
    x[N - 1] = b[N - 1] / U[P[N - 1], N - 1]
    for i in range(N - 2, -1, -1):
        s = b[i]
        for j in range(N - 1, i, -1):
            s -= x[j] * U[P[i], j]
        x[i] = s / U[P[i], i]
    return x

# Solves Lx = b for x assuming L is an lower-triangle matrix
def forwardSub(L, b, P):
    PB = (len(P) - 1) * np.ones_like(P) - P
    return backSub(L[::-1,::-1], b[::-1], PB[::-1])[::-1]

# Solves a general system Ax = b
def solve(A, b):
    L, U, P = LUFactorize(A)
    c = forwardSub(L, b, P)
    return backSub(U, c, P), P

N = 100
A = np.random.rand(N, N)
b = np.random.rand(N)

x, P = solve(A, b)
print((A @ x)[P] - b)

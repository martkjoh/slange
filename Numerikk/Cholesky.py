import numpy as np
np.set_printoptions(2)

N = 7
A = np.random.rand(N, N) * np.sqrt(10)
A = A @ A.T
x = np.random.rand(N) - np.ones(N) / 2

def Cholesky(A):
    N = len(A)
    A = np.copy(A)
    L = np.zeros((N, N))
    for i in range(N):
        L[i, i] = np.sqrt(A[i, i])
        for j in range(i + 1, N):
            L[i, j] = A[i, j] / L[i, i]
            print(L)
        
        for j in range(i + 1, N):
            for k in range(i + 1, N):
                A[j, k] -= L[i, j] * L[i, k]
        

    return L

L = Cholesky(A)
print(L.T @ L - A)

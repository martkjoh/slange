import numpy as np

def jacobi(A, b, x0, tol = 1e-10):
    n = len(A)
    M = np.copy(A)
    DInv = np.zeros((n, n))
    k = 0
    for i in range(n):
        DInv[i, i] = 1 / M[i, i]
        M[i, i] = 0

    while (True):
        x = DInv @ (b - M @ x0)
        if max(abs(x - x0))  < tol:
            return x
        x0 = x
        k += 1
        print(max(abs(x - x0)))


def gaussSeidel(A, b, x0, tol = 1e-10):
    n = len(A)
    x = np.copy(x0)
    k = 0

    while (True):
        print(k)
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i == j:
                    continue
                s -= A[i, j] * x[j]
            x[i] = s / A[i, i]

        if max(abs(x - x0)) < tol:
            return x

        x0 = np.copy(x)
        k += 1




if __name__ == "__main__":
    n = 1000
    A = np.random.rand(n, n) + np.diag(np.ones(n) * n)
    b = np.random.rand(n)
    x = np.random.rand(n)

    x = jacobi(A, b, x)

    print()
    print(max(abs(A @ x - b)))
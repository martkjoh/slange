import numpy as np
import matplotlib.pyplot as plt

from scipy import sparse
from scipy.sparse.linalg import eigs as sparse_eig

def get_D2x(N):
    """ 3 point stencil for second derivative with periodic bc's """
    daig_0 = -2 * np.ones(N)
    diag_1 = np.ones(N - 1)
    D2x = sparse.diags([1, diag_1, daig_0, diag_1, 1], [-(N-1), -1, 0, 1, (N-1)])
    return D2x

def find_eigenvecs(N):
    D2x = get_D2x(N)
    w, v = sparse_eig(D2x, which="SM")

    x = np.linspace(0, 1, N)

    for i in range(5):
        plt.plot(x, v[:, i])
    plt.show()

find_eigenvecs(100)
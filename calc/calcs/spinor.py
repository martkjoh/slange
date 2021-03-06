import sympy as sp
import numpy as np

from sympy import I, sqrt
from sympy.physics.quantum.dagger import Dagger
from sympy.printing import pprint

# Has einsum impolementation that supports sympy symobls
import opt_einsum as oe

# . needed for this to work when imported
from .tensors import INDX, contract, raise_indx, lower_indx


# I = sp.Rational(1)*I
dim = 4
g = np.diag([1, -1, -1, -1])  # The minkowski metric

# Pauli matrices
s = np.empty((3, 2, 2), dtype=type(sp.Rational(1)))

one = sp.Rational(1)
s[0] = np.array([
    [0, one],
    [one, 0]
])
s[1] = np.array([
    [0, -I],
    [I, 0]
])
s[2] = np.array([
    [one, 0],
    [0, -one]
])

# Dirac matricies
Oh = np.zeros((2, 2), dtype=type(sp.Rational))
eye = np.identity(2, dtype=type(sp.Rational))
Id = np.block([
    [eye, Oh],
    [Oh, eye]
    ])

γ = np.empty((4, 4, 4), type(sp.Rational(1)))
γ[0] = np.block([
    [eye, Oh],
    [Oh, -eye]
])

for i in range(3):
    γ[i+1] = np.block([
        [Oh, s[i]],
        [-s[i], Oh]
    ]).reshape(4, 4)

γ5 = I * (γ[0] @ γ[1] @ γ[2] @ γ[3])
γ5_γ = np.array([γ5 @ γ[i] for i in range(dim)])
γ_γ5 = np.array([γ[i] @ γ5 for i in range(dim)])

# Returns the adjoint spinor
def adj(u):
    return Dagger(u) @ γ[0]

def slash(a):
    return sp.Matrix(sum([γ[i] * a[i] for i in range(dim)]))

def contract_tensor_vector(T, p):
    """ Contracts tensor with list of vectors recursivley """
    if len(p)==0: return T
    return contract_tensor_vector(sum([T[i, ...] * p[0][i] for i in range(dim)]), p[1::])


def Tr(γ_list):
    """ Returns TR[γ_list[0] γ_list[1] ...] """
    # Einsum does not accept sp.Rational :(
    # γ_list = [np.array(γ, dtype=type(1j)) for γ in γ_list] 
    indcs = "abcdefghijklmn" # just in case
    nr_indx = len(γ_list)
    shape = [dim] * nr_indx + [dim, dim]
    A = np.full(shape, γ_list[0])

    for i, γ in enumerate(γ_list[1::]):
        s_indx = indcs[:len(γ_list)] + "xy, "
        s_indx += indcs[len(γ_list) - 2 - i] + "yz -> "
        s_indx += indcs[:len(γ_list)] + "xz"
        A = oe.contract(s_indx, A, γ, backend='object')

    return oe.contract("...ii", A, backend='object')


def test():
    """
    We are considering electron muon scattering, following the feinmann diagram below.
    Assuming all particles have helicity one, and the CM-fram, motion in z-dir, meaning 
    line 1 and 4 have spin up, line 3 and 4 have spin down. This gives the spinnors below.
    p2\     /p4
    \   ^
        \ / μ
    γ §
        §
        / \e
    ^   \.
    p1/     \p3
    """

    # This is to make sure sympy knows these are real numbers
    me, Ee, Em, mm, g = sp.symbols("me, Ee, mm, Em g", positive=True)
    ap = sp.symbols("ap", positive=True)  # sqrt(Ee + me)
    am = sp.symbols("am", positive=True)  # sqrt(Ee - me)
    bp = sp.symbols("bp", positive=True)  # sqrt(Em + mm)
    bm = sp.symbols("bm", positive=True)  # sqrt(Em - mm)

    u1 = np.array([ap, 0, am, 0], dtype=type(I))
    u2 = np.array([0, bp, 0, bm], dtype=type(I))
    u3 = np.array([0, ap, 0, am], dtype=type(I))
    u4 = np.array([bp, 0, bm, 0], dtype=type(I))

    M = 0
    for i in range(dim):
        M += g[i, i] * ((adj(u3) @ γ[i] @ u1) * (adj(u4) @ γ[i] @ u2))
        
    M *= g ** 2 / (4 * am * bp * bm * ap)

    pprint(M.simplify())


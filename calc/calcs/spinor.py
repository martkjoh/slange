import sympy as sp
import numpy as np

from sympy import I, sqrt, ask, Q
from sympy.physics.quantum.dagger import Dagger
from sympy.printing import pprint

dim = 4
g = np.diag([1, -1, -1, -1])  # The minkowski metric

# Pauli matrices
s = np.empty((3, 2, 2), dtype=type(I))
s[0] = np.array([
    [0, 1],
    [1, 0]
])
s[1] = np.array([
    [0, -I],
    [I, 0]
])
s[2] = np.array([
    [1, 0],
    [0, -1]
])

# Dirac matricies
Oh = np.zeros((2, 2))
eye = np.identity(2)

gamma = np.empty((4, 4, 4), dtype=type(I))
gamma[0] = np.block([
    [eye, Oh],
    [Oh, -eye]
])

for i in range(3):
    gamma[i+1] = np.block([
        [Oh, s[i]],
        [-s[i], Oh]
    ]).reshape(4, 4)

# Returns the adjoint spinor
def adj(u):
    return Dagger(u) @ gamma[0]

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
    M += g[i, i] * ((adj(u3) @ gamma[i] @ u1) * (adj(u4) @ gamma[i] @ u2))
    
M *= g ** 2 / (4 * am * bp * bm * ap)

pprint(M.simplify())


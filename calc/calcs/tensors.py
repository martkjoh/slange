from sympy import Matrix
from sympy import symbols, diff, cos, sin, simplify, Rational
from sympy.core.symbol import Symbol

import numpy as np
import sympy as sp

from IPython.display import display, Latex

#############
# UTILITIES #
#############

def INDX(i, place, num_indx):
    """
    Acceses an index at 'place' for 'num_indx' order tensor
    T_(a0 ... âp ... an-1) = T[INDX(i, place=p, num_indx=n)] = T[:,...<-p-> , i, :,...<-(n-p-1)->]
    """
    indx = []
    assert place<num_indx
    for j in range(num_indx):
        if place==j: indx.append(i)
        else: indx.append(slice(None))
    return tuple(indx)


def get_g_inv(g):
    return np.array(Matrix(g)**(-1))


def Christoffel_print(C, var):
    """ A function for dsiplaying christoffels symbols """
    for i in range(len(var)):
        s = "$\Gamma^" + str(var[i]) + "_{\\alpha \\beta} = "
        display(Latex(s + sp.latex(simplify(Matrix(C[i]))) + "$"))


def contract(T, g=None, g_inv=None, num_indx=2, upper=1, indx=(0, 1)):
    """
    contracts indecies indx=(a_p, a_q) on tensor T with 'num_indx', 
    'upper' of whom are upper. If upper=0, all indecies are assumed lower.
    With indx=(a_k, a_l), upper=n, num_indx=n+m, this gives
    T^(a_0...a_n-1)_(a_n...a_n+m-1) -> T^(a_0...a_k=a...a_n-1)_(a_n...a_k...a_n+m-1),
    with the necesarry metric. If wrong metric is given, this wil throw error.
    """
    assert indx[0] < indx[1]  # we have to know if the index to the left dissapears
    dim = np.shape(T)[0]
    a = (indx[0] < upper) + (indx[1] < upper) # number of upper indecies to be contracted
    if a==2: g0 = g # two upper
    elif a==0: g0 = g_inv # two lower
    else: g0 = np.identity(dim, dtype=Rational)

    Tc = Rational(0) * np.ones((T.shape)[:-2], dtype=Rational)
    for i in range(dim):
        for j in range(dim):
            Tc += g0[i, j] * (T[INDX(i, indx[0], num_indx)])[INDX(j, indx[1] - 1, num_indx - 1)]

    return Tc


def raise_indx(T, g_inv, indx, num_indx):
    """ Raise index 'indx' of a tensor T with 'num_indx' indices. """
    dim = np.shape(T)[0]
    Tu = np.zeros_like(T)
    for i in range(dim):
        I = INDX(i, indx, num_indx)
        for j in range(dim):
            J = INDX(j, indx, num_indx)
            Tu[I] += g_inv[i, j] * T[J]
        Tu[I] = simplify(Tu[I])
    return Tu


def lower_indx(T, g, indx, num_indx):
    """ Lower index 'indx' of a tensor T with 'num_indx' indices. """
    return raise_indx(T, g, indx, num_indx)


# Print functions for jupyter notebook

def print_christoffel(C, var):
    """ A function for dsiplaying christoffels symbols """
    output = []
    for i in range(len(var)):
        txt = "$$"
        txt += "\Gamma^" + sp.latex(var[i]) + "_{\\alpha \\beta} ="
        txt += sp.latex(Matrix(C[i]))
        txt += "$$"
        output.append(display(Latex(txt)))
    return output

def print_tensor(T, name="T"):
    return display(Latex("$$" + name + "=" + sp.latex(Matrix(T)) +"$$"))

def print_scalar(S, name="S"):
    return display(Latex("$$" + name + "=" + sp.latex(S) +"$$"))


############
# GEOMETRY #
############

def Christoffel(g, g_inv, var):
    """ 
    Work out the christoffel symbols, given a metric an its variables 
    Γ^i_jk = C[i, j, k]
    """
    dim = len(var)
    C = np.zeros((dim, dim, dim), dtype=Symbol)
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                for m in range(dim):
                    C[i, j, k] += \
                        Rational(1, 2) * (g_inv)[i, m] \
                        * (
                            + diff(g[m, k], var[j])
                            - diff(g[k, j], var[m])
                            + diff(g[m, j], var[k])
                        )
    return C

def Riemann_tensor(C, var):
    """ 
    Riemann_tensor(Christoffel_symbols, (x_1, ...)) = R[i, j, k, l] = R^i_jkl
    Compute the Riemann tensor from the Christoffel symbols 
    R^α_βρσ = ∂ρ Γ^α_βσ - ∂σ Γ^α_βρ + Γ^α_κρ Γ^κ_ βσ - Γ^α_κσ Γ^κ_βρ
    """
    dim = len(var)
    R = np.zeros([dim] * 4, dtype=Symbol)
    indx = [(i, j, k, l)
        for i in range(dim)
        for j in range(dim)
        for k in range(dim)
        for l in range(dim)
    ]
    for (a, b, r, s) in indx:
        R[a, b, r, s] += diff(C[a, b, s], var[r]) - diff(C[a, b, r], var[s])
        for k in range(dim):
            R[a, b, r, s] += C[a, k, r] * C[k, b, s] - C[a, k, s] * C[k, b, r]
    return R


def Ricci_tensor(Rie):
    return - contract(Rie, upper=1, num_indx=4, indx=(0, 2))

def Ricci_scalar(Ricci, g_inv):
    return contract(Ricci, upper=0, g_inv=g_inv)


def Kretschmann_scalar(Rie, g, g_inv):
    Ru = raise_indx(raise_indx(raise_indx(Rie, g_inv, 1, 4), g_inv, 2, 3), g_inv, 3, 4)
    Rl = lower_indx(Rie, g, 0, 4)

    return simplify(sum(sum(sum(sum(Ru * Rl)))))


def metric_analysis(g, var):
    display(Latex("$" + sp.latex(Matrix(g)) + "$"))
    g_inv = get_g_inv(g)

    C = Christoffel(g, g_inv, var)
    Christoffel_print(C, var)

    Rie = Riemann_tensor(C, var)
    Ricci = Ricci_tensor(Rie)
    print("Ricci tensor:")
    display(Latex("$" + sp.latex(Matrix(Ricci)) + "$"))
    
    R = Ricci_scalar(Ricci, g_inv)
    print("Ricci scalar:")
    display(Latex("$" + sp.latex(simplify(R)) + "$"))


    # K = Kretschmann_scalar(Rie, g, g_inv)
    # print("Kretschmann scalar:")
    # pprint(simplify(K))


#########
# TESTS #
#########

def test_contract():
    g = np.diag((-1, 1, 1, 1))
    g_inv = get_g_inv(g)
    A = np.array([
        [-2, 0, 0, 0],
        [4, 1, 0, 50],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    print(contract(A, g=g, upper=2))
    print(contract(A, upper=1))
    print(contract(A, g_inv=g_inv, upper=0))
 

def hyperbolic_plane():
    x, y = symbols("x, y")
    var = (x, y)

    g = np.array([
        [1 / y** 2, 0],
        [0, 1 / y** 2]
    ])

    metric_analysis(g, var)


def two_sphere():
    t, p = symbols("θ, φ")
    r = symbols("r")
    var = (t, p)
    g = r**2 * np.array([
        [1,  0       ],
        [0, sin(t)**2]
    ])
    metric_analysis(g, var)


def flat_spherical_3d():
    r, t, p = symbols("r, θ, φ")
    x1 = r * cos(p) * sin(t)
    x2 = r * sin(p) * sin(t)
    x3 = r * cos(t)

    var = (r, t, p)
    J = Matrix([x1, x2, x3]).jacobian(var)
    g = np.array(simplify(J.T *J))

    metric_analysis(g, var)


def arbitrary_isotropic_metric():
    t, r, th, ph = symbols("t, r, θ, φ")
    x1 = r * cos(ph) * sin(th)
    x2 = r * sin(ph) * sin(th)
    x3 = r * cos(th)

    eta = sp.diag(1, -1, -1, -1)
    var = (t, r, th, ph)
    J = Matrix([t, x1, x2, x3]).jacobian(var)
    g = np.array(simplify(J.T *eta* J))

    A = sp.Function("A", real=True)(r)
    B = sp.Function("B", real=True)(r)
    g[0, 0] *= A
    g[1, 1] *= B
    return g, var


def schwarzschild():
    g, var = arbitrary_isotropic_metric()
    t, r, th, ph = var
    g = Matrix(g).subs(-g[1, 1], 1 / g[0, 0])
    M = symbols("M")
    g = Matrix(g).subs(g[0, 0], 1 - 2*M/r)
    
    metric_analysis(g, var)

def reissner_norstroem():
    g, var = arbitrary_isotropic_metric()
    t, r, th, ph = var
    g = Matrix(g).subs(-g[1, 1], 1 / g[0, 0])
    M, k = symbols("M, k")
    g = Matrix(g).subs(g[0, 0], 1 - 2*M/r + k/(2*r**2))
    
    metric_analysis(g, var)

def kerr():
    M, a = symbols("M, a")
    t, r, th, ph = symbols("t, r, θ, φ")
    var = (t, r, th, ph)
    dim = len(var)

    rho = r**2 + a**2*cos(th)**2
    delta = r ** 2 - 2 * M * r + a ** 2

    g = np.zeros((dim, dim), dtype=type(t))

    g[0, 0]  = 1 - 2 * M * r / rho**2
    g[0, 2] = g[2, 0] = 2 * M * r * sin(th)**2 / rho**2
    g[1, 1] = - rho**2 / delta
    g[2, 2] = rho**2
    g[3, 3] = (r ** 2 + a ** 2 + 2 * M * r * a ** 2 * sin(th) / rho ** 2) * sin(th)** 2

    metric_analysis(g, var)


if __name__ == "__main__":
    # reissner_norstroem()
    # kerr()
    flat_spherical_3d()

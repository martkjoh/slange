from sympy.physics.secondquant import Commutator, F, Fd, wicks, NO
from sympy import symbols, simplify

a = symbols("b0:8")
exp = F(a[1])*F(a[0])*Fd(a[3])*Fd(a[2]) * F(a[4])*F(a[5])*Fd(a[6])*Fd(a[7])


exp = wicks(exp)
print(exp)

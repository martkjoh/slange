from math import pi
from math import sqrt

R = 0.1
L = 0.5
m_1 = 0.2
m_2 = 0.25
M = m_1 + m_2
g = 9.81


I = (1/2 * m_1 * R**2) + m_1 * L**2 + (1/3) * m_2 * L**2

CM = (1/M) * (L * m_1 + (L/2) * m_2)

omega = sqrt((2 * M * g * CM) / I)

F_n = M * g + M * omega**2 * CM

print(F_n)

from calcs.numerics import *


R = 0.1 * AU
M = 2 * m_earth
r = 5e4 * ly
ω = sqrt(G * M / (4 * R**2))
10 / (2 * pi)

A = 8 * G/c**2 * M * (R * ω / c)**2 / r 
print("1c) Amplitude = ", A)

F = c ** 3 * ω / (16 * pi * G) * A**2
print("2a) Flux = ", F)

f = 1 / 300
sci(sqrt(1 - (1 - f)** 2))

# dR = 2e4
dEdR = 4 / 5 * R_earth / (24 * 3600 / 2 / pi)
sci(dEdR)

dL = R_earth * A
print("Dissipation due to GW's:")
sci(dEdR*dL)
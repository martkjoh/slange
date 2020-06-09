import numpy as np
from numpy import sqrt, pi, sin, cos
import matplotlib.pyplot as plt

# Jones-vector
v = np.array([
    1, 
    3j
])

# Normalization
A = 1 / sqrt(abs(v) @ abs(v))
v = A * v

# The difference in phase between the components of
phi = np.angle(v[0]) - np.angle(v[1])

# Finding the direction of polarization
dirOfPol = ""
if phi >= 0: dirOfPol = "positive"
else: dirOfPol = "negative"

# Drawing the polarization diagram
theta = np.linspace(0, 2*pi, 100)
x = abs(v[0]) * cos(theta)
y = abs(v[1]) * sin(theta - pi / 2 - phi)

fig, ax = plt.subplots()
fig.suptitle("Ploarization of $\\vec v = ({:1.3f}, {:1.3f})$, in ".format(v[0], v[1]) + dirOfPol + " direction." )
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.grid()
ax.plot(x, y)
plt.show()
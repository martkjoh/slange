import numpy as np
import matplotlib.pyplot as plt
from LU_faktorisering import LUFactor, splitLU, backSub, solve
np.set_printoptions(2)

n = 120
dx = 10 / n

I = np.identity(n)
D = np.zeros((n, n))

d = [0, 4/5, -1/5, -4/105, -1/280]
# d = [0, 2 / 3, - 1/ 12]
# d = [0, 1/2]
m = len(d)
for i in range(n):
    for j in range(-m + 1, m):
        if (i + j) < 0 or (i + j) >= n:
            continue
        D[i, i + j] = np.sign(j) * d[abs(j)] / dx
 
a = 8
c = 0.8
dampedOscil = (D @ D + c * D + a * I)

x = np.linspace(0, dx * (n - 1), n)

b = np.zeros(n)
b[0] = 0
b[1] = dx


y, P = solve(dampedOscil, x)

fig, ax = plt.subplots()
ax.plot(x, y)

# ax.plot(x,  np.exp(-x * c / 2))
# ax.plot(x, - np.exp(-x * c / 2))
plt.show()
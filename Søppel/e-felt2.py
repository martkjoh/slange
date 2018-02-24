from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
cut = False

def z(x, y):
    return (8*(np.e**x*y)**2+8*(2+x**2*np.sin(y)))**(5/7)

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
x, y = np.meshgrid(x, y)
#rs = [a/((x+a)**2 + (y-a)**2) for a in np.arange(-10, 10, 4)]\
#    +[1/((x+4+a)**2 + (y-a+4)**2) for a in np.arange(-10, 10, 4)]\
#    +[1/((x+8+a)**2 + (y-a+8)**2) for a in np.arange(-10, 10, 4)]\
#    +[1/((x-4+a)**2 + (y-a-4)**2) for a in np.arange(-10, 10, 4)]\
#    +[1/((x-8+a)**2 + (y-a-8)**2) for a in np.arange(-10, 10, 4)]

#E = sum(rs)
E = z(x, y)
print(E)
if cut:
    for a in range(len(E)):
        for b in range(len(E[a])):
            if E[a][b] > 10:
                E[a][b] = 10
            if E[a][b] < -10:
                E[a][b] = -10
z_min, z_max = min([min(x) for x in E]),  max([max(x) for x in E])
ax.set_zlim(-20, 20)
surf = ax.plot_surface(x, y, E, cmap=cm.coolwarm)
#bottom = ax.contour(x, y, E, zdir='z', cmap=cm.coolwarm)

#fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
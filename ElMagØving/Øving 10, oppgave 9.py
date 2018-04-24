import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def B(z, b):
  return 1 / ((1 + (z + b)**2)**(3/2)) + 1/(1 + (z - b)**2)**(3/2)


def animate(n):
  b =  n/50
  line.set_data(z, B(z, b))
  return line,



z = np.linspace(-5, 5, 100)
fig = plt.figure()
ax = fig.subplots(1)
ax.set_ylim(0, 2  )
line = ax.plot(z, B(z, 1))[0]

A = animation.FuncAnimation(fig, animate, interval=10, blit=True, frames=300)
plt.show()
from matplotlib import pyplot as plt
from matplotlib import style

x_liste = [x for x in range(100)]
y_liste = [x**2 for x in x_liste]

fig = plt.figure(1)
plt.xticks([])
plt.yticks([])
plt.ylabel("Suksess", size="30")
plt.xlabel("Tid", size="30")
plt.plot(x_liste, y_liste)
plt.grid()
plt.show()

print([1]*5)
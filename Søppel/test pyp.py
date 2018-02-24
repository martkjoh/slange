from matplotlib import pyplot as plt

x = [x/10 for x in range(100)]
y = [x**2 for x in x]

plt.plot(x,y)
plt.show()

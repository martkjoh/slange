from matplotlib import pyplot as plt


datax = "Avstand [cm]"
dataxinvers = "1/r^2"
datay = "Kraft [mN]"
data2x = "* standard ladning"
datay2 = "Kraft [mN]"

fil = open("Data2.csv", "r")
data = [[float(y.strip()) for y in x.split(",")] for x in fil.readlines()]
#data = data[:-1]
for line in data:
    print(line)

x = [x[0] for x in data]
y = [sum(x[1:])/(len(x)-1) for x in data]
x = [1/x for x in x]
plt.plot(x, y)
plt.xlabel(data2x)
plt.ylabel(datay2)

plt.legend()
plt.show()
from matplotlib import pyplot as plt

fil = open("Penger.tsv", "r")
data = [x.split("\t") for x in fil.readlines()]
fil.close()
for i in range(1, len(data)):
    data[i][-1] = float(data[i][-1][2:]
                        .strip()
                        .replace("-", "-")
                        .replace(",", ".")
                        .replace(" ", ""))
for line in data:
    print(line)

x = [x for x in range(1, len(data))]
y = [data[i][3] for i in x]

plt.plot(x, y)
plt.show()
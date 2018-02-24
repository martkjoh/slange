from random import randint as r

occ = [x for x in range(11)]
for i in range(1000000):
    occ[r(0, 10)] += 1

print(occ)

av = 0
for i, x in enumerate(occ):
    av += i*x

av = av/sum(occ)
print(av)
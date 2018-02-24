import random as r

a = [0 for x in range(100000)]
for b in range(100000):
    c = 0
    while c < 1000:
        c += r.uniform(0, 1000)
        a[b] += 1
print(sum(a)/(len(a)))

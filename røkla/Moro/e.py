import random as r

n = 1000000
m = 100
a = 0
for b in range(n):
    c = 0
    while c < m:
        c += r.uniform(0, m)
        a += 1
print(a/n)

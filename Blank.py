primes = [2]

for i in range(2, 2000000):
    for x in primes:
        if i % x == 0:
            break
        if x == primes[-1]:
            primes.append(i)
            break


print(sum(primes)) 
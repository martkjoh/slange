n = 2000000
primes = [2]
sum = 2

for i in range(3, n):
    for j in primes:
        if i % j == 0:
            break
    else:
        primes.append(i)
        sum += i
        print(sum)
print(sum)

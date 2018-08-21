<<<<<<< HEAD
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
=======
primes = [2]

for i in range(2, 2000000):
    for x in primes:
        if i % x == 0:
            break
        if x == primes[-1]:
            primes.append(i)
            break


print(sum(primes)) 
>>>>>>> 3d3748c5ce2b72de6e51d3768bc1a40192c15c88

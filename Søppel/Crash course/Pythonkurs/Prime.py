from math import sqrt

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    i = 3
    while i<= sqrt(n):
        if n%i==0:
            return False
        i+=1
    return True

print(isPrime(9))

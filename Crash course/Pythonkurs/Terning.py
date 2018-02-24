from random import randint

def snittKast(n):
    total = 0
    i = 0
    while i<n:
        total += randint(1,6)
        i+=1
    return float(total)/n

print(snittKast(20))

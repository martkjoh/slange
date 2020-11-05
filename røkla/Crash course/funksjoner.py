from random import randint as r


def isPrime(x):
    primes = [2]
    for a in range(2, x//2 + 2):
        if x % a == 0:
            return False
    return True

def av_terningkast(n):
    av = 0
    for x in range(n):
        av += r(1, 6)
    return av/n


def størst(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return False


def kvad(x):
    return x**2


def fib(n, np1, lim):
    if lim:
        return fib(np1, np1+n, lim-1)
    else:
        return n


def doble_odde(x):
    if not x%2 == 0:
        return 2*x
    return False


def remove_dup(lst):
    return list(set(lst))


def mult_mat(n):
    return [[a*b for b in range(n+1)] for a in range(n+1)]


def app_kat(katalog, navn, nummer):
    if navn in katalog:
        katalog[navn].append(nummer)
    else:
        katalog[navn] = [nummer]

kat = {"Martin": [99456712], "Nils": [34567284, 19384756], "Hans": [99478564]}


def lag_fil(filnavn, txt):
    fil = open(filnavn, "w")
    fil.write(txt)
    fil.close()

def app_fil(filnavn, txt):
    fil = open(filnavn, "a")
    fil.write(txt)
    fil.close()


lag_fil("Hallo.txt", "hallo")
app_fil("Hallo.txt", "verden")

fil = open("Hallo.txt", "r")
print(fil.read())
fil.close()

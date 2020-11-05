x = 123456
y = x
primtall = [2]
primfaktorer = []
i = 2
tall = 1

while x % 2 == 0:   
    primfaktorer.append(2)
    x = x/2
    tall *= 2
i += 1
while True:
    for j in primtall:
        if i % j == 0:
            for l in range(i%80):
                    print(l * "x")
            for l in range(i%80):
                    print(-(l-i%80) * "x")
            break
        if j == primtall[-1]:
            primtall.append(i)
            while x % i == 0:
                primfaktorer.append(i)
                x = x/i
                print(tall)
                tall *= i
                if tall == x:
                    break
    i += 1


print("produktet av", primfaktorer, "er", tall)

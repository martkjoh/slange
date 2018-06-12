x = 20
for i in range(1, 20)[::-1]:
    if x % i == 0:
        continue
    else:
        for j in range(1, i // 2):
            if x % j == 0 and i % j == 0:
                continue
            else:
                x *= j

print(x)

for i in range(1, 21):
    print(i, x/i)

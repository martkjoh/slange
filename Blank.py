for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            if i**2 + j**2 == k**2:
                if i + j + k == 1000:
                    print(i*j*k)

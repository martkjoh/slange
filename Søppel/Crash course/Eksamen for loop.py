def som_OL(fy, ly):
    ys = []
    for y in range(fy, ly + 1):
        if y%4 == 0:
            ys.append(y)
    return ys

print(som_OL(1999, 2012))
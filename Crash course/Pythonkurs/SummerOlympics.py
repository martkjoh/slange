def summerOlympics(firstYear,lastYear):
    years = []
    for i in range(firstYear,lastYear+1):
        if i%4 == 0:
            years.append(i)
    return years

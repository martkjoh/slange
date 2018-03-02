def payment(pris, antall):
    if antall > 3:
        return 0.9*antall*pris
    else:
        return antall*pris

def get_price(konsert):
    fil = open('prices.txt')
    linjer = fil.readlines()
    for i in range(len(linjer)):
        linjer[i]=linjer[i].split(';')
    for i in linjer:
        if i[0]== konsert:
            fil.close()
            return i[1]
    fil.close()
    return -1

def write_to_file(navn,konsert,antall,filnavn):
    pris = payment(int(get_price(konsert)),antall)
    fil = open(filnavn,'a')
    fil.write(konsert+';'+str(antall)+';'+str(pris)+';'+navn+'\n')
    fil.close()

def ticket(navn,konsert,antall):
    return([navn,konsert,antall,payment(int(get_price(konsert)),antall)])
print(ticket("jo","The Rectorats",8))


write_to_file("jo","The Rectorats",8,'billetter.txt')

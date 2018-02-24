def removeDup(liste):
    nyliste = []
    for i in liste:
        if i not in nyliste:
            nyliste.append(i)
    return nyliste

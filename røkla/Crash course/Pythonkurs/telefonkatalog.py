def leggTilNummer(navn,nummer,katalog):
    if navn in katalog:
        katalog[navn].append(nummer)
    else:
        katalog[navn] = [nummer]
    return katalog


def finnNumre(navn,katalog):
    if navn in katalog:
        return katalog[navn]
    return -1

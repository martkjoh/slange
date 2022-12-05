karakter = {
    'exphil'    : 'C',
    'mekfys'    : 'A',
    'itkg'      : 'C',
    'matte1'    : 'A',
    'elmag'     : 'A',
    'matte2'    : 'B',
    'matte3'    : 'A',
    'kjemi'     : 'A',
    'fluid'     : 'A',
    'termisk'   : 'A',
    'tekled'    : 'A',
    'matte4K'   : 'A',
    'stat'      : 'B',
    'vitber'    : 'A',
    'QM'        : 'A',
    'optikk'    : 'C',
    'klasmek'   : 'A',
    'partikkel' : 'A',
    'QM2'       : 'A',
    'QFT1'      : 'B',
    'kvantefast': 'A',
    'compfys'   : 'A',
    'EiT'       : 'A',
    'medisin'   : 'A',
    'proj'      : 'A',
    'master'    : 'A'
 }

studiepoeng = {
    'exphil'    : 7.5,
    'mekfys'    : 7.5,
    'itkg'      : 7.5,
    'matte1'    : 7.5,
    'elmag'     : 7.5,
    'matte2'    : 7.5,
    'matte3'    : 7.5,
    'kjemi'     : 7.5,
    'fluid'     : 7.5,
    'termisk'   : 7.5,
    'tekled'    : 7.5,
    'matte4K'   : 7.5,
    'stat'      : 7.5,
    'vitber'    : 7.5,
    'QM'        : 7.5,
    'optikk'    : 7.5,
    'klasmek'   : 7.5,
    'partikkel' : 7.5,
    'QM2'       : 7.5,
    'QFT1'      : 7.5,
    'kvantefast': 7.5,
    'compfys'   : 7.5,
    'EiT'       : 7.5,
    'medisin'   : 7.5,
    'proj'      : 15,
    'master'    : 30
 }

karakter_til_poeng = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2,
    'E' : 1
}


snitt = 0
sp_total = 0

for fag, kar in karakter.items():
    tall = karakter_til_poeng[kar]
    sp = studiepoeng[fag]
    snitt += tall*sp
    sp_total += sp

snitt = snitt/sp_total
print(
    'snitt = {}'.format(snitt), 
    'studiepoeng = {}'.format(sp_total),
    '{}'.format(sp_total/300)
)

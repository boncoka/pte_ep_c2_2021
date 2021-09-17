olom_terfogata = 11.34 # g/cm^3
rez_terfogata = 8.69 # g/cm^3
rez_surusege = 18
olom_surusege = 23
rez = rez_terfogata * rez_surusege
olom = olom_terfogata * olom_surusege

print("Az olom nehezebb:",olom > rez)

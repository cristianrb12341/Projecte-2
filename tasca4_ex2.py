nota = float(input("Introdueix una nota (o -1 per acabar): "))
hi_ha_deu = False

while nota != -1:
    if nota == 10:
        hi_ha_deu = True
    nota = float(input("Introdueix una nota (o -1 per acabar): "))

if hi_ha_deu:
    print("Hi ha hagut alguna nota que té un 10")
else:
    print("No hi ha cap 10")
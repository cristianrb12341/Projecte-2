hi_ha_negatiu = False

for i in range(10):
    num = float(input("Introdueix un nombre: "))
    if num < 0:
        hi_ha_negatiu = True

if hi_ha_negatiu:
    print("hi havia almenys un nombre negatiu")
else:
    print("no hi ha cap nombre negatiu") 
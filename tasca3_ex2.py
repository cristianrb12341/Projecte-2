num1 = float(input("Introdueix el primer nombre: "))
num2 = float(input("Introdueix el segon nombre: "))
num3 = float(input("Introdueix el tercer nombre: "))

if num1 > num2 and num1 > num3:
    print("El major és:", num1)
elif num2 > num3:
    print("El major és:", num2)
else:
    print("El major és:", num3)
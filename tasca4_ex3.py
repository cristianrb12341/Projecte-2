for i in range(10):
    num = float(input("Introdueix un nombre: "))
    if num < 0:
        print("hi havia almenys un nombre negatiu")
        break
else:
    print("no hi ha cap nombre negatiu")
# 1. Demanem dos nombres enters
num1 = int(input("Introdueix el primer nombre enter: "))
num2 = int(input("Introdueix el segon nombre enter: "))

# 2. Calculem les operacions
suma = num1 + num2
resta = num1 - num2
multiplicacio = num1 * num2

# 3. Comprovem la divisió per evitar errors si num2 és 0
if num2 != 0:
    divisio = num1 / num2
else:
    divisio = "No es pot dividir per zero"

# 4. Imprimim els resultats
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicació: {multiplicacio}")
print(f"Divisió: {divisio}")
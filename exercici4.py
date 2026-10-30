# Exercici 4: Casting de float a int

# 1. Demanem dos nombres en coma flotant (decimals)
num_float1 = float(input("Introdueix el primer nombre decimal: "))
num_float2 = float(input("Introdueix el segon nombre decimal: "))

# 2. Sumem els dos decimals
resultat_decimal = num_float1 + num_float2

# 3. Fent 'casting' (convertim el resultat decimal a un nombre enter)
resultat_enter = int(resultat_decimal)

# 4. Imprimim els dos resultats per veure la diferència
print("Resultat decimal original:", resultat_decimal)
print("Resultat convertit a enter (int):", resultat_enter)
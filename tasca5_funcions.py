def calcular_preu(peces, ma_obra):
    total = peces + ma_obra
    return total

preu = calcular_preu(45, 30)
print("Cost total:", preu, "€")

def aplicar_descompte(preu, tipus_client):
    tipus = tipus_client.lower()
    
    if tipus == "particular":
        return preu
    elif tipus == "empresa":
        return preu * 0.90
    elif tipus == "client habitual":
        return preu * 0.85
    else:
        print("Error: tipus de client no vàlid.")
        return preu

def calcular_iva(preu):
    iva = preu * 0.21
    return iva

def calcular_factura(preu, tipus_client):
    preu_descompte = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_descompte)
    total = preu_descompte + iva
    return total

def mostrar_menu():
    print("\n===== SERVEI TÈCNIC INFORMÀTIC =====")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")

def nova_reparacio():
    nom = input("Nom del client: ")
    peces = float(input("Cost de les peces (€): "))
    ma_obra = float(input("Cost de la mà d'obra (€): "))
    tipus = input("Tipus de client (Particular / Empresa / Client habitual): ")

    preu_inicial = calcular_preu(peces, ma_obra)
    preu_amb_descompte = aplicar_descompte(preu_inicial, tipus)
    descompte = preu_inicial - preu_amb_descompte
    iva = calcular_iva(preu_amb_descompte)
    total = calcular_factura(preu_inicial, tipus)

    print("\n--- FACTURA ---")
    print("Client:", nom)
    print("Preu inicial:", preu_inicial, "€")
    print("Descompte aplicat:", round(descompte, 2), "€")
    print("IVA (21%):", round(iva, 2), "€")
    print("Total a pagar:", round(total, 2), "€")

    return total

num_reparacions = 0
facturacio_total = 0

opcio = ""
while opcio != "4":
    mostrar_menu()
    opcio = input("Selecciona una opció: ")

    if opcio == "1":
        factura = nova_reparacio()
        num_reparacions = num_reparacions + 1
        facturacio_total = facturacio_total + factura
    elif opcio == "2":
        print("Nombre de reparacions realitzades:", num_reparacions)
    elif opcio == "3":
        print("Facturació total acumulada:", round(facturacio_total, 2), "€")
    elif opcio == "4":
        print("Sortint del programa. Fins aviat!")
    else:
        print("Opció no vàlida.")
while True:
    nota = float(input("Introdueix una nota (o -1 per acabar): "))
    
    if nota == -1:
        print("No hi ha cap 10")
        break
    elif nota == 10:
        print("Hi ha hagut alguna nota que té un 10")
        break
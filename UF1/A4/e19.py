selection = int(input("Selecciona una opción:\n1.\tLiteratura\n2.\tCinema\n3.\tMúsica\n4.\tVideojocs\n5.\tSortir"))

while selection != 5:
    if selection == 1:
        print("Literatura")
    elif selection == 2:
        print("Cinema")
    elif selection == 3:
        print("Música")
    elif selection > 5:
        print("Opción no válida")
    else:
        print("Videojocs")
    selection = int(input("Selecciona una opción:\n1.\tLiteratura\n2.\tCinema\n3.\tMúsica\n4.\tVideojocs\n5.\tSortir"))
    #selection = input("Selecciona una opción:\n1.\tLiteratura\n2.\tCinema\n3.\tMúsica\n4.\tVideojocs\n5.\tSortir").lower()
print("Hasta luego")
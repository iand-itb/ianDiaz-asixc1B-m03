'''
Ian Díaz Pérez
14/12/2023
Programa que a partir de unas coordenadas del taulell d'escacs, dibuixa amb "*" el recorregut possible de un alfil en la posició determinada.
'''
try:
    BLANC = "B"
    NEGRE = "N"
    pos = input("Introduce una posición para el alfil con dos números separados por un espacio (y x): ").split()
    y = int(pos[0])
    x = int(pos[1])
    while y < 1 or y > 8 or x > 8 or x < 1:
        pos = input("Introduce una posición para el alfil con dos números separados por un espacio (y x): ").split()
        y = int(pos[0])
        x = int(pos[1])
    for i in range(1, 9):
        for j in range(1, 9):
            if i == y and j == x:
                print("*", end=" ")
            elif j == x - (y - i) or j == x + (y - i):
                print("*", end=" ")
            elif (i + j) % 2 == 0:
                print(BLANC, end=" ")
            else:
                print(NEGRE, end=" ")
            print(" ", end="")
        print()
except Exception as e:
    if ValueError:
        print("Introduce un valor de coordenada correcto.")
    else:
        print(e)
'''
Ian Díaz Pérez
ASIX1cB
1/2/2024
e2 VALORS DE LA MATRIU: matriu quadrada de 0's amb 1 a les vores.
'''
try:
    nFil, nCol = 1, 2
    #matrix = [[0]*nCol for i in range(nFil)]
    matrix = []
    while nFil != nCol:
        nFil, nCol = int(input()), int(input())
        print("La matriz debe ser cuadrada (nFilas = nColumnas)\n")
    for i in range(nFil):
        if i == 0 or i + 1 == nFil:
            matrix.append([1]*nCol)
        else:
            matrix.append([1] + [0]* (nCol - 2) + [1])
    for x in range(nFil):
        for y in range(nCol):
            if y + 1 == nCol:
                print(matrix[x][y])
            else:
                print(matrix[x][y], end=" ")
except Exception as e:
    print(e)
    if TypeError:
        print("Introduce valores numéricos para el tamaño de la matriz.")

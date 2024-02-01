nFil, nCol = int(input()), int(input())
matrix = [[0]*nCol for i in range(nFil)]

for x in range(nFil):
    for y in range(nCol):
        print(matrix[x][y], end="")

#for i in range(nFil):
#    print(matrix[i])

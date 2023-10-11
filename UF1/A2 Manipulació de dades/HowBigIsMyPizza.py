'''
Ian Díaz
M03 UF1
Calcular la superfície d'una pizza a partir del diàmetre
11/10/23
'''

import math

#Demanem el diàmetre de la pizza com a float.
diametre = float(input("Introdueix el diàmetre de la pizza en centímetres...\t"))

superficie = math.pi * (diametre**2 / 4)

print(f"\nLa superficie de la pizza es: {superficie:.2f}cm")
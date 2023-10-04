"""
Ian Diaz
M03 UF1
4/10/2023
Programa per trovar el següent nombre
"""
import math
try:
    num = int(input("Introdüeix un nombre qualsevol...\n"))
    nextNum = num + 1
    print("El següent nombre és: " + str(nextNum))
except Exception as e:
    print(e)
    exit(1)
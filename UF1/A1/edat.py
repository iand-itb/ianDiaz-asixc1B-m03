"""
Ian Diaz
M03 UF1
21/9/2023
Exemple
"""

# Definició de la variable edat proporcionada per l'usuari com a int
try:
    edat = int(input("Introdueix la teva edat\n"))

# Comparem el valor de la variable "edat" amb 18. Depenent de si es major o igual, o menor mostrem un output diferent.
    if edat >= 18:
        print("Ets major d'edat")
    else:
        print("Pa tu casa, a ver pocoyo")
# Si el codi dins de "try: " falla, s'executa l'except i surt del programa amb codi "1" (error)s
except Exception as e:
    print("Introdueix una edat vàlida... Error: ")
    print(e)
    exit(1)
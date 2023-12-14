'''
Ian Díaz Pérez
14/12/2023
Programa que llegeix nombre enter positiu i determina la quantitat de dígits que té.
'''
try:
    digitos = 0
    num = input("Introduce un número entero: ")
    if int(num) > 0:
        for digito in int(num):
            digitos +=1
        print(f'El número "{num}" tiene {digitos} digitos.')
    else:
        print("Por favor, introduce un número entero positivo.")
except Exception as e:
    if ValueError:
        print("Por favor, introduce un número entero.")
    else:
        print(e)
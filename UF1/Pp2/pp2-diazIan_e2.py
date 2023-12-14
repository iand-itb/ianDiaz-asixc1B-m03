'''
Ian Díaz Pérez
14/12/2023
Programa que indica quantes vegades apareix una lletra a una frase en concret.
'''
try:
    caracter = input("Introduce el carácter a buscar: ")
    frase = input("Introduce la frase en la que buscar: ")
    count = 0
    for letra in frase:
        if letra == caracter:
            count +=1
    print(f'La frase "{frase}" contiene {count} carácteres "{caracter}".')
except Exception as e:
    if ValueError:
        print("Introduce una frase y carácter válidos")
    else:
        print(e)
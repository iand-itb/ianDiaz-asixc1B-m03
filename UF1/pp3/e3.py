'''
Ian Díaz Pérez
1/2/2024
ASIX1cB
e3 ENCRIPTAR FRASES: a = 1, b = 2 ...
'''
try:
    OFFSET = 97
    frase = input().lower()
    dec = []
    for character in frase:
        if character == " ":
            dec.append(" ")
        else:
            dec.append(ord(character) - OFFSET)

    for i in range(len(dec)):
        if i + 1 == len(dec) or dec[i+1] == " ":
            print(f'{dec[i]}', end="")
        elif str(dec[i]) == " ":
            print(" ", end="")
        else:
            print(dec[i], end=":")

except Exception as e:
    print(e)
    if TypeError:
        print("Introduce una frase válida")
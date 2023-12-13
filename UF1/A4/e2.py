import random
try:
    num = ""
    CORRECTO = random.randint(1, 100)
    intentos = 0
    print(CORRECTO)
    while num != CORRECTO and intentos < 10:
        num = int(input("Adivina el número: "))
        intentos +=1
        if num > CORRECTO:
            print("El número que has introducido es más grande.")
        elif num < CORRECTO:
            print("El número que has introducido es más pequeño.")
    if num == CORRECTO:
        print("Victoria")
except Exception as e:
    if ValueError:
        print("Introduce un valor numérico.")
    else:
        print(e)
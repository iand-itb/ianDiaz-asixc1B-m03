import random
#bucle while con try except para reintentar si ocurre un ValueError
while True:
    try:
        CORRECTO = 0
        guess = random.randint(1, 100)
        top = 100
        bot = 1
        intentos = 0
        while CORRECTO < 1 or CORRECTO > 100:
            CORRECTO = int(input("Introduce un número a adivinar entre el 1 y el 100: "))
        while guess != CORRECTO and intentos < 10:
            ask = input(f"Es más grande que {guess} ?\n")
            if ask == "si":
                bot = guess
            elif ask == "no":
                top = guess
            guess = random.randint(bot + 1, top - 1)
            intentos +=1
        if guess == CORRECTO:
            print(f"He adivinado el número ({guess}), y me han sobrado {10 - intentos} intentos.")
        if intentos >= 10:
            print("\nMe he quedado sin intentos...")
    except Exception as e:
        if ValueError:
            print("\nPor favor, introduce un valor numérico.")
            continue
        else:
            print(e)
    break
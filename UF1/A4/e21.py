import random
try:
    CORRECTO = int(input("Introduce un número a adivinar entre el 1 y el 100: "))
    guess = random.randint(1, 100)
    top = 100
    bot = 1
    intentos = 0
    while CORRECTO < 1 or CORRECTO > 100:
        CORRECTO = int(input("Introduce un número a adivinar entre el 1 y el 100: "))
    while guess != CORRECTO and intentos < 10:
        ask = input(f"Es más grande que {guess} ?\n").lower()
        if ask == "si":
            bot = guess
        elif ask == "no":
            top = guess
        else:
            print("Responde a la pregunta con 'si' o 'no'")
            break
        if CORRECTO == 1:
            guess = random.randint(bot, top -1)
        elif CORRECTO == 100:
            guess = random.randint(bot +1, top)
        else:
            guess = random.randint(bot +1, top -1)
        intentos +=1
    if guess == CORRECTO:
        print(f"He adivinado el número ({guess}), y me han sobrado {10 - intentos} intentos.")
    if intentos >= 10:
        print("\nMe he quedado sin intentos...")
except Exception as e:
    if ValueError:
        print("\nPor favor, introduce un valor numérico.")
    else:
        print(e)
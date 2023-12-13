try:
    souH = float(input("Introduce el sueldo por hora: "))
    totalH = 0
    totalS = 0

    for dia in range(1, 7):
        horas = int(input(f"Horas trabajadas dia {dia}:\t"))
        totalH += horas
        totalS += horas * souH

    print(f"\nTotal horas trabajadas:\t{totalH}h\nTotal sueldo a cobrar:\t{totalS:.2f}€")
except Exception as e:
    if ValueError:
        print("Introduce valores numéricos.")
    else:
        print(e)
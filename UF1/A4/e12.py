estalviat = 0
for mes in range(12):
    estMes = float(input(f"Cuánto quieres ahorrar este mes? ({mes + 1})\t"))
    estalviat += estMes
    if mes != 0 and mes != 11:
        print(f"De momento habrías ahorrado {estalviat:.2f}€")
print(f"Ahorrarías un total de {estalviat:.2f}€")
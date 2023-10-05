"""
Ian Diaz Perez
5/10/23
exercici 20 de reforç
"""

strMonedes = str(input("Introdüeix el nombre de monedes que tens de 2€, 1€, 50 cents, 20 cents, 10 cents i 5 cents separades per un espai...\n"))
monedes = []
monedes = strMonedes.split()
monedes[0] = int(monedes[0]) * 200
monedes[1] = int(monedes[1]) * 100
monedes[2] = int(monedes[2]) * 50
monedes[3] = int(monedes[3]) * 20
monedes[4] = int(monedes[4]) * 10
monedes[5] = int(monedes[5]) * 5
print(monedes)
totalcentims = int(monedes[0] + monedes[1] + monedes[2] + monedes[3] + monedes[4] + monedes[5])
totaleuros = float(totalcentims / 100)
print("Tens un total de: " + str(totaleuros) + "€")
limit = input("Introduce 2 numeros separados por un espacio: ").split()
num1 = int(limit[0])
num2 = int(limit[1])
entrada = ""
suma = 0
fora = 0
enLimit = False
while num1 > num2:
    limit = input("Introduce 2 numeros separados por un espacio: ").split()
    num1 = int(limit[0])
    num2 = int(limit[1])
    entrada = int(input("Introduce un numero: "))
while entrada != 0:
    entrada = int(input("Introduce un numero: "))
    if entrada > num1 and entrada < num2:
        suma += entrada
    elif entrada < num1 or entrada > num2:
        fora += 1
    elif entrada == num1 or entrada == num2:
        enLimit = True
print(f"Suma nums interiors: {suma}\nNums fora del interval: {fora}")
if enLimit == True:
    print("Has introducido algun numero igual a alguno de los limites.")
else:
    print("No has introducido ningun numero igual a alguno de los limites")
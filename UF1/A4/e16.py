try:
    inp = input("Introduce el número de trabajadores de la empresa y el sueldo por hora: ").split()
    trabajadores = int(inp[0])
    sueldo = float(inp[1])
    sTotal = 0
    for trabajador in range(1, trabajadores + 1):
        hSemana = int(input(f"Horas trabajadas a la semana de trabajador {trabajador}: "))
        sTotal += sueldo * hSemana

    print(f"Total correspondiente al sueldo pagado en una semana: {sTotal:.2f}€")
except Exception as e:
    if ValueError:
        print("Introduce valores númericos.")
    else:
        print(e)
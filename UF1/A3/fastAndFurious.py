'''
Ian Diaz
8/11/23
ASIXc M03 UF1 A3
Descripció: Calcular velocitat instantània i velocitat mitjana.
'''

try:
    initVel = float(input("Introdueix la velocitat inicial (m/s): "))
    accel =  float(input("Introdueix la acceleració (m/s\u00B2): "))
    time = float(input("Introdueix el temps (s): "))
    instVel = initVel + accel * time

    print(f"La velocitat instantània es: {instVel:.2f}m/s")
    if instVel > 0:
        medVel = (initVel + instVel) / 2
        print(f"La velocitat mediana es: {medVel:.2f}m/s")
    else:
        print("El vehicle està parat, no es pot calcular la velocitat mitjana.")
except ValueError:
    print("Introdueix números decimals.")
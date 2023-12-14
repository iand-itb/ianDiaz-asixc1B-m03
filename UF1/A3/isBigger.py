'''
Ian Diaz
8/11/23
ASIXc M03 UF1 A3
Descripció: Compara 2 números i els intercanvia si el primer és igual o major que el segon.
'''

try:

    prim = int(input("Introdueix un número: "))
    seg = int(input("Introdueix un segon número: "))

    if prim >= seg:
        prim, seg = seg, prim
        print(prim, seg)
    else:
        print("El primer número NO es major que el segon.")

except ValueError:
    print("Introdueix un número.")
    exit()
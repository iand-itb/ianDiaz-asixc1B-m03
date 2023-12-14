'''
Ian Diaz
8/11/23
ASIXc M03 UF1 A3
Descripció: Calcular el preu total de la factura de l'aigua arrodonit a 2 decimals.
'''
try:

    hab = input("Introdueix la lletra identificativa del teu tipus d'habitatge: ").upper()
    gastat = float(input("Introdueix el número de m\u00B3 d'aigua gastats: "))
    match hab:
        case "A": quotaFixa = 2.46
        case "B": quotaFixa = 6.40
        case "C": quotaFixa = 7.25
        case "D": quotaFixa = 11.21
        case "E": quotaFixa = 12.10
        case "F": quotaFixa = 17.28
        case "G": quotaFixa = 28.01
        case "H": quotaFixa = 40.50
        case "I": quotaFixa = 61.31
        case _:
            print("Tipus d'habitatge invàlid.")
            exit()
    if gastat > 0:
        if gastat <= 6:
            preu = quotaFixa + gastat * 0.5849
        elif gastat >= 7 and gastat <= 9:
            preu = quotaFixa + gastat * 1.1699
        elif gastat >= 10 and gastat <= 15:
            preu = quotaFixa + gastat * 1.7548
        elif gastat >= 16 and gastat <= 18:
            preu = quotaFixa + gastat * 2.3397
        elif gastat > 18:
            preu = quotaFixa + gastat * 2.9246
    else:
        print("Introdueix un número vàlid de m\u00B3 d'aigua gastats")
        exit()

    print(f"\nEl preu de la teva factura de l'aigua és: {preu:.2f}€")
    #print("El preu de la teva factura de l'aigua és: " + str(round(preu, 2)) + "€")
except ValueError:
    print("Introdueix valors vàlids.")
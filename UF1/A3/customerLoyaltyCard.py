'''
Ian Diaz
8/11/23
ASIXc M03 UF1 A3
Descripció: Calcular l'import amb descompte en cas de tenir la targeta de client, segons uns criteris.
'''
try:
    imp = float(input("Introdueix l'import de la factura amb IVA inclòs."))
    targClient = input("Tens targeta de client? (S/N): ").upper()
    iva = 1.21
    disc = 0.79
    if imp >= 100:
        if targClient == "S":
            preuDesc = imp * disc
            preuIva = preuDesc * iva
            print(f"Preu total: {imp:.2f}€, aplicat descompte: {preuIva:.2f}€")
        else:
            print("Necessites la targeta client per a poder aplicar el descompte.")
    else:
        print("L'import ha de ser igual o major a 100€.")
except ValueError:
    print("Introdueix només números a l'import de la factura.")
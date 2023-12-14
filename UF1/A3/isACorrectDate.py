'''
Ian Diaz
8/11/23
ASIXc M03 UF1 A3
Descripció: Comprovar si la data és correcte.
'''

try:
    data = input("Introdueix una data amb format DD/MM/YYYY: ").split("/")
    print(data)
    dia = int(data[0])
    mes = int(data[1])
    any = int(data[2])

    if dia > 0 and dia <= 31:
        if mes > 0 and mes <= 12:
            if any > 0:
                if mes == 2 and dia > 28 and not any % 4 == 0:
                    print("Data incorrecte.")
                    exit()
                if mes == 2 and any % 4 == 0 and dia > 29:
                    print("Data incorrecte.")
                    exit()
                if mes in [4,6,9,11] and dia > 30:
                    print("Data incorrecte.")
                    exit()
                print("Data correcte.")
            else:
                print("Data incorrecte.")
                exit()
        else:
            print("Data incorrecte.")
            exit()
    else:
        print("Data incorrecte.")
except ValueError:
    print("Introdueix una data valida.")
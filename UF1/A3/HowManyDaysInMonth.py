'''
Ian Díaz
M03 UF1
Mostrar el numero de dias de un mes
25/10/2023
'''

monthNum = int(input())

match monthNum:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12: print("31")
    case 2: print("28")
    case 4 | 6 | 9 | 11: print("30")

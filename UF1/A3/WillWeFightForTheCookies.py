'''
Ian Díaz
M03 UF1
Mostrar si se pelea o se come las galletas
25/10/2023
'''
try:
    uinput = input()
    people = int(uinput.split(" ")[0])
    cookies = int(uinput.split(" ")[1])
    if cookies % people == 0:
        print("Let's eat!")
    else:
        print("Let's fight!")
except ValueError:
    print("Incorrect values")
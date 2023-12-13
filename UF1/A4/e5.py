VOCALES = "aeiou"
inp = 0

while inp != " ":
    inp = input("Introduce una vocal, para terminar introduce un espacio:\t").lower()
    if len(inp) > 1:
        pass
    else:
        if inp in VOCALES:
            print("VOCAL")
        elif inp == " ":
            print("Saliendo...")
        else:
            print("NO VOCAL")
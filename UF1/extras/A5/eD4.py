try:
    numAlum = int(input("Numero de alumnos: "))
    alumnes = {input(f'Nombre de alumno {alumne + 1}: '): [] for alumne in range(numAlum)}
    print(type(alumnes))
    print(alumnes)
    for alum in alumnes:
        nota = 10
        while nota > -1:
            nota = int(input(f'Nota para el alumno {alum}: '))
            if nota > -1:
                alumnes[alum].append(nota)
            else:
                pass
            print(type(alumnes))
    print(alumnes)
except Exception as e:
    if TypeError:
        print(e)
        print('Introduce valores validos.')
    else:
        print(e)
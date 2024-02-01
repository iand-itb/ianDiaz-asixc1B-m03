try:
    SIZE = 100
    words = []
    word = ""
    mitjana = 0
    for i in range(SIZE):
        while word != "\\q":
            word = input("Palabra: ")
            if word != "\\q":
                words.append(word)
            else:
                pass
    shortest = len(min(words))
    longest = len(max(words))
    mitjana = mitjana / len(words)
    for palabra in words:
        mitjana+= len(palabra)
        toTuple = [f'{palabra}, {len(palabra)}' for palabra in words if len(palabra) == shortest]
        tupla = tuple(toTuple)
    print(f'Mitjana:{mitjana}, Més llarga:{longest}, Més curta:{shortest}')
    print(tupla)
except Exception as e:
    print(e)
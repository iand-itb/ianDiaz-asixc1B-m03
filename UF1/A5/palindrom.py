from unidecode import unidecode
especiales = '!\"#$%&\'()*+,-./:;<=>?[]^_'
frase = input().lower()
cleanstr = frase.replace(" ", "")
for character in cleanstr:
    for special in especiales:
        if character == special:
            cleanstr.replace(character, "")
clean = list(unidecode(cleanstr))
rev = clean[::-1]
if rev == cleanstr:
    print(clean)
    print("Es palindrom")
else:
    print(rev[::-1])
    print("no")

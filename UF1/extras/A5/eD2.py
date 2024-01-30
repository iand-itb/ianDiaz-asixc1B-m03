string = input()
dicc = [character for character in string]
occ = {character:string.count(character) for character in dicc}
print(occ)

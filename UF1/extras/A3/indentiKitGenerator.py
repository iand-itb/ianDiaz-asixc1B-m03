tipus = input("Dime que cara tiene: ").lower().split()
cabells = ""
ulls = ""
nas = ""
boca = ""
match tipus[0]:
    case "arrissats" : cabells = "@"*5
    case "llisos" : cabells = "V"*5
    case "pentinats": cabells = "X"*5

match tipus[1]:
    case "aclucats": ulls = ".-.-."
    case "rodons": ulls = ".o-o."
    case "estrellats": ulls = ".*-*."

match tipus[2]:
    case "aixafat": nas = "..O.."
    case "arromagat": nas = "..C.."
    case "agilenc": nas = "..V.."

match tipus[3]:
    case "normal": boca = ".==."
    case "bigoti": boca = ".~~~."
    case "dents-sortides": boca = ".www."

print(f"{cabells}\n{ulls}\n{nas}\n{boca}")
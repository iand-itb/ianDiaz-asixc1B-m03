'''
9/2/2024
Ian Díaz Pérez
ASIXc1B
m03 UF2 ex. MatchAnalyzer
'''

team1, team2 = None, None
teams = []
points = []
transl = []
loop = 0
def get_teams():
    global team1, team2
    team1, team2 = input(), input()
    teams.append(team1)
    teams.append(team2)


def validate_points(currPoints, oldPoints, loop):
    if len(currPoints) == 2:
        if loop > 0:
            set1, set2 = [currPoints[0], oldPoints[0]], [currPoints[1], oldPoints[1]]
            if set1[0] < set1[1] or set2[0] < set2[1] or set1[0] - set1[1] > 3 or set2[0] - set2[1] > 3:
                return False
            else:
                return True
        else:
            if currPoints[0] > 3 or currPoints[1] > 3:
                return False
            else:
                return True
    else:
        return False


def add_points():
    global loop
    currPoints = []
    while True:
        oldPoints = currPoints
        currPoints = input().split(" ")
        if '-1' in currPoints:
            break
        currPoints = [int(point) for point in currPoints]
        if validate_points(currPoints, oldPoints, loop):
            points.append(currPoints)
            translate_points(points, currPoints, oldPoints)
            loop += 1
        else:
            print("Puntos inválidos.")
            currPoints = oldPoints

def translate_points(currPoints, oldPoints):
    translations = {
        1: 'Tir lliure',
        2: 'Cistella',
        3: 'Triple'
    }
    if loop > 0:
        diff = [currPoints[0] - oldPoints[0], currPoints[1] - oldPoints[1]]
        for point in diff:
            if point > 0:
                transl.append(translations[point] + f' de {teams[diff.index(point)]}')
    else:
        for point in currPoints:
            if point > 0:
                transl.append(translations[point] + f' de {teams[currPoints.index(point)]}')

def announces():
    global loop
    if loop > 0:
        for announce in transl:
            print(announce)
        if points[-1][0] > points[-1][1]:
            print(f'Guanya {team1}.')
        elif points[-1][0] == points[-1][1]:
            print('Empat')
        else:
            print(f'Guanya {team2}')
try:
    get_teams()
    add_points()
    announces()
except Exception as e:
    print(f'Error ocurred: {e}')
    if TypeError or ValueError:
        print("Introdueix valors numérics vàlids.")
    elif IndexError:
        print("Introdueix la quantitat correcta de punts.")

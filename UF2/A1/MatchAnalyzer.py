teams = []
team1, team2 = [], []
points = []
total = []
transl = []
loop = 0

def get_teams():
    t = []
    global team1, team2
    while len(t) != 2:
        t = input("Enter 2 teams: ").split(" ")
        for team in t:
            teams.append(team)
    team1, team2 = teams[0], teams[1]


def validate_points(currPoints, oldPoints, loop):
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


def add_points():
    global loop
    currPoints = []
    while True:
        oldPoints = currPoints
        currPoints = input(f'Puntos actuales de cada equipo ({teams[0]} {teams[1]}): ').split(" ")
        if '-1' in currPoints:
            break
        currPoints = [int(point) for point in currPoints]
        if validate_points(currPoints, oldPoints, loop):
            points.append(currPoints)
            translate_points(points, currPoints, oldPoints)
            print(transl)
            print(points)
            loop += 1
        else:
            print("Puntos incorrectos")
            print(points)
            currPoints = oldPoints


def translate_points(points, currPoints, oldPoints):
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
            else:
                pass


def calculate_total(points):
    totalT1, totalT2 = 0, 0
    for i in range(len(points)):
        for set in points:
            totalT1 += set[0]
            totalT2 += set[1]
    total.append(totalT1)
    total.append(totalT2)

get_teams()
add_points()
calculate_total(points)
print(teams)
print(points)

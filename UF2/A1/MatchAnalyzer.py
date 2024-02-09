teams = []
team1, team2 = [], []
points = []
total = []
loop = 0

def get_teams():
    t = []
    while len(t) != 2:
        t = input("Enter 2 teams: ").split(" ")
        for team in t:
            teams.append(team)


def validate_points(currPoints, oldPoints, loop):
    if loop > 0:
        set1, set2 = [currPoints[0], oldPoints[0]], [currPoints[1], oldPoints[1]]
        if set1[0] < set1[1] or set2[0] < set2[1]:
            return False
        else:
            return True
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
            print(points)
        else:
            print("Puntos incorrectos")
            print(points)
            currPoints = oldPoints
        loop += 1


#def translate_points()


get_teams()
add_points()
print(teams)
print(points)

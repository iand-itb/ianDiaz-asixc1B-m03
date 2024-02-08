teams = []
points = []


def get_teams():
    t = []
    while len(t) != 2:
        t = input("Enter 2 teams: ").split(" ")
        for team in t:
            teams.append(team)


def add_points():
    currPoints = []
    while True:
        oldPoints = currPoints
        currPoints = input("Enter points for teams now (enter -1 to stop): ").split(" ")
        if '-1' in currPoints:
            break
        currPoints = [int(point) for point in currPoints]
        for point in currPoints:
            for oldpoint in oldPoints:
                if oldpoint > point:
                    break
                else:
                    if len(currPoints) != 2:
                        print("Please enter points for both teams.")
                    else:
                        points.append(currPoints)


get_teams()
add_points()
print(teams)
print(points)

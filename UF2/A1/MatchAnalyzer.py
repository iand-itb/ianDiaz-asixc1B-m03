teams = []
points = []


def get_teams():
    t = []
    while len(t) != 2:
        t = input("Enter 2 teams: ").split(" ")
        teams.append(t)


def add_points():
    while True:
        currPoints = input("Enter points for teams now (enter -1 to stop): ").split(" ")
        if '-1' in currPoints:
            break
        currPoints = [int(x) for x in currPoints]
        if len(currPoints) != 2:
            print("Please enter points for both teams.")
        else:
            points.append(currPoints)


get_teams()
add_points()
print(teams)
print(points)

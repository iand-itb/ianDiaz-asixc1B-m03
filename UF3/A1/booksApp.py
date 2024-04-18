import os

outFile = os.path.join('.', 'books.out')

numBooks = int(input())
titles = []
authors = []
pages = []

def getInput():
    for i in range(numBooks):
        titles.append(input())
        authors.append(input())
        pages.append(input())

def createList():
    list = []
    for i in range(numBooks):
        list.append(f'{titles[i]} - {authors[i]} - {pages[i]} pàgines\n')
    return list
def getShortestAndLongest(list):
    ind = pages.sort()
    shortest =
    
    longest =
def writeOutput(list):
    with open(outFile, 'a') as out:
        out.write('Llibres\n----------')
        out.write(list)
        out.write(f'----------\nTotal: {numBooks} llibres\nLlibre més curt: ')

getInput()
print(createList())
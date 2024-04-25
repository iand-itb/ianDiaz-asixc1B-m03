import csv
import os

csvfile = os.path.join('.', '2023_03_Marc_BicingNou_INFORMACIO.csv')
capacityList = []
idList = []
def getCsvDat():
    with open(csvfile, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['station_id'] not in idList:
                idList.append(row['station_id'])
                capacityList.append(int(row['capacity']))
        print(capacityList)


def getCaps():
    print(f'Maxima capacitat: {str(max(capacityList))}')
    print(f'Capacitat total: {str(sum(capacityList))}')

getCsvDat()
getCaps()
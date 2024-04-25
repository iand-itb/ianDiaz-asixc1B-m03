import json
import os

jsonfile = os.path.join('.', 'opendatabcn_NP-NASIA_Platges-js.json')
districts = []
ciutatVellaCount = 0

def getJsonData():
    with open(jsonfile, 'r') as f:
        data = json.load(f)
    return data

def parseJson(data):
    ciutatVellaCount = 0
    for i in range(len(data)):
        if data[i]["addresses"][0]["district_name"] not in districts:
            districts.append(data[i]["addresses"][0]["district_name"])
        if data[i]["addresses"][0]["district_name"] == 'Ciutat Vella':
            ciutatVellaCount =+1
    return ciutatVellaCount

data = getJsonData()
print(parseJson(data))
print(districts)
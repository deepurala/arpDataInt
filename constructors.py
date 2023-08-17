import requests
import pandas as pd
 
URL = "http://ergast.com/api/f1/constructors.json"
 
limit = 100
offset = 0
constructors = []
while True:
    PARAMS = {'limit':limit, 'offset': offset}

    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    for item in data['MRData']['ConstructorTable']['Constructors']:
        constructors.append(item)
    if offset > int(data['MRData']['total']):
        break
    offset += limit

pd.DataFrame(constructors).to_csv('constructors.csv', index=False)

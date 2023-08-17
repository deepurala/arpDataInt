import requests
import json
 
URL = "http://ergast.com/api/f1/seasons.json"
 
limit = 100
offset = 0
seasons = []
while True:
    PARAMS = {'limit':limit, 'offset': offset}

    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    for item in data['MRData']['SeasonTable']['Seasons']:
        seasons.append(item)
    if offset > int(data['MRData']['total']):
        break
    offset += limit

print(json.dumps(seasons))

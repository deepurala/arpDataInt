import requests
import json
 
URL = "http://ergast.com/api/f1/drivers.json"
 
limit = 100
offset = 0
drivers = []
while True:
    PARAMS = {'limit':limit, 'offset': offset}

    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    for item in data['MRData']['DriverTable']['Drivers']:
        drivers.append(item)
    if offset > int(data['MRData']['total']):
        break
    offset += limit

print(json.dumps(drivers))


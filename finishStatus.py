import requests
import pandas as pd
 
URL = "http://ergast.com/api/f1/status.json"
 
limit = 100
offset = 0
status = []
while True:
    PARAMS = {'limit':limit, 'offset': offset}

    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    for item in data['MRData']['StatusTable']['Status']:
        status.append(item)
    if offset > int(data['MRData']['total']):
        break
    offset += limit

pd.DataFrame(status).to_csv('status.csv', index=False)

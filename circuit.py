import requests
import pandas as pd
from flatten_json import flatten
 
URL = "http://ergast.com/api/f1/circuits.json"
 
limit = 100
offset = 0
circuits = []
while True:
    PARAMS = {'limit':limit, 'offset': offset}

    r = requests.get(url = URL, params = PARAMS)

    data = r.json()
    for item in data['MRData']['CircuitTable']['Circuits']:
        flat_circuits = flatten(item)
        circuits.append(flat_circuits)
    if offset > int(data['MRData']['total']):
        break
    offset += limit
print(circuits)
pd.DataFrame(circuits).to_csv('circuits.csv', index=False)

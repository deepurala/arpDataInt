import requests
import pandas as pd
from flatten_json import flatten
 
seasonsURL = "http://ergast.com/api/f1/seasons.json?limit=200&offset=0"
seasons = []

r = requests.get(url = seasonsURL)
data = r.json()
for item in data['MRData']['SeasonTable']['Seasons']:
    seasons.append(item)

season = [s['season'] for s in seasons ]



limit = 100
offset = 0
races = []

for s in season:
    raceURL = 'http://ergast.com/api/f1/'+s+'.json'
    r = requests.get(url = raceURL) 
    while True:
        data = r.json()
        for item in data['MRData']['RaceTable']['Races']:
            flat_races = flatten(item)
            races.append(flat_races)
        if offset > int(data['MRData']['total']):
            break
        offset += limit

pd.DataFrame(races).to_csv('races.csv', index=False)

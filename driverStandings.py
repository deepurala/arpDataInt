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
driverStandings = []

for s in season:
    driverStandingURL = 'http://ergast.com/api/f1/'+s+'driverStandings.json'
    r = requests.get(url = driverStandingURL) 
    while True:
        data = r.json()
        for item in data['MRData']['StandingsTable']['StandingsLists']:
            flat_standing = flatten(item)
            driverStandings.append(flat_standing)
        if offset > int(data['MRData']['total']):
            break
        offset += limit

pd.DataFrame(driverStandings).to_csv('driverStandings.csv', index=False)

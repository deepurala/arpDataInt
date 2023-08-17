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
seasonRaceDict = {}


for s in season:
    while True:
        raceURL = 'http://ergast.com/api/f1/' + s + '.json'
        PARAMS = {'limit': limit, 'offset': offset}

        r = requests.get(url=raceURL, params=PARAMS)
        data = r.json()
        
        total_races = int(data['MRData']['total'])
        
        for item in data['MRData']['RaceTable']['Races']:
            flat_races = flatten(item)
            races.append(flat_races['round'])
        
        if offset + limit >= total_races:
            break
        
        offset += limit
    seasonRaceDict[s].append(races)


print(seasonRaceDict)
#pd.DataFrame(races).to_csv('races.csv', index=False)

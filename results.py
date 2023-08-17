import requests
import pandas as pd

def flatten(d):
    # Helper function to flatten a nested dictionary
    def items():
        for key, value in d.items():
            if isinstance(value, dict):
                for subkey, subvalue in flatten(value).items():
                    yield key + '.' + subkey, subvalue
            else:
                yield key, value

    return dict(items())
 

seasonRaceDict = {}

seasonsURL = "http://ergast.com/api/f1/seasons.json?limit=200&offset=0"
seasons = []

r = requests.get(url = seasonsURL)
data = r.json()
for item in data['MRData']['SeasonTable']['Seasons']:
    seasons.append(item)

season = [s['season'] for s in seasons ]
limit = 100
offset = 0

for s in season:
    races = []  
    
    while True:
        raceURL = 'http://ergast.com/api/f1/' + s + '.json'
        PARAMS = {'limit': limit, 'offset': offset}

        r = requests.get(url=raceURL, params=PARAMS)
        data = r.json()
        
        total_races = int(data['MRData']['total'])
        
        for item in data['MRData']['RaceTable']['Races']:
            flat_races = flatten(item)
            races.append(flat_races['round'])
        
        if s not in seasonRaceDict:
            seasonRaceDict[s] = [] 
        seasonRaceDict[s].extend(races)
        
        if offset + limit >= total_races:
            break
        
        offset += limit


result = []
limit = 100

for season, rounds in seasonRaceDict.items():
    for round in rounds:
        offset = 0
        while True:
            raceURL = 'http://ergast.com/api/f1/' + season +'/'+ round + '/results.json'
            PARAMS = {'limit': limit, 'offset': offset}

            r = requests.get(url=raceURL, params=PARAMS)
            
            data = r.json()
    
            for item in data['MRData']['RaceTable']['Races']:
                for res in item['Results']:
                    flat_result = flatten(item)
                    result.append(flat_result)
        
            total = int(data['MRData']['total'])
            offset += limit
            if offset >= total:
                break

pd.DataFrame(result).to_csv('results.csv', index=False)
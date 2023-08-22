import csv

# Step 1: Create mappings for driverId, constructorId, and statusId
driver_mapping = {}
constructor_mapping = {}
status_mapping = {}

with open('srcCSV/drivers.csv', 'r', encoding="utf8") as driver_file:
    driver_reader = csv.DictReader(driver_file)
    for row in driver_reader:
        driver_mapping[int(row['driverId'])] = row['driverRef']

with open('srcCSV/constructors.csv', 'r', encoding="utf8") as constructor_file:
    constructor_reader = csv.DictReader(constructor_file)
    for row in constructor_reader:
        constructor_mapping[int(row['constructorId'])] = row['constructorRef']

with open('srcCSV/status.csv', 'r', encoding="utf8") as status_file:
    status_reader = csv.DictReader(status_file)
    for row in status_reader:
        status_mapping[int(row['statusId'])] = row['status']

# Step 2: Create a mapping for raceId to raceYear and raceRound
race_mapping = {}
with open('srcCSV/races.csv', 'r', encoding="utf8") as race_file:
    race_reader = csv.DictReader(race_file)
    for row in race_reader:
        race_mapping[int(row['raceId'])] = {'year': row['year'], 'round': row['round']}

# Step 3: Process results.csv and write to output.csv
with open('srcCSV/results.csv', 'r', encoding="utf8") as results_file, open('results.csv', 'w', newline='') as output_file:
    results_reader = csv.DictReader(results_file)
    fieldnames = results_reader.fieldnames
    fieldnames.extend(['raceYear', 'raceRound'])  # Add new columns 'raceYear' and 'raceRound'
    results_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    results_writer.writeheader()

    for row in results_reader:
        driver_id = int(row['driverId'])
        constructor_id = int(row['constructorId'])
        status_id = int(row['statusId'])

        driver_ref = driver_mapping.get(driver_id, '')  # Get driverRef from mapping
        constructor_ref = constructor_mapping.get(constructor_id, '')  # Get constructorRef from mapping
        status = status_mapping.get(status_id, '')  # Get status from mapping

        race_id = int(row['raceId'])
        race_info = race_mapping.get(race_id, {})  # Get raceYear and raceRound from mapping

        row['driverId'] = driver_ref  # Replace driverId with driverRef
        row['constructorId'] = constructor_ref  # Replace constructorId with constructorRef
        row['statusId'] = status  # Replace statusId with status
        row['raceYear'] = race_info.get('year', '')  # Add 'raceYear' column
        row['raceRound'] = race_info.get('round', '')  # Add 'raceRound' column
        del row['raceId']  # Remove 'raceId' column
        results_writer.writerow(row)
import csv

# Step 1: Create a mapping of driverId to driverRef from driver.csv
driver_mapping = {}
with open('srcCSV/drivers.csv', 'r', encoding="utf8") as driver_file:
    driver_reader = csv.DictReader(driver_file)
    for row in driver_reader:
        driver_mapping[int(row['driverId'])] = row['driverRef']

# Step 2: Create a mapping of constructorId to constructorRef from constructor.csv
constructor_mapping = {}
with open('srcCSV/constructors.csv', 'r', encoding="utf8") as constructor_file:
    constructor_reader = csv.DictReader(constructor_file)
    for row in constructor_reader:
        constructor_mapping[int(row['constructorId'])] = row['constructorRef']

# Step 3: Create a mapping of statusId to status from status.csv
status_mapping = {}
with open('srcCSV/status.csv', 'r', encoding="utf8") as status_file:
    status_reader = csv.DictReader(status_file)
    for row in status_reader:
        status_mapping[int(row['statusId'])] = row['status']

race_mapping = {}
with open('srcCSV/races.csv', 'r', encoding="utf8") as race_file:
    race_reader = csv.DictReader(race_file)
    for row in race_reader:
        race_mapping[int(row['raceId'])] = {'year': row['year'], 'round': row['round']}

# Step 4: Replace driverId, constructorId, and statusId with driverRef, constructorRef, and status in results.csv
with open('srcCSV/results.csv', 'r', encoding="utf8") as results_file, open('results.csv', 'w', newline='') as output_file:
    results_reader = csv.DictReader(results_file)
    fieldnames = results_reader.fieldnames
    results_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    results_writer.writeheader()


    for row in results_reader:
        driver_id = int(row['driverId'])
        constructor_id = int(row['constructorId'])
        status_id = int(row['statusId'])
        race_id = int(row['raceId'])

        driver_ref = driver_mapping.get(driver_id, '')  # Get driverRef from mapping
        constructor_ref = constructor_mapping.get(constructor_id, '')  # Get constructorRef from mapping
        status = status_mapping.get(status_id, '')  # Get status from mapping
        race_info = race_mapping.get(race_id, {})  # Get raceYear and raceRound from mapping

        row['driverId'] = driver_ref  # Replace driverId with driverRef
        row['constructorId'] = constructor_ref  # Replace constructorId with constructorRef
        row['statusId'] = status  # Replace statusId with status
        row['raceId'] = f"{race_info.get('year', '')} - {race_info.get('round', '')}"  # Replace raceId with raceYear and raceRound
        results_writer.writerow(row)
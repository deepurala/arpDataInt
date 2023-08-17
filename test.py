# Assuming you have the 'seasonRaceDict' dictionary with seasons as keys and arrays of rounds as values
seasonRaceDict = {
    '2021': ['1', '2', '3', '4'],
    '2022': ['1', '2', '3', '4', '5']
}

# Loop through the dictionary's key-value pairs
for season, rounds in seasonRaceDict.items():
    print(f"Season: {season}")
    print("Rounds:", ', '.join(rounds))
    print()  # Add a newline for separation

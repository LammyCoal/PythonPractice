dictionaries = [{
    'name': "Messi",
    'position': 10,
    'jersey number': 10,
    'goal scored': 900,
    'trophies': 45
},
    {
    'name': "Ronaldo",
    'position': 9,
    'jersey number': 7,
    'goal scored': 950,
    'trophies': 38
    },
    {
    'name': "Neymar",
    'position': 11,
    'jersey number': 10,
    'goal scored': 350,
    'trophies': 30}
]

answer = [player['position'] for player in dictionaries]
dictionaries[1]['position'] = 7
dictionaries[0]['goal scored'] += 40
dictionaries[1]['goal scored'] += 50
dictionaries[2]['goal scored'] += 60
dictionaries[0]['trophies'] += 10
dictionaries[1]['trophies'] += 15
dictionaries[2]['trophies'] += 20

average_goals = sum(player['goal scored'] for player in dictionaries)
average_trophies = sum(players['trophies'] for players in dictionaries)

print(f"Messi goals: {dictionaries[0]['goal scored']}", f" Ronaldo goals: {dictionaries[1]['goal scored']}", f" Neymar's goals: {dictionaries[2]['goal scored']}")
print(dictionaries[0]['trophies'], dictionaries[1]['trophies'], dictionaries[2]['trophies'])

print(f'The total goals of the GOATS are {average_goals}')
print(f'The total trophies of the GOATS are {average_trophies}')

hello dictionary.
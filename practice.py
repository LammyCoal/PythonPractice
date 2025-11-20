import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
    return name.capitalize()

capped_suffix = list(map(capitalize_suffix, suffixes))

def create_fantasy_name(list1, list2):
    return random.choice(list1) + ' ' + random.choice(list2)

random_name = [
    create_fantasy_name(prefixes, capped_suffix)
    for name in range(10)
]

def fire_in_name(name):
    return 'Fire' in name

def concatenate_names(name1, name2):
    return name1 + ', ' + name2

filtering = list(filter(fire_in_name, random_name))
reduction = reduce(concatenate_names, filtering) if filtering else "no fire in names"

def display_name_info():
    print('Random name: ')
    for name in random_name:
        print(name)
    print()


    print(f"Filtered name: {filtering}")
    print(f"Reducted name: {reduction}")


display_name_info()
# casino game
import random

def play():
    symbols = ['🍒', ' 🍇', '🍉', '7️⃣']
    winner = ['7️⃣', '7️⃣', '7️⃣']

    result = random.choices(symbols, k=3)
    while True:
        print(f'{result[0]} | {result[1]} | {result[2]}')
        if result == winner:
            print ('Jackpot!!')
        else:
            print('Thanks for playing!')

        Answer = input("y/n: ")

        if Answer == 'n':
            break


play()

# calculating area of planet
from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

r = 0

random_planet = ch(planets)
if random_planet == "Mercury":
    r = 2440
elif random_planet == "Venus":
    r = 6052
elif random_planet == "Earth":
    r = 6371
elif random_planet == "Mars":
    r = 3390
elif random_planet == "Saturn":
    r = 58232
else:
    print("Oops! An error occured.")

calc = 4 * pi * r**2
area = round(calc, 2)

print(f'The area of {random_planet} is {area}.')


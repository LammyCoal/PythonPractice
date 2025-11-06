import random

def birthday():
    bday_message= [
            'Hope you have a very Happy Birthday! 🎈',
        'It is your special day - go out there and celebrate!',
        'You were born and the world got better – everybody wins! 🥳',
        'Have lots of fun on your special day! 🎂',
        'Another year of you going around the sun! 🌞'
        ]
    random_message = random.choice(bday_message)

    return random_message
